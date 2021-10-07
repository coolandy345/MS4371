
from gui_main.qt_core import *
from gui_main.gui.uis.windows.main_window import *
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



import numpy as np
import pyqtgraph as pg


class tempUnit():
    def __init__(
        self,
        Step_Type=0,
        time_hour=0,
        time_min=0,
        SV=0,
        N2_flowRate=0,
        PID_muffle_No=0,
        PID_heater_No=0,
        time_keep=0,
        test_measure_enable=0,
        test_measure_PatternNo=0,
        ):
        
        self.Step_Type=Step_Type
        self.time_hour=time_hour
        self.time_min=time_min
        self.SV=SV
        self.N2_flowRate=N2_flowRate
        self.PID_muffle_No=PID_muffle_No
        self.PID_heater_No=PID_heater_No
        self.time_keep=time_keep
        self.test_measure_enable=test_measure_enable
        self.test_measure_PatternNo=test_measure_PatternNo
        
            
        


class templist():
    def __init__(
        self,
        name="",
        step_number=0,
        gas_condition=0,
        RT_measure=False
        ):
        
        self.name=name
        self.step_number=step_number
        self.gas_condition=gas_condition
        self.RT_measure=RT_measure
        self.units=[]
        for _step in range(1,21):
            self.units.append(tempUnit())

    def checkData(self):

        for step in range(1,self.step_number+1):

            if(self.units[step].Step_Type==PyTempStep.Temp_Type):
                pass
            elif (self.units[step].Step_Type==PyTempStep.Test_Type):
                if not(step==0):
                    self.units[step].SV=self.units[step-1].SV
                pass
            elif (self.units[step].Step_Type==PyTempStep.End_Type):
                pass

        pass
    def checkRule(self):
        hasEndStep=False
        errorRule=""
        for step in range(1,self.step_number+1):
            if(self.units[step].Step_Type==PyTempStep.End_Type):
                hasEndStep=True
            
        if not hasEndStep:
            errorRule+="無効入力：Endステップは必要"

        return errorRule
    

    def getStep(self,step):
        unit=tempUnit()
        unit.Step_Type=self.units[step].Step_Type
        unit.SV=self.units[step].SV
        unit.N2_flowRate=self.units[step].N2_flowRate
        unit.PID_muffle_No=self.units[step].PID_muffle_No
        unit.PID_heater_No=self.units[step].PID_heater_No
        unit.test_measure_enable=self.units[step].test_measure_enable
        unit.test_measure_PatternNo=self.units[step].test_measure_PatternNo
        unit.time_hour=self.units[step].time_hour
        unit.time_keep=self.units[step].time_keep
        unit.time_min=self.units[step].time_min

        return unit

    def setStep(self,step,input):

        self.units[step].Step_Type=input.Step_Type
        self.units[step].SV=input.SV
        self.units[step].N2_flowRate=input.N2_flowRate
        self.units[step].PID_muffle_No=input.PID_muffle_No
        self.units[step].PID_heater_No=input.PID_heater_No
        self.units[step].test_measure_enable=input.test_measure_enable
        self.units[step].test_measure_PatternNo=input.test_measure_PatternNo
        self.units[step].time_hour=input.time_hour
        self.units[step].time_keep=input.time_keep
        self.units[step].time_min=input.time_min

      


