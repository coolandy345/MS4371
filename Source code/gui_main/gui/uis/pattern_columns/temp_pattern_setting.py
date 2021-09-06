
from gui_main.qt_core import *
from gui_main.gui.uis.windows.main_window import *
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *
from gui_main.gui.core.json_settings import Settings
from gui_main.gui.core.json_themes import Themes
import threading

#from modbus_TcpServer import ModbusRegistorClass
import modbus_TcpServer
import time


class tempUnit():
    def __init__(
        self,
        SV=0,
        time_hour=0,
        time_min=0,
        time_keep=0,
        N2_flowRate=0,
        PID_No=0,
        test_measure=False,
        test_measure_PatternNo=0,
        cascade_control=False,
        end_step=False,
        Step_Type=0,
        Unit_type=0
        ):
        
        
        self.Step_Type=Step_Type
        self.SV=SV
        self.time_hour=time_hour
        self.time_min=time_min
        self.time_keep=time_keep
        self.N2_flowRate=N2_flowRate
        self.PID_No=PID_No
        self.cascade_control=cascade_control
        self.test_measure=test_measure
        self.test_measure_PatternNo=test_measure_PatternNo
        self.end_step=end_step
        
            
            
        


class templist():
    def __init__(
        self,
        name="",
        step_number=0,
        gas_condition=0,
        RT_measure=False,
        units=[]
        ):
        self.name=name
        self.step_number=step_number
        self.gas_condition=gas_condition
        self.RT_measure=RT_measure
        self.units=units
      


