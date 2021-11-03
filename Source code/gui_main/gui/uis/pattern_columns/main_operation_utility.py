import threading
import time
from gui_main.qt_core import *
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *
import random
from modbus_TcpServer import MeasurePackage
from registor_manager import *
from quantiphy import Quantity


class Memory_Manager():
    def __init__( 
            self, 
            Master_memoryPool={},
            queuePool={}
    ):
        self.Master_memoryPool=Master_memoryPool
        self.queuePool=queuePool
        self.memoryPool={}

        self.memory_Reload()

        main_MemoryUpLoad_Thread = threading.Thread(target = self.main_MemoryUpLoad_Work,daemon=True)
        main_MemoryUpLoad_Thread.start()

        main_MemoryDownLoad_Thread = threading.Thread(target = self.main_MemoryDownLoad_Work,daemon=True)
        main_MemoryDownLoad_Thread.start()



    def memory_Reload(self):
        """
        DownLoad All the Master_memoryPool to local GUI memoryPool
        """

        for key in self.Master_memoryPool.keys():
            self.memoryPool[key]=self.Master_memoryPool[key]

            
    def main_MemoryDownLoad_Work(self):
        """
        DownLoad the Master_memoryPool to local GUI memoryPool
        When request is got , this thread will delay 0.1s for any other request and do it  at one time
        """
        while 1:
            getItem_list=[]
            getItem_list.append(self.queuePool["memory_DownlaodToGUI_request_Queue"].get())
            
            #Wait for 0.1s for any others request
            time.sleep(0.1)
            while not self.queuePool["memory_DownlaodToGUI_request_Queue"].empty():
                getItem_list.append(self.queuePool["memory_DownlaodToGUI_request_Queue"].get())

            
            #Check the pools has been changed
            poolNameList=[]
            for getItem in getItem_list:
                poolNameList.append(getItem.pool_name)
                #item.registor_name

            poolNameList = list(dict.fromkeys(poolNameList))

            import_pool={}
            for poolname in poolNameList:
                import_pool[poolname]=[]

            for getItem in getItem_list:
                import_pool[getItem.pool_name].append(getItem)

            #print("getItem",poolNameList)
            for pool_name in poolNameList:

                for item in import_pool[pool_name]:
                    value=self.Master_memoryPool[item.pool_name][item.registor_name].getValue()
                    self.memoryPool[item.pool_name][item.registor_name].setValue(value)

    def main_MemoryUpLoad_Work(self):
        """
        UpLoad the local GUI memoryPool to Master_memoryPool
        When request is got , this thread will delay 0.1s for any other request and do it  at one time
        """

        while 1:
            #Wait for any Master memoryPool update request
            getItem_list=[]
            getItem_list.append(self.queuePool["memory_UploadToMaster_Queue"].get())
            #Wait for 0.1s for any others request
            time.sleep(0.1)
            #Collected al  item in this 0.1s
            while not self.queuePool["memory_UploadToMaster_Queue"].empty():
                getItem_list.append(self.queuePool["memory_UploadToMaster_Queue"].get())

            
            #Check the pools has been changed
            poolNameList=[]
            for item in getItem_list:
                poolNameList.append(item.pool_name)
                #item.registor_name

            #Remove Duplicates From poolNameList
            poolNameList = list(dict.fromkeys(poolNameList))

            #Update the local GUI memoryPool to Master_memoryPool
            for pool_name in poolNameList:
                self.Master_memoryPool[pool_name]=self.memoryPool[pool_name]

            #Send database update request
            for item in getItem_list:
                sendItem=MemoryUnit(item.pool_name,item.registor_name)
                self.queuePool["database_Uplaod_Queue"].put(sendItem)



