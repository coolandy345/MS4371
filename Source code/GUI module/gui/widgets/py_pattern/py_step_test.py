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

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from .ui_test_pattern import *

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


class PyTestStep(QWidget):

    BG_Type  =  0
    Test_BG_Type     = 1
    End_Type     =  2

    def __init__(
        self , 
        parent = None,
        app_parent = None,
        active = 1,
        step = 1,
        type = 0,
        test_voltage = 25,
        test_time = 0,
        test_sample_time = 0,
        BG_time = 0,
        BG_sample_time = 0
    ):
        super().__init__()
        # Parameter
        self._active = active
        self._step = step
        self._type = type
        self._test_voltage = test_voltage
        self._test_time = test_time
        self._test_sample_time = test_sample_time
        self._BG_time = BG_time
        self._BG_sample_time = BG_sample_time
        # Parent
        self._parent = parent
        self._app_parent = app_parent

        # base prepare
        # ///////////////////////////////////////////////////////////////
        self.setFixedSize(190,260)
        self.pattern_frame = QFrame(self)
        self.pattern_frame.setContentsMargins(0,0,0,0)
        self.pattern = Ui_test_pattern()
        self.pattern.setupUi( self.pattern_frame)
        self.pattern.page.setCurrentIndex(self._active)

        # icon_bottum_ui_setting
        # ///////////////////////////////////////////////////////////////
        self.icon_bottum_ui_setting();

        # Parameter_setting
        # ///////////////////////////////////////////////////////////////
        self.parameter_setting()

        
        
        
    def parameter_setting(self):
        # Step number setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.label.setText("STEP %d" %self._step)

        # Step type setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.comboBox.setCurrentIndex(self._type)

        # test_voltage setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.lineEdit.setText("%d" % self._test_voltage)

        # test_time setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.lineEdit_2.setText("%d" % self._test_time)

        # test_sample_time setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.lineEdit_4.setText("%d" % self._test_sample_time)

        # BG_time setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.lineEdit_5.setText("%d" % self._BG_time)

        # BG_sample_time setting
        # ///////////////////////////////////////////////////////////////
        self.pattern.lineEdit_7.setText("%d" % self._BG_sample_time)





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
        self.pattern.gridLayout_2.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)
         
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



