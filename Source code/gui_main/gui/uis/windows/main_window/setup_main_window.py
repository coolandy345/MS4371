# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
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

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
# -*- coding: utf-8 -*-

from gui_main.gui.widgets.py_table_widget.py_table_widget import PyTableWidget

from . testprofile_function import Testfile_manager


from . functions_main_window import *
import sys
import os
import time
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui_main.qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.widgets import *


# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# IMPORT ICON
# ///////////////////////////////////////////////////////////////
from gui_main.gui.widgets.py_left_column.py_icon import *

from gui_main.gui.uis.pattern_columns import *


import numpy as np
import pyqtgraph as pg


#from gui.uis.control_column import *



# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self,main_namespace,Master_memoryPool,queuePool,eventPool):
        super().__init__()

        self.main_namespace=main_namespace
        self.Master_memoryPool=Master_memoryPool
        self.queuePool=queuePool
        
        self.eventPool=eventPool
        self.setup_gui()
        

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "fi-rr-file-check.svg",
            "btn_id" : "btn_PrepareMenu",
            "btn_text" : "運転前準備",
            "btn_tooltip" : "運転前準備",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "fi-rr-data-transfer.svg",
            "btn_id" : "btn_OperateMenu",
            "btn_text" : "運転操作",
            "btn_tooltip" : "運転操作",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "fi-rr-database.svg",
            "btn_id" : "btn_ParameterPatternMenu",
            "btn_text" : "測定パラメータ設定",
            "btn_tooltip" : "測定パラメータ設定",
            "show_top" : True,
            "is_active" : False
        },
        #{
        #    "btn_icon" : "fi-rr-link.svg",
        #    "btn_id" : "btn_ConnectionMenu",
        #    "btn_text" : "通信接続設定",
        #    "btn_tooltip" : "通信接続設定",
        #    "show_top" : True,
        #    "is_active" : False
        #}
    ]

     # ADD TITLE BAR MENUS
     #///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "設定",
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()
        else:
            return self.sender()




    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.main_namespace.setWindowTitle(self.main_namespace.settings["app_name"])

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.main_namespace.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.main_namespace.ui.title_bar.clicked.connect(self.main_namespace.btn_clicked)
        self.main_namespace.ui.title_bar.released.connect(self.main_namespace.btn_released)
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.main_namespace.settings["custom_title_bar"]:
            self.main_namespace.setWindowFlag(Qt.FramelessWindowHint)
            self.main_namespace.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.main_namespace.settings["custom_title_bar"]:
            self.main_namespace.left_grip = PyGrips(self.main_namespace, "left", self.main_namespace.hide_grips)
            self.main_namespace.right_grip = PyGrips(self.main_namespace, "right", self.main_namespace.hide_grips)
            self.main_namespace.top_grip = PyGrips(self.main_namespace, "top", self.main_namespace.hide_grips)
            self.main_namespace.bottom_grip = PyGrips(self.main_namespace, "bottom", self.main_namespace.hide_grips)
            self.main_namespace.top_left_grip = PyGrips(self.main_namespace, "top_left", self.main_namespace.hide_grips)
            self.main_namespace.top_right_grip = PyGrips(self.main_namespace, "top_right", self.main_namespace.hide_grips)
            self.main_namespace.bottom_left_grip = PyGrips(self.main_namespace, "bottom_left", self.main_namespace.hide_grips)
            self.main_namespace.bottom_right_grip = PyGrips(self.main_namespace, "bottom_right", self.main_namespace.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.main_namespace.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        

        # SET SIGNALS
        self.main_namespace.ui.left_menu.clicked.connect(self.main_namespace.btn_clicked)
        self.main_namespace.ui.left_menu.released.connect(self.main_namespace.btn_released)
        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        #self.main_namespace.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.main_namespace.ui.title_bar.clicked.connect(self.main_namespace.btn_clicked)
        self.main_namespace.ui.title_bar.released.connect(self.main_namespace.btn_released)

        # ADD Title
        self.main_namespace.ui.title_bar.set_title(self.main_namespace.settings["app_name"])
        
        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.main_namespace.ui.left_column.clicked.connect(self.main_namespace.btn_clicked)
        self.main_namespace.ui.left_column.released.connect(self.main_namespace.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self.main_namespace, self.main_namespace.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self.main_namespace,
            menu = self.main_namespace.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self.main_namespace, self.main_namespace.ui.right_column.menu_1)


        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.main_namespace.settings = settings.items
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.main_namespace.themes = themes.items

        self.main_namespace.ui.load_pages.stackedWidget.setCurrentWidget(self.main_namespace.ui.load_pages.page_AutoOperate)

        self.main_namespace.MMG=Memory_Manager(Master_memoryPool=self.Master_memoryPool,queuePool=self.queuePool)
        self.main_namespace.testPattern=TestPatternWidget(self.main_namespace,queuePool=self.queuePool)
        self.main_namespace.tempPattern=TempPatternWidget(self.main_namespace,queuePool=self.queuePool)
        self.main_namespace.main_utility_manager= Main_utility_manager(self.main_namespace,queuePool=self.queuePool,eventPool=self.eventPool)
        self.main_namespace.testfile_manager=Testfile_manager(self.main_namespace,queuePool=self.queuePool)
        
        

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):

        #self.main_namespace.tempPattern.graphResize()

        if self.main_namespace.settings["custom_title_bar"]:
            self.main_namespace.left_grip.setGeometry(5, 10, 10, self.main_namespace.height())
            self.main_namespace.right_grip.setGeometry(self.main_namespace.width() - 15, 10, 10, self.main_namespace.height())
            self.main_namespace.top_grip.setGeometry(5, 5, self.main_namespace.width() - 10, 10)
            self.main_namespace.bottom_grip.setGeometry(5, self.main_namespace.height() - 15, self.main_namespace.width() - 10, 10)
            self.main_namespace.top_right_grip.setGeometry(self.main_namespace.width() - 20, 5, 15, 15)
            self.main_namespace.bottom_left_grip.setGeometry(5, self.main_namespace.height() - 20, 15, 15)
            self.main_namespace.bottom_right_grip.setGeometry(self.main_namespace.width() - 20, self.main_namespace.height() - 20, 15, 15)


    





    