import threading
import time
from gui_main.qt_core import *
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *
import random
from modbus_TcpServer import MeasurePackage

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

        self.choose_pattern=0

        self.graph_Item="Resistor"

        self.timeUnit=1
        self.timeLabel="s"
        self.timeMaxRange=10
        self.timeMinRange=1

        self.utility_setup()
        self.graph_setup()
        
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
        elif btn_name == "manualMeasurement_pushButton":
            pass
        elif btn_name == "voltageOutput_pushButton":
            pass
        elif btn_name == "outputStop_pushButton":
            pass
        elif btn_name == "gasFreeflow_pushButton":
            pass
        elif btn_name == "eMSstop_pushButton":
            pass
        elif btn_name == "measurement_comboBox":
            pass
        elif btn_name == "voltage_lineEdit":
            pass
        elif btn_name == "AutoMode_pattern_comboBox":
            pass

        elif btn_name == "graphItem_combobox":
            index=self._parent.ui.load_pages.graphItem_combobox.currentText()
            if index=="抵抗値":
                self.graph_Item="Resistor"
                self._parent.ui.load_pages.timeUnit_Label.setVisible (True)
                self._parent.ui.load_pages.timeUnit_comboBox.setVisible (True)
                self._parent.ui.load_pages.frame_66.setVisible (True)
            elif index=="運転パターン":
                self.graph_Item="Pattern"
                self._parent.ui.load_pages.timeUnit_Label.setVisible (False)
                self._parent.ui.load_pages.timeUnit_comboBox.setVisible (False)
                self._parent.ui.load_pages.frame_66.setVisible (False)

                
                self.timeUnit=3600
                self.timeLabel="hr"
                self.timeMaxRange=10
                self.timeMinRange=1
                
            
        elif btn_name == "timeUnit_comboBox":

            index=self._parent.ui.load_pages.timeUnit_comboBox.currentText()
            if index=="1s/div":
                self.timeUnit=1
                self.timeLabel="s"
                self.timeMaxRange=10
                self.timeMinRange=1
            elif index=="1min/div":
                self.timeUnit=60
                self.timeLabel="min"
                self.timeMaxRange=10
                self.timeMinRange=1
            elif index=="1h/div":
                self.timeUnit=3600
                self.timeLabel="hour"
                self.timeMaxRange=10
                self.timeMinRange=1

            self.graph_update()

        
    def utility_update(self):
        self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndexChanged.disconnect()
        self._parent.ui.load_pages.AutoMode_pattern_comboBox.clear()
        self._parent.ui.load_pages.AutoMode_pattern_comboBox.addItems(self._parent.tempPattern.patternFile_nameList)
        self._parent.ui.load_pages.AutoMode_pattern_comboBox.setCurrentIndex(self.choose_pattern)
        self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndexChanged.connect(self.btn_callback)

    def utility_setup(self):

        self.graph_setup()

        self._parent.ui.load_pages.btn_AutoMode.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.btn_ManaualMode.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.autostart_pushButton.clicked.connect(self.btn_callback)

        self._parent.ui.load_pages.manualMeasurement_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.voltageOutput_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.outputStop_pushButton.clicked.connect(self.btn_callback)

        self._parent.ui.load_pages.gasFreeflow_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.autostart_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.eMSstop_pushButton.clicked.connect(self.btn_callback)

        self._parent.ui.load_pages.voltage_lineEdit.editingFinished.connect(self.btn_callback)
        self._parent.ui.load_pages.measurement_comboBox.currentIndexChanged.connect(self.btn_callback)

        self._parent.ui.load_pages.graphItem_combobox.currentIndexChanged.connect(self.btn_callback)
        self._parent.ui.load_pages.timeUnit_comboBox.currentIndexChanged.connect(self.btn_callback)
        
        self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndexChanged.connect(self.btn_callback)

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
        
    def graph_update(self):
        self.data_array=[]

        if self.graph_Item=="Resistor":
            for data in self.memoryPool["Read Measurement Data"]:
                XYdata={}
                XYdata["x"]=data.time/self.timeUnit
                XYdata["y"]=data.resistor
                self.data_array.append(XYdata)
            self._parent.curve.setData(self.data_array)
        else:
            self.choose_pattern=self.memoryPool["System memory"]["choose_Pattern"].getValue()
            if choose_pattern:
                pattern_availible_number=self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_実行STEP数".format(choose_pattern)].getValue()
            
                self.data_array.append({"x":0,"y":0})
                for step in (1,pattern_availible_number+1):
                    XYdata={}
                    XYdata["x"]=self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_ステップ累計時間".format(choose_pattern,step)].getValue()
                    XYdata["y"]=self.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_SV値".format(choose_pattern,step)].getValue()
                    self.data_array.append(XYdata)
            #not choose_pattern yet 
            else:
                self.data_array=[]
            self._parent.curve.setData(self.data_array)

        self._parent.realTimeData_Graph.setLabel(axis='bottom', text='時間', units=self.timeLabel)
        self._parent.realTimeData_Graph.setLimits(minXRange=self.timeMinRange,maxXRange=self.timeMaxRange)

    def graph_setup(self):
        self._parent.realTimeData_Graph =pg.PlotWidget(background=None,title="測定抵抗値")
        self._parent.realTimeData_Graph.setLabel(axis='left', text='抵抗値', units='Ω')
        self._parent.realTimeData_Graph.setLabel(axis='bottom', text='時間', units='s')

        self._parent.Xaxis = self._parent.realTimeData_Graph.getAxis('bottom')
        self._parent.realTimeData_Graph.setAxisItems({'bottom':self._parent.Xaxis})
        
        self._parent.Yaxis = self._parent.realTimeData_Graph.getAxis('left')
        self._parent.Yaxis.enableAutoSIPrefix(True)

        self._parent.realTimeData_Graph.showGrid(x=True, y=True)
        self._parent.realTimeData_Graph.setMouseEnabled(x=True, y=False)
        self._parent.realTimeData_Graph.setLimits(minXRange=1,maxXRange=10)
        self._parent.realTimeData_Graph.setLimits(xMin=0,yMin=0)

        self._parent.curve=self._parent.realTimeData_Graph.plot(pen=pg.mkPen((225, 230, 241),width=5), 
                                   symbolBrush=(0,0,0),
                                   symbolPen='w', 
                                   #symbol='o', 
                                   symbolSize=5, 
                                   name="予定パターン")
        
        self.data_array=[]
        self.time=0
        self._parent.curve.setData(self.data_array)
        self._parent.ui.load_pages.realtime_grapgLayout.addWidget(self._parent.realTimeData_Graph, Qt.AlignCenter, Qt.AlignCenter)

        
    def regularWork(self):

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
        self.gPIBConnecton_2635B_icon_active=self.memoryPool["System memory"]["2635B connection"].getValue()
        self.gPIBConnecton_2657A_icon_active=self.memoryPool["System memory"]["2657A connection"].getValue()

        
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

 

