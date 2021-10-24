# ///////////////////////////////////////////////////////////////
#
# BY: KOU IKUTETSU
# PROJECT MADE WITH: Qt Designer and PySide6
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

    #clicked = Signal(object)
    #released = Signal(object)

    Temp_Type  =    0
    Test_Type  =    1
    End_Type   =    2



    timeframe_grayout="background-color: rgb(41,45,55);border-width: 1px;border-style: solid;border-radius: 5px;border-color: rgb(0, 0, 0);"
    timeframe_normal="background-color: rgb(30,34,41);border-width: 1px;border-style: solid;border-radius: 5px;border-color: rgb(0, 0, 0);"

    step_temp_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(200, 133, 0);border:none;"
    step_test_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(73, 73, 220);border:none;"
    step_RTtest_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(53 ,206, 220);border:none;"
    step_end_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(0, 168, 123);border:none;"

    time_gray_out_style="background-color: rgb(41,45,55);border:none;color: rgb(41,45,55);"
    time_normal_style="background-color: rgb(30,34,41);border:none;color: rgb(225, 230, 241);"

    label_gray_out_style="font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\"; color: rgb(91, 94, 98); border:none;"
    label_normal_style="font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\"; color: rgb(225, 230, 241); border:none;"

    line_gray_out_style="background-color: rgba(0, 0, 0,20);    color:  rgba(0, 0, 0,20);    border-width: 1px;    border-style: solid;    border-radius: 5px;    padding-left:5px;    padding-right:5px;    font: 12px \"游ゴシック\";"
    line_normal_style="background-color: rgba(0, 0, 0,80);    color: rgb(225, 230, 241);    border-width: 1px;    border-style: solid;    border-radius: 5px;    padding-left:5px;    padding-right:5px;    font: 12px \"游ゴシック\";"

    focus_normal_style="border-color: rgb(231, 214, 85);background-color: rgb(44, 49, 60);border-width: 5px;    border-style: solid;    border-radius: 10px;"
    focus_gray_out_style="border-color: rgb(44, 49, 60);background-color: rgb(44, 49, 60);border-width: 5px;    border-style: solid;    border-radius: 10px;"
    

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
        self._test_pattern = test_pattern
        self._n2_flowrate = n2_flowrate
        self._PID_muffle_no = PID_muffle_no
        self._PID_heater_no = PID_heater_no
        # Parent
        self._parent = parent
        
        # base prepare
        # ///////////////////////////////////////////////////////////////
        self.setFixedSize(200,300)
        self.pattern_frame = QFrame(self)
        self.pattern_frame.setContentsMargins(0,0,0,0)
        self.pattern = Ui_temp_pattern()
        self.pattern.setupUi( self.pattern_frame)
        self.pattern.page.setCurrentIndex(self._active)

        self.FocusStyleChange=False
        self.FocusStyle=self.focus_gray_out_style
        self.timer=QTimer()
        self.timer.timeout.connect(self.focus_Style_Work)
        self.timer.start(100)

        focus_Style_Thread = threading.Thread(target = self.focus_Style_Work,daemon=True)
        focus_Style_Thread.start()

        
        # Parameter_setting
        # ///////////////////////////////////////////////////////////////
        self.parameter_setting()
        
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






    def focus_Style_Work(self):
        #while 1:
            #time.sleep(0.1)
        if self.FocusStyleChange:
            self.pattern.page.setStyleSheet(self.FocusStyle)
            self.FocusStyleChange=False


    def parameter_setting(self):
        self.pattern.Step_label.setText("STEP %d" %self._step)
        self.pattern.Type_comboBox.setCurrentIndex(self._type)
        self.pattern.Hour_lineEdit.setValue(self._hour)
        self.pattern.Min_lineEdit.setValue(self._minute)
        self.pattern.SV_lineEdit.setValue(self._temperature)
        self.pattern.N2_lineEdit.setValue(self._n2_flowrate)

        self.pattern.PID_muffle_comboBox.setCurrentIndex(self._PID_muffle_no)
        self.pattern.PID_heater_comboBox.setCurrentIndex(self._PID_heater_no)

        self.pattern.KeepTime_lineEdit.setValue(self._keep_seccond)
        self.pattern.TestPattern_comboBox.setCurrentIndex(self._test_pattern)


    def icon_bottum_ui_setting(self):
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
        self.pattern.Hour_lineEdit.valueChanged.connect(self.modifly_callback)
        self.pattern.Min_lineEdit.valueChanged.connect(self.modifly_callback)
        self.pattern.SV_lineEdit.valueChanged.connect(self.modifly_callback)
        self.pattern.N2_lineEdit.valueChanged.connect(self.modifly_callback)
        self.pattern.KeepTime_lineEdit.valueChanged.connect(self.modifly_callback)
        self.pattern.TestPattern_comboBox.currentIndexChanged.connect(self.modifly_callback)

        self.pattern.PID_muffle_comboBox.currentIndexChanged.connect(self.modifly_callback)
        self.pattern.PID_heater_comboBox.currentIndexChanged.connect(self.modifly_callback)
        
    def modifly_callback(self):
        self.modifly_callbackWorker=modifly_callbackThread(self,self.sender())
        QThreadPool.globalInstance().start(self.modifly_callbackWorker)
        #self.modifly_callbackWorker.start()
    
    #When infomation is modifly by user , call back to this function
    def modifly_callbackWork(self,sender):
        if (sender==None):
            return
        
        try:
            #Close menu any way
            self._parent.tempPattern.close_menu()

        except AttributeError: #When self._parent.tempPattern is not initial yet
            return

        #print("click in side step after modifly STEP ", self._step," name = ",self.sender().objectName())
        self._hour=self.pattern.Hour_lineEdit.value()
        self._minute=self.pattern.Min_lineEdit.value()

        self._temperature=self.pattern.SV_lineEdit.value()
        self._n2_flowrate=self.pattern.N2_lineEdit.value()

        self._PID_muffle_no=self.pattern.PID_muffle_comboBox.currentIndex()
        self._PID_heater_no=self.pattern.PID_heater_comboBox.currentIndex()

        self._keep_seccond=self.pattern.KeepTime_lineEdit.value()
        self._test_pattern=self.pattern.TestPattern_comboBox.currentIndex()
        
        #Call upper mother renew information
        self._parent.tempPattern.step_modifly_manager(self._step)
    
        

    def type_modifly_callback(self):
        if (self.pattern.Type_comboBox.currentText()) == "昇降温":
            
            self._type=self.Temp_Type
            self.pattern.Step_label.setStyleSheet(self.step_temp_type_style)

            self.pattern.Hour_lineEdit.setEnabled(True)
            self.pattern.Hour_lineEdit.setStyleSheet(self.time_normal_style)
            self.pattern.Min_lineEdit.setEnabled(True)
            self.pattern.Min_lineEdit.setStyleSheet(self.time_normal_style)
            self.pattern.time_frame.setStyleSheet(self.timeframe_normal)
            self.pattern.Time_label.setStyleSheet(self.label_normal_style)
            self.pattern.label_4.setStyleSheet(self.time_normal_style)
            self.pattern.SV_lineEdit.setEnabled(True)
            self.pattern.SV_lineEdit.setStyleSheet(self.line_normal_style)
            self.pattern.SV_label.setStyleSheet(self.label_normal_style)
            self.pattern.N2_lineEdit.setEnabled(True)
            self.pattern.N2_lineEdit.setStyleSheet(self.line_normal_style)
            self.pattern.N2_label.setStyleSheet(self.label_normal_style)
            self.pattern.PID_muffle_comboBox.setEnabled(True)
            self.pattern.PID_muffle_comboBox.setStyleSheet(self.line_normal_style)
            self.pattern.PID_heater_comboBox.setEnabled(True)
            self.pattern.PID_heater_comboBox.setStyleSheet(self.line_normal_style)
            self.pattern.PID_muffle_label.setStyleSheet(self.label_normal_style)
            self.pattern.PID_heater_label.setStyleSheet(self.label_normal_style)
            self.pattern.KeepTime_lineEdit.setValue(0)
            self.pattern.KeepTime_lineEdit.setDisabled(True)
            self.pattern.KeepTime_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.KeepTime_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.TestPattern_comboBox.setDisabled(True)
            self.pattern.TestPattern_comboBox.setStyleSheet(self.line_gray_out_style)
            self.pattern.TestPattern_label.setStyleSheet(self.label_gray_out_style)
            self.update_testFileCombobox(0)
            
        elif (self.pattern.Type_comboBox.currentText()) == "測定":

            self._type=self.Test_Type
            self.pattern.Step_label.setStyleSheet(self.step_test_type_style)

            self.pattern.Hour_lineEdit.setEnabled(True)
            self.pattern.Hour_lineEdit.setStyleSheet(self.time_normal_style)
            self.pattern.Min_lineEdit.setEnabled(True)
            self.pattern.Min_lineEdit.setStyleSheet(self.time_normal_style)
            self.pattern.Time_label.setStyleSheet(self.label_normal_style)
            self.pattern.time_frame.setStyleSheet(self.timeframe_normal)
            self.pattern.label_4.setStyleSheet(self.time_normal_style)
            self.pattern.SV_lineEdit.setEnabled(False)
            self.pattern.SV_lineEdit.setStyleSheet(self.label_normal_style)
            self.pattern.SV_label.setStyleSheet(self.label_normal_style)
            
            self.pattern.N2_lineEdit.setEnabled(True)
            self.pattern.N2_lineEdit.setStyleSheet(self.line_normal_style)
            self.pattern.N2_label.setStyleSheet(self.label_normal_style)
            self.pattern.PID_muffle_comboBox.setEnabled(True)
            self.pattern.PID_muffle_comboBox.setStyleSheet(self.line_normal_style)
            self.pattern.PID_muffle_label.setStyleSheet(self.label_normal_style)
            self.pattern.PID_heater_comboBox.setEnabled(True)
            self.pattern.PID_heater_comboBox.setStyleSheet(self.line_normal_style)
            self.pattern.PID_heater_label.setStyleSheet(self.label_normal_style)


            self.pattern.KeepTime_lineEdit.setEnabled(True)
            self.pattern.KeepTime_lineEdit.setStyleSheet(self.line_normal_style)
            self.pattern.KeepTime_label.setStyleSheet(self.label_normal_style)
            self.pattern.TestPattern_comboBox.setEnabled(True)
            self.pattern.TestPattern_comboBox.setStyleSheet(self.line_normal_style)
            self.pattern.TestPattern_label.setStyleSheet(self.label_normal_style)
            self.update_testFileCombobox()

        elif (self.pattern.Type_comboBox.currentText()) == "END":

            self._type=self.End_Type
            self.pattern.Step_label.setStyleSheet(self.step_end_type_style)

            self.pattern.Hour_lineEdit.setValue(0)
            self.pattern.Hour_lineEdit.setEnabled(False)
            self.pattern.Hour_lineEdit.setStyleSheet(self.time_gray_out_style)
            self.pattern.Min_lineEdit.setValue(0)
            self.pattern.Min_lineEdit.setEnabled(False)
            self.pattern.Min_lineEdit.setStyleSheet(self.time_gray_out_style)
            self.pattern.Time_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.time_frame.setStyleSheet(self.timeframe_grayout)
            self.pattern.label_4.setStyleSheet(self.time_gray_out_style)
            self.pattern.SV_lineEdit.setValue(0)
            self.pattern.SV_lineEdit.setEnabled(False)
            self.pattern.SV_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.SV_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.N2_lineEdit.setValue(0)
            self.pattern.N2_lineEdit.setEnabled(False)
            self.pattern.N2_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.N2_label.setStyleSheet(self.label_gray_out_style)


            self.pattern.PID_muffle_comboBox.setEnabled(False)
            self.pattern.PID_muffle_comboBox.setStyleSheet(self.line_gray_out_style)
            self.pattern.PID_muffle_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.PID_heater_comboBox.setEnabled(False)
            self.pattern.PID_heater_comboBox.setStyleSheet(self.line_gray_out_style)
            self.pattern.PID_heater_label.setStyleSheet(self.label_gray_out_style)

            self.pattern.KeepTime_lineEdit.setValue(0)
            self.pattern.KeepTime_lineEdit.setDisabled(False)
            self.pattern.KeepTime_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.KeepTime_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.TestPattern_comboBox.setDisabled(False)
            self.pattern.TestPattern_comboBox.setStyleSheet(self.line_gray_out_style)
            self.pattern.TestPattern_label.setStyleSheet(self.label_gray_out_style) 
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
        return


    def setFocusStyle(self,enable):
        if enable:
            self.FocusStyle=self.focus_normal_style
            self.FocusStyleChange=True
        else:
            self.FocusStyle=self.focus_gray_out_style
            self.FocusStyleChange=True
        

    def enableEndType(self,enable):
        if enable:
            if self.pattern.Type_comboBox.count()==2:
                self.pattern.Type_comboBox.addItems(["END"])

        else:
            self.pattern.Type_comboBox.removeItem(2)

    

        

