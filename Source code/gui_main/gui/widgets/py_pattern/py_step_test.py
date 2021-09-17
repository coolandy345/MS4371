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
from .ui_test_pattern import *

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


class PyTestStep(QWidget):

    #clicked = Signal(object)
    #released = Signal(object)

    Test_Type  =    0
    End_Type   =    1

    step_bg_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(53 ,206, 220);border:none;"
    #step_testbg_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(200, 133, 0);border:none;"
    step_testbg_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(73, 73, 220);border:none;"
    step_end_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(0, 168, 123);border:none;"

    label_gray_out_style="font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\"; color: rgb(91, 94, 98); border:none;"
    label_normal_style="font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\"; color: rgb(225, 230, 241); border:none;"

    line_gray_out_style="background-color: rgba(0, 0, 0,20);    color:  rgba(0, 0, 0,20);    border-width: 1px;    border-style: solid;    border-radius: 5px;    padding-left:5px;    padding-right:5px;    font: 12px \"游ゴシック\";"
    line_normal_style="background-color: rgba(0, 0, 0,80);    color: rgb(225, 230, 241);    border-width: 1px;    border-style: solid;    border-radius: 5px;    padding-left:5px;    padding-right:5px;    font: 12px \"游ゴシック\";"

    def __init__(
        self , 
        parent = None,
        app_parent = None,
        active = 1,
        step = 0,
        type = 0,
        voltage = 0
    ):
        super().__init__()
        # Parameter
        self._active = active
        self._step = step
        self._type = type
        self._voltage = voltage

        # Parent
        self._parent = parent
        self._app_parent = app_parent
        # base prepare
        # ///////////////////////////////////////////////////////////////
        self.setFixedSize(140,133)
        self.pattern_frame = QFrame(self)
        self.pattern_frame.setContentsMargins(0,0,0,0)
        self.pattern = Ui_test_pattern()
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
            step=self._step,
            parent_type="Test type"
            )
        self._menu.menu_frame.move(60, 0)
        self._menu.menu_frame.hide()
        self.type_modifly_callback()
        

    def parameter_setting(self):
        
        self.pattern.Step_label.setText("STEP %d" %self._step)
        self.pattern.Type_comboBox.setCurrentIndex(self._type)
        self.pattern.SV_lineEdit.setValue(self._voltage)

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
        self.icon.setObjectName("new_test_Step_Buttom")

         
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
        self.pattern.Type_comboBox.currentIndexChanged.connect(self.type_modifly_callback)
        self.pattern.SV_lineEdit.editingFinished.connect(self.modifly_callback)


    #When infomation is modifly by user , call back to this function
    def modifly_callback(self):

        if (self.sender()==None):
            return
        
        try:
            #Close menu any way
            self._parent.testPattern.close_menu()

        except AttributeError: #When self._parent.tempPattern is not initial yet
            return

        print("click in side step after modifly STEP ", self._step," name = ",self.sender().objectName())
        
        self._voltage=self.pattern.SV_lineEdit.value()
        
        #Call upper mother renew information
        self._parent.testPattern.step_modifly_manager(self._step)
        
    def type_modifly_callback(self):


        if (self.pattern.Type_comboBox.currentText()) == "BG":
            
            self._type=self.Test_Type
            self.pattern.Step_label.setStyleSheet(self.step_bg_type_style)

            self.pattern.SV_lineEdit.setValue(0)
            self.pattern.SV_lineEdit.setEnabled(False)
            self.pattern.SV_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.SV_label.setStyleSheet(self.label_gray_out_style)

            
            
        elif (self.pattern.Type_comboBox.currentText()) == "測定+BG":

            self._type=self.Test_Type
            self.pattern.Step_label.setStyleSheet(self.step_testbg_type_style)

            self.pattern.SV_lineEdit.setEnabled(True)
            self.pattern.SV_lineEdit.setStyleSheet(self.line_normal_style)
            self.pattern.SV_label.setStyleSheet(self.label_normal_style)

        elif (self.pattern.Type_comboBox.currentText()) == "END":

            self._type=self.End_Type
            self.pattern.Step_label.setStyleSheet(self.step_end_type_style)

            self.pattern.SV_lineEdit.setValue(0)
            self.pattern.SV_lineEdit.setEnabled(False)
            self.pattern.SV_lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.SV_label.setStyleSheet(self.label_gray_out_style)
        
        self.modifly_callback()

    def show_menu(self):
        self._parent.testPattern.show_one_menu(self._step)

    def close_menu(self):
        self._parent.testPattern.close_menu()
        
    def mousePressEvent(self, event):
        self._parent.testPattern.close_menu()

    def leaveEvent(self, event):
        self._parent.testPattern.close_menu()

        

