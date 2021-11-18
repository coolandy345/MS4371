from gui_main.qt_core import *
from gui_main.gui.uis.windows.main_window import *
from gui_main.gui.uis.pattern_columns.pattern_function import templist,tempUnit
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *
from gui_main.gui.core.json_settings import Settings
from gui_main.gui.core.json_themes import Themes
from PyQt5.QtCore import QTimer
import threading

#from modbus_TcpServer import ModbusRegistorClass
import modbus_TcpServer
import time
import sys

import copy

from registor_manager import *

import numpy as np
import pyqtgraph as pg

class update_graph_Thread(QRunnable):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        self.parent.update_graph_work()

class patternFile_Save_Thread(QRunnable):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        self.parent.patternFile_Save_work()


class TempPatternWidget(QWidget):
    
    def __init__( 
            self, 
            parent = None,
            queuePool={}
    ):
        super().__init__()

        self._parent=parent
        self.Step_number=0
        self.queuePool=queuePool
        self.step_widges_list=[]
        self.patternFiles=[]
        self.availlible_patternFile_count=0
        self.focus_patternFile_number=0
        self.focus_step_number=0
        self.cache_step=tempUnit()
        self.cache_steplist=templist()
        self.paste_ready=False
        self.content_Change=False
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
        self.timer.timeout.connect(self.ultility_Update_Work)
        self.timer.start(10)

        #ultility_Update_Thread = threading.Thread(target = self.ultility_Update_Work,daemon=True)
        #ultility_Update_Thread.start()

        self.test=0
        self.test1=0

    

    
        
    def setup_TempPattern(self):
        self.step_widges_list=[None]
        for _step in range(1,21):
            temp_step = PyTempStep(
                active=False,
                step=_step,
                type=PyTempStep.Temp_Type,
                parent = self._parent,
                )
            self.step_widges_list.append(temp_step)
            self.step_widges_list[_step].setVisible (False)
            self._parent.ui.load_pages.horizontalLayout_3.addWidget(self.step_widges_list[_step])
            #self._parent.ui.load_pages.scrollArea_3.setMinimumSize(QSize(0, 380))
        
        
    def setup_TempGraph(self):
        self.graph =pg.PlotWidget(background=None,title="温度パターン")
        
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
        #self.graph.setMinimumSize(QSize(500, 300))
        #self.graph.setFixedSize(500, 300)

        self.curve=self.graph.plot(
                                   pen=pg.mkPen('w',width=5), 
                                   symbolBrush=(0,0,0),
                                   symbolPen='w', 
                                   #symbol='o', 
                                   symbolSize=5, 
                                   name="予定パターン")
        
        self._parent.ui.load_pages.gridLayout_9.addWidget(self.graph, Qt.AlignCenter, Qt.AlignCenter)
        
        

        self.GraphRegionList=[]
        self.GraphRegionList.append(None)
        self.GraphStepLabelList=[]
        self.GraphStepLabelList.append(None)

        for _step in range(1,21):

            region = PyGraphRegionItem(
                    parent  =self,
                    app_parent = self._parent,
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
        
        #print("new_TempPattern")
        #self.update_Request=True
        self.update()

    def memory_reader(self):
        #print("memory_reader")
        _patternFile_lists=[None]

        #Try to get number of PTN list
        self.availlible_patternFile_count=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["有効PTN総数"].getValue()
        self.focus_patternFile_number=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["フォーカスPTN番号"].getValue()
        #Auto load last pattern
        if self.focus_patternFile_number==0:
            if self.availlible_patternFile_count:
                self.focus_patternFile_number=self.availlible_patternFile_count
        else:
            if self.focus_patternFile_number>self.availlible_patternFile_count:
                self.focus_patternFile_number=self.availlible_patternFile_count
        
        
        self.patternFile_nameList=[]

        for ptn_no in range(1,21):

            
            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_測定雰囲気".format(ptn_no)].getValue()==1:
                gas=1
            elif self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_測定雰囲気".format(ptn_no)].getValue()==2:
                gas=2
            elif self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_測定雰囲気".format(ptn_no)].getValue()==4:
                gas=3
            else:
                gas=0

            pattern=templist(
                active          =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_パターン有効".format(ptn_no)].getValue(),
                comment         =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_註記".format(ptn_no)].value,
                step_number     =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_実行STEP数".format(ptn_no)].getValue()+1,
                gas_condition   =gas,
                RT_measure      =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_RT計測".format(ptn_no)].getValue(),
                RT_testpattern  =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_RT測定パターン".format(ptn_no)].getValue(),
                asciicode_0    =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_名称_0".format(ptn_no)].getValue(),
                asciicode_1    =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_名称_1".format(ptn_no)].getValue(),
                asciicode_2    =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_名称_2".format(ptn_no)].getValue(),
                asciicode_3    =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_名称_3".format(ptn_no)].getValue()
                )
            
            if pattern.active:
                self.patternFile_nameList.append(pattern.name)
            
            units=[None]
            
            for step_no in range(1,21):


                unit=tempUnit(
                    Step_Type               =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_STEP種類".format(ptn_no,step_no)].getValue(),
                    step_time               =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_ステップ所要時間".format(ptn_no,step_no)].getValue(),
                    total_time               =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_ステップ累計時間".format(ptn_no,step_no)].getValue(),
                    time_hour               =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_時間_時".format(ptn_no,step_no)].getValue(),
                    time_min                =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_時間_分".format(ptn_no,step_no)].getValue(),
                    SV                      =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_SV値".format(ptn_no,step_no)].getValue(),
                    N2_flowRate             =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_N2流量".format(ptn_no,step_no)].getValue(),
                    PID_muffle_No           =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_マッフル_PID_No".format(ptn_no,step_no)].getValue(),
                    PID_heater_No           =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_ヒーター_PID_No".format(ptn_no,step_no)].getValue(),
                    time_keep               =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_キープ時間".format(ptn_no,step_no)].getValue(),

                    sp_limit_up             =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_スレーブSP上限".format(ptn_no,step_no)].getValue(),
                    sp_limit_down        =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_スレーブSP下限".format(ptn_no,step_no)].getValue(),
                    shift               =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_シフト".format(ptn_no,step_no)].getValue(),



                    test_measure_enable     =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_測定有".format(ptn_no,step_no)].getValue(),
                    test_measure_PatternNo  =self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_測定パターン".format(ptn_no,step_no)].getValue()
                    )
                units.append(unit)

            pattern.units=units
            _patternFile_lists.append(pattern)
        self.patternFiles=_patternFile_lists
        #print("memory_reader finish")

    def memory_writer(self):

        for file_number in range(1,21):

            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_0".format(file_number),self.patternFiles[file_number].asciicode_0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_1".format(file_number),self.patternFiles[file_number].asciicode_1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_2".format(file_number),self.patternFiles[file_number].asciicode_2)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_3".format(file_number),self.patternFiles[file_number].asciicode_3)

            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_註記".format(file_number),self.patternFiles[file_number].comment)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_パターン有効".format(file_number),self.patternFiles[file_number].active)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_実行STEP数".format(file_number),self.patternFiles[file_number].step_number-1)

            
            if self.patternFiles[file_number].gas_condition==1:
                gas=1
            elif self.patternFiles[file_number].gas_condition==2:
                gas=2
            elif self.patternFiles[file_number].gas_condition==3:
                gas=4
            else:
                gas=0



            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_測定雰囲気".format(file_number),gas)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_RT計測".format(file_number),self.patternFiles[file_number].RT_measure)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_RT測定パターン".format(file_number),self.patternFiles[file_number].RT_testpattern)


            for step in range(1,21):
                step_unit=self.patternFiles[file_number].getStep(step)

                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_SV値".format(file_number,step),step_unit.SV)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_ステップ所要時間".format(file_number,step),step_unit.step_time)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_ステップ累計時間".format(file_number,step),step_unit.total_time)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_時間_時".format(file_number,step),step_unit.time_hour)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_時間_分".format(file_number,step),step_unit.time_min)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_キープ時間".format(file_number,step),step_unit.time_keep)

                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_スレーブSP上限".format(file_number,step),step_unit.sp_limit_up)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_スレーブSP下限".format(file_number,step),step_unit.sp_limit_down)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_シフト".format(file_number,step),step_unit.shift)

                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_N2流量".format(file_number,step),step_unit.N2_flowRate)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_マッフル_PID_No".format(file_number,step),step_unit.PID_muffle_No)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_ヒーター_PID_No".format(file_number,step),step_unit.PID_heater_No)
                
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定パターン".format(file_number,step),step_unit.test_measure_PatternNo)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP種類".format(file_number,step),step_unit.Step_Type)

                if step<=self.patternFiles[file_number].step_number:
                    if self.patternFiles[file_number].units[step].Step_Type==tempUnit.temp_unit_type:
                        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP情報".format(file_number,step),2)
                        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(file_number,step),0)

                    elif self.patternFiles[file_number].units[step].Step_Type==tempUnit.test_unit_type:
                        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP情報".format(file_number,step),2)
                        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(file_number,step),1)
                    elif self.patternFiles[file_number].units[step].Step_Type==tempUnit.End_unit_type:
                        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP情報".format(file_number,step),1)
                        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(file_number,step),0)
                else:
                    self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP情報".format(file_number,step),0)
                    self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(file_number,step),0)
        



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
        self._parent.ui.load_pages.patternfile_comboBox.setCurrentIndex(self.focus_patternFile_number-1)
        self._parent.ui.load_pages.patternfile_comboBox.currentIndexChanged.connect(self.ui_click_callback)

        
        self._parent.ui.load_pages.commect_lineEdit.textChanged.disconnect()
        self._parent.ui.load_pages.commect_lineEdit.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.commect_lineEdit.setText(str(self.cache_steplist.comment))
        self._parent.ui.load_pages.commect_lineEdit.textChanged.connect(self.ui_click_callback)


        hour=self.cache_steplist.total_time//60
        min=self.cache_steplist.total_time%60
        self._parent.ui.load_pages.Temp_Totaltime_Label.setText("合計時間：{} 時間 {} 分".format(hour,min))
        
        if self.cache_steplist.RT_measure==2 and self.editorEnable:

            self._parent.ui.load_pages.RT_testpattern_combobox.setEnabled(self.editorEnable)

            self._parent.ui.load_pages.RT_testpattern_combobox.currentIndexChanged.disconnect()
            self._parent.ui.load_pages.RT_testpattern_combobox.clear()
            self._parent.ui.load_pages.RT_testpattern_combobox.addItems(self._parent.testPattern.patternFile_nameList)
            self._parent.ui.load_pages.RT_testpattern_combobox.setCurrentIndex(self.cache_steplist.RT_testpattern-1)
            self._parent.ui.load_pages.RT_testpattern_combobox.currentIndexChanged.connect(self.ui_click_callback)

        elif self.cache_steplist.RT_measure==1:
            self._parent.ui.load_pages.RT_testpattern_combobox.setEnabled(False)
            self.cache_steplist.RT_testpattern=0
        else:
            self._parent.ui.load_pages.RT_testpattern_combobox.setEnabled(False)
            self.cache_steplist.RT_testpattern=0




        self._parent.ui.load_pages.gas_Combobox.currentIndexChanged.disconnect()
        self._parent.ui.load_pages.gas_Combobox.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.gas_Combobox.setCurrentIndex(self.cache_steplist.gas_condition-1)
        self._parent.ui.load_pages.gas_Combobox.currentIndexChanged.connect(self.ui_click_callback)

        self._parent.ui.load_pages.RT_combobox.currentIndexChanged.disconnect()
        self._parent.ui.load_pages.RT_combobox.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.RT_combobox.setCurrentIndex(self.cache_steplist.RT_measure-1)
        self._parent.ui.load_pages.RT_combobox.currentIndexChanged.connect(self.ui_click_callback)

        

        self.save_IconButtonActiveState=self.content_Change
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

        self.delete_IconButton = PyIconButton_simple(
                icon = "fi-rr-trash.svg",
                icon_active = "fi-rr-trash.svg",
                icon_hover = "fi-rr-trash.svg",
                icon_deactive = "fi-rr-trash-deactive.svg",
                btn_id = "削除",
                tooltip_text = "削除",
                width = 30,
                height = 30,
                bg_color = self.themes["app_color"]["regular_icon"]["icon_bg"],
                bg_color_hover = self.themes["app_color"]["regular_icon"]["icon_bg_hover"],
                bg_color_pressed = self.themes["app_color"]["regular_icon"]["icon_bg_pressed"],

            )
        self._parent.ui.load_pages.verticalLayout_11.addWidget(self.delete_IconButton, Qt.AlignCenter, Qt.AlignCenter)
        self.delete_IconButton.clicked.connect(self.ui_click_callback)

        self.add_IconButton = PyIconButton_simple(
                icon = "fi-rr-file-add.svg",
                icon_active = "fi-rr-file-add.svg",
                icon_hover = "fi-rr-file-add.svg",
                icon_deactive = "fi-rr-file-add-deactive.svg",
                btn_id = "追加",
                tooltip_text = "追加",
                width = 30,
                height = 30,
                bg_color = self.themes["app_color"]["regular_icon"]["icon_bg"],
                bg_color_hover = self.themes["app_color"]["regular_icon"]["icon_bg_hover"],
                bg_color_pressed = self.themes["app_color"]["regular_icon"]["icon_bg_pressed"],

            )
        self._parent.ui.load_pages.verticalLayout_12.addWidget(self.add_IconButton, Qt.AlignCenter, Qt.AlignCenter)
        self.add_IconButton.clicked.connect(self.ui_click_callback)

        self.save_IconButton = PyIconButton_simple(
                icon = "fi-rr-edit.svg",
                icon_active = "fi-rr-edit.svg",
                icon_hover = "fi-rr-edit.svg",
                icon_deactive = "fi-rr-edit-deactive.svg",
                btn_id = "保存",
                tooltip_text = "編集",
                width = 30,
                height = 30,
                bg_color = self.themes["app_color"]["regular_icon"]["icon_bg"],
                bg_color_hover = self.themes["app_color"]["regular_icon"]["icon_bg_hover"],
                bg_color_pressed = self.themes["app_color"]["regular_icon"]["icon_bg_pressed"],
            )
        self._parent.ui.load_pages.verticalLayout_13.addWidget(self.save_IconButton, Qt.AlignCenter, Qt.AlignCenter)
        self.save_IconButton.clicked.connect(self.ui_click_callback)
        

        self._parent.ui.load_pages.patternfile_comboBox.currentIndexChanged.connect(self.ui_click_callback)
        self._parent.ui.load_pages.commect_lineEdit.textChanged.connect(self.ui_click_callback)
        self._parent.ui.load_pages.gas_Combobox.currentIndexChanged.connect(self.ui_click_callback)
        self._parent.ui.load_pages.RT_combobox.currentIndexChanged.connect(self.ui_click_callback)
        self._parent.ui.load_pages.RT_testpattern_combobox.currentIndexChanged.connect(self.ui_click_callback)
        
        
    # update step widge
    # /////////////////////////////
    def updata_step_widge(self):
        #print("updata_step_widge_work")
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
                self.step_widges_list[_step].pattern.Hour_lineEdit.setText("{}".format(unit.time_hour))
                self.step_widges_list[_step].pattern.Min_lineEdit.setText("{}".format(unit.time_min))
                self.step_widges_list[_step].pattern.SV_lineEdit.setText("{}".format(unit.SV))
                self.step_widges_list[_step].pattern.N2_lineEdit.setText("{}".format(unit.N2_flowRate*0.1))
                self.step_widges_list[_step].pattern.PID_muffle_comboBox.setCurrentIndex(unit.PID_muffle_No)
                self.step_widges_list[_step].pattern.PID_heater_comboBox.setCurrentIndex(unit.PID_heater_No)

                self.step_widges_list[_step].pattern.Sp_limit_up_lineEdit.setText("{}".format(unit.sp_limit_up))
                self.step_widges_list[_step].pattern.Sp_limit_down_lineEdit.setText("{}".format(unit.sp_limit_down))
                self.step_widges_list[_step].pattern.Shift_lineEdit.setText("{}".format(unit.shift))

                pass
            elif unit.Step_Type==tempUnit.test_unit_type:  #test unit
                self.step_widges_list[_step].pattern.SV_lineEdit.setText("{}".format(unit.SV))
                self.step_widges_list[_step].pattern.PID_muffle_comboBox.setCurrentIndex(unit.PID_muffle_No)
                self.step_widges_list[_step].pattern.PID_heater_comboBox.setCurrentIndex(unit.PID_heater_No)
                self.step_widges_list[_step].pattern.KeepTime_lineEdit.setText("{}".format(unit.time_keep))

                self.step_widges_list[_step].pattern.Sp_limit_up_lineEdit.setText("{}".format(unit.sp_limit_up))
                self.step_widges_list[_step].pattern.Sp_limit_down_lineEdit.setText("{}".format(unit.sp_limit_down))
                self.step_widges_list[_step].pattern.Shift_lineEdit.setText("{}".format(unit.shift))

                self.step_widges_list[_step].update_testFileCombobox(unit.test_measure_PatternNo)
                #self.step_widges_list[_step].pattern.TestPattern_comboBox.setCurrentIndex(unit.test_measure_PatternNo)
                pass
            elif unit.Step_Type==tempUnit.End_unit_type:  #End unit
                pass
        
        
        #print("updata_step_widge_work finish")
        
    # update graph
    # /////////////////////////////
    def update_graph(self):
        #self.update_graph_Worker=update_graph_Thread(self)
        #QThreadPool.globalInstance().start(self.update_graph_Worker)

        update_graph_Thread = threading.Thread(target = self.update_graph_work,daemon=True)
        update_graph_Thread.start()

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


        if btn_name=="削除":
            self.patternFile_Delete()
        elif btn_name=="保存":
            self.patternFile_Save()
        elif btn_name=="追加":
            self.patternFile_New()

        elif btn_name=="patternfile_comboBox":
            
            if self.content_Change:
                
                result=self.lunchOptionDialog("変更内容は未保存です。内容を保存しますか",PyDialog.warning_3_type)

                if result=="Yes":
                    #User is want to save file
                    self.patternFile_Save_work()
                    
                elif result=="No":
                    #User is do not want to save file
                    pass

                elif result=="Cancel":
                    #User is not want Delete file
                    self._parent.ui.load_pages.patternfile_comboBox.currentIndexChanged.disconnect()
                    self._parent.ui.load_pages.patternfile_comboBox.setCurrentIndex(self.focus_patternFile_number-1)
                    self._parent.ui.load_pages.patternfile_comboBox.currentIndexChanged.connect(self.ui_click_callback)
                    return

            
            self.focus_patternFile_number=self._parent.ui.load_pages.patternfile_comboBox.currentIndex()+1
            
            self.patternFile_Load()

        elif btn_name=="commect_lineEdit":
            self.cache_steplist.set_Comment(self._parent.ui.load_pages.commect_lineEdit.text())
            
            #self.update_Request=True
            self.update()

        elif btn_name=="gas_Combobox":
            self.cache_steplist.set_gas_condition(self._parent.ui.load_pages.gas_Combobox.currentIndex()+1)
            
            #self.update_Request=True
            self.update()

        elif btn_name=="RT_combobox":
            self.cache_steplist.set_RT_measure(self._parent.ui.load_pages.RT_combobox.currentIndex()+1)
            
            #self.update_Request=True
            self.update()

        elif btn_name=="RT_testpattern_combobox": 
            self.cache_steplist.set_RT_testpattern(self._parent.ui.load_pages.RT_testpattern_combobox.currentIndex()+1)
            
            self.update()
        
        
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

        
        #self.update_Request=True
        self.update()

    def patternFile_Delete(self):

        result=self.lunchOptionDialog("温度パターン \"{}\" 削除しますか？".format(self.patternFile_nameList[self.focus_patternFile_number-1]),PyDialog.warning_2_type)

        if result=="No":
            return

        self.availlible_patternFile_count-=1
        self.set_memorypool_register("Modbus Registor Pool - Registor","有効PTN総数",self.availlible_patternFile_count)

        self.patternFiles.append(templist())
        self.patternFiles.pop(self.focus_patternFile_number)

        if self.focus_patternFile_number>self.availlible_patternFile_count:
            self.focus_patternFile_number=self.availlible_patternFile_count

        if self.focus_patternFile_number:
            self.cache_steplist=self.patternFiles[self.focus_patternFile_number]
        else:
            self.cache_steplist=templist()

        self.memory_writer()
        self.patternFile_Load()

        
    def patternFile_Save(self):
        self.patternFile_Save_Worker=patternFile_Save_Thread(self)
        QThreadPool.globalInstance().start(self.patternFile_Save_Worker)


    def patternFile_Save_work(self):
        #Refresh patternFiles

        self.patternFiles[self.focus_patternFile_number]=copy.deepcopy(self.cache_steplist)
        
        
        list=self.cache_steplist
        
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_0".format(self.focus_patternFile_number),list.asciicode_0)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_1".format(self.focus_patternFile_number),list.asciicode_1)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_2".format(self.focus_patternFile_number),list.asciicode_2)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_名称_3".format(self.focus_patternFile_number),list.asciicode_3)


        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_註記".format(self.focus_patternFile_number),list.comment)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_パターン有効".format(self.focus_patternFile_number),list.active)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_実行STEP数".format(self.focus_patternFile_number),list.step_number-1)


        if list.gas_condition==1:
            gas=1
        elif list.gas_condition==2:
            gas=2
        elif list.gas_condition==3:
            gas=4
        else:
            gas=0


        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_測定雰囲気".format(self.focus_patternFile_number),gas)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_RT計測".format(self.focus_patternFile_number),list.RT_measure)
        self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_RT測定パターン".format(self.focus_patternFile_number),list.RT_testpattern)
        
        for step in range(1,21):
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_SV値".format(self.focus_patternFile_number,step),list.units[step].SV)
            
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_ステップ所要時間".format(self.focus_patternFile_number,step),list.units[step].step_time)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_ステップ累計時間".format(self.focus_patternFile_number,step),list.units[step].total_time)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_時間_時".format(self.focus_patternFile_number,step),list.units[step].time_hour)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_時間_分".format(self.focus_patternFile_number,step),list.units[step].time_min)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_キープ時間".format(self.focus_patternFile_number,step),list.units[step].time_keep)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_スレーブSP上限".format(self.focus_patternFile_number,step),list.units[step].sp_limit_up)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_スレーブSP下限".format(self.focus_patternFile_number,step),list.units[step].sp_limit_down)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_シフト".format(self.focus_patternFile_number,step),list.units[step].shift)


            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_N2流量".format(self.focus_patternFile_number,step),list.units[step].N2_flowRate)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_マッフル_PID_No".format(self.focus_patternFile_number,step),list.units[step].PID_muffle_No)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_ヒーター_PID_No".format(self.focus_patternFile_number,step),list.units[step].PID_heater_No)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(self.focus_patternFile_number,step),list.units[step].test_measure_enable)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定パターン".format(self.focus_patternFile_number,step),list.units[step].test_measure_PatternNo)
            self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP種類".format(self.focus_patternFile_number,step),list.units[step].Step_Type)

            if step<=list.step_number:
                if list.units[step].Step_Type==tempUnit.temp_unit_type:
                    self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP情報".format(self.focus_patternFile_number,step),2)
                    self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(self.focus_patternFile_number,step),0)

                elif list.units[step].Step_Type==tempUnit.test_unit_type:
                    self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP情報".format(self.focus_patternFile_number,step),2)
                    self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(self.focus_patternFile_number,step),1)
                elif list.units[step].Step_Type==tempUnit.End_unit_type:
                    self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP情報".format(self.focus_patternFile_number,step),1)
                    self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(self.focus_patternFile_number,step),0)
            else:
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_STEP情報".format(self.focus_patternFile_number,step),0)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PTNData_{}_STEP_{}_測定有".format(self.focus_patternFile_number,step),0)




        
        
        #Reload cache_list from memory
        self.patternFile_Load()

    def patternFile_New(self):
        NameString_fromDialog=""

        if self.content_Change:
            result=self.lunchOptionDialog("変更内容は未保存です。保存してから新規作成しますか？",PyDialog.warning_3_type)

            if result=="Yes":
                #User is not want Delete file
                self.patternFile_Save_work()
                NameString_fromDialog=self.lunchMessageDialog("新規パターン作成","新規ファイル名称入力 :")
                
            elif result=="No":
                #User is not want Delete file
                NameString_fromDialog=self.lunchMessageDialog("新規パターン作成","新規ファイル名称入力 :")

            elif result=="Cancel":
                #User is not want Delete file
                return

        else:
            NameString_fromDialog=self.lunchMessageDialog("新規パターン作成","新規ファイル名称入力 :")

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

    def set_memorypool_register(self,pool_name,registor_name,value):
        
        if self._parent.MMG.memoryPool[pool_name][registor_name].getValue()!=value:
            self._parent.MMG.memoryPool[pool_name][registor_name].setValue(value)
            sendItem=MemoryUnit(pool_name,registor_name)
            self.queuePool["memory_UploadToMaster_Queue"].put(sendItem)

    def ultility_Update_Work(self):
        
        #print("self.test1 = ",self.test1)
        #self.test1+=1
        #while 1:
        #    time.sleep(0.1)

            #if time.time()-self.test >0.2 and time.time()-self.test <1000:
            #    print("Temp lag occur time = ",time.time()-self.test)

            #self.test=time.time()

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
            self.un_focus_step(self.focus_step_number)
            self.cache_steplist.step_number-=1

            #print("pattern_menu_delete ",self.focus_step_number)
            pass


        self.close_menu()
        #self.update_Request=True
        self.update()

    def focus_step(self,_step):
        self.step_widges_list[_step].setFocusStyle(True)
        self.GraphRegionList[_step].setFocusStyle(True)
        self.focus_step_number=_step

    def un_focus_step(self,_step):
        self.step_widges_list[_step].setFocusStyle(False)
        self.GraphRegionList[_step].setFocusStyle(False)
        
        if self.focus_step_number==_step:
            self.focus_step_number=1

    def close_menu(self):
        for step in range(1,21):
            self.step_widges_list[step]._menu.menu_frame.hide()

    def close_one_menu(self,step):
        self.step_widges_list[step]._menu.menu_frame.hide()

    def content_change_check(self):

        #total time calculate
        for step in range(1,self.cache_steplist.step_number+1):

            self.cache_steplist.units[step].step_time  =(self.cache_steplist.units[step].time_hour*60)+self.cache_steplist.units[step].time_min

            if step==1:
                self.cache_steplist.units[step].total_time=self.cache_steplist.units[step].step_time
            else:
                self.cache_steplist.units[step].total_time=self.cache_steplist.units[step].step_time+self.cache_steplist.units[step-1].total_time

        #Temp_Totaltime_Label
        if self.cache_steplist.step_number!=0:
            self.cache_steplist.total_time=self.cache_steplist.units[self.cache_steplist.step_number].total_time
        else:
            self.cache_steplist.total_time=0
        #print("content_change_check",self.cache_steplist.total_time)

        if (self.cache_steplist!=None and
            self.patternFiles[self.focus_patternFile_number]!=None
            ):
            self.content_Change=False

            if(
                self.cache_steplist.name            != self.patternFiles[self.focus_patternFile_number].name or
                self.cache_steplist.asciicode_0    != self.patternFiles[self.focus_patternFile_number].asciicode_0 or
                self.cache_steplist.asciicode_1    != self.patternFiles[self.focus_patternFile_number].asciicode_1 or
                self.cache_steplist.asciicode_2    != self.patternFiles[self.focus_patternFile_number].asciicode_2 or
                self.cache_steplist.asciicode_3    != self.patternFiles[self.focus_patternFile_number].asciicode_3 or

                self.cache_steplist.comment         != self.patternFiles[self.focus_patternFile_number].comment or
                self.cache_steplist.active          != self.patternFiles[self.focus_patternFile_number].active or
                self.cache_steplist.step_number     != self.patternFiles[self.focus_patternFile_number].step_number or
                self.cache_steplist.gas_condition   != self.patternFiles[self.focus_patternFile_number].gas_condition or
                self.cache_steplist.RT_measure      != self.patternFiles[self.focus_patternFile_number].RT_measure  or
                self.cache_steplist.RT_testpattern      != self.patternFiles[self.focus_patternFile_number].RT_testpattern 
                
                ):
                self.content_Change=True

        
            for step in range(1,21):

                cache_stepUnit=self.cache_steplist.getStep(step)
                memory_stepUnit=self.patternFiles[self.focus_patternFile_number].getStep(step)

                if(
                cache_stepUnit.Step_Type                !=memory_stepUnit.Step_Type or
                cache_stepUnit.SV                       !=memory_stepUnit.SV or
                float(cache_stepUnit.N2_flowRate)              !=float(memory_stepUnit.N2_flowRate) or
                cache_stepUnit.PID_muffle_No            !=memory_stepUnit.PID_muffle_No or
                cache_stepUnit.PID_heater_No            !=memory_stepUnit.PID_heater_No or
                cache_stepUnit.test_measure_enable      !=memory_stepUnit.test_measure_enable or
                cache_stepUnit.test_measure_PatternNo   !=memory_stepUnit.test_measure_PatternNo or
                cache_stepUnit.time_hour                !=memory_stepUnit.time_hour or
                cache_stepUnit.time_keep                !=memory_stepUnit.time_keep or
                cache_stepUnit.sp_limit_up                !=memory_stepUnit.sp_limit_up or
                cache_stepUnit.sp_limit_down                !=memory_stepUnit.sp_limit_down or
                cache_stepUnit.shift                !=memory_stepUnit.shift or
                cache_stepUnit.time_min                 !=memory_stepUnit.time_min
                ):
                    self.content_Change=True
                    #print("------------------------------------------------------------------")
                    #print()
                    #print()
                    #print("cache_stepUnit")
                    #print(cache_stepUnit.print_unit())
                    #print()
                    #print("memory_stepUnit")
                    #print(memory_stepUnit.print_unit())


    def step_modifly_manager(self,step):


        stepUnit=self.cache_steplist.getStep(step)

        stepUnit.Step_Type                          =self.step_widges_list[step]._type
        stepUnit.time_hour                          =self.step_widges_list[step]._hour
        stepUnit.time_min                           =self.step_widges_list[step]._minute
        stepUnit.SV                                     =self.step_widges_list[step]._temperature
        stepUnit.N2_flowRate                     =self.step_widges_list[step]._n2_flowrate
        stepUnit.PID_muffle_No                  =self.step_widges_list[step]._PID_muffle_no
        stepUnit.PID_heater_No                  =self.step_widges_list[step]._PID_heater_no
        stepUnit.time_keep                          =self.step_widges_list[step]._keep_seccond
        stepUnit.sp_limit_up                         =self.step_widges_list[step]._sp_limit_up
        stepUnit.sp_limit_down                     =self.step_widges_list[step]._sp_limit_down
        stepUnit.shift                                     =self.step_widges_list[step]._shift
        stepUnit.test_measure_PatternNo   =self.step_widges_list[step]._test_pattern

        self.cache_steplist.setStep(step,stepUnit)
        
        #self.update_Request=True
        self.update()
        

    def update(self):

        self.content_change_check()
        self.updata_step_widge()
        self.update_graph()
        self.utility_update()
        


    