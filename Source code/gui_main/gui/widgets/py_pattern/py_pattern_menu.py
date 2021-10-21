# ///////////////////////////////////////////////////////////////
import os
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui_main.qt_core import *
from .ui_pattern_menu import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.widgets import *

from gui_main.gui.core.functions import *

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


class PyStepMenu(QWidget):

    Active_style="QPushButton{color: rgb(225, 230, 241);font: 13px  \"游ゴシック\";border:none;Text-align:left;}QPushButton:hover {background-color: rgb(29, 33, 40);}QPushButton:pressed {background-color: rgb(69, 140, 207);}"

    Deactive_style="QPushButton{color: rgb(99, 99, 99);font: 13px  \"游ゴシック\";border:none;Text-align:left;}QPushButton:hover {background-color: rgb(29, 33, 40);}QPushButton:pressed {background-color: rgb(69, 140, 207);}"


    def __init__(
        self , 
        parent = None,
        app_parent = None,
        step = 1,
        parent_type=""
    ):
        super().__init__()
        # Parameter

        # Parent
        self._parent = parent
        self._app_parent = app_parent 
        self._step = step
        self._parent_type = parent_type
        
        # base prepare
        # ///////////////////////////////////////////////////////////////
        self.menu_frame = QFrame(self._parent)
        self.menu_frame.setContentsMargins(0,0,0,0)
        self.menu = Ui_pattern_menu()
        self.menu.setupUi( self.menu_frame)
        self.menu.pattern_menu_cut_pushButton.clicked.connect(self.function_callback)
        self.menu.pattern_menu_copy_pushButton.clicked.connect(self.function_callback)
        self.menu.pattern_menu_paste_pushButton.clicked.connect(self.function_callback)
        self.menu.pattern_menu_rightinsert_pushButton.clicked.connect(self.function_callback)
        self.menu.pattern_menu_leftinsert_pushButton.clicked.connect(self.function_callback)
        self.menu.pattern_menu_rightinsertblank_pushButton.clicked.connect(self.function_callback)
        self.menu.pattern_menu_leftinsertblank_pushButton.clicked.connect(self.function_callback)
        self.menu.pattern_menu_delete_pushButton.clicked.connect(self.function_callback)




    def function_callback(self):
        btn = self.sender()
        if self._parent_type=="Temp type":
            self._app_parent.tempPattern.menu_btn_handler(btn.objectName())
        elif self._parent_type=="Test type":
            self._app_parent.testPattern.menu_btn_handler(btn.objectName())

    def paintEvent(self, event):
        print("paintEvent of menu")

    def paste_SetEnable(self, paste_enable,add_enable):

        pattern_menu_paste_pushButton=False
        pattern_menu_rightinsert_pushButton=False
        pattern_menu_leftinsert_pushButton=False
        pattern_menu_rightinsertblank_pushButton=False
        pattern_menu_leftinsertblank_pushButton=False

        if paste_enable :
            pattern_menu_paste_pushButton=True

        if paste_enable and add_enable:
            pattern_menu_rightinsert_pushButton=True
            pattern_menu_leftinsert_pushButton=True

        if add_enable :
            pattern_menu_rightinsertblank_pushButton=True
            pattern_menu_leftinsertblank_pushButton=True

        #-------pattern_menu_paste_pushButton-----------------------------------
        if pattern_menu_paste_pushButton  :
            self.menu.pattern_menu_paste_pushButton.setEnabled(True)
            self.menu.pattern_menu_paste_pushButton.setStyleSheet(self.Active_style)
        else:
            self.menu.pattern_menu_paste_pushButton.setEnabled(False)
            self.menu.pattern_menu_paste_pushButton.setStyleSheet(self.Deactive_style)
        #-------pattern_menu_rightinsert_pushButton-----------------------------------
        if pattern_menu_rightinsert_pushButton  :
            self.menu.pattern_menu_rightinsert_pushButton.setEnabled(True)
            self.menu.pattern_menu_rightinsert_pushButton.setStyleSheet(self.Active_style)
        else:
            self.menu.pattern_menu_rightinsert_pushButton.setEnabled(False)
            self.menu.pattern_menu_rightinsert_pushButton.setStyleSheet(self.Deactive_style)
        #-------pattern_menu_leftinsert_pushButton-----------------------------------
        if pattern_menu_leftinsert_pushButton  :
            self.menu.pattern_menu_leftinsert_pushButton.setEnabled(True)
            self.menu.pattern_menu_leftinsert_pushButton.setStyleSheet(self.Active_style)
        else:
            self.menu.pattern_menu_leftinsert_pushButton.setEnabled(False)
            self.menu.pattern_menu_leftinsert_pushButton.setStyleSheet(self.Deactive_style)
        #-------pattern_menu_rightinsertblank_pushButton-----------------------------------
        if pattern_menu_rightinsertblank_pushButton  :
            self.menu.pattern_menu_rightinsertblank_pushButton.setEnabled(True)
            self.menu.pattern_menu_rightinsertblank_pushButton.setStyleSheet(self.Active_style)
        else:
            self.menu.pattern_menu_rightinsertblank_pushButton.setEnabled(False)
            self.menu.pattern_menu_rightinsertblank_pushButton.setStyleSheet(self.Deactive_style)
        #-------pattern_menu_leftinsertblank_pushButton-----------------------------------
        if pattern_menu_leftinsertblank_pushButton  :
            
            self.menu.pattern_menu_leftinsertblank_pushButton.setEnabled(True)
            self.menu.pattern_menu_leftinsertblank_pushButton.setStyleSheet(self.Active_style)
        else:
            
            self.menu.pattern_menu_leftinsertblank_pushButton.setEnabled(False)
            self.menu.pattern_menu_leftinsertblank_pushButton.setStyleSheet(self.Deactive_style)



    def add_paste_SetEnable(self):
        pass