class TempPatternWidget(QWidget):
    
    def __init__( 
            self, 
            parent = None,
            app_parent = None,
            choose_step=0,
            choose_pattern=1,
            memory_pool={}
    ):
        #threading.Timer(1,self.sayhi).start()
        super().__init__()

        self.step_widges_list=[]
        self._parent=parent
        self._app_parent=app_parent
        self.setup_utility()
        self.setup_TempPattern()
        self.Step_number=0
        self.memory_pool=memory_pool
        self.pattern_lists=[]
        self.memory_reader()
        self.choose_step=choose_step
        self.choose_pattern=choose_pattern


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
                    SV              =Modbus_Registor_pool["PTNData_{}_STEP_{}_SV値".format(ptn_no,step_no)].value,
                    time_hour       =Modbus_Registor_pool["PTNData_{}_STEP_{}_時間_時".format(ptn_no,step_no)].value,
                    time_min        =Modbus_Registor_pool["PTNData_{}_STEP_{}_時間_分".format(ptn_no,step_no)].value,
                    time_keep       =Modbus_Registor_pool["PTNData_{}_STEP_{}_キープ時間".format(ptn_no,step_no)].value,
                    N2_flowRate     =Modbus_Registor_pool["PTNData_{}_STEP_{}_N2流量".format(ptn_no,step_no)].value,
                    PID_No          =Modbus_Registor_pool["PTNData_{}_STEP_{}_PID No.".format(ptn_no,step_no)].value,
                    test_measure    =Modbus_Registor_pool["PTNData_{}_STEP_{}_測定有".format(ptn_no,step_no)].value,
                    #test_measure_PatternNo=Modbus_Registor_pool["PTNData_{}_STEP_{}_時間_分".format(ptn_no,step_no)].value,
                    cascade_control =Modbus_Registor_pool["PTNData_{}_STEP_{}_カスケード制御有".format(ptn_no,step_no)].value,
                    Step_Type       =Modbus_Registor_pool["PTNData_{}_STEP_{}_STEP情報".format(ptn_no,step_no)].value
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


            self.step_widges_list[_step].pattern.Type_comboBox.currentIndexChanged.connect(self.ui_click_callback)
            self.step_widges_list[_step].pattern.Hour_lineEdit.editingFinished.connect(self.ui_click_callback)
            self.step_widges_list[_step].pattern.Min_lineEdit.editingFinished.connect(self.ui_click_callback)
            self.step_widges_list[_step].pattern.Temp_lineEdit.editingFinished.connect(self.ui_click_callback)
            self.step_widges_list[_step].pattern.N2_lineEdit.editingFinished.connect(self.ui_click_callback)
            self.step_widges_list[_step].pattern.PID_comboBox.currentIndexChanged.connect(self.ui_click_callback)
            self.step_widges_list[_step].pattern.KeepTime_lineEdit.editingFinished.connect(self.ui_click_callback)
            self.step_widges_list[_step].pattern.TestPattern_comboBox.currentIndexChanged.connect(self.ui_click_callback)


        
    
    def new_TempPattern(self):
        self.pattern_lists[self.choose_pattern].step_number+=1
        self.updata_step_widge()


    
    # update step widge
    # /////////////////////////////
    def updata_step_widge(self):
        #adjust the Visible of each step
        

        for _step in range(1,21):

            if _step<=self.pattern_lists[self.choose_pattern].step_number :
                self.step_widges_list[_step].setVisible (True)
                self.step_widges_list[_step].pattern.page.setCurrentIndex(True)
            else:
                self.step_widges_list[_step].setVisible (False)
                self.step_widges_list[_step].pattern.page.setCurrentIndex(False)

            unit=tempUnit()
            unit=self.pattern_lists[self.choose_pattern].units[_step]
            index=unit.Step_Type
            self.step_widges_list[_step].pattern.Type_comboBox.setCurrentIndex(index)
            
            if index==0:    #temp unit
                self.step_widges_list[_step].pattern.Hour_lineEdit.setText("{}".format(unit.time_hour))
                self.step_widges_list[_step].pattern.Min_lineEdit.setText("{}".format(unit.time_min))
                self.step_widges_list[_step].pattern.Temp_lineEdit.setText("{}".format(unit.SV))
                self.step_widges_list[_step].pattern.N2_lineEdit.setText("{}".format(unit.N2_flowRate))
                self.step_widges_list[_step].pattern.PID_comboBox.setCurrentIndex(unit.PID_No)
                pass
            elif index==1:  #test unit
                self.step_widges_list[_step].pattern.KeepTime_lineEdit.setText("{}".format(unit.time_keep))
                self.step_widges_list[_step].pattern.TestPattern_comboBox.setCurrentIndex(unit.test_measure_PatternNo)
                pass
            elif index==2:  #End unit
                pass
            elif index==3:  #RT test 
                self.step_widges_list[_step].pattern.TestPattern_comboBox.setCurrentIndex(unit.test_measure_PatternNo)
                pass
        self.step_widges_list[1].pattern.Type_comboBox.clear()
        self.step_widges_list[1].pattern.Type_comboBox.addItems(["昇降温","測定","END","RT測定"])


        if not self.pattern_lists[self.choose_pattern].step_number ==20:
            self.step_widges_list[self.pattern_lists[self.choose_pattern].step_number+1].setVisible (True)
            self.step_widges_list[self.pattern_lists[self.choose_pattern].step_number+1].pattern.page.setCurrentIndex(False)
            

    def ui_click_callback(self):
        #self.updata_step_widge()
        print("click")
        pass

    #def sayhi(self):
    #    print("hi")
    #    threading.Timer(1, self.sayhi).start()

    def scroll_adjust_TempPattern(self):
        self._parent.ui.load_pages.scrollArea_3.horizontalScrollBar().setValue(self._parent.ui.load_pages.scrollArea_3.horizontalScrollBar().maximum())

    def menu_btn_handler(self,btn):
        if btn == "pattern_menu_cut_pushButton":
            self.temp_step_widges=self.step_widges_list[self.choose_step]
            print("step ",self.choose_step)
            self.step_widges_list.remove(self.step_widges_list[self.choose_step])
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
        #self.close_one_menu(step)
        if self.choose_step==step:
            self.close_menu()
            self.choose_step=0
        elif  self.choose_step==0:
            self.step_widges_list[step]._menu.menu_frame.show()
            self.choose_step=step
        else:
            self.close_menu()
            self.step_widges_list[step]._menu.menu_frame.show()
            self.choose_step=step
        

    




    