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


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()

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

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self,memory_pool):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

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
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self.ui.load_pages.stackedWidget.setCurrentWidget(self.ui.load_pages.page_AutoOperate)

        self.ui.load_pages.btn_AutoMode.clicked.connect(self.btn_clicked)
        self.ui.load_pages.btn_ManaualMode.clicked.connect(self.btn_clicked)

        self.MS_ConnectionToggle=PyToggle()
        self.ui.load_pages.gridLayout_27.addWidget(self.MS_ConnectionToggle)

        self.Tester_ConnectionToggle=PyToggle()
        self.ui.load_pages.gridLayout_28.addWidget(self.Tester_ConnectionToggle)
        self.tempPattern=TempPatternWidget(self,app_parent=self.ui.central_widget,memory_pool=memory_pool)
        self.testPattern=TestPatternWidget(self,app_parent=self.ui.central_widget,memory_pool=memory_pool)
        
        self.stop_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("stop-button-extralarge.svg"),
                parent = self,
                app_parent = self.ui.central_widget,
                tooltip_text = "停止中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["dark_three"],
            )
        self.ui.load_pages.Layout_Status_STOP.addWidget(self.stop_icon, Qt.AlignCenter, Qt.AlignCenter)

        # rererherherher

        self.heating_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("heater-extralarge.svg"),
                parent = self,
                app_parent = self.ui.central_widget,
                tooltip_text = "昇温中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_color"],
                icon_color_pressed = self.themes["app_color"]["icon_color"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = "#1e2229",
                bg_color_pressed = "#1e2229",
            )
        self.ui.load_pages.Layout_Status_Heating.addWidget(self.heating_icon, Qt.AlignCenter, Qt.AlignCenter)


        self.keepTemp_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("reuse-extralarge.svg"),
                parent = self,
                app_parent = self.ui.central_widget,
                tooltip_text = "温度キープ中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["dark_three"],
            )
        self.ui.load_pages.Layout_Status_KeepTemp.addWidget(self.keepTemp_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.testing_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("oscilloscope-extralarge.svg"),
                parent = self,
                app_parent = self.ui.central_widget,
                tooltip_text = "測定中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["dark_three"],
            )
        self.ui.load_pages.Layout_Status_Testing.addWidget(self.testing_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.testFinishing_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("cold-temperature-extralarge.svg"),
                parent = self,
                app_parent = self.ui.central_widget,
                tooltip_text = "測定終了(降温中)",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["dark_three"],
            )
        self.ui.load_pages.Layout_Status_TestFinishing.addWidget(self.testFinishing_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.error_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-exclamation-extralarge.svg"),
                parent = self,
                app_parent = self.ui.central_widget,
                tooltip_text = "警報発生中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = "#ff5869",
                icon_color_hover = "#ff5869",
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["dark_three"],
            )
        self.ui.load_pages.Layout_Status_Error.addWidget(self.error_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.ethernetConnecton_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("ethernet-extralarge.svg"),
                parent = self,
                app_parent = self.ui.central_widget,
                tooltip_text = "電気炉接続",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["dark_three"],
            )
        self.ui.load_pages.Layout_Status_EthernetConnecton.addWidget(self.ethernetConnecton_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.gPIBConnecton_1_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("link-2657A-extralarge.svg"),
                parent = self,
                app_parent = self.ui.central_widget,
                tooltip_text = "2657A接続",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["dark_three"],
            )
        self.ui.load_pages.Layout_Status_GPIBConnecton_1.addWidget(self.gPIBConnecton_1_icon, Qt.AlignCenter, Qt.AlignCenter)

        self.gPIBConnecton_2_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("link-2635B-extralarge.svg"),
                parent = self,
                app_parent = self.ui.central_widget,
                tooltip_text = "2635B接続",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = "#1e2229",
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["dark_three"],
            )
        self.ui.load_pages.Layout_Status_GPIBConnecton_2.addWidget(self.gPIBConnecton_2_icon, Qt.AlignCenter, Qt.AlignCenter)

        #self.win = pg.GraphicsLayoutWidget(show=True)
        #self.win.resize(2000,500)
        #self.win.setBackground(None)
        #pg.setConfigOptions(antialias=True)
        #self.plot = self.win.addPlot(title="昇降温動作パターン")
        #self.plot.setLabel(axis='bottom', text='STEP', units='')
        #self.plot.setLabel(axis='left', text='温度', units='℃')
        
        #self.plot.showGrid(x=True, y=True)
        #self.plot.setMouseEnabled(x=True, y=False)
        #self.plot.addLegend()
        #self.plot.plot(x=[0,1,2],y=[5,10,10],pen=pg.mkPen((65,74,88), width=10), symbolBrush=(0,200,200),symbolPen='w', symbol='o', symbolSize=5, name="予定パターン")
        #self.plot.plot(x=[0,1],y=[5,10],pen=pg.mkPen((1,74,88), width=10), symbolBrush=(0,200,200),symbolPen='w', symbol='o', symbolSize=5, name="実際温度")
        
        #self.ui.load_pages.gridLayout_29.addWidget(self.win, Qt.AlignCenter, Qt.AlignCenter)

        

        self.win =pg.PlotWidget(background=None,title="抵抗測定値")
        
        self.win.setLabel(axis='bottom', text='時間', units='ms')
        self.win.setLabel(axis='left', text='抵抗値', units='Ω')

        self.win.setLimits(xMin=-0.9,xMax=20.9)
        self.axis = self.win.getAxis('bottom')
        self.axis.setStyle(autoReduceTextSpace=True)
        self.axis.setTickSpacing(2,1)
        self.win.setAxisItems({'bottom':self.axis})
        
        self.win.showGrid(x=True, y=True)
        self.win.setMouseEnabled(x=True, y=False)
        self.win.addLegend()

        self.win.plot(x=[0,1,2],y=[5,10,10],pen=pg.mkPen((65,74,88), width=10), symbolBrush=(0,200,200),symbolPen='w', symbol='o', symbolSize=5, name="予定パターン")
        
        self.ui.load_pages.gridLayout_9.addWidget(self.win, Qt.AlignCenter, Qt.AlignCenter)
        

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)





    