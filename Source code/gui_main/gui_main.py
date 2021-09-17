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
from gui_main.gui.uis.windows.main_window.functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui_main.qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui_main.gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.widgets import *

from main import shotdown_entire_app


# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self,memory_pool):
        super().__init__()


        self.focus_step_number=0
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.memory_pool=memory_pool
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips

        SetupMainWindow.setup_gui(self,memory_pool=self.memory_pool)
        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////

        
        self.show()


        self.ui.left_menu.toggle_animation()


    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)
        # LEFT MENU
        # ///////////////////////////////////////////////////////////////

        # OPEN PAGE
        if btn.objectName() == "btn_PrepareMenu":
            # Select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        if btn.objectName() == "btn_OperateMenu":
            # Select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
        
        if btn.objectName() == "btn_ParameterPatternMenu":
            # Select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 3
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

        if btn.objectName() == "btn_ConnectionMenu":
            # Select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page 4
            MainFunctions.set_page(self, self.ui.load_pages.page_4)


        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

        if btn.objectName() == "btn_AutoMode":
            self.ui.load_pages.stackedWidget.setCurrentWidget(self.ui.load_pages.page_AutoOperate)

        if btn.objectName() == "btn_ManaualMode":
            self.ui.load_pages.stackedWidget.setCurrentWidget(self.ui.load_pages.page_ManaulOperate)
        
        if btn.objectName() == "new_temp_Step_Buttom":
            self.tempPattern.new_TempPattern()

        if btn.objectName() == "new_test_Step_Buttom":
            self.testPattern.new_TestPattern()
        
        #self.SetupMainWindow.
        self.tempPattern.close_menu()
        self.testPattern.close_menu()

        # DEBUG 
        #print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        if btn.objectName() == "new_temp_Step_Buttom":
            self.tempPattern.scroll_adjust_TempPattern()
            pass

        if btn.objectName() == "new_test_Step_Buttom":
            self.testPattern.scroll_adjust_TestPattern()
            pass

        # DEBUG
        #print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.tempPattern.close_menu()
       # self.tempPattern.step_widges_list[self.focus_step_number-1].close_menu()
        self.focus_step_number=0
        self.dragPos = event.globalPos()




def initial_GUI(memory_pool):
    print("Gui initialing")
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("motoyama_icon.ico"))
    window = MainWindow(memory_pool)
    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    
    #sys.exit(app.exec_())
    app.exec_()
    print("Gui has been close")
    #shotdown_entire_app()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":

    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("motoyama_icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())