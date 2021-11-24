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

    #clicked = pyqtSignal(object)
    #released = pyqtSignal(object)



    def __init__(
        self , 
        parent = None,
        active = 1,
        step = 0,
        voltage = 0
    ):
        super().__init__()
        # Parameter
        self._active = active
        self._step = step
        self._voltage = voltage

        # Parent
        self._parent = parent
        # base prepare
        # ///////////////////////////////////////////////////////////////
        self.setFixedSize(140,133)
        self.pattern_frame = QFrame(self)
        self.pattern_frame.setContentsMargins(0,0,0,0)
        self.pattern = Ui_test_pattern()
        self.pattern.setupUi( self.pattern_frame)
        self.pattern.page.setCurrentIndex(self._active)



        
        # Menu_setting
        # ///////////////////////////////////////////////////////////////

        
        # icon_bottum_ui_setting
        # ///////////////////////////////////////////////////////////////
        self.icon_bottum_ui_setting()




        #self._menu=PyStepMenu(
        #    parent=self,
        #    app_parent=self._parent,
        #    step=self._step,
        #    parent_type="Test type"
        #    )
        #self._menu.menu_frame.move(60, -50)
        #self._menu.menu_frame.hide()


        

    def parameter_setting(self):
        
        self.pattern.Step_label.setText("STEP %d" %self._step)
        self.pattern.Valtage_lineEdit.setText(str(self._voltage))
        self.pattern.Valtage_lineEdit.setValidator(QDoubleValidator(decimals=2))

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
        self.icon.setObjectName("new_test_Step_Buttom")
        
         
        self.menu_icon = PyIconButton_simple(
                icon = "fi-rr-cross-small.svg",
                icon_active = "fi-rr-cross-small.svg",
                icon_hover = "fi-rr-cross-small.svg",
                icon_deactive = "fi-rr-cross-small-deactive.svg",
                btn_id = "ステップ {} menu編集".format(self._step),
                tooltip_text = "編集",
                width = 30,
                height = 30,
                bg_color = "rgb(44, 49, 60)",
                bg_color_hover = "rgb(63, 70, 86)",
                bg_color_pressed = "rgb(112, 125, 153)"

            )
        self.pattern.gridLayout_6.addWidget(self.menu_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.menu_icon.clicked.connect(self.delete_step)

        self.pattern.Valtage_lineEdit.editingFinished.connect(self.modifly_callback)


    def maxmin(self,max,min,data):
        if data>=max:
            return max,True
        elif data<=min:
            return min,True
        else:
            return data,False

    #When infomation is modifly by user , call back to this function
    def modifly_callback(self):
        if (self.sender()==None):
            return
        print("Valtage_lineEdit")
        data=float(self.pattern.Valtage_lineEdit.text())
        self._voltage,err=self.maxmin(2000,-2000,data)
        if err:
            self.pattern.Valtage_lineEdit.setText(str(self._voltage))

        #Call upper mother renew information
        self._parent.testPattern.step_modifly_manager(self._step)
        
    def addStepBtn_presscallback(self):
        self._parent.testPattern.new_TestPattern()

    def addStepBtn_releasecallback(self):
        self._parent.testPattern.scroll_adjust_TestPattern()

    def delete_step(self):

        self._parent.testPattern.menu_btn_handler("pattern_menu_delete_pushButton")



    def enterEvent(self, event):
        if self.pattern.page.currentIndex() ==1:
            self._parent.testPattern.focus_step(self._step)

        
    def leaveEvent(self, event):
        if self.pattern.page.currentIndex() ==1:
            self._parent.testPattern.un_focus_step(self._step)

    def paintEvent(self, event):
        return


    def setFocusStyle(self,enable):
        if enable:
            self.pattern.frame_4. setFocus()
        else:
            self.pattern.frame_4. clearFocus()
        


    