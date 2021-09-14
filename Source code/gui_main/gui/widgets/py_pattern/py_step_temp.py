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

    def __init__(
        self , 
        parent = None,
        app_parent = None,
        active = 1,
        step = 1,
        type = 0,
        temperature = 25,
        hour = 0,
        minute = 0,
        keep_seccond = 0,
        test_pattern = 0,
        n2_flowrate = 0,
        PID_no = 0
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
        self._PID_no = PID_no

        # Parent
        self._parent = parent
        self._app_parent = app_parent
        
        # base prepare
        # ///////////////////////////////////////////////////////////////
        self.setFixedSize(200,300)
        self.pattern_frame = QFrame(self)
        self.pattern_frame.setContentsMargins(0,0,0,0)
        self.pattern = Ui_temp_pattern()
        self.pattern.setupUi( self.pattern_frame)
        self.pattern.page.setCurrentIndex(self._active)
        
        # icon_bottum_ui_setting
        # ///////////////////////////////////////////////////////////////
        self.icon_bottum_ui_setting()
        
        # Parameter_setting
        # ///////////////////////////////////////////////////////////////
        self.parameter_setting()
        # Menu_setting
        # ///////////////////////////////////////////////////////////////
        self._menu=PyStepMenu(
            parent=self,
            app_parent=self._parent,
            step=self._step

            )
        self._menu.menu_frame.move(60, 0)

        self._menu.menu_frame.hide()
        self.type_change_callback()


    def parameter_setting(self):
        
        self.pattern.Step_label.setText("STEP %d" %self._step)
        self.pattern.Type_comboBox.setCurrentIndex(self._type)
        self.pattern.Hour_lineEdit.setValue(self._hour)
        self.pattern.Min_lineEdit.setValue(self._minute)
        self.pattern.Temp_lineEdit.setValue(self._temperature)
        self.pattern.N2_lineEdit.setValue(self._n2_flowrate)
        self.pattern.PID_comboBox.setCurrentIndex(self._PID_no)
        self.pattern.KeepTime_lineEdit.setValue(self._keep_seccond)
        self.pattern.TestPattern_comboBox.setCurrentIndex(self._test_pattern)

    def icon_bottum_ui_setting(self):
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        self.settings = Settings().items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        self.themes = Themes().items

        self.icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-plus-large.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                tooltip_text = "ステップ追加",
                width = 80,
                height = 80,
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
        self.grayout_color="#606267"
        self.pattern.gridLayout_2.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)
        self.icon.clicked.connect(self._parent.btn_clicked)
        self.icon.released.connect(self._parent.btn_released)
        self.icon.setObjectName("new_temp_Step_Buttom")


         
        self.menu_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-menu-dots-vertical.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                tooltip_text = "編集",
                width = 20,
                height = 30,
                radius = 2,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = "#2c313c",
                bg_color_hover = "#2c313c",
                bg_color_pressed = "#6db6ee",
            )
        self.pattern.gridLayout_6.addWidget(self.menu_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.menu_icon.clicked.connect(self.show_menu)
        self.pattern.Type_comboBox.currentIndexChanged.connect(self.type_change_callback)
        self.pattern.Hour_lineEdit.editingFinished.connect(self.step_modifly_callback)
        self.pattern.Min_lineEdit.editingFinished.connect(self.step_modifly_callback)
        self.pattern.Temp_lineEdit.editingFinished.connect(self.step_modifly_callback)
        self.pattern.N2_lineEdit.editingFinished.connect(self.step_modifly_callback)
        self.pattern.PID_comboBox.currentIndexChanged.connect(self.step_modifly_callback)
        self.pattern.KeepTime_lineEdit.editingFinished.connect(self.step_modifly_callback)
        self.pattern.TestPattern_comboBox.currentIndexChanged.connect(self.step_modifly_callback)


    #When infomation is modifly by user , call back to this function
    def step_modifly_callback(self):

        if (self.sender()==None):
            return
        
        try:
            #Close menu any way
            self._parent.tempPattern.close_menu()

        except AttributeError: #When self._parent.tempPattern is not initial yet
            return

        print("click in side step after modifly STEP ", self._step," name = ",self.sender().objectName())
        self._hour=self.pattern.Hour_lineEdit.value()
        self._minute=self.pattern.Hour_lineEdit.value()
        self._temperature=self.pattern.Hour_lineEdit.value()
        self._n2_flowrate=self.pattern.Hour_lineEdit.value()
        self._keep_seccond=self.pattern.Hour_lineEdit.value()
        self._test_pattern=self.pattern.Hour_lineEdit.value()
        self._hour=self.pattern.Hour_lineEdit.value()
        self._hour=self.pattern.Hour_lineEdit.value()


    def type_change_callback(self):

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
            self.pattern.Temp_lineEdit.setEnabled(True)
            self.pattern.Temp_lineEdit.setStyleSheet(self.line_normal_style)
            self.pattern.Temp_label.setStyleSheet(self.label_normal_style)
            self.pattern.N2_lineEdit.setEnabled(True)
            self.pattern.N2_lineEdit.setStyleSheet(self.line_normal_style)
            self.pattern.N2_label.setStyleSheet(self.label_normal_style)
            self.pattern.PID_comboBox.setEnabled(True)
            self.pattern.PID_comboBox.setStyleSheet(self.line_normal_style)
            self.pattern.PID_label.setStyleSheet(self.label_normal_style)
            self.pattern.KeepTime_lineEdit.setValue(0)
            self.pattern.KeepTime_lineEdit.setDisabled(True)
            self.pattern.KeepTime_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.KeepTime_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.TestPattern_comboBox.setDisabled(True)
            self.pattern.TestPattern_comboBox.setStyleSheet(self.line_gray_out_style)
            self.pattern.TestPattern_label.setStyleSheet(self.label_gray_out_style)
            
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
            self.pattern.Temp_lineEdit.setValue(0)
            self.pattern.Temp_lineEdit.setEnabled(False)
            self.pattern.Temp_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.Temp_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.N2_lineEdit.setValue(0)
            self.pattern.N2_lineEdit.setEnabled(False)
            self.pattern.N2_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.N2_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.PID_comboBox.setEnabled(False)
            self.pattern.PID_comboBox.setStyleSheet(self.line_gray_out_style)
            self.pattern.PID_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.KeepTime_lineEdit.setEnabled(True)
            self.pattern.KeepTime_lineEdit.setStyleSheet(self.line_normal_style)
            self.pattern.KeepTime_label.setStyleSheet(self.label_normal_style)
            self.pattern.TestPattern_comboBox.setDisabled(True)
            self.pattern.TestPattern_comboBox.setStyleSheet(self.line_normal_style)
            self.pattern.TestPattern_label.setStyleSheet(self.label_normal_style)

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
            self.pattern.Temp_lineEdit.setValue(0)
            self.pattern.Temp_lineEdit.setEnabled(False)
            self.pattern.Temp_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.Temp_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.N2_lineEdit.setValue(0)
            self.pattern.N2_lineEdit.setEnabled(False)
            self.pattern.N2_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.N2_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.PID_comboBox.setEnabled(False)
            self.pattern.PID_comboBox.setStyleSheet(self.line_gray_out_style)
            self.pattern.PID_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.KeepTime_lineEdit.setValue(0)
            self.pattern.KeepTime_lineEdit.setDisabled(False)
            self.pattern.KeepTime_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.KeepTime_label.setStyleSheet(self.label_gray_out_style)
            self.pattern.TestPattern_comboBox.setDisabled(False)
            self.pattern.TestPattern_comboBox.setStyleSheet(self.line_gray_out_style)
            self.pattern.TestPattern_label.setStyleSheet(self.label_gray_out_style) 

        self.step_modifly_callback()

    def show_menu(self):
        self._parent.tempPattern.show_one_menu(self._step)

    def close_menu(self):
        self._parent.tempPattern.close_menu()
        
    def mousePressEvent(self, event):
        self._parent.tempPattern.close_menu()

    def leaveEvent(self, event):
        self._parent.tempPattern.close_menu()

        

