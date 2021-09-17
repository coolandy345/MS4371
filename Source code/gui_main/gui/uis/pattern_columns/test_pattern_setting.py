
from gui_main.qt_core import *
from gui_main.gui.uis.windows.main_window import *
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *
from gui_main.gui.core.json_settings import Settings
from gui_main.gui.core.json_themes import Themes

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import threading

#from modbus_TcpServer import ModbusRegistorClass
import modbus_TcpServer
import time

import numpy as np
import pyqtgraph as pg


class testUnit():
    def __init__(
        self,
        Step_Type=0,
        voltage=0,
        ):
        self.Step_Type=Step_Type
        self.voltage=voltage
        
class testlist():
    def __init__(
        self,
        name="",
        comment="",
        step_number=0,
        test_time=0,
        test_sampletime=0,
        BG0_test_time=0,
        BG_test_time=0,
        BG_sampletime=0,

        ):
        
        self.name=name
        self.comment=comment
        self.step_number=step_number
        self.test_time=test_time
        self.test_sampletime=test_sampletime
        self.BG0_test_time=BG0_test_time
        self.BG_test_time=BG_test_time
        self.BG_sampletime=BG_sampletime
        self.units=[]
        for _step in range(1,10):
            self.units.append(testUnit())
      

class TestPatternWidget(QWidget):
    
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
        #threading.Timer(2,self.sayhi).start()
        super().__init__()
        self.step_widges_list=[]
        self._parent=parent
        self._app_parent=app_parent
        self.Step_number=0
        self.memory_pool=memory_pool
        self.pattern_lists=[]
        self.choose_step=choose_step
        self.choose_pattern=choose_pattern
        self.cache_step=testUnit()
        self.cache_steplist=testlist()

        self.memory_reader()
        self.setup_utility()
        self.setup_TempPattern()
        self.setup_TempGraph()
        self.load_list_From_Memory()
        self.updata_step_widge()


    def memory_reader(self):

        mudbusunit=modbus_TcpServer.ModbusPackage()
        Modbus_Registor_pool=self.memory_pool["Test Pattern Memory"]
        _20_pattern_lists=[None]
        
        for ptn_no in range(1,21):
            pattern=testlist(
                name            =Modbus_Registor_pool["PTNData_{}_名称".format(ptn_no)].value,
                step_number     =Modbus_Registor_pool["PTNData_{}_実行STEP数".format(ptn_no)].value,
                comment         =Modbus_Registor_pool["PTNData_{}_註記".format(ptn_no)].value,
                test_time       =Modbus_Registor_pool["PTNData_{}_測定時間".format(ptn_no)].value,
                test_sampletime =Modbus_Registor_pool["PTNData_{}_測定sampletime".format(ptn_no)].value,
                BG0_test_time    =Modbus_Registor_pool["PTNData_{}_BG0測定時間".format(ptn_no)].value,
                BG_test_time    =Modbus_Registor_pool["PTNData_{}_BG測定時間".format(ptn_no)].value,
                BG_sampletime   =Modbus_Registor_pool["PTNData_{}_BG測定sampletime".format(ptn_no)].value,
                )
            units=[None]
            for step_no in range(1,9):

                unit=testUnit(
                    Step_Type               =Modbus_Registor_pool["PTNData_{}_STEP_{}_STEP情報".format(ptn_no,step_no)].value,
                    voltage               =Modbus_Registor_pool["PTNData_{}_STEP_{}_電圧".format(ptn_no,step_no)].value,
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
        self._parent.ui.load_pages.gridLayout_44.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)
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
        self._parent.ui.load_pages.gridLayout_45.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)
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
        self._parent.ui.load_pages.gridLayout_43.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)
        self.icon.clicked.connect(self.ui_click_callback)


    def setup_TempPattern(self):
        self.step_widges_list=[None]
        
        for _step in range(1,21):
            temp_step = PyTestStep(
                active=False,
                step=_step,
                type=PyTestStep.Test_Type,
                parent = self._parent,
                app_parent=self._app_parent,
                )
            
            self.step_widges_list.append(temp_step)
            widge=self.step_widges_list[_step]            
            widge.setVisible (False)            
            self._parent.ui.load_pages.horizontalLayout_6.addWidget(widge)
        self._parent.ui.load_pages.scrollArea_4.setMinimumSize(QSize(0, 160))
        
    def setup_TempGraph(self):
        self.win1 =pg.PlotWidget(background=None,title="予定パターン")
        
        self.win1.setLabel(axis='left', text='電圧', units='V')

        self.win1.setLimits(xMin=0.9,xMax=20.9)
        self.axis = self.win1.getAxis('bottom')
        self.axis.setStyle(autoReduceTextSpace=False)
        self.axis.setTickSpacing(1,1)
        self.win1.setAxisItems({'bottom':self.axis})

        self.axis = self.win1.getAxis('left')
        self.axis.enableAutoSIPrefix(False)
        
        self.win1.showGrid(x=True, y=True)
        self.win1.setMouseEnabled(x=False, y=False)

        #self.win1.addLegend()

        #self.win1.setMinimumSize(QSize(1100, 300))

        self.win1.plot(x=[1,2,2,3,3,4,4,5,5,6,7,8,9,10],y=[0,0,2000,2000,0,0,-2000,-2000,0,0,0,0,0,0],pen=pg.mkPen((65,74,88), width=10), symbolBrush=(0,200,200),symbolPen='w', symbol='o', symbolSize=5, name="予定パターン")
        
        self._parent.ui.load_pages.horizontalLayout_5.addWidget(self.win1, Qt.AlignCenter, Qt.AlignCenter)
        
        

        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        self.win1.setSizePolicy(sizePolicy1)


        #self._parent.ui.load_pages.horizontalLayout_5.update()
        
        


        
     
    def new_TestPattern(self):
        
        self.cache_steplist.units[self.cache_steplist.step_number]=testUnit()
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

        for _step in range(1,9):
            if _step<=self.cache_steplist.step_number :
                self.step_widges_list[_step].setVisible (True)
                self.step_widges_list[_step].pattern.page.setCurrentIndex(True)
            else:
                self.step_widges_list[_step].setVisible (False)
                self.step_widges_list[_step].pattern.page.setCurrentIndex(False)
            unit=testUnit()
            unit=self.cache_steplist.units[_step]
            index=unit.Step_Type
            self.step_widges_list[_step].pattern.Type_comboBox.setCurrentIndex(index)
            
            if index==0:    #test unit
                self.step_widges_list[_step].pattern.SV_lineEdit.setValue(unit.voltage)
                pass
            elif index==1:  #end unit
                pass

        if not self.cache_steplist.step_number ==8:
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
            print("test finish")
            self.timer.stop()

    def scroll_adjust_TestPattern(self):
        self._parent.ui.load_pages.scrollArea_4.horizontalScrollBar().setValue(self._parent.ui.load_pages.scrollArea_4.horizontalScrollBar().maximum())

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

        self.cache_steplist.units[step].Step_Type=self.step_widges_list[step]._type
        self.cache_steplist.units[step].voltage=self.step_widges_list[step]._voltage
        

    




    