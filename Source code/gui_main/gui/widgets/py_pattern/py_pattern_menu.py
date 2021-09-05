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


    def __init__(
        self , 
        parent = None,
        app_parent = None,
    ):
        super().__init__()
        # Parameter

        # Parent
        self._parent = parent
        self._app_parent = app_parent

        # base prepare
        # ///////////////////////////////////////////////////////////////
        self.menu_frame = QFrame(self._parent)
        self.menu_frame.setContentsMargins(0,0,0,0)
        self.menu = Ui_pattern_menu()
        self.menu.setupUi( self.menu_frame)
        print(self._app_parent.btn_clicked)
        self.menu.pattern_menu_cut_pushButton.clicked.connect(self._app_parent.btn_clicked)
        self.menu.pattern_menu_cut_pushButton.setObjectName("pattern_menu_cut_pushButton")

        self.menu.pattern_menu_copy_pushButton.clicked.connect(self._app_parent.btn_clicked)
        self.menu.pattern_menu_copy_pushButton.setObjectName("pattern_menu_copy_pushButton")

        self.menu.pattern_menu_paste_pushButton.clicked.connect(self._app_parent.btn_clicked)
        self.menu.pattern_menu_paste_pushButton.setObjectName("pattern_menu_paste_pushButton")

        self.menu.pattern_menu_rightinsert_pushButton.clicked.connect(self._app_parent.btn_clicked)
        self.menu.pattern_menu_rightinsert_pushButton.setObjectName("pattern_menu_rightinsert_pushButton")

        self.menu.pattern_menu_leftinsert_pushButton.clicked.connect(self._app_parent.btn_clicked)
        self.menu.pattern_menu_leftinsert_pushButton.setObjectName("pattern_menu_leftinsert_pushButton")

        self.menu.pattern_menu_rightinsertblank_pushButton.clicked.connect(self._app_parent.btn_clicked)
        self.menu.pattern_menu_rightinsertblank_pushButton.setObjectName("pattern_menu_rightinsertblank_pushButton")

        self.menu.pattern_menu_leftinsertblank_pushButton.clicked.connect(self._app_parent.btn_clicked)
        self.menu.pattern_menu_leftinsertblank_pushButton.setObjectName("pattern_menu_leftinsertblank_pushButton")

        self.menu.pattern_menu_delete_pushButton.clicked.connect(self._app_parent.btn_clicked)
        self.menu.pattern_menu_delete_pushButton.setObjectName("pattern_menu_delete_pushButton")

