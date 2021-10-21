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

class modifly_callbackThread(QRunnable):
    def __init__(self, parent,sender):
        super().__init__()
        self.parent = parent
        self.sender=sender

    def run(self):
        self.parent.modifly_callbackWork(self.sender)

class PyTestStep(QWidget):

    #clicked = Signal(object)
    #released = Signal(object)


    step_bg_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(53 ,206, 220);border:none;"
    #step_testbg_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(200, 133, 0);border:none;"
    step_testbg_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(73, 73, 220);border:none;"
    step_end_type_style="font: 12px \"游ゴシック\";color: rgb(0,0,0);padding-left:5px;background-color: rgb(0, 168, 123);border:none;"

    label_gray_out_style="font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\"; color: rgb(91, 94, 98); border:none;"
    label_normal_style="font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\"; color: rgb(225, 230, 241); border:none;"

    line_gray_out_style="background-color: rgba(0, 0, 0,20);    color:  rgba(0, 0, 0,20);    border-width: 1px;    border-style: solid;    border-radius: 5px;    padding-left:5px;    padding-right:5px;    font: 12px \"游ゴシック\";"
    line_normal_style="background-color: rgba(0, 0, 0,80);    color: rgb(225, 230, 241);    border-width: 1px;    border-style: solid;    border-radius: 5px;    padding-left:5px;    padding-right:5px;    font: 12px \"游ゴシック\";"

    focus_normal_style="border-color: rgb(231, 214, 85);background-color: rgb(44, 49, 60);border-width: 5px;    border-style: solid;    border-radius: 10px;"
    focus_gray_out_style="border-color: rgb(44, 49, 60);background-color: rgb(44, 49, 60);border-width: 5px;    border-style: solid;    border-radius: 10px;"
    


    def __init__(
        self , 
        parent = None,
        app_parent = None,
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
        self._app_parent = app_parent
        # base prepare
        # ///////////////////////////////////////////////////////////////
        self.setFixedSize(140,133)
        self.pattern_frame = QFrame(self)
        self.pattern_frame.setContentsMargins(0,0,0,0)
        self.pattern = Ui_test_pattern()
        self.pattern.setupUi( self.pattern_frame)
        self.pattern.page.setCurrentIndex(self._active)

        self.FocusStyleChange=False
        self.FocusStyle=self.focus_gray_out_style
        self.timer=QTimer()
        self.timer.timeout.connect(self.timerCallback)
        self.timer.start(100)

        # Parameter_setting
        # ///////////////////////////////////////////////////////////////
        self.parameter_setting()
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

    def timerCallback(self):
        if self.FocusStyleChange:
            self.pattern.page.setStyleSheet(self.FocusStyle)
            self.FocusStyleChange=False
        

    def parameter_setting(self):
        
        self.pattern.Step_label.setText("STEP %d" %self._step)
        self.pattern.Valtage_lineEdit.setValue(self._voltage)

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
                icon_color = self.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = self.themes["app_color"]["dark_one"],
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["green"],
            )
        self.grayout_color="#606267"
        self.pattern.gridLayout_2.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)
        self.icon.clicked.connect(self.addStepBtn_presscallback)
        self.icon.released.connect(self.addStepBtn_releasecallback)
        self.icon.setObjectName("new_test_Step_Buttom")

         
        self.menu_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-cross-small.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                tooltip_text = "削除",
                width = 20,
                height = 30,
                radius = 2,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#2c313c",
                bg_color_hover = "#2c313c",
                bg_color_pressed = "#6db6ee",
            )
        self.pattern.gridLayout_6.addWidget(self.menu_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.menu_icon.clicked.connect(self.show_menu)

        self.pattern.Valtage_lineEdit.valueChanged.connect(self.modifly_callback)

    def modifly_callback(self):
        self.modifly_callbackWorker=modifly_callbackThread(self,self.sender())
        QThreadPool.globalInstance().start(self.modifly_callbackWorker)
        #self.modifly_callbackWorker.start()

    #When infomation is modifly by user , call back to this function
    def modifly_callbackWork(self,sender):
        if (sender==None):
            return
        
        self._voltage=self.pattern.Valtage_lineEdit.value()
        #Call upper mother renew information
        self._parent.testPattern.step_modifly_manager(self._step)
        
    def addStepBtn_presscallback(self):
        self._parent.testPattern.new_TestPattern()

    def addStepBtn_releasecallback(self):
        self._parent.testPattern.scroll_adjust_TestPattern()

    def show_menu(self):

        self._parent.testPattern.menu_btn_handler("pattern_menu_delete_pushButton")

        #if self._menu.menu_frame.isVisible():
        #    self._menu.menu_frame.hide()
        #else:
        #    self._menu.paste_SetEnable(self._parent.testPattern.paste_ready,self._parent.testPattern.activeStep_noFull)
        #    self._menu.menu_frame.show()


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
            self.FocusStyle=self.focus_normal_style
            self.FocusStyleChange=True
        else:
            self.FocusStyle=self.focus_gray_out_style
            self.FocusStyleChange=True
        


    