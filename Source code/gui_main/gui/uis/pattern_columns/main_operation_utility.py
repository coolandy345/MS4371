import threading
import time
from gui_main.qt_core import *
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *

class Main_utility_manager(QWidget):
    def __init__( 
            self, 
            parent = None,
            app_parent = None,
            memoryPool={},
            queuePool={}
    ):
        super().__init__()

        self._parent=parent
        self._app_parent=app_parent
        self.memoryPool=memoryPool
        self.queuePool=queuePool

        self.Main_utility_setup()

        connnection_check_Thread = threading.Thread(target = self.connnection_check_Work)
        connnection_check_Thread.start()

        status_Lamp_Thread = threading.Thread(target = self.status_Lamp_Work)
        status_Lamp_Thread.start()


        self.ready_icon_active=False
        self.stop_icon_active=False
        self.vacuum_icon_active=False
        self.heating_icon_active=False
        self.keepTemp_icon_active=False
        self.testing_icon_active=False
        self.testFinishing_icon_active=False
        self.error_icon_active=False
        self.ethernetConnecton_icon_active=False
        self.usbConnecton_icon_active=False
        self.gPIBConnecton_2657A_icon_active=False
        self.gPIBConnecton_2635B_icon_active=False


        
        self.timer=QTimer()
        self.timer.timeout.connect(self.regularWork)
        self.timer.start(10)


        


    def btn_callback(self):
        btn_name=self.sender().objectName()

        if btn_name == "btn_AutoMode":
            self._parent.ui.load_pages.stackedWidget.setCurrentWidget(self._parent.ui.load_pages.page_AutoOperate)
        elif btn_name == "btn_ManaualMode":
            self._parent.ui.load_pages.stackedWidget.setCurrentWidget(self._parent.ui.load_pages.page_ManaulOperate)
        elif btn_name == "autostart_pushButton":
            self._parent.testfile_manager.prepare_folder()


    def Main_utility_setup(self):

        self._parent.ui.load_pages.btn_AutoMode.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.btn_ManaualMode.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.autostart_pushButton.clicked.connect(self.btn_callback)

        

        
        self._parent.ready_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-play-extralarge.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "運転可",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = self._parent.themes["app_color"]["dark_three"],
                bg_color_pressed = self._parent.themes["app_color"]["dark_three"],
            )
        self._parent.ui.load_pages.Layout_Status_RunReady.addWidget(self._parent.ready_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.stop_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("stop-button-extralarge.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "停止中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = self._parent.themes["app_color"]["dark_three"],
                bg_color_pressed = self._parent.themes["app_color"]["dark_three"],
            )
        self._parent.ui.load_pages.Layout_Status_STOP.addWidget(self._parent.stop_icon, Qt.AlignCenter, Qt.AlignCenter)

        
        self._parent.vacuum_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-shuffle-extralarge.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "真空置換中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = "#1e2229",
                bg_color_pressed = "#1e2229",
            )
        self._parent.ui.load_pages.Layout_Status_Vacuum.addWidget(self._parent.vacuum_icon, Qt.AlignCenter, Qt.AlignCenter)


        self._parent.heating_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("heater-extralarge.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "昇温中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = "#1e2229",
                bg_color_pressed = "#1e2229",
            )
        self._parent.ui.load_pages.Layout_Status_Heating.addWidget(self._parent.heating_icon, Qt.AlignCenter, Qt.AlignCenter)


        self._parent.keepTemp_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("reuse-extralarge.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "温度キープ中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = self._parent.themes["app_color"]["dark_three"],
                bg_color_pressed = self._parent.themes["app_color"]["dark_three"],
            )
        self._parent.ui.load_pages.Layout_Status_KeepTemp.addWidget(self._parent.keepTemp_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.testing_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("oscilloscope-extralarge.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "測定中",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = self._parent.themes["app_color"]["dark_three"],
                bg_color_pressed = self._parent.themes["app_color"]["dark_three"],
            )
        self._parent.ui.load_pages.Layout_Status_Testing.addWidget(self._parent.testing_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.testFinishing_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("cold-temperature-extralarge.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "測定終了(降温中)",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = self._parent.themes["app_color"]["dark_three"],
                bg_color_pressed = self._parent.themes["app_color"]["dark_three"],
            )
        self._parent.ui.load_pages.Layout_Status_TestFinishing.addWidget(self._parent.testFinishing_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.error_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-exclamation-extralarge.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "電気炉警報",
                width = 60,
                height = 60,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["critical_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["critical_icon"]["icon_hover"],
                icon_color_pressed = self._parent.themes["app_color"]["critical_icon"]["icon_pressed"],
                icon_color_deactive = self._parent.themes["app_color"]["critical_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = self._parent.themes["app_color"]["dark_three"],
                bg_color_pressed = self._parent.themes["app_color"]["dark_three"],
            )
        self._parent.ui.load_pages.Layout_Status_Error.addWidget(self._parent.error_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.ethernetConnecton_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("ethernet.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "電気炉接続",
                width = 45,
                height = 45,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = self._parent.themes["app_color"]["dark_three"],
                bg_color_pressed = self._parent.themes["app_color"]["dark_three"],
            )
        self._parent.ui.load_pages.Layout_Status_EthernetConnecton.addWidget(self._parent.ethernetConnecton_icon, Qt.AlignCenter, Qt.AlignCenter)

        
        self._parent.usbConnecton_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("usb-symbol-svgrepo-com.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "USB インターフェース",
                width = 45,
                height =45,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = self._parent.themes["app_color"]["dark_three"],
                bg_color_pressed = self._parent.themes["app_color"]["dark_three"],
            )
        self._parent.ui.load_pages.Layout_Status_USBConnecton.addWidget(self._parent.usbConnecton_icon, Qt.AlignCenter, Qt.AlignCenter)



        self._parent.gPIBConnecton_2657A_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("link-2657A.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "2657A接続",
                width = 45,
                height = 45,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = self._parent.themes["app_color"]["dark_three"],
                bg_color_pressed = self._parent.themes["app_color"]["dark_three"],
            )
        self._parent.ui.load_pages.Layout_Status_2657A_GPIBConnecton.addWidget(self._parent.gPIBConnecton_2657A_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.gPIBConnecton_2635B_icon = PyIconButton(
                icon_path = Functions.set_svg_icon("link-2635B.svg"),
                parent = self._parent,
                app_parent = self._parent.ui.central_widget,
                tooltip_text = "2635B接続",
                width = 45,
                height = 45,
                radius = 10,
                dark_one = self._parent.themes["app_color"]["dark_one"],
                icon_color = self._parent.themes["app_color"]["regular_icon"]["icon_color"],
                icon_color_hover = self._parent.themes["app_color"]["regular_icon"]["icon_hover"],
                icon_color_pressed = self._parent.themes["app_color"]["regular_icon"]["icon_pressed"],
                icon_color_deactive = self._parent.themes["app_color"]["regular_icon"]["icon_deactive"],
                bg_color = "#1e2229",
                bg_color_hover = self._parent.themes["app_color"]["dark_three"],
                bg_color_pressed = self._parent.themes["app_color"]["dark_three"],
            )
        self._parent.ui.load_pages.Layout_Status_2635B_GPIBConnecton.addWidget(self._parent.gPIBConnecton_2635B_icon, Qt.AlignCenter, Qt.AlignCenter)
        
        
    def regularWork(self):


        if self.ready_icon_active != self._parent.ready_icon._is_active:
            self._parent.ready_icon.set_active(self.ready_icon_active)
        if self.stop_icon_active != self._parent.stop_icon._is_active:
            self._parent.stop_icon.set_active(self.stop_icon_active)
        if self.vacuum_icon_active != self._parent.vacuum_icon._is_active:
            self._parent.vacuum_icon.set_active(self.vacuum_icon_active)
        if self.heating_icon_active != self._parent.heating_icon._is_active:
            self._parent.heating_icon.set_active(self.heating_icon_active)
        if self.keepTemp_icon_active != self._parent.keepTemp_icon._is_active:
            self._parent.keepTemp_icon.set_active(self.keepTemp_icon_active)
        if self.testing_icon_active != self._parent.testing_icon._is_active:
            self._parent.testing_icon.set_active(self.testing_icon_active)
        if self.testFinishing_icon_active != self._parent.testFinishing_icon._is_active:
            self._parent.testFinishing_icon.set_active(self.testFinishing_icon_active)
        if self.error_icon_active != self._parent.error_icon._is_active:
            self._parent.error_icon.set_active(self.error_icon_active)
        if self.ethernetConnecton_icon_active != self._parent.ethernetConnecton_icon._is_active:
            self._parent.ethernetConnecton_icon.set_active(self.ethernetConnecton_icon_active)
        if self.usbConnecton_icon_active != self._parent.usbConnecton_icon._is_active:
            self._parent.usbConnecton_icon.set_active(self.usbConnecton_icon_active)
        if self.gPIBConnecton_2657A_icon_active != self._parent.gPIBConnecton_2657A_icon._is_active:
            self._parent.gPIBConnecton_2657A_icon.set_active(self.gPIBConnecton_2657A_icon_active)
        if self.gPIBConnecton_2635B_icon_active != self._parent.gPIBConnecton_2635B_icon._is_active:
            self._parent.gPIBConnecton_2635B_icon.set_active(self.gPIBConnecton_2635B_icon_active)


    def status_Lamp_Work(self):

        while 1:
            self.ready_icon_active=self.memoryPool["Modbus Registor Pool - Registor"]["運転可"].getValue()
            self.stop_icon_active=self.memoryPool["Modbus Registor Pool - Registor"]["停止中"].getValue()
            self.vacuum_icon_active=self.memoryPool["Modbus Registor Pool - Registor"]["真空置換中"].getValue()
            self.heating_icon_active=self.memoryPool["Modbus Registor Pool - Registor"]["昇温中"].getValue()
            self.keepTemp_icon_active=self.memoryPool["Modbus Registor Pool - Registor"]["温度ｷｰﾌﾟ中"].getValue()
            self.testing_icon_active=self.memoryPool["Modbus Registor Pool - Registor"]["測定中"].getValue()
            self.testFinishing_icon_active=self.memoryPool["Modbus Registor Pool - Registor"]["運転終了"].getValue()
            self.error_icon_active=self.memoryPool["Modbus Registor Pool - Registor"]["PLC警報"].getValue()
            self.ethernetConnecton_icon_active=self.memoryPool["System memory"]["Ethernet conneciton"].getValue()
            self.usbConnecton_icon_active=self.memoryPool["System memory"]["GPIB USB conneciton"].getValue()
            self.gPIBConnecton_1_icon_active=self.memoryPool["System memory"]["2635B connection"].getValue()
            self.gPIBConnecton_2_icon_active=self.memoryPool["System memory"]["2657A connection"].getValue()

            time.sleep(0.1)

    def connnection_check_Work(self):
        
        while 1:
            if self.memoryPool["System memory"]["GPIB USB conneciton"].getValue():
                pass
                #self._parent.ui.load_pages.label_47.setVisible(True)
            else:
                pass
                #self._parent.ui.load_pages.label_47.setVisible(False)
        time.sleep(0.5)