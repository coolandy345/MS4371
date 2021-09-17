
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
        self.memory_reader()
        self.setup_utility()
        self.setup_TempPattern()
        self.setup_TempGraph()
        self.load_list_From_Memory()
        self.updata_step_widge()

    

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
        self.win1 =pg.PlotWidget(background=None,title="予定パターン")
        
        self.win1.setLabel(axis='left', text='温度', units='℃')

        self.win1.setLimits(xMin=0.9,xMax=20.9)
        self.axis = self.win1.getAxis('bottom')
        self.axis.setStyle(autoReduceTextSpace=False)
        self.axis.setTickSpacing(1,1)
        self.win1.setAxisItems({'bottom':self.axis})
        
        self.axis = self.win1.getAxis('left')
        self.axis.enableAutoSIPrefix(False)
        
        self.win1.showGrid(x=True, y=True)
        self.win1.setMouseEnabled(x=True, y=False)

        #self.win1.addLegend()

        self.win1.setMinimumSize(QSize(1100, 300))
        self.win1.plot(x=[1,2,3,4,5,6,7,8],y=[0,0,10,10,30,30,0,0],pen=pg.mkPen((65,74,88), width=10), symbolBrush=(0,200,200),symbolPen='w', symbol='o', symbolSize=5, name="予定パターン")
        
        self._parent.ui.load_pages.horizontalLayout_4.addWidget(self.win1, Qt.AlignCenter, Qt.AlignCenter)
        


        
     
    def new_TempPattern(self):
        
        self.cache_steplist.units[self.cache_steplist.step_number]=tempUnit()
        self.cache_steplist.step_number+=1
        self.updata_step_widge()
        pass

    def load_list_From_Memory(self):
        
        
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
                self.step_widges_list[_step].setVisible (False)
                self.step_widges_list[_step].pattern.page.setCurrentIndex(False)

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
                self.step_widges_list[_step].pattern.KeepTime_lineEdit.setValue(unit.time_keep)
                self.step_widges_list[_step].pattern.TestPattern_comboBox.setCurrentIndex(unit.test_measure_PatternNo)
                pass
            elif index==2:  #End unit
                pass


        if not self.cache_steplist.step_number ==20:
            self.step_widges_list[self.cache_steplist.step_number+1].setVisible (True)
            self.step_widges_list[self.cache_steplist.step_number+1].pattern.page.setCurrentIndex(False)
            

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
            print("temp finish")
            self.timer.stop()

    def scroll_adjust_TempPattern(self):
        self._parent.ui.load_pages.scrollArea_3.horizontalScrollBar().setValue(self._parent.ui.load_pages.scrollArea_3.horizontalScrollBar().maximum())

    def menu_btn_handler(self,btn):

        
        if btn == "pattern_menu_cut_pushButton":
            self.cache_step=self.cache_steplist.units[self.choose_step]

            print("pattern_menu_cut ",self.choose_step)
            

            self.cache_steplist.step_number-=1
            self.cache_steplist.units.append(tempUnit())
            self.cache_steplist.units.remove(self.cache_steplist.units[self.choose_step])

            pass
        elif btn == "pattern_menu_copy_pushButton":
            pass
        elif btn == "pattern_menu_paste_pushButton":
            pass
        elif btn == "pattern_menu_rightinsert_pushButton":
            pass
        elif btn == "pattern_menu_leftinsert_pushButton":
            pass
        elif btn == "pattern_menu_rightinsertblank_pushButton":
            pass
        elif btn == "pattern_menu_leftinsertblank_pushButton":
            pass
        elif btn == "pattern_menu_delete_pushButton":
            pass
        self.close_menu()
        self.updata_step_widge()

    def close_menu(self):
        if not self.choose_step==0:
            self.step_widges_list[self.choose_step]._menu.menu_frame.hide()
            self.choose_step=0

    def show_one_menu(self,step):

        self.close_menu()

        if self.choose_step==step:
            self.choose_step=0
        elif  self.choose_step==0:
            self.step_widges_list[step]._menu.menu_frame.show()
            self.choose_step=step
        else:
            self.step_widges_list[step]._menu.menu_frame.show()
            self.choose_step=step

    def step_modifly_manager(self,step):

        self.cache_steplist.units[step].Step_Type=self.step_widges_list[step]._type#
        self.cache_steplist.units[step].time_hour=self.step_widges_list[step]._type
        self.cache_steplist.units[step].time_min=self.step_widges_list[step]._type
        self.cache_steplist.units[step].SV=self.step_widges_list[step]._type
        self.cache_steplist.units[step].N2_flowRate=self.step_widges_list[step]._type
        self.cache_steplist.units[step].PID_No=self.step_widges_list[step]._type
        self.cache_steplist.units[step].time_keep=self.step_widges_list[step]._type
        self.cache_steplist.units[step].test_measure_enable=self.step_widges_list[step]._type
        self.cache_steplist.units[step].test_measure_PatternNo=self.step_widges_list[step]._type
        
        

    




    