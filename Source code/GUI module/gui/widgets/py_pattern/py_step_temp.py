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
from qt_core import *
from .ui_temp_pattern import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

from gui.core.functions import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes


from system.profile_manager import *

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import *

from .py_pattern_menu import *


class PyTempStep(QWidget):

    clicked = Signal(object)
    released = Signal(object)

    Temp_Type  =  0
    Test_Type     = 1
    End_Type     =  2

    label_gray_out_style="font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\"; color: rgb(91, 94, 98); border:none;"
    label_normal_style="font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\"; color: rgb(225, 230, 241); border:none;"

    line_gray_out_style="background-color: rgba(0, 0, 0,20);    color: rgb(225, 230, 241);    border-width: 1px;    border-style: solid;    border-radius: 5px;    padding-left:5px;    padding-right:5px;    font: 12px \"游ゴシック\";"
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
        test_pattern = "",
        n2_flowrate = 0
    ):
        super().__init__()
        # Parameter
        self._active = active
        self._step = step
        self._type = type
        self._temperature = temperature
        self._hour = hour
        self._minute = minute
        self._keep_seccond = keep_seccond
        self._test_pattern = test_pattern
        self._n2_flowrate = n2_flowrate
        # Parent
        self._parent = parent
        self._app_parent = app_parent

        # base prepare
        # ///////////////////////////////////////////////////////////////
        self.setFixedSize(195,265)
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
            app_parent=self._parent
            )
        self._menu.menu_frame.move(50, 0)
        self.close_menu()

        self.mode_respond()

    def parameter_setting(self):
        # Step number setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.label.setText("STEP %d" %self._step)

        # Step type setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.comboBox.setCurrentIndex(self._type)

        # temperature setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.lineEdit.setText("%d" % self._temperature)

        # hours setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.lineEdit_2.setText("%d" % self._hour)


        self.pattern.lineEdit_3.setText("%d" % self._minute)
        self.pattern.lineEdit_4.setText("%d" % self._keep_seccond)
        self.pattern.lineEdit_5.setText("%d" % self._n2_flowrate)
        self.pattern.comboBox_2.setCurrentIndex(self._type)
        self.pattern.comboBox_2.addItems(profile_manager.scan_temp_profile())
        
        

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
        self.menu_icon.clicked.connect(self._parent.btn_clicked)
        self.menu_icon.setObjectName("menu_temp_Step_Buttom - STEP %d" %self._step)

        self.pattern.comboBox.currentIndexChanged.connect(self.mode_respond)

    def mode_respond(self):
        if (self.pattern.comboBox.currentText()) == "昇降温":
            self.pattern.label_2.setStyleSheet(self.label_normal_style)
            self.pattern.lineEdit.setStyleSheet(self.line_normal_style)
            self.pattern.label_7.setStyleSheet(self.label_normal_style)
            self.pattern.lineEdit_5.setStyleSheet(self.line_normal_style)

            self.pattern.label_5.setStyleSheet(self.label_gray_out_style)
            self.pattern.label_6.setStyleSheet(self.label_gray_out_style)
            self.pattern.lineEdit_4.setStyleSheet(self.line_gray_out_style)
            
            self.pattern.comboBox_2.clear()
        elif (self.pattern.comboBox.currentText()) == "測定":
            

            self.pattern.label_2.setStyleSheet(self.label_gray_out_style)
            self.pattern.lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.label_7.setStyleSheet(self.label_gray_out_style)
            self.pattern.lineEdit_5.setStyleSheet(self.line_gray_out_style)
            
            self.pattern.label_5.setStyleSheet(self.label_normal_style)
            self.pattern.label_6.setStyleSheet(self.label_normal_style)
            self.pattern.lineEdit_4.setStyleSheet(self.line_normal_style)
            self.pattern.comboBox_2.addItems(profile_manager.scan_temp_profile())
        elif (self.pattern.comboBox.currentText()) == "END":

            self.pattern.label_2.setStyleSheet(self.label_gray_out_style)
            self.pattern.lineEdit.setStyleSheet(self.line_gray_out_style)
            self.pattern.label_7.setStyleSheet(self.label_gray_out_style)
            self.pattern.lineEdit_5.setStyleSheet(self.line_gray_out_style)
            self.pattern.label_5.setStyleSheet(self.label_gray_out_style)
            self.pattern.label_6.setStyleSheet(self.label_gray_out_style)
            self.pattern.lineEdit_4.setStyleSheet(self.line_gray_out_style)

            
            self.pattern.comboBox_2.clear()



    def show_menu(self):
        self.move_menu()
        self._menu.menu_frame.show()
        pass

    def close_menu(self):
        self._menu.menu_frame.hide()
        pass

    def move_menu(self):
        pass

