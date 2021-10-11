# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
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

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
# -*- coding: utf-8 -*-

from gui_main.gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os

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

class workThread(QThread):

    trigger = Signal()

    #def __int__(self):
    #    # 初始化函式
    #    print("Initial")
    #    super(workThread, self).__init__()

    def run(self):
        self.trigger.emit()


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self,main_namespace,memorypool):
        super().__init__()

        self.main_namespace=main_namespace
        self.memorypool=memorypool
        self.setup_gui(self.memorypool)

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
        {
            "btn_icon" : "fi-rr-link.svg",
            "btn_id" : "btn_ConnectionMenu",
            "btn_text" : "通信接続設定",
            "btn_tooltip" : "通信接続設定",
            "show_top" : True,
            "is_active" : False
        }
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
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


    def tempPatternInitWork(self):
        self.main_namespace.tempPattern=TempPatternWidget(self.main_namespace,app_parent=self.main_namespace.ui.central_widget,memory_pool=self.memorypool)
        

    def testPatternInitWork(self):
        self.main_namespace.testPattern=TestPatternWidget(self.main_namespace,app_parent=self.main_namespace.ui.central_widget,memory_pool=self.memorypool)
        


    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self,memory_pool):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.main_namespace.setWindowTitle(self.main_namespace.settings["app_name"])
        
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
        self.main_namespace.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

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
        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.main_namespace.settings = settings.items
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.main_namespace.themes = themes.items

        self.main_namespace.ui.load_pages.stackedWidget.setCurrentWidget(self.main_namespace.ui.load_pages.page_AutoOperate)

        self.main_namespace.ui.load_pages.btn_AutoMode.clicked.connect(self.main_namespace.btn_clicked)
        self.main_namespace.ui.load_pages.btn_ManaualMode.clicked.connect(self.main_namespace.btn_clicked)

        self.main_namespace.MS_ConnectionToggle=PyToggle()
        self.main_namespace.ui.load_pages.gridLayout_27.addWidget(self.main_namespace.MS_ConnectionToggle)
        
        self.main_namespace.Tester_ConnectionToggle=PyToggle()
        self.main_namespace.ui.load_pages.gridLayout_28.addWidget(self.main_namespace.Tester_ConnectionToggle)
        
        self.tempPatternThread = workThread(self.main_namespace)
        self.tempPatternThread.trigger.connect(self.tempPatternInitWork)
        self.tempPatternThread.start()

        self.testPatternThread = workThread(self.main_namespace)
        self.testPatternThread.trigger.connect(self.testPatternInitWork)
        self.testPatternThread.start()



        self.main_namespace.stop_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("stop-button-extralarge.svg"),
                parent = self.main_namespace,
                app_parent = self.main_namespace.ui.central_widget,
                tooltip_text = "停止中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.main_namespace.themes["app_color"]["dark_one"],
                icon_color = self.main_namespace.themes["app_color"]["icon_color"],
                icon_color_hover = self.main_namespace.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.main_namespace.themes["app_color"]["white"],
                icon_color_active = self.main_namespace.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.main_namespace.themes["app_color"]["dark_three"],
                bg_color_pressed = self.main_namespace.themes["app_color"]["dark_three"],
            )
        self.main_namespace.ui.load_pages.Layout_Status_STOP.addWidget(self.main_namespace.stop_icon, Qt.AlignCenter, Qt.AlignCenter)

        # rererherherher

        self.main_namespace.heating_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("heater-extralarge.svg"),
                parent = self.main_namespace,
                app_parent = self.main_namespace.ui.central_widget,
                tooltip_text = "昇温中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.main_namespace.themes["app_color"]["dark_one"],
                icon_color = self.main_namespace.themes["app_color"]["icon_color"],
                icon_color_hover = self.main_namespace.themes["app_color"]["icon_color"],
                icon_color_pressed = self.main_namespace.themes["app_color"]["icon_color"],
                icon_color_active = self.main_namespace.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = "#1e2229",
                bg_color_pressed = "#1e2229",
            )
        self.main_namespace.ui.load_pages.Layout_Status_Heating.addWidget(self.main_namespace.heating_icon, Qt.AlignCenter, Qt.AlignCenter)


        self.main_namespace.keepTemp_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("reuse-extralarge.svg"),
                parent = self.main_namespace,
                app_parent = self.main_namespace.ui.central_widget,
                tooltip_text = "温度キープ中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.main_namespace.themes["app_color"]["dark_one"],
                icon_color = self.main_namespace.themes["app_color"]["icon_color"],
                icon_color_hover = self.main_namespace.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.main_namespace.themes["app_color"]["white"],
                icon_color_active = self.main_namespace.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.main_namespace.themes["app_color"]["dark_three"],
                bg_color_pressed = self.main_namespace.themes["app_color"]["dark_three"],
            )
        self.main_namespace.ui.load_pages.Layout_Status_KeepTemp.addWidget(self.main_namespace.keepTemp_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.main_namespace.testing_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("oscilloscope-extralarge.svg"),
                parent = self.main_namespace,
                app_parent = self.main_namespace.ui.central_widget,
                tooltip_text = "測定中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.main_namespace.themes["app_color"]["dark_one"],
                icon_color = self.main_namespace.themes["app_color"]["icon_color"],
                icon_color_hover = self.main_namespace.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.main_namespace.themes["app_color"]["white"],
                icon_color_active = self.main_namespace.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.main_namespace.themes["app_color"]["dark_three"],
                bg_color_pressed = self.main_namespace.themes["app_color"]["dark_three"],
            )
        self.main_namespace.ui.load_pages.Layout_Status_Testing.addWidget(self.main_namespace.testing_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.main_namespace.testFinishing_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("cold-temperature-extralarge.svg"),
                parent = self.main_namespace,
                app_parent = self.main_namespace.ui.central_widget,
                tooltip_text = "測定終了(降温中)",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.main_namespace.themes["app_color"]["dark_one"],
                icon_color = self.main_namespace.themes["app_color"]["icon_color"],
                icon_color_hover = self.main_namespace.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.main_namespace.themes["app_color"]["white"],
                icon_color_active = self.main_namespace.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.main_namespace.themes["app_color"]["dark_three"],
                bg_color_pressed = self.main_namespace.themes["app_color"]["dark_three"],
            )
        self.main_namespace.ui.load_pages.Layout_Status_TestFinishing.addWidget(self.main_namespace.testFinishing_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.main_namespace.error_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-exclamation-extralarge.svg"),
                parent = self.main_namespace,
                app_parent = self.main_namespace.ui.central_widget,
                tooltip_text = "警報発生中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.main_namespace.themes["app_color"]["dark_one"],
                icon_color = "#ff5869",
                icon_color_hover = "#ff5869",
                icon_color_pressed = self.main_namespace.themes["app_color"]["white"],
                icon_color_active = self.main_namespace.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.main_namespace.themes["app_color"]["dark_three"],
                bg_color_pressed = self.main_namespace.themes["app_color"]["dark_three"],
            )
        self.main_namespace.ui.load_pages.Layout_Status_Error.addWidget(self.main_namespace.error_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.main_namespace.ethernetConnecton_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("ethernet-extralarge.svg"),
                parent = self.main_namespace,
                app_parent = self.main_namespace.ui.central_widget,
                tooltip_text = "電気炉接続",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.main_namespace.themes["app_color"]["dark_one"],
                icon_color = self.main_namespace.themes["app_color"]["icon_color"],
                icon_color_hover = self.main_namespace.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.main_namespace.themes["app_color"]["white"],
                icon_color_active = self.main_namespace.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.main_namespace.themes["app_color"]["dark_three"],
                bg_color_pressed = self.main_namespace.themes["app_color"]["dark_three"],
            )
        self.main_namespace.ui.load_pages.Layout_Status_EthernetConnecton.addWidget(self.main_namespace.ethernetConnecton_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.main_namespace.gPIBConnecton_1_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("link-2657A-extralarge.svg"),
                parent = self.main_namespace,
                app_parent = self.main_namespace.ui.central_widget,
                tooltip_text = "2657A接続",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.main_namespace.themes["app_color"]["dark_one"],
                icon_color = self.main_namespace.themes["app_color"]["icon_color"],
                icon_color_hover = self.main_namespace.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.main_namespace.themes["app_color"]["white"],
                icon_color_active = self.main_namespace.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.main_namespace.themes["app_color"]["dark_three"],
                bg_color_pressed = self.main_namespace.themes["app_color"]["dark_three"],
            )
        self.main_namespace.ui.load_pages.Layout_Status_GPIBConnecton_1.addWidget(self.main_namespace.gPIBConnecton_1_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.main_namespace.gPIBConnecton_2_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("link-2635B-extralarge.svg"),
                parent = self.main_namespace,
                app_parent = self.main_namespace.ui.central_widget,
                tooltip_text = "2635B接続",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.main_namespace.themes["app_color"]["dark_one"],
                icon_color = self.main_namespace.themes["app_color"]["icon_color"],
                icon_color_hover = self.main_namespace.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.main_namespace.themes["app_color"]["white"],
                icon_color_active = self.main_namespace.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.main_namespace.themes["app_color"]["dark_three"],
                bg_color_pressed = self.main_namespace.themes["app_color"]["dark_three"],
            )
        self.main_namespace.ui.load_pages.Layout_Status_GPIBConnecton_2.addWidget(self.main_namespace.gPIBConnecton_2_icon, Qt.AlignCenter, Qt.AlignCenter)

        
        

        #self.main_namespace.win =pg.PlotWidget(background=None,title="抵抗測定値")
        
        #self.main_namespace.win.setLabel(axis='bottom', text='時間', units='ms')
        #self.main_namespace.win.setLabel(axis='left', text='抵抗値', units='Ω')

        #self.main_namespace.win.setLimits(xMin=-0.9,xMax=20.9)
        #self.main_namespace.axis = self.main_namespace.win.getAxis('bottom')
        #self.main_namespace.axis.setStyle(autoReduceTextSpace=True)
        #self.main_namespace.axis.setTickSpacing(2,1)
        #self.main_namespace.win.setAxisItems({'bottom':self.main_namespace.axis})
        
        #self.main_namespace.win.showGrid(x=True, y=True)
        #self.main_namespace.win.setMouseEnabled(x=True, y=False)
        #self.main_namespace.win.addLegend()

        #self.main_namespace.win.plot(x=[0,1,2,3,8],y=[5,10,10,0,50],pen=pg.mkPen((65,74,88), width=10), symbolBrush=(0,200,200),symbolPen='w', symbol='o', symbolSize=5, name="予定パターン")
        
        #self.main_namespace.ui.load_pages.gridLayout_9.addWidget(self.main_namespace.win, Qt.AlignCenter, Qt.AlignCenter)
        


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


    





    