class Main_utility_manager(QWidget):
    def __init__( 
            self, 
            parent = None,
            queuePool={},
            eventPool={}
    ):
        super().__init__()

        self._parent=parent
        self.queuePool=queuePool
        self.eventPool=eventPool

        

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

        self.realTime_Temp=0
        self.realTime_Voltage=0
        self.realTime_Current=0
        self.realTime_Resistor=0

        
        #self.timer=QTimer()
        #self.timer.timeout.connect(self.ultility_Update_Work)
        #self.timer.start(10)

        ultility_Update_Thread = threading.Thread(target = self.ultility_Update_Work,daemon=True)
        ultility_Update_Thread.start()

        realtime_data_Update_Thread = threading.Thread(target = self.realtime_data_Update_Work,daemon=True)
        realtime_data_Update_Thread.start()

    def autoRun_logic(self):

        self.ethernetConnecton_icon_active
        
        self.autostart_signal=True
        self.remoteConnect_signal=True
        self.stop_signal=True
        self.gasFreeflow_signal=True

        self.ready_icon_active
        self.stop_icon_active
        self.vacuum_icon_active
        self.heating_icon_active
        self.keepTemp_icon_active
        self.testing_icon_active
        self.testFinishing_icon_active
        self.error_icon_active


        #
        if self.ethernetConnecton_icon_active and self.ready_icon_active and not self.error_icon_active:
            






            pass

        else:
            
            if self._parent.ui.load_pages.AutoMode_pattern_comboBox.isEnabled():
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.setEnabled(False)

            if self._parent.ui.load_pages.remoteConnect_pushButton.isEnabled():
                self._parent.ui.load_pages.remoteConnect_pushButton.setEnabled(False)
            if self._parent.ui.load_pages.remoteConnect_pushButton.isChecked():
                self._parent.ui.load_pages.remoteConnect_pushButton.setChecked(False)
                
            if self._parent.ui.load_pages.eMSstop_pushButton.isEnabled():
                self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(False)
            if self._parent.ui.load_pages.eMSstop_pushButton.isChecked():
                self._parent.ui.load_pages.eMSstop_pushButton.setChecked(False)
                
            if self._parent.ui.load_pages.autostart_pushButton.isEnabled():
                self._parent.ui.load_pages.autostart_pushButton.setEnabled(False)
            if self._parent.ui.load_pages.autostart_pushButton.isChecked():
                self._parent.ui.load_pages.autostart_pushButton.setChecked(False)
                
            if self._parent.ui.load_pages.gasFreeflow_pushButton.isEnabled():
                self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(False)
            if self._parent.ui.load_pages.gasFreeflow_pushButton.isChecked():
                self._parent.ui.load_pages.gasFreeflow_pushButton.setChecked(False)



    def wait_Operator_Start_Work(self):
        if self.eventPool["Auto Run Start confirm"].wait(0.1):
            self.eventPool["Auto Run Start confirm"].clear()
            print("operator is starting")
        else:
            self._parent.testfile_manager.set_content_Editeable(True)
            print("operator is fail")
            
    def set_memorypool_register(self,pool_name,registor_name,value):
        
        if self._parent.MMG.memoryPool[pool_name][registor_name].getValue()!=value:
            self._parent.MMG.memoryPool[pool_name][registor_name].setValue(value)
            sendItem=MemoryUnit(pool_name,registor_name)
            self.queuePool["memory_UploadToMaster_Queue"].put(sendItem)
            
    def btn_callback(self):
        btn_name=self.sender().objectName()
        print(btn_name,"is press")

        if btn_name == "btn_AutoMode":
            self._parent.ui.load_pages.stackedWidget.setCurrentWidget(self._parent.ui.load_pages.page_AutoOperate)
        elif btn_name == "btn_ManaualMode":
            self._parent.ui.load_pages.stackedWidget.setCurrentWidget(self._parent.ui.load_pages.page_ManaulOperate)
        elif btn_name == "autostart_pushButton":
            self.autostart_signal=True
            #self.eventPool["Auto Run Start"].set()
            #wait_Operator_Start_Thread = threading.Thread(target = self.wait_Operator_Start_Work,daemon=True)
            #wait_Operator_Start_Thread.start()

            self._parent.testfile_manager.set_content_Editeable(False)

            self._parent.ui.load_pages.AutoMode_pattern_comboBox.setEnabled(False)

            self._parent.ui.load_pages.autostart_pushButton.setEnabled(False)
            self._parent.ui.load_pages.autostart_pushButton.setChecked(1)
            self._parent.ui.load_pages.autostart_pushButton.setText("運転中")

            self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(True)
            self._parent.ui.load_pages.eMSstop_pushButton.setChecked(0)
            
            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",0)

            #Check all condition to start sequence
                # Lock parameter setting
                # Prepare folder to recorda
                # Tell PLC to start pattern

            #self._parent.testfile_manager.prepare_folder()

        elif btn_name == "remoteConnect_pushButton":
            
            self.remoteConnect_signal=True
            set=self._parent.ui.load_pages.remoteConnect_pushButton.isChecked()
            self.set_memorypool_register("Modbus Registor Pool - Registor","リモート",int(set))
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",0)
            #self.set_memorypool_register("Modbus Registor Pool - Registor","PC警報",int(set))


            pass

        elif btn_name == "manualMeasurement_pushButton":
            self.eventPool["Test Event2"].set()
             # Read valtage and current from gpib device


            pass
        elif btn_name == "voltageOutput_pushButton":
            self.eventPool["Test Event1"].set()
            # Check if we can output valtage
            # Let GPIB device to output valtage
            pass

        elif btn_name == "gasFreeflow_pushButton":
            self.gasFreeflow_signal=True
            # Set Gas registor to memory bus
            #self.set_memorypool_register("Modbus Registor Pool - Registor","大気圧",1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
            
            pass



        elif btn_name == "eMSstop_pushButton" or btn_name == "outputStop_pushButton":
            self.stop_signal=True
            self.eventPool["GPIB Stop"].set()
            self._parent.testfile_manager.set_content_Editeable(True)

            self._parent.ui.load_pages.autostart_pushButton.setEnabled(True)
            self._parent.ui.load_pages.autostart_pushButton.setChecked(0)
            self._parent.ui.load_pages.autostart_pushButton.setText("運転開始")

            self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(False)
            self._parent.ui.load_pages.eMSstop_pushButton.setChecked(1)

            
            self._parent.ui.load_pages.AutoMode_pattern_comboBox.setEnabled(True)

            self.set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",1)

            
            #Stop Auto sequence
                #if we ok to process
                    #Lock auto start check box

             #Reset GPIB device any way

            pass

        elif btn_name == "measurement_comboBox":
            # Set measurement mode 

            pass

        elif btn_name == "voltage_lineEdit":
            # Set output voltage limit
            self.set_memorypool_register("System memory","Manual_Measurement_Voltage",float(self._parent.ui.load_pages.voltage_lineEdit.text()))


        elif btn_name == "AutoMode_pattern_comboBox":

            self._parent.ui.load_pages.autostart_pushButton.setEnabled(True)
            self._parent.ui.load_pages.autostart_pushButton.setChecked(0)

            self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(False)
            self._parent.ui.load_pages.eMSstop_pushButton.setChecked(0)

            #choose pattern
            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.",int(self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndex()+1))
            time.sleep(0.1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",1)

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
        pass
        #self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndexChanged.disconnect()
        #self._parent.ui.load_pages.AutoMode_pattern_comboBox.clear()
        #self._parent.ui.load_pages.AutoMode_pattern_comboBox.addItems(self._parent.tempPattern.patternFile_nameList)
        #self._parent.ui.load_pages.AutoMode_pattern_comboBox.setCurrentIndex(self.choose_pattern)
        #self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndexChanged.connect(self.btn_callback)

    def utility_setup(self):

        self.graph_setup()

        self._parent.ui.load_pages.btn_AutoMode.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.btn_ManaualMode.clicked.connect(self.btn_callback)

        self._parent.ui.load_pages.manualMeasurement_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.voltageOutput_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.outputStop_pushButton.clicked.connect(self.btn_callback)



        
        self._parent.ui.load_pages.remoteConnect_pushButton.clicked.connect(self.btn_callback)

        self._parent.ui.load_pages.gasFreeflow_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.autostart_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.eMSstop_pushButton.clicked.connect(self.btn_callback)

        self._parent.ui.load_pages.voltage_lineEdit.editingFinished.connect(self.btn_callback)
        self._parent.ui.load_pages.voltage_lineEdit.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.measurement_comboBox.currentIndexChanged.connect(self.btn_callback)

        self._parent.ui.load_pages.graphItem_combobox.currentIndexChanged.connect(self.btn_callback)
        self._parent.ui.load_pages.timeUnit_comboBox.currentIndexChanged.connect(self.btn_callback)
        
        self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndexChanged.connect(self.btn_callback)

        self._parent.ready_icon = PyIconButton_simple(
                icon = "fi-rr-play-extralarge.svg",
                icon_active = "fi-rr-play-extralarge.svg",
                icon_hover = "fi-rr-play-extralarge.svg",
                icon_deactive = "fi-rr-play-extralarge-deactive.svg",
                btn_id = "運転可",
                tooltip_text = "運転可",
                width = 60,
                height = 60,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        self._parent.ui.load_pages.Layout_Status_RunReady.addWidget(self._parent.ready_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.stop_icon = PyIconButton_simple(
                icon = "stop-button-extralarge.svg",
                icon_active = "stop-button-extralarge.svg",
                icon_hover = "stop-button-extralarge.svg",
                icon_deactive = "stop-button-extralarge-deactive.svg",
                btn_id = "停止中",
                tooltip_text = "停止中",
                width = 60,
                height = 60,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        
        self._parent.ui.load_pages.Layout_Status_STOP.addWidget(self._parent.stop_icon, Qt.AlignCenter, Qt.AlignCenter)

        
        self._parent.vacuum_icon = PyIconButton_simple(
                icon = "fi-rr-shuffle-extralarge.svg",
                icon_active = "fi-rr-shuffle-extralarge.svg",
                icon_hover = "fi-rr-shuffle-extralarge.svg",
                icon_deactive = "fi-rr-shuffle-extralarge-deactive.svg",
                btn_id = "真空置換中",
                tooltip_text = "真空置換中",
                width = 60,
                height = 60,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        
        self._parent.ui.load_pages.Layout_Status_Vacuum.addWidget(self._parent.vacuum_icon, Qt.AlignCenter, Qt.AlignCenter)


        self._parent.heating_icon = PyIconButton_simple(
                icon = "heater-extralarge.svg",
                icon_active = "heater-extralarge.svg",
                icon_hover = "heater-extralarge.svg",
                icon_deactive = "heater-extralarge-deactive.svg",
                btn_id = "昇温中",
                tooltip_text = "昇温中",
                width = 60,
                height = 60,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        
        self._parent.ui.load_pages.Layout_Status_Heating.addWidget(self._parent.heating_icon, Qt.AlignCenter, Qt.AlignCenter)


        self._parent.keepTemp_icon = PyIconButton_simple(
                icon = "reuse-extralarge.svg",
                icon_active = "reuse-extralarge.svg",
                icon_hover = "reuse-extralarge.svg",
                icon_deactive = "reuse-extralarge-deactive.svg",
                btn_id = "温度キープ中",
                tooltip_text = "温度キープ中",
                width = 60,
                height = 60,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        
        self._parent.ui.load_pages.Layout_Status_KeepTemp.addWidget(self._parent.keepTemp_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.testing_icon = PyIconButton_simple(
                icon = "oscilloscope-extralarge.svg",
                icon_active = "oscilloscope-extralarge.svg",
                icon_hover = "oscilloscope-extralarge.svg",
                icon_deactive = "oscilloscope-extralarge-deactive.svg",
                btn_id = "測定中",
                tooltip_text = "測定中",
                width = 60,
                height = 60,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        
        self._parent.ui.load_pages.Layout_Status_Testing.addWidget(self._parent.testing_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.testFinishing_icon = PyIconButton_simple(
                icon = "cold-temperature-extralarge.svg",
                icon_active = "cold-temperature-extralarge.svg",
                icon_hover = "cold-temperature-extralarge.svg",
                icon_deactive = "cold-temperature-extralarge-deactive.svg",
                btn_id = "測定終了(降温中)",
                tooltip_text = "測定終了(降温中)",
                width = 60,
                height = 60,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        self._parent.ui.load_pages.Layout_Status_TestFinishing.addWidget(self._parent.testFinishing_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.error_icon = PyIconButton_simple(
                icon = "fi-rr-exclamation-extralarge.svg",
                icon_active = "fi-rr-exclamation-extralarge.svg",
                icon_hover = "fi-rr-exclamation-extralarge.svg",
                icon_deactive = "fi-rr-exclamation-extralarge-deactive.svg",
                btn_id = "電気炉警報",
                tooltip_text = "電気炉警報",
                width = 60,
                height = 60,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        self._parent.ui.load_pages.Layout_Status_Error.addWidget(self._parent.error_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.ethernetConnecton_icon = PyIconButton_simple(
                icon = "ethernet.svg",
                icon_active = "ethernet.svg",
                icon_hover = "ethernet.svg",
                icon_deactive = "ethernet-deactive.svg",
                btn_id = "電気炉接続",
                tooltip_text = "電気炉接続",
                width = 45,
                height = 45,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        self._parent.ui.load_pages.Layout_Status_EthernetConnecton.addWidget(self._parent.ethernetConnecton_icon, Qt.AlignCenter, Qt.AlignCenter)

        
        self._parent.usbConnecton_icon = PyIconButton_simple(
                icon = "usb-symbol-svgrepo-com.svg",
                icon_active = "usb-symbol-svgrepo-com.svg",
                icon_hover = "usb-symbol-svgrepo-com.svg",
                icon_deactive = "usb-symbol-svgrepo-com-deactive.svg",
                btn_id = "USB インターフェース",
                tooltip_text = "USB インターフェース",
                width = 45,
                height = 45,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        self._parent.ui.load_pages.Layout_Status_USBConnecton.addWidget(self._parent.usbConnecton_icon, Qt.AlignCenter, Qt.AlignCenter)



        self._parent.gPIBConnecton_2657A_icon = PyIconButton_simple(
                icon = "link-2657A.svg",
                icon_active = "link-2657A.svg",
                icon_hover = "link-2657A.svg",
                icon_deactive = "link-2657A-deactive.svg",
                btn_id = "2657A接続",
                tooltip_text = "2657A接続",
                width = 45,
                height = 45,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        self._parent.ui.load_pages.Layout_Status_2657A_GPIBConnecton.addWidget(self._parent.gPIBConnecton_2657A_icon, Qt.AlignCenter, Qt.AlignCenter)

        self._parent.gPIBConnecton_2635B_icon = PyIconButton_simple(
                icon = "link-2635B.svg",
                icon_active = "link-2635B.svg",
                icon_hover = "link-2635B.svg",
                icon_deactive = "link-2635B-deactive.svg",
                btn_id = "2635B接続",
                tooltip_text = "2635B接続",
                width = 45,
                height = 45,
                bg_color =  "#1e2229",
                bg_color_hover =  "#1e2229",
                bg_color_pressed =  "#1e2229",
            )
        self._parent.ui.load_pages.Layout_Status_2635B_GPIBConnecton.addWidget(self._parent.gPIBConnecton_2635B_icon, Qt.AlignCenter, Qt.AlignCenter)

    def graph_update(self):
        self.data_array=[]

        if self.graph_Item=="Resistor":
            #for data in self._parent.MMG.memoryPool["Read Measurement Data"]:
            #    XYdata={}
            #    XYdata["x"]=data.time/self.timeUnit
            #    XYdata["y"]=data.resistor
            #    self.data_array.append(XYdata)
            self._parent.curve.setData(self.data_array)
        else:
            self.choose_pattern=self._parent.MMG.memoryPool["System memory"]["choose_Pattern"].getValue()
            if choose_pattern:
                pattern_availible_number=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_実行STEP数".format(choose_pattern)].getValue()
            
                self.data_array.append({"x":0,"y":0})
                for step in (1,pattern_availible_number+1):
                    XYdata={}
                    XYdata["x"]=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_ステップ累計時間".format(choose_pattern,step)].getValue()
                    XYdata["y"]=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_SV値".format(choose_pattern,step)].getValue()
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
        self._parent.curve.setData(self.data_array)
        self._parent.ui.load_pages.realtime_grapgLayout.addWidget(self._parent.realTimeData_Graph, Qt.AlignCenter, Qt.AlignCenter)

    def realtime_data_Update_Work(self):
        #print("realtime_data_Update_Work")
        while 1:
            time.sleep(0.1)

            

            if self.realTime_Temp!=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["温度PV値"].getValue():
                self.realTime_Temp=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["温度PV値"].getValue()
                self._parent.ui.load_pages.realtime_Temp_lineEdit.setText("{}".format(Quantity(self.realTime_Temp,"℃").render(prec=4)))

            elif self.realTime_Voltage!=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["現在電圧値"].getValue():
                self.realTime_Voltage=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["現在電圧値"].getValue()
                self._parent.ui.load_pages.realtime_Voltage_lineEdit.setText("{}".format(Quantity(self.realTime_Voltage,"V").render(prec=4)))

            elif self.realTime_Current!=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["現在電流値"].getValue():
                self.realTime_Current=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["現在電流値"].getValue()
                self._parent.ui.load_pages.realtime_Current_lineEdit.setText("{}".format(Quantity(self.realTime_Current,"A").render(prec=4)))

            elif self.realTime_Resistor!=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["現在抵抗値"].getValue():
                self.realTime_Resistor=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["現在抵抗値"].getValue()
                self._parent.ui.load_pages.realtime_Resistor_lineEdit.setText("{}".format(Quantity(self.realTime_Resistor,"Ω").render(prec=4)))


            #if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定開始"].getValue():
            #    print("測定開始　信号到達")

    def ultility_Update_Work(self):
        self.AutoMode_pattern_comboBox_contantList=[]

        while 1:

            time.sleep(0.1)

            #self.time=0
            #XYdata={}
            #XYdata["x"]=self.time/self.timeUnit
            #XYdata["y"]=random.random()*1000
            #self.data_array.append(XYdata)
            #self._parent.curve.setData(self.data_array)
            #self.time+=1
            if self.AutoMode_pattern_comboBox_contantList !=self._parent.tempPattern.patternFile_nameList:
                self.AutoMode_pattern_comboBox_contantList=self._parent.tempPattern.patternFile_nameList
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndexChanged.disconnect()
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.clear()
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.addItems(self.AutoMode_pattern_comboBox_contantList)
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.setCurrentIndex(self.choose_pattern)
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndexChanged.connect(self.btn_callback)
        
            self.ethernetConnecton_icon_active=self._parent.MMG.memoryPool["System memory"]["Ethernet conneciton"].getValue()
            self.usbConnecton_icon_active=self._parent.MMG.memoryPool["System memory"]["GPIB USB conneciton"].getValue()
            self.gPIBConnecton_2635B_icon_active=self._parent.MMG.memoryPool["System memory"]["2635B connection"].getValue()
            self.gPIBConnecton_2657A_icon_active=self._parent.MMG.memoryPool["System memory"]["2657A connection"].getValue()



            if self._parent.MMG.memoryPool["System memory"]["Ethernet conneciton"].getValue():

                if self.ready_icon_active!=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転可"].getValue():
                    self.ready_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転可"].getValue()

                    self._parent.ui.load_pages.autostart_pushButton.setEnabled(self.ready_icon_active)
                    self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(self.ready_icon_active)


                self.stop_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["停止中"].getValue()
                self.vacuum_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["真空置換中"].getValue()
                self.heating_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["昇温中"].getValue()
                self.keepTemp_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["温度ｷｰﾌﾟ中"].getValue()
                self.testing_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定中"].getValue()
                self.testFinishing_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転終了"].getValue()
                self.error_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PLC警報"].getValue()

                if not self._parent.ui.load_pages.remoteConnect_pushButton.isEnabled():
                    self._parent.ui.load_pages.remoteConnect_pushButton.setEnabled(True)



            else:
                self.ready_icon_active=0
                self.stop_icon_active=0
                self.vacuum_icon_active=0
                self.heating_icon_active=0
                self.keepTemp_icon_active=0
                self.testing_icon_active=0
                self.testFinishing_icon_active=0
                self.error_icon_active=0

                
                
                if self._parent.ui.load_pages.remoteConnect_pushButton.isEnabled():
                    self._parent.ui.load_pages.remoteConnect_pushButton.setEnabled(False)
                if self._parent.ui.load_pages.remoteConnect_pushButton.isChecked():
                    self._parent.ui.load_pages.remoteConnect_pushButton.setChecked(False)
                
                #if self._parent.ui.load_pages.eMSstop_pushButton.isEnabled():
                #    self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(False)
                #if self._parent.ui.load_pages.eMSstop_pushButton.isChecked():
                #    self._parent.ui.load_pages.eMSstop_pushButton.setChecked(False)
                
                #if self._parent.ui.load_pages.autostart_pushButton.isEnabled():
                #    self._parent.ui.load_pages.autostart_pushButton.setEnabled(False)
                #if self._parent.ui.load_pages.autostart_pushButton.isChecked():
                #    self._parent.ui.load_pages.autostart_pushButton.setChecked(False)
                
                #if self._parent.ui.load_pages.gasFreeflow_pushButton.isEnabled():
                #    self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(False)
                #if self._parent.ui.load_pages.gasFreeflow_pushButton.isChecked():
                #    self._parent.ui.load_pages.gasFreeflow_pushButton.setChecked(False)


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


 

