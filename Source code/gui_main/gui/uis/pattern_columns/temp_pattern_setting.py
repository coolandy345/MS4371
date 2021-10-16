
from gui_main.qt_core import *
from gui_main.gui.uis.windows.main_window import *
from gui_main.gui.uis.pattern_columns.pattern_function import templist,tempUnit
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *
from gui_main.gui.core.json_settings import Settings
from gui_main.gui.core.json_themes import Themes
from PySide6.QtCore import QTimer
import threading

#from modbus_TcpServer import ModbusRegistorClass
import modbus_TcpServer
import time
import sys

import copy

from registor_manager import *

import numpy as np
import pyqtgraph as pg



class updata_step_widge_Thread(QRunnable):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        self.parent.updata_step_widge_work()

class update_graph_Thread(QRunnable):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        self.parent.update_graph_work()

class regular_Thread(QRunnable):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        for i in range(1,10000):
            self.parent.regularWork()
            QThread.msleep(10)
            print(QThreadPool.globalInstance().activeThreadCount())


class workThread(QThread):

    trigger = Signal()

    def __int__(self):
        # 初始化函式
        super().__init__()

    def run(self):
        self.trigger.emit()




        


class TempPatternWidget(QWidget):
    
    def __init__( 
            self, 
            parent = None,
            app_parent = None,
            focus_step_number=0,
            memoryPool={},
            queuePool={}
    ):
        

        super().__init__()

        
        self._parent=parent
        self._app_parent=app_parent
        self.Step_number=0
        self.main_memoryPool=memoryPool
        self.memoryPool={}
        self.queuePool=queuePool
        self.step_widges_list=[]
        self.patternFiles=[]
        self.focus_step_number=focus_step_number
        self.availlible_patternFile_count=0
        self.focus_patternFile_number=0
        self.cache_step=tempUnit()
        self.cache_steplist=templist()
        self.paste_ready=False
        self.activeStep_noFull=False
        self.update_Request=False
        self.IconButtonUpdate=False
        self.delete_IconButtonActiveState=True
        self.add_IconButtonActiveState=False
        self.save_IconButtonActiveState=False
        
        self.utility_setup()
        self.setup_TempPattern()
        self.setup_TempGraph()
        self.memory_reader()
        self.patternFile_Load()
        self.update_Request=True
        
        self.timer=QTimer()
        self.timer.timeout.connect(self.regularWork)
        self.timer.start(10)

        #self.timerWorker=regular_Thread(self)
        #QThreadPool.globalInstance().start(self.timerWorker)
        

        self.test=0
        self.test1=0


    

    
        
    def setup_TempPattern(self):
        self.step_widges_list.append(None)
        for _step in range(1,21):
            temp_step = PyTempStep(
                active=False,
                step=_step,
                type=PyTempStep.Temp_Type,
                parent = self._parent,
                app_parent=self._app_parent,
                )
            self.step_widges_list.append(temp_step)
            self.step_widges_list[_step].setVisible (False)
            self._parent.ui.load_pages.horizontalLayout_3.addWidget(self.step_widges_list[_step])
            self._parent.ui.load_pages.scrollArea_3.setMinimumSize(QSize(0, 320))
        
        
    def setup_TempGraph(self):
        self.graph =pg.PlotWidget(background=None,title="予定パターン")
        
        self.graph.setLabel(axis='left', text='温度', units='℃')

        self.graph.setLimits(xMin=0.9,xMax=20.9)
        self.Xaxis = self.graph.getAxis('bottom')
        self.Xaxis.setStyle(autoReduceTextSpace=False)
        self.Xaxis.setTickSpacing(1,1)
        self.Xaxis.setTextPen(pg.mkPen((25,28,34)))
        self.graph.setAxisItems({'bottom':self.Xaxis})
        
        self.Yaxis = self.graph.getAxis('left')
        self.Yaxis.enableAutoSIPrefix(False)

        self.graph.showGrid(x=True, y=True)
        self.graph.setMouseEnabled(x=True, y=False)
        self.graph.setLimits(minXRange=9,maxXRange=20)
        self.graph.setMinimumSize(QSize(1100, 300))

        self.curve=self.graph.plot(pen=pg.mkPen((225, 230, 241),width=5), 
                                   symbolBrush=(0,0,0),
                                   symbolPen='w', 
                                   #symbol='o', 
                                   symbolSize=5, 
                                   name="予定パターン")
        
        self._parent.ui.load_pages.horizontalLayout_4.addWidget(self.graph, Qt.AlignCenter, Qt.AlignCenter)
        
        

        self.GraphRegionList=[]
        self.GraphRegionList.append(None)
        self.GraphStepLabelList=[]
        self.GraphStepLabelList.append(None)

        for _step in range(1,21):

            region = PyGraphRegionItem(
                    parent = self._parent,
                    brush = QBrush(QColor(0, 0, 0, 0)),
                    hoverBrush=QBrush(QColor(0, 10, 10, 100)),
                    pen=pg.mkPen(50,50,50),
                    step=_step,
                    movable=False
                    )
            region.setRegion([_step, 1+_step])
            self.GraphRegionList.append(region)
            self.graph.plotItem.addItem(self.GraphRegionList[_step], ignoreBounds=True)
            
            #text="STEP %d" %_step
            #print(text)
            label=pg.TextItem(
                text="STEP %d" %_step,
                )
            label.setPos(_step+0.1, 20)
            self.GraphStepLabelList.append(label)
            self.graph.plotItem.addItem(self.GraphStepLabelList[_step], ignoreBounds=True)
            
            
     
    def new_TempPattern(self):
        self.cache_steplist.setStep(self.cache_steplist.step_number+1,tempUnit())
        self.cache_steplist.step_number+=1

        self.update_Request=True


    def reload_MainMemoryFromDatabase(self):
        databaseLoadThread(self.main_memoryPool)

    def memory_reader(self):
        #Reload Memory from Database
        #self.reload_MainMemoryFromDatabase()

        for key in self.main_memoryPool.keys():
            self.memoryPool[key]=self.main_memoryPool[key]

        _patternFile_lists=[None]

        #Try to get number of PTN list
        self.availlible_patternFile_count=self.memoryPool["Modbus Registor Pool - Registor"]["有効PTN総数"].value
        self.focus_patternFile_number=self.memoryPool["Modbus Registor Pool - Registor"]["フォーカスPTN番号"].value
        #Auto load last pattern
        if self.focus_patternFile_number==0:
            if self.availlible_patternFile_count:
                self.focus_patternFile_number=self.availlible_patternFile_count
        else:
            if self.focus_patternFile_number>self.availlible_patternFile_count:
                self.focus_patternFile_number=self.availlible_patternFile_count
        
        
        self.patternFile_nameList=[""]

        for ptn_no in range(1,21):

            pattern=templist(
                active          =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_パターン有効".format(ptn_no)].value,
                comment         =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_註記".format(ptn_no)].value,
                step_number     =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_実行STEP数".format(ptn_no)].value,
                gas_condition   =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_測定雰囲気".format(ptn_no)].value,
                RT_measure      =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_RT計測".format(ptn_no)].value,
                up_asciicode    =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_名称_Up".format(ptn_no)].value,
                down_asciicode  =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_名称_Down".format(ptn_no)].value
                )
            
            if pattern.active:
                self.patternFile_nameList.append(pattern.name)
            
            units=[None]
            
            for step_no in range(1,21):

                unit=tempUnit(
                    Step_Type               =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_STEP情報".format(ptn_no,step_no)].value,
                    time_hour               =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_時間_時".format(ptn_no,step_no)].value,
                    time_min                =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_時間_分".format(ptn_no,step_no)].value,
                    SV                      =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_SV値".format(ptn_no,step_no)].value,
                    N2_flowRate             =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_N2流量".format(ptn_no,step_no)].value,
                    PID_muffle_No           =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_マッフル_PID_No".format(ptn_no,step_no)].value,
                    PID_heater_No           =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_ヒーター_PID_No".format(ptn_no,step_no)].value,
                    time_keep               =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_キープ時間".format(ptn_no,step_no)].value,
                    test_measure_enable     =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_測定有".format(ptn_no,step_no)].value,
                    test_measure_PatternNo  =self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_測定パターン".format(ptn_no,step_no)].value
                
                    )
                units.append(unit)
            pattern.units=units
            _patternFile_lists.append(pattern)
        
        self.patternFiles=_patternFile_lists


    def memory_writer(self):

        for file_number in range(1,21):

            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_Up".format(file_number),self.patternFiles[file_number].up_asciicode)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_Down".format(file_number),self.patternFiles[file_number].down_asciicode)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_註記".format(file_number),self.patternFiles[file_number].comment)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_パターン有効".format(file_number),self.patternFiles[file_number].active)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_実行STEP数".format(file_number),self.patternFiles[file_number].step_number)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_測定雰囲気".format(file_number),self.patternFiles[file_number].gas_condition)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_RT計測".format(file_number),self.patternFiles[file_number].RT_measure)

            for step in range(1,21):
                step_unit=self.patternFiles[file_number].getStep(step)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_SV値".format(file_number,step),step_unit.SV)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_時間_時".format(file_number,step),step_unit.time_hour)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_時間_分".format(file_number,step),step_unit.time_min)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_キープ時間".format(file_number,step),step_unit.time_keep)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_N2流量".format(file_number,step),step_unit.N2_flowRate)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_マッフル_PID_No".format(file_number,step),step_unit.PID_muffle_No)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_ヒーター_PID_No".format(file_number,step),step_unit.PID_heater_No)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(file_number,step),step_unit.test_measure_enable)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定パターン".format(file_number,step),step_unit.test_measure_PatternNo)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP情報".format(file_number,step),step_unit.Step_Type)



    def utility_update(self):
        #Check if we can still create new pattern list
        if self.patternFiles[20].active:
            self.add_IconButtonActiveState=False
            self.IconButtonUpdate=True
        else:
            self.add_IconButtonActiveState=True
            self.IconButtonUpdate=True


        #Scan Avilible pattern import to patternfile_comboBox
        self._parent.ui.load_pages.patternfile_comboBox.currentIndexChanged.disconnect()
        self._parent.ui.load_pages.patternfile_comboBox.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.patternfile_comboBox.clear()
        self._parent.ui.load_pages.patternfile_comboBox.addItems(self.patternFile_nameList)
        self._parent.ui.load_pages.patternfile_comboBox.setCurrentIndex(self.focus_patternFile_number)
        self._parent.ui.load_pages.patternfile_comboBox.currentIndexChanged.connect(self.ui_click_callback)

        
        self._parent.ui.load_pages.commect_lineEdit.textEdited.disconnect()
        self._parent.ui.load_pages.commect_lineEdit.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.commect_lineEdit.setText(self.cache_steplist.comment)
        self._parent.ui.load_pages.commect_lineEdit.textEdited.connect(self.ui_click_callback)


        self._parent.ui.load_pages.gas_Combobox.currentIndexChanged.disconnect()
        self._parent.ui.load_pages.gas_Combobox.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.gas_Combobox.setCurrentIndex(self.cache_steplist.gas_condition)
        self._parent.ui.load_pages.gas_Combobox.currentIndexChanged.connect(self.ui_click_callback)

        self._parent.ui.load_pages.RT_combobox.currentIndexChanged.disconnect()
        self._parent.ui.load_pages.RT_combobox.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.RT_combobox.setCurrentIndex(self.cache_steplist.RT_measure)
        self._parent.ui.load_pages.RT_combobox.currentIndexChanged.connect(self.ui_click_callback)

        

        self.save_IconButtonActiveState=self.cache_steplist.content_Change
        self.delete_IconButtonActiveState=self.editorEnable

        self.IconButtonUpdate=True
        



        errormessage=self.cache_steplist.checkRule()
        
        self._parent.ui.load_pages.PatternErrorMessagelabel.setText(errormessage)


    def utility_setup(self):
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        self.settings = Settings()

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        self.themes = Themes().items

        self.focus_patternFile_number=self.settings.items["App User Interface parameter Setting"]["focus_patternFile_No"]
        
        self.delete_IconButton = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-trash.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                btn_id = "削除",
                tooltip_text = "削除",
                width = 30,
                height = 30,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["critical_icon"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["critical_icon"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["critical_icon"]["icon_pressed"],
                icon_color_deactive = self.themes["app_color"]["critical_icon"]["icon_deactive"],
                bg_color = self.themes["app_color"]["critical_icon"]["icon_bg"],
                bg_color_hover = self.themes["app_color"]["critical_icon"]["icon_bg_hover"],
                bg_color_pressed = self.themes["app_color"]["critical_icon"]["icon_bg_pressed"],
            )
        self._parent.ui.load_pages.gridLayout_34.addWidget(self.delete_IconButton, Qt.AlignCenter, Qt.AlignCenter)
        self.delete_IconButton.clicked.connect(self.ui_click_callback)

        self.add_IconButton = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-file-add.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                btn_id = "追加",
                tooltip_text = "追加",
                width = 30,
                height = 30,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = self.themes["app_color"]["regular_icon"]["icon_bg"],
                bg_color_hover = self.themes["app_color"]["regular_icon"]["icon_bg_hover"],
                bg_color_pressed = self.themes["app_color"]["regular_icon"]["icon_bg_pressed"],
            )
        self._parent.ui.load_pages.gridLayout_35.addWidget(self.add_IconButton, Qt.AlignCenter, Qt.AlignCenter)
        self.add_IconButton.clicked.connect(self.ui_click_callback)

        

        self.save_IconButton = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-edit.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                btn_id = "保存",
                tooltip_text = "保存",
                width = 30,
                height = 30,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = self.themes["app_color"]["regular_icon"]["icon_bg"],
                bg_color_hover = self.themes["app_color"]["regular_icon"]["icon_bg_hover"],
                bg_color_pressed = self.themes["app_color"]["regular_icon"]["icon_bg_pressed"],
            )
        self._parent.ui.load_pages.gridLayout_36.addWidget(self.save_IconButton, Qt.AlignCenter, Qt.AlignCenter)
        self.save_IconButton.clicked.connect(self.ui_click_callback)
        

        self._parent.ui.load_pages.patternfile_comboBox.currentIndexChanged.connect(self.ui_click_callback)
        self._parent.ui.load_pages.commect_lineEdit.textEdited.connect(self.ui_click_callback)
        self._parent.ui.load_pages.gas_Combobox.currentIndexChanged.connect(self.ui_click_callback)
        self._parent.ui.load_pages.RT_combobox.currentIndexChanged.connect(self.ui_click_callback)
        
        
    # update step widge
    # /////////////////////////////
    def updata_step_widge(self):
        self.updata_step_widge_Worker=updata_step_widge_Thread(self)
        QThreadPool.globalInstance().start(self.updata_step_widge_Worker)

    def updata_step_widge_work(self):
        #adjust the Visible of each step
        for _step in range(1,21):
            
            if _step<=self.cache_steplist.step_number :
                self.step_widges_list[_step].setVisible (True)
                self.step_widges_list[_step].pattern.page.setCurrentIndex(True)
            else:
                if _step==self.cache_steplist.step_number+1 and self.editorEnable:
                    self.step_widges_list[_step].setVisible (True)
                    self.step_widges_list[_step].pattern.page.setCurrentIndex(False)
                else:
                    self.step_widges_list[_step].setVisible (False)
                    self.step_widges_list[_step].pattern.page.setCurrentIndex(False)
            #Only last step has End type
            if _step==self.cache_steplist.step_number :
                self.step_widges_list[_step].enableEndType(True)
            else:
                self.step_widges_list[_step].enableEndType(False)

            #Check if we can still add step unit
            if self.cache_steplist.step_number<20:
                self.activeStep_noFull=True
            else:
                self.activeStep_noFull=False

            unit=tempUnit()
            unit=self.cache_steplist.getStep(_step)
            
            self.step_widges_list[_step].pattern.Type_comboBox.setCurrentIndex(unit.Step_Type)

            if unit.Step_Type==tempUnit.temp_unit_type:    #temp unit
                self.step_widges_list[_step].pattern.Hour_lineEdit.setValue(unit.time_hour)
                self.step_widges_list[_step].pattern.Min_lineEdit.setValue(unit.time_min)

                self.step_widges_list[_step].pattern.SV_lineEdit.setValue(unit.SV)
                self.step_widges_list[_step].pattern.N2_lineEdit.setValue(unit.N2_flowRate)
                self.step_widges_list[_step].pattern.PID_muffle_comboBox.setCurrentIndex(unit.PID_muffle_No)
                self.step_widges_list[_step].pattern.PID_heater_comboBox.setCurrentIndex(unit.PID_heater_No)

                pass
            elif unit.Step_Type==tempUnit.test_unit_type:  #test unit
                self.step_widges_list[_step].pattern.SV_lineEdit.setValue(unit.SV)
                self.step_widges_list[_step].pattern.PID_muffle_comboBox.setCurrentIndex(unit.PID_muffle_No)
                self.step_widges_list[_step].pattern.PID_heater_comboBox.setCurrentIndex(unit.PID_heater_No)
                self.step_widges_list[_step].pattern.KeepTime_lineEdit.setValue(unit.time_keep)
                self.step_widges_list[_step].pattern.TestPattern_comboBox.setCurrentIndex(unit.test_measure_PatternNo)
                pass
            elif unit.Step_Type==tempUnit.End_unit_type:  #End unit
                pass
        
        
        
    # update graph
    # /////////////////////////////
    def update_graph(self):
        self.update_graph_Worker=update_graph_Thread(self)
        QThreadPool.globalInstance().start(self.update_graph_Worker)

    def update_graph_work(self):
        data_array=[{"x":1,"y":0}]
        SV_array=[0]
        for _step in range(1,21):
            if _step<=self.cache_steplist.step_number:
                #load Graph data
                xy_dot={}
                unit=self.cache_steplist.getStep(_step)
                xy_dot["x"]=_step+1
                xy_dot["y"]=unit.SV
                data_array.append(xy_dot)
                SV_array.append(unit.SV)
                #load Region
                self.GraphRegionList[_step].show()
                #load Label
                self.GraphStepLabelList[_step].show()
            else:
                #load Region
                self.GraphRegionList[_step].hide()
                #load Label
                self.GraphStepLabelList[_step].hide()
        
        self.curve.setData(data_array)
        maxpos=max(SV_array)
        if(maxpos<1):
            self.graph.setYRange(0, 10)
            for _step in range(1,21):
                self.GraphStepLabelList[_step].setPos(_step+0.1,10)
        else:
            self.graph.setYRange(0, 1.2*maxpos)
            for _step in range(1,21):
                self.GraphStepLabelList[_step].setPos(_step+0.1,1.2*maxpos)
    

    def lunchOptionDialog(self,message,type):

        '''
        PyDialog.error_type
        PyDialog.warning_2_type
        PyDialog.warning_3_type
        '''

        diag = PyDialog(type,message)
        return(str(diag.exec()))

    def lunchMessageDialog(self,title,message):
        diag = PyMessageDialog(title,message)
        return(str(diag.exec()))



    def ui_click_callback(self):

        btn_name=self.sender().objectName()

        print("btn_name = ",btn_name)

        if btn_name=="削除":
            self.patternFile_Delete()
        elif btn_name=="保存":
            self.patternFile_Save()
        elif btn_name=="追加":
            self.patternFile_New()
        elif btn_name=="patternfile_comboBox":
            self.focus_patternFile_number=self._parent.ui.load_pages.patternfile_comboBox.currentIndex()
            #maybe confirm if we still not save
            self.patternFile_Load()

        elif btn_name=="commect_lineEdit":
            self.cache_steplist.set_Comment(self._parent.ui.load_pages.commect_lineEdit.text())
            self.update_Request=True

        elif btn_name=="gas_Combobox":
            self.cache_steplist.set_gas_condition(self._parent.ui.load_pages.gas_Combobox.currentIndex())
            self.update_Request=True

        elif btn_name=="RT_combobox":
            self.cache_steplist.set_RT_measure(self._parent.ui.load_pages.RT_combobox.currentIndex())
            self.update_Request=True
        




    def patternFile_Load(self):

        self.set_memorypool_register("Modbus Registor Pool - Registor","フォーカスPTN番号",self.focus_patternFile_number)

        self.memory_reader()

        #Reset paste function
        self.paste_ready=False

        if(self.focus_patternFile_number>=1 and self.focus_patternFile_number<=20):
            self.cache_steplist=copy.deepcopy(self.patternFiles[self.focus_patternFile_number])
            self.editorEnable=True
        else:
            self.editorEnable=False

        self.update_Request=True

    



    def patternFile_Delete(self):

        delete=False

        if self.content_Change:
            result=self.lunchOptionDialog("変更内容は未保存です。削除しますか？",PyDialog.warning_2_type)

            if result=="Yes":
                delete=True
                
            elif result=="No":
                #User is not want Delete file
                return
        else:
            delete=True

        if delete:
            self.availlible_patternFile_count-=1
            self.set_memorypool_register("Modbus Registor Pool - Registor","有効PTN総数",self.availlible_patternFile_count)

            self.patternFiles.append(templist())
            self.patternFiles.pop(self.focus_patternFile_number)

            if self.focus_patternFile_number>0:
                self.focus_patternFile_number-=1

            if self.focus_patternFile_number:
                self.cache_steplist=self.patternFiles[self.focus_patternFile_number]
            else:
                self.cache_steplist=templist()


            print("self.availlible_patternFile_count =",self.availlible_patternFile_count)
            print("self.focus_patternFile_number =",self.focus_patternFile_number)

            self.memory_writer()

            self.patternFile_Load()

        
    def patternFile_Save(self):
        self.patternFile_Save_Worker=patternFile_Save_Thread(self)
        QThreadPool.globalInstance().start(self.patternFile_Save_Worker)

    def patternFile_Save_work(self):
        print("B")
        #Refresh patternFiles
        self.patternFiles[self.focus_patternFile_number]=copy.deepcopy(self.cache_steplist)
        
        
        list=self.cache_steplist

        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_Up".format(self.focus_patternFile_number),list.up_asciicode)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_Down".format(self.focus_patternFile_number),list.down_asciicode)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_註記".format(self.focus_patternFile_number),list.comment)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_パターン有効".format(self.focus_patternFile_number),list.active)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_実行STEP数".format(self.focus_patternFile_number),list.step_number)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_測定雰囲気".format(self.focus_patternFile_number),list.gas_condition)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_RT計測".format(self.focus_patternFile_number),list.RT_measure)
        
        for step in range(1,21):
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_SV値".format(self.focus_patternFile_number,step),list.units[step].SV)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_時間_時".format(self.focus_patternFile_number,step),list.units[step].time_hour)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_時間_分".format(self.focus_patternFile_number,step),list.units[step].time_min)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_キープ時間".format(self.focus_patternFile_number,step),list.units[step].time_keep)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_N2流量".format(self.focus_patternFile_number,step),list.units[step].N2_flowRate)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_マッフル_PID_No".format(self.focus_patternFile_number,step),list.units[step].PID_muffle_No)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_ヒーター_PID_No".format(self.focus_patternFile_number,step),list.units[step].PID_heater_No)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(self.focus_patternFile_number,step),list.units[step].test_measure_enable)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定パターン".format(self.focus_patternFile_number,step),list.units[step].test_measure_PatternNo)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP情報".format(self.focus_patternFile_number,step),list.units[step].Step_Type)
            
        

        #Reload cache_list from memory
        self.patternFile_Load()

    def patternFile_New(self):
        NameString_fromDialog=""
        #if self.cache_steplist is not change
        NameString_fromDialog=self.lunchMessageDialog("Create new pattern","New Pattern Name :")
        #if self.cache_steplist is  changed
        #NameString_fromDialog=self.lunchMessageDialog("Create new pattern","未保存のパターンは破棄されます。宜しでしょうか?")

        #if we got availible name string
        if NameString_fromDialog!="Dialog reject" and NameString_fromDialog!="":
            
            #Create new cache_steplist
            self.availlible_patternFile_count+=1
            self.focus_patternFile_number=self.availlible_patternFile_count
            self.cache_steplist=templist(name=NameString_fromDialog)
            self.cache_steplist.set_Active(True)
            #write new availlible_patternFile_count to memory
            self.set_memorypool_register("Modbus Registor Pool - Registor","有効PTN総数",self.availlible_patternFile_count)

            #Save it to database
            self.patternFile_Save()

                 
    def set_memorypool_register(self,Main_memorypool,memory_name,value):
        
        if self.memoryPool[Main_memorypool][memory_name].getValue()!=value:
            self.memoryPool[Main_memorypool][memory_name].setValue(value)
            self.main_memoryPool[Main_memorypool]=self.memoryPool[Main_memorypool]
            sendItem=memoryUnit(Main_memorypool,memory_name)
            self.queuePool["memory_Write_Queue"].put(sendItem)

    def regularWork(self):
        
        #print("self.test1 = ",self.test1)
        self.test1+=1


        if time.time()-self.test >0.2 and time.time()-self.test <1000:
            print("lag occur time = ",time.time()-self.test)

        self.test=time.time()

        if self.IconButtonUpdate:
            self.delete_IconButton.set_active(self.delete_IconButtonActiveState)
            self.add_IconButton.set_active(self.add_IconButtonActiveState)
            self.save_IconButton.set_active(self.save_IconButtonActiveState)
            self.IconButtonUpdate=False
        
        if self.update_Request:
            self.update_Request=False
            self.update()


    def scroll_adjust_TempPattern(self):
        self._parent.ui.load_pages.scrollArea_3.horizontalScrollBar().setValue(self._parent.ui.load_pages.scrollArea_3.horizontalScrollBar().maximum())

    def menu_btn_handler(self,btn):
        if btn == "pattern_menu_cut_pushButton":
            self.cache_step=self.cache_steplist.getStep(self.focus_step_number)
            self.cache_steplist.step_number-=1
            self.cache_steplist.units.append(tempUnit())
            self.cache_steplist.units.pop(self.focus_step_number)
            self.paste_ready=True
            #print("pattern_menu_cut ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_copy_pushButton":

            self.cache_step=self.cache_steplist.getStep(self.focus_step_number)
            self.paste_ready=True

            #print("pattern_menu_copy ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_paste_pushButton":
            if self.paste_ready:
                self.cache_steplist.setStep(self.focus_step_number,self.cache_step)
            #print("pattern_menu_paste ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_rightinsert_pushButton":
            if not self.cache_steplist.step_number==20:
                if self.paste_ready:
                    self.cache_steplist.units.pop(20)
                    self.cache_steplist.units.insert(self.focus_step_number+1,tempUnit())
                    self.cache_steplist.setStep(self.focus_step_number+1,self.cache_step)
                    self.cache_steplist.step_number+=1
            #print("pattern_menu_rightinsert ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_leftinsert_pushButton":
            if not self.cache_steplist.step_number==20:
                if self.paste_ready:
                    self.cache_steplist.units.pop(20)
                    self.cache_steplist.units.insert(self.focus_step_number,tempUnit())
                    self.cache_steplist.setStep(self.focus_step_number,self.cache_step)
                    self.cache_steplist.step_number+=1
            #print("pattern_menu_leftinsert ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_rightinsertblank_pushButton":
            if not self.cache_steplist.step_number==20:
                self.cache_steplist.units.pop(20)
                self.cache_steplist.units.insert(self.focus_step_number+1,tempUnit())
                self.cache_steplist.step_number+=1
            #print("pattern_menu_rightinsertblank ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_leftinsertblank_pushButton":
            if not self.cache_steplist.step_number==20:
                self.cache_steplist.units.pop(20)
                self.cache_steplist.units.insert(self.focus_step_number,tempUnit())
                self.cache_steplist.step_number+=1
            #print("pattern_menu_leftinsertblank ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_delete_pushButton":
            self.cache_steplist.units.append(tempUnit())
            self.cache_steplist.units.pop(self.focus_step_number)
            self.cache_steplist.step_number-=1
            #print("pattern_menu_delete ",self.focus_step_number)
            pass


        self.close_menu()
        self.update_Request=True

    def focus_step(self,_step):
        self.step_widges_list[_step].setFocusStyle(True)
        self.GraphRegionList[_step].setFocusStyle(True)
        self.focus_step_number=_step

    def un_focus_step(self,_step):
        self.step_widges_list[_step].setFocusStyle(False)
        self.GraphRegionList[_step].setFocusStyle(False)
        
        if self.focus_step_number==_step:
            self.focus_step_number=0

    def close_menu(self):
        for step in range(1,21):
            self.step_widges_list[step]._menu.menu_frame.hide()

    def close_one_menu(self,step):
        self.step_widges_list[step]._menu.menu_frame.hide()

    def content_change_check(self):

        if (self.cache_steplist!=None and
            self.patternFiles[self.focus_patternFile_number]!=None
            ):
            self.content_Change=False

            if(
                self.cache_steplist.name            != self.patternFiles[self.focus_patternFile_number].name or
                self.cache_steplist.up_asciicode    != self.patternFiles[self.focus_patternFile_number].up_asciicode or
                self.cache_steplist.down_asciicode  != self.patternFiles[self.focus_patternFile_number].down_asciicode or
                self.cache_steplist.comment         != self.patternFiles[self.focus_patternFile_number].comment or
                self.cache_steplist.active          != self.patternFiles[self.focus_patternFile_number].active or
                self.cache_steplist.step_number     != self.patternFiles[self.focus_patternFile_number].step_number or
                self.cache_steplist.gas_condition   != self.patternFiles[self.focus_patternFile_number].gas_condition or
                self.cache_steplist.RT_measure      != self.patternFiles[self.focus_patternFile_number].RT_measure 
                ):
                self.content_Change=True

        
            for step in range(1,21):

                cache_stepUnit=self.cache_steplist.getStep(step)
                memory_stepUnit=self.patternFiles[self.focus_patternFile_number].getStep(step)

                if(
                cache_stepUnit.Step_Type                !=memory_stepUnit.Step_Type or
                cache_stepUnit.SV                       !=memory_stepUnit.SV or
                cache_stepUnit.N2_flowRate              !=memory_stepUnit.N2_flowRate or
                cache_stepUnit.PID_muffle_No            !=memory_stepUnit.PID_muffle_No or
                cache_stepUnit.PID_heater_No            !=memory_stepUnit.PID_heater_No or
                cache_stepUnit.test_measure_enable      !=memory_stepUnit.test_measure_enable or
                cache_stepUnit.test_measure_PatternNo   !=memory_stepUnit.test_measure_PatternNo or
                cache_stepUnit.time_hour                !=memory_stepUnit.time_hour or
                cache_stepUnit.time_keep                !=memory_stepUnit.time_keep or
                cache_stepUnit.time_min                 !=memory_stepUnit.time_min
                ):
                    self.content_Change=True


            self.cache_steplist.content_Change=self.content_Change

    def step_modifly_manager(self,step):
        stepUnit=self.cache_steplist.getStep(step)

        stepUnit.Step_Type              =self.step_widges_list[step]._type
        stepUnit.time_hour              =self.step_widges_list[step]._hour
        stepUnit.time_min               =self.step_widges_list[step]._minute
        stepUnit.SV                     =self.step_widges_list[step]._temperature
        stepUnit.N2_flowRate            =self.step_widges_list[step]._n2_flowrate
        stepUnit.PID_muffle_No          =self.step_widges_list[step]._PID_muffle_no
        stepUnit.PID_heater_No          =self.step_widges_list[step]._PID_heater_no
        stepUnit.time_keep              =self.step_widges_list[step]._keep_seccond
        stepUnit.test_measure_PatternNo =self.step_widges_list[step]._test_pattern

        self.cache_steplist.setStep(step,stepUnit)

        self.update_Request=True


    def update(self):
        self.content_change_check()
        self.updata_step_widge()
        self.update_graph()
        self.utility_update()

    def graphResize(self):
        addwidth=self._parent.width()-1470
        self.graph.setMinimumSize(QSize(1100+addwidth, 300))



class patternFile_Save_Thread(QRunnable):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        self.parent.patternFile_Save_work()

    