class TempPatternWidget(QWidget):
    
    def __init__( 
            self, 
            parent = None,
            app_parent = None,
            choose_step=0,
            choose_pattern=1,
            memory_pool={}
    ):
        #self.timer=QTimer()
        #self.timer.timeout.connect(self.sayhi)
        #self.timer.start(10)
        #threading.Timer(1,self.sayhi).start()
        super().__init__()

        self.step_widges_list=[]
        self._parent=parent
        self._app_parent=app_parent
        self.Step_number=0
        self.memory_pool=memory_pool
        self.pattern_lists=[]
        self.choose_step=choose_step
        self.choose_pattern=choose_pattern
        self.cache_step=tempUnit()
        self.cache_steplist=templist()

        self.paste_ready=False

        self.memory_reader()
        self.setup_utility()
        self.setup_TempPattern()
        self.setup_TempGraph()
        self.load_list_From_Memory()
        self.updata_step_widge()
        self.update_graph()

        self.step_widges_list[1].setVisible (True)
        self.step_widges_list[1].pattern.page.setCurrentIndex(False)
    

    def memory_reader(self):

        mudbusunit=modbus_TcpServer.ModbusPackage()
        Modbus_Registor_pool=self.memory_pool["Modbus Registor Memory"]
        _20_pattern_lists=[None]
        
        for ptn_no in range(1,21):
            pattern=templist(
                name            =Modbus_Registor_pool["PTNData_{}_名称".format(ptn_no)].value,
                step_number     =Modbus_Registor_pool["PTNData_{}_実行STEP数".format(ptn_no)].value,
                gas_condition   =Modbus_Registor_pool["PTNData_{}_測定雰囲気".format(ptn_no)].value,
                RT_measure      =Modbus_Registor_pool["PTNData_{}_RT計測".format(ptn_no)].value
                )
            units=[None]
            
            for step_no in range(1,21):

                unit=tempUnit(
                    Step_Type               =Modbus_Registor_pool["PTNData_{}_STEP_{}_STEP情報".format(ptn_no,step_no)].value,
                    time_hour               =Modbus_Registor_pool["PTNData_{}_STEP_{}_時間_時".format(ptn_no,step_no)].value,
                    time_min                =Modbus_Registor_pool["PTNData_{}_STEP_{}_時間_分".format(ptn_no,step_no)].value,
                    SV                      =Modbus_Registor_pool["PTNData_{}_STEP_{}_SV値".format(ptn_no,step_no)].value,
                    N2_flowRate             =Modbus_Registor_pool["PTNData_{}_STEP_{}_N2流量".format(ptn_no,step_no)].value,
                    PID_muffle_No           =Modbus_Registor_pool["PTNData_{}_STEP_{}_マッフル_PID_No".format(ptn_no,step_no)].value,
                    PID_heater_No           =Modbus_Registor_pool["PTNData_{}_STEP_{}_ヒーター_PID_No".format(ptn_no,step_no)].value,
                    time_keep               =Modbus_Registor_pool["PTNData_{}_STEP_{}_キープ時間".format(ptn_no,step_no)].value,
                    #test_measure_enable     =Modbus_Registor_pool["PTNData_{}_STEP_{}_測定有".format(ptn_no,step_no)].value,
                    #test_measure_PatternNo  =Modbus_Registor_pool["PTNData_{}_STEP_{}_測定 No.".format(ptn_no,step_no)].value
                    )
                units.append(unit)
            pattern.units=units
            _20_pattern_lists.append(pattern)
        self.pattern_lists=_20_pattern_lists

    def setup_utility(self):
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        self.settings = Settings().items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        self.themes = Themes().items

        self.icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-trash.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                tooltip_text = "削除",
                width = 30,
                height = 30,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = "#ff5869",
                icon_color_hover = "#ff5869",
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = self.themes["app_color"]["dark_one"],
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["green"],
            )
        self._parent.ui.load_pages.gridLayout_34.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)
        self.icon.clicked.connect(self.ui_click_callback)

        self.icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-file-add.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                tooltip_text = "追加",
                width = 30,
                height = 30,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = self.themes["app_color"]["dark_one"],
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["green"],
            )
        self._parent.ui.load_pages.gridLayout_35.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)
        self.icon.clicked.connect(self.ui_click_callback)

        self.icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-edit.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                tooltip_text = "保存",
                width = 30,
                height = 30,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = self.themes["app_color"]["dark_one"],
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["green"],
            )
        self._parent.ui.load_pages.gridLayout_36.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)
        self.icon.clicked.connect(self.ui_click_callback)

        self.RT_MeasurementToggle=PyToggle()
        self._parent.ui.load_pages.gridLayout_37.addWidget(self.RT_MeasurementToggle, Qt.AlignCenter, Qt.AlignCenter)

    def setup_TempPattern(self):
        self.step_widges_list=[None]
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

        self.cache_steplist.units[self.cache_steplist.step_number+1]=tempUnit()
        self.cache_steplist.step_number+=1

        self.updata_step_widge()
        self.update_graph()

    def load_list_From_Memory(self):

        #Reset paste function
        self.paste_ready=False

        if(self.choose_pattern>=1 and self.choose_pattern<=20):
            self.cache_steplist=self.pattern_lists[self.choose_pattern]
        else:
            print("Choose list is out of range , now is choose No.",self.choose_pattern)
        
    # update step widge
    # /////////////////////////////
    def updata_step_widge(self):
        #adjust the Visible of each step
        for _step in range(1,21):


            if _step<=self.cache_steplist.step_number :
                self.step_widges_list[_step].setVisible (True)
                self.step_widges_list[_step].pattern.page.setCurrentIndex(True)
            else:
                if _step==self.cache_steplist.step_number+1:
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

            if self.paste_ready:
                self.step_widges_list[_step]._menu.menu.pattern_menu_paste_pushButton.setEnabled(True)
            else:
                self.step_widges_list[_step]._menu.menu.pattern_menu_paste_pushButton.setEnabled(False)

            unit=tempUnit()
            unit=self.cache_steplist.units[_step]
            index=unit.Step_Type
            self.step_widges_list[_step].pattern.Type_comboBox.setCurrentIndex(index)
            if index==0:    #temp unit
                self.step_widges_list[_step].pattern.Hour_lineEdit.setValue(unit.time_hour)
                self.step_widges_list[_step].pattern.Min_lineEdit.setValue(unit.time_min)

                self.step_widges_list[_step].pattern.SV_lineEdit.setValue(unit.SV)
                self.step_widges_list[_step].pattern.N2_lineEdit.setValue(unit.N2_flowRate)
                self.step_widges_list[_step].pattern.PID_muffle_comboBox.setCurrentIndex(unit.PID_muffle_No)
                self.step_widges_list[_step].pattern.PID_heater_comboBox.setCurrentIndex(unit.PID_heater_No)

                pass
            elif index==1:  #test unit
                self.step_widges_list[_step].pattern.SV_lineEdit.setValue(unit.SV)
                self.step_widges_list[_step].pattern.PID_muffle_comboBox.setCurrentIndex(unit.PID_muffle_No)
                self.step_widges_list[_step].pattern.PID_heater_comboBox.setCurrentIndex(unit.PID_heater_No)
                self.step_widges_list[_step].pattern.KeepTime_lineEdit.setValue(unit.time_keep)
                self.step_widges_list[_step].pattern.TestPattern_comboBox.setCurrentIndex(unit.test_measure_PatternNo)
                pass
            elif index==2:  #End unit
                pass

        errormessage=self.cache_steplist.checkRule()
        self._parent.ui.load_pages.PatternErrorMessagelabel.setText(errormessage)

    def update_graph(self):

        data_array=[{"x":1,"y":0}]
        SV_array=[0]
        for _step in range(1,21):
            if _step<=self.cache_steplist.step_number:
                #load Graph data
                xy_dot={}
                unit=self.cache_steplist.units[_step]
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
        
        



    def ui_click_callback(self):
        #self.updata_step_widge()
        #print("click")
        pass

    def sayhi(self):
        self.axis = self.win1.getAxis('left')
        self.axis.label.setRotation(0)
        self.axis.label.setPos(-40,110)
        self.win1.setPos(50,6)
        if self.win1.isVisible():
            self.timer.stop()

    def scroll_adjust_TempPattern(self):
        self._parent.ui.load_pages.scrollArea_3.horizontalScrollBar().setValue(self._parent.ui.load_pages.scrollArea_3.horizontalScrollBar().maximum())

    def menu_btn_handler(self,btn):

        if btn == "pattern_menu_cut_pushButton":
            self.cache_step=self.cache_steplist.getStep(self.choose_step)
            self.cache_steplist.step_number-=1
            self.cache_steplist.units.append(tempUnit())
            self.cache_steplist.units.pop(self.choose_step)
            self.paste_ready=True
            #print("pattern_menu_cut ",self.choose_step)
            pass

        elif btn == "pattern_menu_copy_pushButton":

            self.cache_step=self.cache_steplist.getStep(self.choose_step)
            self.paste_ready=True

            #print("pattern_menu_copy ",self.choose_step)
            pass

        elif btn == "pattern_menu_paste_pushButton":
            if self.paste_ready:
                self.cache_steplist.setStep(self.choose_step,self.cache_step)
            #print("pattern_menu_paste ",self.choose_step)
            pass

        elif btn == "pattern_menu_rightinsert_pushButton":
            if not self.cache_steplist.step_number==20:
                if self.paste_ready:
                    self.cache_steplist.units.pop(20)
                    self.cache_steplist.units.insert(self.choose_step+1,tempUnit())
                    self.cache_steplist.setStep(self.choose_step+1,self.cache_step)
                    self.cache_steplist.step_number+=1
            #print("pattern_menu_rightinsert ",self.choose_step)
            pass

        elif btn == "pattern_menu_leftinsert_pushButton":
            if not self.cache_steplist.step_number==20:
                if self.paste_ready:
                    self.cache_steplist.units.pop(20)
                    self.cache_steplist.units.insert(self.choose_step,tempUnit())
                    self.cache_steplist.setStep(self.choose_step,self.cache_step)
                    self.cache_steplist.step_number+=1
            #print("pattern_menu_leftinsert ",self.choose_step)
            pass

        elif btn == "pattern_menu_rightinsertblank_pushButton":
            if not self.cache_steplist.step_number==20:
                self.cache_steplist.units.pop(20)
                self.cache_steplist.units.insert(self.choose_step+1,tempUnit())
                self.cache_steplist.step_number+=1
            #print("pattern_menu_rightinsertblank ",self.choose_step)
            pass

        elif btn == "pattern_menu_leftinsertblank_pushButton":
            if not self.cache_steplist.step_number==20:
                self.cache_steplist.units.pop(20)
                self.cache_steplist.units.insert(self.choose_step,tempUnit())
                self.cache_steplist.step_number+=1
            #print("pattern_menu_leftinsertblank ",self.choose_step)
            pass

        elif btn == "pattern_menu_delete_pushButton":
            self.cache_steplist.units.append(tempUnit())
            self.cache_steplist.units.pop(self.choose_step)
            self.cache_steplist.step_number-=1
            #print("pattern_menu_delete ",self.choose_step)
            pass

        self.close_menu()
        self.updata_step_widge()
        self.update_graph()

    def focus_step(self,_step):
        self.step_widges_list[_step].setFocusStyle(True)
        self.GraphRegionList[_step].setFocusStyle(True)
        self.choose_step=_step
        #self.updata_step_widge()
        #self.update_graph()

    def un_focus_step(self,_step):
        self.step_widges_list[_step].setFocusStyle(False)
        self.GraphRegionList[_step].setFocusStyle(False)
        if self.choose_step==_step:
            self.choose_step=0
            #self.updata_step_widge()
            #self.update_graph()
        #self.close_menu()

    def close_menu(self):
        for step in range(1,21):
            self.step_widges_list[step]._menu.menu_frame.hide()
        self.choose_step=0

    def show_one_menu(self,step):

        if self.step_widges_list[step]._menu.menu_frame.isVisible():
            self.close_menu()
        else:
            self.step_widges_list[step]._menu.menu_frame.show()
        

    def step_modifly_manager(self,step):
        self.cache_steplist.units[step].Step_Type=self.step_widges_list[step]._type
        self.cache_steplist.units[step].time_hour=self.step_widges_list[step]._hour
        self.cache_steplist.units[step].time_min=self.step_widges_list[step]._minute
        self.cache_steplist.units[step].SV=self.step_widges_list[step]._temperature
        self.cache_steplist.units[step].N2_flowRate=self.step_widges_list[step]._n2_flowrate
        self.cache_steplist.units[step].PID_muffle_No=self.step_widges_list[step]._PID_muffle_no
        self.cache_steplist.units[step].PID_heater_No=self.step_widges_list[step]._PID_heater_no
        self.cache_steplist.units[step].time_keep=self.step_widges_list[step]._keep_seccond
        self.cache_steplist.units[step].test_measure_PatternNo=self.step_widges_list[step]._test_pattern
        
        self.cache_steplist.checkData()
        
        self.updata_step_widge()
        self.update_graph()
        
    def graphResize(self):
        addwidth=self._parent.width()-1470
        self.graph.setMinimumSize(QSize(1100+addwidth, 300))
        pass

    




    