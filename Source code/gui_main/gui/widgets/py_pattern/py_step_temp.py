# ///////////////////////////////////////////////////////////////
#
# BY: KOU IKUTETSU
# PROJECT MADE WITH: Qt Designer and PyQt5
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
import os
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui_main.qt_core import *
from .ui_temp_pattern import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.widgets import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.core.json_themes import Themes


from gui_main.system.profile_manager import *

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.core.functions import *

from .py_pattern_menu import *

import threading
import time


class modifly_callbackThread(QRunnable):
    def __init__(self, parent,sender):
        super().__init__()
        self.parent = parent
        self.sender=sender

    def run(self):
        self.parent.modifly_callbackWork(self.sender)

class PyTempStep(QWidget):

    #clicked = pyqtSignal(object)
    #released = pyqtSignal(object)

    Temp_Type  =    0
    Test_Type  =    1
    End_Type   =    2



    #timeframe_grayout="background-color: rgb(41,45,55);border-width: 1px;border-style: solid;border-radius: 5px;border-color: rgb(0, 0, 0);"
    #timeframe_normal="background-color: rgb(30,34,41);border-width: 1px;border-style: solid;border-radius: 5px;border-color: rgb(0, 0, 0);"

    #step_temp_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(200, 133, 0);border:none;"
    #step_test_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(73, 73, 220);border:none;"
    #step_end_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(0, 168, 123);border:none;"

    #time_gray_out_style="background-color: rgb(41,45,55);border:none;color: rgb(41,45,55);"
    #time_normal_style="background-color: rgb(30,34,41);border:none;color: rgb(225, 230, 241);"

    #label_gray_out_style="font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\"; color: rgb(91, 94, 98); border:none;"
    #label_normal_style="font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\"; color: rgb(225, 230, 241); border:none;"

    #line_gray_out_style="background-color: rgba(0, 0, 0,20);    color:  rgba(0, 0, 0,20);    border-width: 1px;    border-style: solid;    border-radius: 5px;    padding-left:5px;    padding-right:5px;    font: 12px \"游ゴシック\";"
    #line_normal_style="background-color: rgba(0, 0, 0,80);    color: rgb(225, 230, 241);    border-width: 1px;    border-style: solid;    border-radius: 5px;    padding-left:5px;    padding-right:5px;    font: 12px \"游ゴシック\";"

    def __init__(
        self , 
        parent = None,
        active = 1,
        step = 1,
        type = 0,
        temperature = 25,
        hour = 0,
        minute = 0,
        keep_seccond = 0,
        sp_limit_up = 0,
        sp_limit_down = 0,
        shift = 0,
        test_pattern = 0,
        n2_flowrate = 0,
        PID_muffle_no = 0,
        PID_heater_no = 0,
    ):
        super().__init__()
        # Parameter
        self._active = active
        self._step = step
        self._type = type
        self._hour = hour
        self._minute = minute
        self._temperature = temperature
        self._keep_seccond = keep_seccond
        self._sp_limit_up=sp_limit_up
        self._sp_limit_down=sp_limit_down
        self._shift=shift
        self._test_pattern = test_pattern
        self._n2_flowrate = n2_flowrate
        self._PID_muffle_no = PID_muffle_no
        self._PID_heater_no = PID_heater_no
        # Parent
        self._parent = parent
        
        # base prepare
        # ///////////////////////////////////////////////////////////////
        self.setFixedSize(200,380)
        self.pattern_frame = QFrame(self)
        self.pattern_frame.setContentsMargins(0,0,0,0)
        self.pattern = Ui_temp_pattern()
        self.pattern.setupUi( self.pattern_frame)
        self.pattern.page.setCurrentIndex(self._active)


        # icon_bottum_ui_setting
        # ///////////////////////////////////////////////////////////////
        self.icon_bottum_ui_setting()

        self.update_testFileCombobox(self._test_pattern)
        
        # Menu_setting
        # ///////////////////////////////////////////////////////////////
        self._menu=PyStepMenu(
            parent=self,
            app_parent=self._parent,
            step=self._step,
            parent_type="Temp type"

            )
        self._menu.menu_frame.move(60, 0)
        self._menu.menu_frame.hide()
        self.type_modifly_callback()


    def parameter_setting(self):
        self.pattern.Step_label.setText("STEP %d" %self._step)
        self.pattern.Type_comboBox.setCurrentIndex(self._type)
        self.pattern.Hour_lineEdit.setText(str(self._hour))
        self.pattern.Hour_lineEdit.setValidator(QIntValidator())
        self.pattern.Min_lineEdit.setText(str(self._minute))
        self.pattern.Min_lineEdit.setValidator(QIntValidator())
        self.pattern.SV_lineEdit.setText(str(self._temperature))
        self.pattern.SV_lineEdit.setValidator(QIntValidator())
        self.pattern.N2_lineEdit.setText("{}".format(self._n2_flowrate*0.1))
        self.pattern.N2_lineEdit.setValidator(QDoubleValidator(decimals=1))

        self.pattern.PID_muffle_comboBox.setCurrentIndex(self._PID_muffle_no)
        self.pattern.PID_heater_comboBox.setCurrentIndex(self._PID_heater_no)

        self.pattern.KeepTime_lineEdit.setText(str(self._keep_seccond))
        self.pattern.KeepTime_lineEdit.setValidator(QIntValidator())
        self.pattern.TestPattern_comboBox.setCurrentIndex(self._test_pattern)


    def icon_bottum_ui_setting(self):

        # Parameter_setting
        # ///////////////////////////////////////////////////////////////
        self.parameter_setting()

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        self.settings = Settings().items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        self.themes = Themes().items
        
        self.icon = PyIconButton_simple(
                icon = "fi-rr-plus-large.svg",
                icon_active = "fi-rr-plus-large.svg",
                icon_hover = "fi-rr-plus-large.svg",
                icon_deactive = "fi-rr-plus-large.svg",
                btn_id = "ステップ {} 追加".format(self._step),
                tooltip_text = "ステップ追加",
                width = 80,
                height = 80,
                bg_color = "rgb(44, 49, 60)",
                bg_color_hover = "rgb(63, 70, 86)",
                bg_color_pressed = "rgb(112, 125, 153)"
            )

        self.pattern.gridLayout_2.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)

        self.icon.clicked.connect(self.addStepBtn_presscallback)
        self.icon.released.connect(self.addStepBtn_releasecallback)

        self.icon.setObjectName("new_temp_Step_Buttom")

        self.menu_icon = PyIconButton_simple(
                icon = "fi-rr-menu-dots-vertical.svg",
                icon_active = "fi-rr-menu-dots-vertical.svg",
                icon_hover = "fi-rr-menu-dots-vertical.svg",
                icon_deactive = "fi-rr-menu-dots-vertical.svg",
                btn_id = "ステップ {} menu編集".format(self._step),
                tooltip_text = "編集",
                width = 30,
                height = 30,
                bg_color = "rgb(44, 49, 60)",
                bg_color_hover = "rgb(63, 70, 86)",
                bg_color_pressed = "rgb(112, 125, 153)"

            )
        self.pattern.gridLayout_6.addWidget(self.menu_icon, Qt.AlignCenter, Qt.AlignCenter)
        self.menu_icon.clicked.connect(self.show_menu)


        self.pattern.Type_comboBox.currentIndexChanged.connect(self.type_modifly_callback)
        self.pattern.Hour_lineEdit.editingFinished.connect(self.modifly_callback)
        self.pattern.Min_lineEdit.editingFinished.connect(self.modifly_callback)
        self.pattern.SV_lineEdit.editingFinished.connect(self.modifly_callback)
        self.pattern.N2_lineEdit.editingFinished.connect(self.modifly_callback)
        self.pattern.PID_muffle_comboBox.currentIndexChanged.connect(self.modifly_callback)
        self.pattern.PID_heater_comboBox.currentIndexChanged.connect(self.modifly_callback)
        self.pattern.KeepTime_lineEdit.editingFinished.connect(self.modifly_callback)
        self.pattern.Sp_limit_up_lineEdit.editingFinished.connect(self.modifly_callback)
        self.pattern.Sp_limit_down_lineEdit.editingFinished.connect(self.modifly_callback)
        self.pattern.Shift_lineEdit.editingFinished.connect(self.modifly_callback)
        self.pattern.TestPattern_comboBox.currentIndexChanged.connect(self.modifly_callback)

        

    def maxmin(self,max,min,data):
        if data>=max:
            return max,True
        elif data<=min:
            return min,True
        else:
            return data,False

    #When infomation is modifly by user , call back to this function
    def modifly_callback(self):
        if (self.sender==None):
            return
        
        try:
            #Close menu any way
            self._parent.tempPattern.close_menu()

        except AttributeError: #When self._parent.tempPattern is not initial yet
            return

        btn_name=self.sender().objectName()
        
        if btn_name=="Hour_lineEdit":
            data=int(self.pattern.Hour_lineEdit.text())
            self._hour,err=self.maxmin(59,0,data)
            if err:
                self.pattern.Hour_lineEdit.setText(str(self._hour))
            
        elif btn_name=="Min_lineEdit":
            data=int(self.pattern.Min_lineEdit.text())
            self._minute,err=self.maxmin(59,0,data)
            if err:
                self.pattern.Min_lineEdit.setText(str(self._minute))

        elif btn_name=="SV_lineEdit":
            data=int(self.pattern.SV_lineEdit.text())
            self._temperature,err=self.maxmin(800,0,data)
            if err:
                self.pattern.SV_lineEdit.setText(str(self._temperature))

        elif btn_name=="N2_lineEdit":
            data=float(self.pattern.N2_lineEdit.text())*10
            self._n2_flowrate,err=self.maxmin(1000,1,data)
            if err:
                self.pattern.N2_lineEdit.setText(str(self._n2_flowrate))


        elif btn_name=="PID_muffle_comboBox":
            self._PID_muffle_no=self.pattern.PID_muffle_comboBox.currentIndex()

        elif btn_name=="PID_heater_comboBox":
            self._PID_heater_no=self.pattern.PID_heater_comboBox.currentIndex()

        elif btn_name=="KeepTime_lineEdit":
            data=int(self.pattern.KeepTime_lineEdit.text())
            self._keep_seccond,err=self.maxmin(1000,0,data)
            if err:
                self.pattern.KeepTime_lineEdit.setText(str(self._keep_seccond))



        elif btn_name=="Sp_limit_up_lineEdit":
            data=int(self.pattern.Sp_limit_up_lineEdit.text())
            self._sp_limit_up,err=self.maxmin(1000,0,data)
            if err:
                self.pattern.Sp_limit_up_lineEdit.setText(str(self._sp_limit_up))

        elif btn_name=="Sp_limit_down_lineEdit":
            data=int(self.pattern.Sp_limit_down_lineEdit.text())
            self._sp_limit_down,err=self.maxmin(1000,0,data)
            if err:
                self.pattern.Sp_limit_down_lineEdit.setText(str(self._sp_limit_down))

        elif btn_name=="Shift_lineEdit":
            data=int(self.pattern.Shift_lineEdit.text())
            self._shift,err=self.maxmin(1000,0,data)
            if err:
                self.pattern.Shift_lineEdit.setText(str(self._shift))

        
        elif btn_name=="TestPattern_comboBox":
            self._test_pattern=self.pattern.TestPattern_comboBox.currentIndex()
        
        #Call upper mother renew information
        self._parent.tempPattern.step_modifly_manager(self._step)
    
        

    def type_modifly_callback(self):
        if (self.pattern.Type_comboBox.currentText()) == "昇降温":
            
            self._type=self.Temp_Type
            self.pattern.Step_label.setEnabled(True)
            
            self.pattern.Time_label.setEnabled(True)
            self.pattern.Hour_lineEdit.setEnabled(True)
            self.pattern.Hour_lineEdit.setReadOnly(False)
            self.pattern.Min_lineEdit.setEnabled(True)
            self.pattern.Min_lineEdit.setReadOnly(False)
            self.pattern.time_frame.setEnabled(True)

            self.pattern.SV_label.setEnabled(True)
            self.pattern.SV_lineEdit.setEnabled(True)
            self.pattern.SV_lineEdit.setReadOnly(False)

            self.pattern.N2_label.setEnabled(True)
            self.pattern.N2_lineEdit.setEnabled(True)
            self.pattern.N2_lineEdit.setReadOnly(False)
            
            self.pattern.PID_muffle_label.setEnabled(True)
            self.pattern.PID_muffle_comboBox.setEnabled(True)
            self.pattern.PID_heater_label.setEnabled(True)
            self.pattern.PID_heater_comboBox.setEnabled(True)
            
            self.pattern.KeepTime_label.setEnabled(False)
            self.pattern.KeepTime_lineEdit.setEnabled(False)
            self.pattern.KeepTime_lineEdit.setReadOnly(False)
            self.pattern.KeepTime_lineEdit.setText("0")
            
            self.pattern.Sp_limit_up_label.setEnabled(True)
            self.pattern.Sp_limit_up_lineEdit.setEnabled(True)
            self.pattern.Sp_limit_up_lineEdit.setReadOnly(False)

            self.pattern.Sp_limit_down_label.setEnabled(True)
            self.pattern.Sp_limit_down_lineEdit.setEnabled(True)
            self.pattern.Sp_limit_down_lineEdit.setReadOnly(False)

            self.pattern.Shift_label.setEnabled(True)
            self.pattern.Shift_lineEdit.setEnabled(True)
            self.pattern.Shift_lineEdit.setReadOnly(False)

            self.pattern.TestPattern_label.setEnabled(False)
            self.pattern.TestPattern_comboBox.setEnabled(False)

            self.update_testFileCombobox(0)
            
        elif (self.pattern.Type_comboBox.currentText()) == "測定":

            self._type=self.Test_Type
            self.pattern.Step_label.setEnabled(False)

            self.pattern.Time_label.setEnabled(True)
            self.pattern.Hour_lineEdit.setEnabled(True)
            self.pattern.Hour_lineEdit.setReadOnly(False)
            self.pattern.Min_lineEdit.setEnabled(True)
            self.pattern.Min_lineEdit.setReadOnly(False)
            self.pattern.time_frame.setEnabled(True)

            self.pattern.SV_label.setEnabled(True)
            self.pattern.SV_lineEdit.setEnabled(True)
            self.pattern.SV_lineEdit.setReadOnly(True)

            self.pattern.N2_label.setEnabled(True)
            self.pattern.N2_lineEdit.setEnabled(True)
            self.pattern.N2_lineEdit.setReadOnly(False)
            
            self.pattern.PID_muffle_label.setEnabled(True)
            self.pattern.PID_muffle_comboBox.setEnabled(True)
            self.pattern.PID_heater_label.setEnabled(True)
            self.pattern.PID_heater_comboBox.setEnabled(True)
            
            self.pattern.KeepTime_label.setEnabled(True)
            self.pattern.KeepTime_lineEdit.setEnabled(True)
            self.pattern.KeepTime_lineEdit.setReadOnly(False)
            
            self.pattern.Sp_limit_up_label.setEnabled(True)
            self.pattern.Sp_limit_up_lineEdit.setEnabled(True)
            self.pattern.Sp_limit_up_lineEdit.setReadOnly(False)

            self.pattern.Sp_limit_down_label.setEnabled(True)
            self.pattern.Sp_limit_down_lineEdit.setEnabled(True)
            self.pattern.Sp_limit_down_lineEdit.setReadOnly(False)

            self.pattern.Shift_label.setEnabled(True)
            self.pattern.Shift_lineEdit.setEnabled(True)
            self.pattern.Shift_lineEdit.setReadOnly(False)

            self.pattern.TestPattern_label.setEnabled(True)
            self.pattern.TestPattern_comboBox.setEnabled(True)

            self.update_testFileCombobox(0)

        elif (self.pattern.Type_comboBox.currentText()) == "END":

            self._type=self.End_Type
            self.pattern.Step_label.setEnabled(False)

            self.pattern.Time_label.setEnabled(False)
            self.pattern.time_frame.setEnabled(False)
            self.pattern.Hour_lineEdit.setEnabled(False)
            self.pattern.Hour_lineEdit.setReadOnly(False)
            self.pattern.Hour_lineEdit.setText("0")
            self.pattern.Min_lineEdit.setEnabled(False)
            self.pattern.Min_lineEdit.setReadOnly(False)
            self.pattern.Min_lineEdit.setText("0")

            self.pattern.SV_label.setEnabled(False)
            self.pattern.SV_lineEdit.setEnabled(False)
            self.pattern.SV_lineEdit.setReadOnly(False)
            self.pattern.SV_lineEdit.setText("0")

            self.pattern.N2_label.setEnabled(False)
            self.pattern.N2_lineEdit.setEnabled(False)
            self.pattern.N2_lineEdit.setReadOnly(False)
            self.pattern.N2_lineEdit.setText("0")
            
            self.pattern.PID_muffle_label.setEnabled(False)
            self.pattern.PID_muffle_comboBox.setEnabled(False)
            self.pattern.PID_heater_label.setEnabled(False)
            self.pattern.PID_heater_comboBox.setEnabled(False)
            
            self.pattern.KeepTime_label.setEnabled(False)
            self.pattern.KeepTime_lineEdit.setEnabled(False)
            self.pattern.KeepTime_lineEdit.setReadOnly(False)
            self.pattern.KeepTime_lineEdit.setText("0")
            
            self.pattern.Sp_limit_up_label.setEnabled(False)
            self.pattern.Sp_limit_up_lineEdit.setEnabled(False)
            self.pattern.Sp_limit_up_lineEdit.setReadOnly(False)
            self.pattern.Sp_limit_up_lineEdit.setText("0")

            self.pattern.Sp_limit_down_label.setEnabled(False)
            self.pattern.Sp_limit_down_lineEdit.setEnabled(False)
            self.pattern.Sp_limit_down_lineEdit.setReadOnly(False)
            self.pattern.Sp_limit_down_lineEdit.setText("0")

            self.pattern.Shift_label.setEnabled(False)
            self.pattern.Shift_lineEdit.setEnabled(False)
            self.pattern.Shift_lineEdit.setReadOnly(False)
            self.pattern.Shift_lineEdit.setText("0")

            self.pattern.TestPattern_label.setEnabled(False)
            self.pattern.TestPattern_comboBox.setEnabled(False)

            self.update_testFileCombobox(0)

        self.modifly_callback()


    def update_testFileCombobox(self,number=None):
        
        testFile_count=len(self._parent.testPattern.patternFile_nameList)
        if number==None:
            if self._test_pattern>testFile_count:
                self._test_pattern=testFile_count-1
            else:
                pass
        else:
            if number>testFile_count:
                self._test_pattern=testFile_count-1
            else:
                self._test_pattern=number

        self.pattern.TestPattern_comboBox.currentIndexChanged.disconnect()
        self.pattern.TestPattern_comboBox.clear()
        self.pattern.TestPattern_comboBox.addItems(self._parent.testPattern.patternFile_nameList)
        self.pattern.TestPattern_comboBox.setCurrentIndex(self._test_pattern)
        self.pattern.TestPattern_comboBox.currentIndexChanged.connect(self.modifly_callback)


    def addStepBtn_presscallback(self):
        self._parent.tempPattern.new_TempPattern()

    def addStepBtn_releasecallback(self):
        self._parent.tempPattern.scroll_adjust_TempPattern()

    def show_menu(self):
        if self._menu.menu_frame.isVisible():
            self._menu.menu_frame.hide()
        else:
            self._menu.paste_SetEnable(self._parent.tempPattern.paste_ready,self._parent.tempPattern.activeStep_noFull)
            self._menu.menu_frame.show()



    def mousePressEvent(self, event):
        self._parent.tempPattern.close_menu()


    def enterEvent(self, event):
        if self.pattern.page.currentIndex() ==1:
            self._parent.tempPattern.focus_step(self._step)

        
    def leaveEvent(self, event):
        if self.pattern.page.currentIndex() ==1:
            self._parent.tempPattern.un_focus_step(self._step)
            self._parent.tempPattern.close_one_menu(self._step)

    def paintEvent(self, event):
        pass


    def setFocusStyle(self,enable):
        if enable:
            self.pattern.frame_6. setFocus()

        else:
            self.pattern.frame_6.clearFocus()

    def enableEndType(self,enable):
        if enable:
            if self.pattern.Type_comboBox.count()==2:
                self.pattern.Type_comboBox.addItems(["END"])

        else:
            self.pattern.Type_comboBox.removeItem(2)

    

        

