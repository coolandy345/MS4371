import threading
import time
from gui_main.qt_core import *
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *
import random
from modbus_TcpServer import MeasurePackage
from registor_manager import *
from quantiphy import Quantity
import numpy as np


class Memory_Manager():
    def __init__( 
            self, 
            PoolSemaphore=None,
            Master_memoryPool={},
            queuePool={}
    ):
        self.PoolSemaphore=PoolSemaphore

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
            
            # #Wait for 0.01s for any others request
            time.sleep(0.01)
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
            self.PoolSemaphore.acquire(timeout=1)
            for pool_name in poolNameList:

                for item in import_pool[pool_name]:
                    value=self.Master_memoryPool[item.pool_name][item.registor_name].getValue()
                    self.memoryPool[item.pool_name][item.registor_name].setValue(value)
                    print("GUI update",item.pool_name,item.registor_name,value)
            self.PoolSemaphore.release()
                
    def main_MemoryUpLoad_Work(self):
        """
        UpLoad the local GUI memoryPool to Master_memoryPool
        When request is got , this thread will delay 0.1s for any other request and do it  at one time
        """

        while 1:
            #Wait for any Master memoryPool update request
            getItem_list=[]
            getItem_list.append(self.queuePool["memory_UploadToMaster_Queue"].get())
            #Wait for 0.01s for any others request
            time.sleep(0.01)
            # Collected al  item in this 0.1s
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
                
                self.PoolSemaphore.acquire(timeout=1)
                self.Master_memoryPool[pool_name]=self.memoryPool[pool_name]
                self.PoolSemaphore.release()

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
        self.autoRunFinishing_icon_active=False
        self.error_icon_active=False
        self.ethernetConnecton_icon_active=False
        self.usbConnecton_icon_active=False
        self.gPIBConnecton_2657A_icon_active=False
        self.gPIBConnecton_2635B_icon_active=False

        self.choose_pattern=0

        self.graph_Item="Measure_Data"

        self.timeUnit=1
        self.timeLabel="s"
        self.timeMaxRange=10
        self.timeMinRange=1
        self.divider=1

        self.PV_Record_Start=False
        self.collect_PV_Data_array_start=False

        self.graph_Update_request=False

        self.utility_setup()

        self.realTime_Temp=0
        self.realTime_Pressure=0
        self.realTime_Voltage=0
        self.realTime_Current=0
        self.realTime_Resistor=0

        self.low_pressure=0

        self.temp_data_array=[]
        self.voltage_data_array=[]
        self.current_data_array=[]
        self.resistance_data_array=[]
        self.temp_sv_data_array=[]
        self.temp_pv_data_array=[]

        self.measurement_start=False


        self.set_setting_Transfer_request=False
        self.set_setting_Transfer_enable=False
        self.set_setting_Transfer_value=0


        self.timer=QTimer()
        self.timer.timeout.connect(self.graph_Update_Work)
        self.timer.start(30)

        ultility_Update_Thread = threading.Thread(target = self.ultility_Update_Work,daemon=True)
        ultility_Update_Thread.start()

        realtime_data_Update_Thread = threading.Thread(target = self.realtime_data_Update_Work,daemon=True)
        realtime_data_Update_Thread.start()

        setting_transfer_Thread = threading.Thread(target = self.setting_transfer_Work,daemon=True)
        setting_transfer_Thread.start()
        

    def autoRun_logic(self):

        self.ethernetConnecton_icon_active
        
        #self.autostart_signal=True
        #self.remoteConnect_signal=True
        #self.stop_signal=True
        #self.gasFreeflow_signal=True

        #self.ready_icon_active
        #self.stop_icon_active
        #self.vacuum_icon_active
        #self.heating_icon_active
        #self.keepTemp_icon_active
        #self.testing_icon_active
        #self.autoRunFinishing_icon_active
        #self.error_icon_active


        #If we got ethernet access
        if self.ethernetConnecton_icon_active:
            if not self._parent.ui.load_pages.remoteConnect_pushButton.isEnabled():
                self._parent.ui.load_pages.remoteConnect_pushButton.setEnabled(True)

        else:
            if self._parent.ui.load_pages.remoteConnect_pushButton.isEnabled():
                self._parent.ui.load_pages.remoteConnect_pushButton.setEnabled(False)
                self.set_memorypool_register("Modbus Registor Pool - Registor","リモート",0)
            if self._parent.ui.load_pages.remoteConnect_pushButton.isChecked():
                self._parent.ui.load_pages.remoteConnect_pushButton.setChecked(False)

        #if PLC is allow us to start
        if (self._parent.ui.load_pages.remoteConnect_pushButton.isChecked() and self.ready_icon_active):

            self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(False)

            #Stop collect PV temperature data
            if self.PV_Record_Start:
                    self.PV_Record_Start=False

            #Enable conent editable
            self._parent.testfile_manager.set_content_Editeable(True)

            #Enbale AutoRun
            self._parent.ui.load_pages.autostart_pushButton.setText("運転開始")
            if not self._parent.ui.load_pages.autostart_pushButton.isEnabled():
                self._parent.ui.load_pages.autostart_pushButton.setEnabled(True)
            if self._parent.ui.load_pages.autostart_pushButton.isChecked():
                self._parent.ui.load_pages.autostart_pushButton.setChecked(False)

            #Enbale FreeGas flow
            if not self._parent.ui.load_pages.gasFreeflow_pushButton.isEnabled():
                self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(True)

            #Enbale pattern be choose
            # if not self._parent.ui.load_pages.AutoMode_pattern_comboBox.isEnabled():
            #     self._parent.ui.load_pages.AutoMode_pattern_comboBox.setEnabled(True)

            #Disbale EMS stop
            if self._parent.ui.load_pages.autostart_pushButton.isEnabled():
                self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(False)
            if self._parent.ui.load_pages.eMSstop_pushButton.isChecked():
                self._parent.ui.load_pages.eMSstop_pushButton.setChecked(False)

        #if PLC is not allow us to start
        else:

            #if PLC is at Running state
            if (self.vacuum_icon_active or
                self.heating_icon_active or
                self.keepTemp_icon_active or
                self.testing_icon_active or
                self.autoRunFinishing_icon_active):

                self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(False)

                #Disable conent editable
                self._parent.testfile_manager.set_content_Editeable(False)

                #Start collecting PV temperature
                if not self.PV_Record_Start:
                    self.PV_Record_Start=True
                    collect_PV_Data_array_Thread = threading.Thread(target = self.collect_PV_Data_array,daemon=True)
                    collect_PV_Data_array_Thread.start()


                #Enbale EMS stop
                if not self._parent.ui.load_pages.autostart_pushButton.isEnabled():
                    self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(True)
                if self._parent.ui.load_pages.eMSstop_pushButton.isChecked():
                    self._parent.ui.load_pages.eMSstop_pushButton.setChecked(True)
                    
            #if PLC is not at Running state also PLC is not allow to start
            else:
                
                if self.realTime_Pressure<self.low_pressure:
                    self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(True)
                else:
                    self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(False)

                    

                if self.PV_Record_Start:
                    self.PV_Record_Start=False



                #Disbale EMS stop
                if self._parent.ui.load_pages.autostart_pushButton.isEnabled():
                    self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(False)
                if self._parent.ui.load_pages.eMSstop_pushButton.isChecked():
                    self._parent.ui.load_pages.eMSstop_pushButton.setChecked(False)

            #Disbale AutoRun
            if self._parent.ui.load_pages.autostart_pushButton.isEnabled():
                self._parent.ui.load_pages.autostart_pushButton.setEnabled(False)
            if self._parent.ui.load_pages.autostart_pushButton.isChecked():
                self._parent.ui.load_pages.autostart_pushButton.setChecked(True)

            #Disbale FreeGas flow
            #if self._parent.ui.load_pages.gasFreeflow_pushButton.isEnabled():
            #    self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(False)
            #if self._parent.ui.load_pages.gasFreeflow_pushButton.isChecked():
            #    self._parent.ui.load_pages.gasFreeflow_pushButton.setChecked(False)

            #Disbale pattern be choose
            # if self._parent.ui.load_pages.AutoMode_pattern_comboBox.isEnabled():
            #     self._parent.ui.load_pages.AutoMode_pattern_comboBox.setEnabled(False)

    def collect_PV_Data_array(self):
        print("collect_PV_Data_array")
        self.pattern_PV_data_array=[]
        if not self.collect_PV_Data_array_start:
            self.collect_PV_Data_array_start=True
            while self.PV_Record_Start:

                XYdata={}
                step=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["実行STEP No."].getValue()
                pattern=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["実行PTN No."].getValue()
                if (step>1 and pattern!=0):
                    base_time=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_ステップ累計時間".format(pattern,step-1)].getValue()/60
                    print("base_time",base_time)
                else:
                    base_time=0
                print("pattern",pattern,"step",step,"base_time",base_time)
                XYdata["x"]=base_time+(self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["STEP実行経過時間（L)"].getValue()/60)
                XYdata["y"]=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["温度PV値"].getValue()
                print("collect_PV_Data_array",XYdata)
                self.pattern_PV_data_array.append(XYdata)
                self.graph_Update_request=True

                time.sleep(60)
            
            
            self.collect_PV_Data_array_start=False
        else:
            print("Fault by collect_PV_Data_array")





    def wait_transferFinish_Work(self):
        self.eventPool["Setting_upload_toPLC_Finish"].wait()
        self.eventPool["Setting_upload_toPLC_Finish"].clear()

        self.set_setting_Transfer_enable=True
        self.set_setting_Transfer_value=100
        self.set_setting_Transfer_request=True

        self.transfer_finish=True


    def setting_transfer_Work(self):
        while 1:
            self.eventPool["Setting_upload_toPLC_Start"].wait()
            self.eventPool["Setting_upload_toPLC_Start"].clear()

            self.transfer_finish=False

            wait_transferFinish_Thread = threading.Thread(target = self.wait_transferFinish_Work,daemon=True)
            wait_transferFinish_Thread.start()
            
            self.set_setting_Transfer_enable=True
            self.set_setting_Transfer_value=0
            self.set_setting_Transfer_request=True

            start_time=time.time()

            while not self.transfer_finish:

                try:
                    getitem=self.queuePool["Setting_upload_toPLC_Queue"].get(timeout=0.05)
                    if getitem:
                        self.set_setting_Transfer_enable=True
                        self.set_setting_Transfer_value=getitem
                        self.set_setting_Transfer_request=True
                except :
                    pass

                if time.time()-start_time>10:
                    self.transfer_finish=True
                
            

            time.sleep(1.5)

            self.set_setting_Transfer_enable=False
            self.set_setting_Transfer_value=0
            self.set_setting_Transfer_request=True
            
    def set_memorypool_register(self,pool_name,registor_name,value):
        
        if self._parent.MMG.memoryPool[pool_name][registor_name].getValue()!=value:
            self._parent.MMG.memoryPool[pool_name][registor_name].setValue(value)
            sendItem=MemoryUnit(pool_name,registor_name)
            self.queuePool["memory_UploadToMaster_Queue"].put(sendItem)

    def maxmin(self,max,min,data):
        if data>=max:
            return max,True
        elif data<=min:
            return min,True
        else:
            return data,False

    def btn_callback(self):

        btn_name=self.sender().objectName()

        print(btn_name)

        if btn_name == "btn_AutoMode":
            self._parent.ui.load_pages.stackedWidget.setCurrentWidget(self._parent.ui.load_pages.page_AutoOperate)

        if btn_name == "Resistor_checkBox":
            self.graph_Update_request=True
            
        if btn_name == "Voltage_checkBox":
            self.graph_Update_request=True
        
        if btn_name == "Current_checkBox":
            self.graph_Update_request=True


        elif btn_name == "Noisetest_pushButton":
            self._parent.ui.load_pages.Noisetest_pushButton.blockSignals(True)
            self._parent.ui.load_pages.Noisetest_pushButton.setChecked(True)

            self.eventPool["Noise Measure Start"].set()
            self.dataRecord_Start=True
            data_receive_Thread = threading.Thread(target = self.data_receive_Work,daemon=True)
            data_receive_Thread.start()

        elif btn_name == "manaualMode_comboBox":
            index=self._parent.ui.load_pages.manaualMode_comboBox.currentIndex()
            self._parent.ui.load_pages.stackedWidget_2.setCurrentIndex(index)

        elif btn_name == "noiseMeasurement_Voltage_lineEdit":
            data=float(self._parent.ui.load_pages.noiseMeasurement_Voltage_lineEdit.text())
            data,err=self.maxmin(1000,0,data)
            if err:
                self._parent.ui.load_pages.noiseMeasurement_Voltage_lineEdit.setText(str(data))

            self.set_memorypool_register("System memory","Noise_Measurement_Voltage",data)
            self.noise_Measurement_Voltage=data

        elif btn_name == "noiseMeasurement_Time_lineEdit":
            data=float(self._parent.ui.load_pages.noiseMeasurement_Time_lineEdit.text())
            data,err=self.maxmin(60,0.1,data)
            if err:
                self._parent.ui.load_pages.noiseMeasurement_Time_lineEdit.setText(str(data))

            self.set_memorypool_register("System memory","Noise_Measurement_Time",data)
            self.noise_Measurement_Time=data


        elif btn_name == "noiseMeasurement_Current_lineEdit":
            data=float(self._parent.ui.load_pages.noiseMeasurement_Current_lineEdit.text())
            data,err=self.maxmin(1000,0,data)
            if err:
                self._parent.ui.load_pages.noiseMeasurement_Current_lineEdit.setText(str(data))

            self.set_memorypool_register("System memory","Noise_Measurement_Current",data)
            self.noise_Measurement_Current=data



        #elif btn_name == "test_pushButton_3":
        #    self.eventPool["Measure Stop"].set()

        elif btn_name == "btn_ManaualMode":
            self._parent.ui.load_pages.stackedWidget.setCurrentWidget(self._parent.ui.load_pages.page_ManaulOperate)
        elif btn_name == "autostart_pushButton":
            self.autostart_signal=True
            self.measurement_start=False

            self._parent.ui.load_pages.autostart_pushButton.setEnabled(False)
            self._parent.ui.load_pages.autostart_pushButton.setChecked(1)
            self._parent.ui.load_pages.autostart_pushButton.setText("運転中")

            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.",int(self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndex()+1))
            self.choose_pattern
            
            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",1)
            #self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",0)
            # self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",0)

            # self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",1)

            self.dataRecord_Start=True
            data_receive_Thread = threading.Thread(target = self.data_receive_Work,daemon=True)
            data_receive_Thread.start()

            #Check all condition to start sequence
                # Lock parameter setting
                # Prepare folder to recorda
                # Tell PLC to start pattern


        elif btn_name == "remoteConnect_pushButton":
            
            self.remoteConnect_signal=True
            set=self._parent.ui.load_pages.remoteConnect_pushButton.isChecked()
            self.set_memorypool_register("Modbus Registor Pool - Registor","リモート",int(set))
            #self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
            # self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)
            #self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",1)
            #self.set_memorypool_register("Modbus Registor Pool - Registor","PC警報",int(set))


            pass

        elif btn_name == "manualMeasurement_pushButton":
            self._parent.ui.load_pages.manualMeasurement_pushButton.blockSignals(True)
            self._parent.ui.load_pages.manualMeasurement_pushButton.setChecked(True)

            #self.eventPool["Test Event2"].set()
             # Read valtage and current from gpib device


            pass
        elif btn_name == "voltageOutput_pushButton":
            self._parent.ui.load_pages.voltageOutput_pushButton.blockSignals(True)
            self._parent.ui.load_pages.voltageOutput_pushButton.setChecked(True)

            #self.eventPool["Test Event1"].set()
            self.dataRecord_Start=True
            data_receive_Thread = threading.Thread(target = self.data_receive_Work,daemon=True)
            data_receive_Thread.start()

        elif btn_name == "gasFreeflow_pushButton":
            self.gasFreeflow_signal=True
            # Set Gas registor to memory bus
            self.set_memorypool_register("Modbus Registor Pool - Registor","大気圧",1)
            #self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
            
        elif btn_name == "outputStop_pushButton":
        
            self.eventPool["Measure Stop"].set()



        elif btn_name == "eMSstop_pushButton":
            self.stop_signal=True
            self.eventPool["Measure Stop"].set()

            self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",1)

          


        elif btn_name == "measurement_comboBox":
            manual_mode=self._parent.ui.load_pages.measurement_comboBox.currentText()
            self.set_memorypool_register("System memory","Manual_Measurement_Mode",manual_mode)

        elif btn_name == "voltage_lineEdit":
            # Set output voltage limit
            self.set_memorypool_register("System memory","Manual_Measurement_Voltage",float(self._parent.ui.load_pages.voltage_lineEdit.text()))

            data=float(self._parent.ui.load_pages.voltage_lineEdit.text())
            data,err=self.maxmin(2000,-2000,data)
            if err:
                self._parent.ui.load_pages.voltage_lineEdit.setText(str(data))

            self.set_memorypool_register("System memory","Manual_Measurement_Voltage",data)

        elif btn_name == "AutoMode_pattern_comboBox":

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["リモート"].getValue():
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.setEnabled(False)

            self._parent.ui.load_pages.autostart_pushButton.setEnabled(True)
            self._parent.ui.load_pages.autostart_pushButton.setChecked(0)

            self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(False)
            self._parent.ui.load_pages.eMSstop_pushButton.setChecked(0)

            #choose pattern
            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.",int(self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndex()+1))
            self.choose_pattern
            # self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",1)

            if self.graph_Item=="Pattern":
                self.graph_Update_request=True


        elif btn_name == "graphItem_combobox":

            index=self._parent.ui.load_pages.graphItem_combobox.currentText()
            if index=="測定数値":
                self.graph_Item="Measure_Data"
                self._parent.ui.load_pages.timeUnit_Label.setVisible (True)
                self._parent.ui.load_pages.timeUnit_comboBox.setVisible (True)
                self._parent.ui.load_pages.frame_19.setVisible (True)
                
                self.graph_Update_request=True

            elif index=="運転パターン":
                self.graph_Item="Pattern"
                self._parent.ui.load_pages.timeUnit_Label.setVisible (False)
                self._parent.ui.load_pages.timeUnit_comboBox.setVisible (False)
                self._parent.ui.load_pages.frame_19.setVisible (False)
                
                self.graph_Update_request=True

                
                
            
            # self.graph_update()
                
            
        elif btn_name == "timeUnit_comboBox":
            self.starttime=time.time()

            index=self._parent.ui.load_pages.timeUnit_comboBox.currentText()
            if index=="1s/div":
                self.timeUnit=1
                self.timeLabel="s"
                self.timeMaxRange=10
                self.divider=1
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
            elif index=="10s/div":
                self.timeUnit=1
                self.timeLabel="s"
                self.timeMaxRange=100
                self.divider=1
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
            elif index=="30s/div":
                self.timeUnit=1
                self.timeLabel="s"
                self.timeMaxRange=300
                self.divider=3
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
            elif index=="1min/div":
                self.timeUnit=60
                self.timeLabel="min"
                self.timeMaxRange=10
                self.divider=6
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)

            elif index=="10min/div":
                self.timeUnit=60
                self.timeLabel="min"
                self.timeMaxRange=100
                self.divider=60
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
            elif index=="1h/div":
                self.timeUnit=3600
                self.timeLabel="hour"
                self.timeMaxRange=3
                self.divider=360
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)
    



            self.check_buttom_axix()

    def data_receive_Work(self):
        print("data_receive_Work")

        self.voltage_data_array=[]
        self.current_data_array=[]
        self.resistance_data_array=[]
        self.temp_sv_data_array=[]
        self.temp_pv_data_array=[]

        self.starttime=time.time()
        self.timeUnit=1
        #while self.dataRecord_Start:
        while True:
            try:
                getItem=self.queuePool["GUI_DataQueue"].get()

                #print("GUI_DataQueue",getItem)
                #self.realTime_Voltage=getItem[-1].voltage
                #self.realTime_Current=getItem[-1].current
                #self.realTime_Resistor=getItem[-1].resistance
                
                for data in getItem:
                    self.realTime_Voltage1=data.voltage
                    self.realTime_Current1=data.current
                    self.realTime_Resistor1=data.resistance
                    print("GUI_DataQueue",data.time,data.voltage,data.current,)
                    XYdata={}
                    XYdata["x"]=float(data.time)
                    XYdata["y"]=float(data.current)
                    self.current_data_array.append(XYdata)

                    XYdata={}
                    XYdata["x"]=float(data.time)
                    XYdata["y"]=float(data.voltage)
                    self.voltage_data_array.append(XYdata)

                    XYdata={}
                    XYdata["x"]=float(data.time)
                    XYdata["y"]=float(data.resistance)
                    self.resistance_data_array.append(XYdata)

                self.graph_Update_request=True



            except:
                pass


    def utility_setup(self):

        self.graph_setup()
        

        self._parent.ui.load_pages.btn_AutoMode.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.btn_ManaualMode.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.manualMeasurement_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.voltageOutput_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.outputStop_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.Noisetest_pushButton.clicked.connect(self.btn_callback)

        self._parent.ui.load_pages.noiseMeasurement_Voltage_lineEdit.setValidator(QDoubleValidator())
        data=self._parent.MMG.memoryPool["System memory"]["Noise_Measurement_Voltage"].getValue()
        self._parent.ui.load_pages.noiseMeasurement_Voltage_lineEdit.setText("{}".format(data))
        self._parent.ui.load_pages.noiseMeasurement_Voltage_lineEdit.editingFinished.connect(self.btn_callback)
        self._parent.ui.load_pages.noiseMeasurement_Time_lineEdit.setValidator(QDoubleValidator())
        data=self._parent.MMG.memoryPool["System memory"]["Noise_Measurement_Time"].getValue()
        self._parent.ui.load_pages.noiseMeasurement_Time_lineEdit.setText("{}".format(data))
        self._parent.ui.load_pages.noiseMeasurement_Time_lineEdit.editingFinished.connect(self.btn_callback)
        self._parent.ui.load_pages.noiseMeasurement_Current_lineEdit.setValidator(QDoubleValidator())
        data=self._parent.MMG.memoryPool["System memory"]["Noise_Measurement_Current"].getValue()
        self._parent.ui.load_pages.noiseMeasurement_Current_lineEdit.setText("{}".format(data))
        self._parent.ui.load_pages.noiseMeasurement_Current_lineEdit.editingFinished.connect(self.btn_callback)

        self._parent.ui.load_pages.Resistor_checkBox.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.Voltage_checkBox.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.Current_checkBox.clicked.connect(self.btn_callback)
        
        self._parent.ui.load_pages.manaualMode_comboBox.currentIndexChanged.connect(self.btn_callback)
        index=self._parent.ui.load_pages.manaualMode_comboBox.currentIndex()
        self._parent.ui.load_pages.stackedWidget_2.setCurrentIndex(index)
        
        self._parent.ui.load_pages.remoteConnect_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.gasFreeflow_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.autostart_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.eMSstop_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.voltage_lineEdit.editingFinished.connect(self.btn_callback)
        self._parent.ui.load_pages.voltage_lineEdit.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.measurement_comboBox.currentIndexChanged.connect(self.btn_callback)
        self._parent.ui.load_pages.graphItem_combobox.currentIndexChanged.connect(self.btn_callback)
        self._parent.ui.load_pages.timeUnit_comboBox.currentIndexChanged.connect(self.btn_callback)
        
        self._parent.ui.load_pages.AutoMode_pattern_comboBox.clear()
        emptylist=[""]
        self._parent.ui.load_pages.AutoMode_pattern_comboBox.addItems(emptylist)
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

        self._parent.autoRunFinishing_icon = PyIconButton_simple(
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
        self._parent.ui.load_pages.Layout_Status_TestFinishing.addWidget(self._parent.autoRunFinishing_icon, Qt.AlignCenter, Qt.AlignCenter)

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
    
    def graph_Update_Work(self):
        if self.graph_Update_request:
            self.graph_Update_request=False
            self.graph_update()

        if self.set_setting_Transfer_request:
            self.set_setting_Transfer_request=False
            self._parent.ui.title_bar.set_setting_Transfer(enable=self.set_setting_Transfer_enable,value=self.set_setting_Transfer_value)

    def check_buttom_axix(self):

        if self.realTime_Resistance_Graph_set:
            self.realTime_Resistance_Graph.setLabel(axis='bottom', text='時間', units=self.timeLabel)
            self.realTime_Voltage_Graph.showLabel("bottom", show=False)
            self.realTime_Current_Graph.showLabel("bottom", show=False)

            self.realTime_Voltage_Graph.setXLink(self.realTime_Voltage_Graph)
            self.realTime_Current_Graph.setXLink(self.realTime_Voltage_Graph)
            self.realTime_Resistance_Graph.setXLink(self.realTime_Voltage_Graph)
        else:
            if self.realTime_Current_Graph_set:
                self.realTime_Current_Graph.setLabel(axis='bottom', text='時間', units=self.timeLabel)
                self.realTime_Voltage_Graph.showLabel("bottom", show=False)
                self.realTime_Resistance_Graph.showLabel("bottom", show=False)

                self.realTime_Voltage_Graph.setXLink(self.realTime_Current_Graph)
                self.realTime_Current_Graph.setXLink(self.realTime_Current_Graph)
                self.realTime_Resistance_Graph.setXLink(self.realTime_Current_Graph)

            else:
                if self.realTime_Voltage_Graph_set:
                    self.realTime_Voltage_Graph.setLabel(axis='bottom', text='時間', units=self.timeLabel)
                    self.realTime_Current_Graph.showLabel("bottom", show=False)
                    self.realTime_Resistance_Graph.showLabel("bottom", show=False)

                    self.realTime_Voltage_Graph.setXLink(self.realTime_Voltage_Graph)
                    self.realTime_Current_Graph.setXLink(self.realTime_Voltage_Graph)
                    self.realTime_Resistance_Graph.setXLink(self.realTime_Voltage_Graph)

                else:
                    
                    self.realTime_Voltage_Graph.showLabel("bottom", show=False)
                    self.realTime_Current_Graph.showLabel("bottom", show=False)
                    self.realTime_Resistance_Graph.showLabel("bottom", show=False)
    def graph_size_adjust(self):

        sum=0
        if self.realTime_Voltage_Graph_set:
            sum+=1
        if self.realTime_Current_Graph_set:
            sum+=1
        if self.realTime_Resistance_Graph_set:
            sum+=1

        if sum==2 and self.realTime_Current_Graph_set and self.realTime_Resistance_Graph_set:
            pass
        elif sum==2 and self.realTime_Voltage_Graph_set and self.realTime_Resistance_Graph_set:
            pass
        elif sum==2 and self.realTime_Current_Graph_set and self.realTime_Voltage_Graph_set:
            self.realTime_Current_Graph
                    

    def graph_update(self):

        if self.graph_Item=="Measure_Data":

            if self.realTime_Temperature_Graph_set:
                self.realTime_Temperature_Graph_set=False
                self.win.removeItem(self.realTime_Temperature_Graph)
                self.realTime_Temperature_Graph.showLabel("bottom", show=False)


            #self.realTime_Voltage_Graph.setVisible (self._parent.ui.load_pages.Resistor_checkBox.isChecked())
            #self.realTime_Current_Graph.setVisible (self._parent.ui.load_pages.Voltage_checkBox.isChecked())
            #self.realTime_Resistance_Graph.setVisible (self._parent.ui.load_pages.Current_checkBox.isChecked())

            #self._parent.ui.load_pages.frame_75.setVisible (self._parent.ui.load_pages.Resistor_checkBox.isChecked())
            #self._parent.ui.load_pages.frame_76.setVisible (self._parent.ui.load_pages.Voltage_checkBox.isChecked())
            #self._parent.ui.load_pages.frame_2.setVisible (self._parent.ui.load_pages.Current_checkBox.isChecked())

            
            if self._parent.ui.load_pages.Voltage_checkBox.isChecked():
                if not self.realTime_Voltage_Graph_set:
                    self.realTime_Voltage_Graph_set=True
                    self.win.addItem(self.realTime_Voltage_Graph,row=0,col=0)
                    self.check_buttom_axix()
            else:
                if self.realTime_Voltage_Graph_set:
                    self.realTime_Voltage_Graph_set=False
                    self.win.removeItem(self.realTime_Voltage_Graph)
                    self.check_buttom_axix()

            if self._parent.ui.load_pages.Current_checkBox.isChecked():
                if not self.realTime_Current_Graph_set:
                    self.realTime_Current_Graph_set=True
                    self.win.addItem(self.realTime_Current_Graph,row=1,col=0)
                    self.check_buttom_axix()
            else:
                if self.realTime_Current_Graph_set:
                    self.realTime_Current_Graph_set=False
                    self.win.removeItem(self.realTime_Current_Graph)
                    self.check_buttom_axix()

            if self._parent.ui.load_pages.Resistor_checkBox.isChecked():
                if not self.realTime_Resistance_Graph_set:
                    self.realTime_Resistance_Graph_set=True
                    self.win.addItem(self.realTime_Resistance_Graph,row=2,col=0)
                    self.check_buttom_axix()
            else:
                if self.realTime_Resistance_Graph_set:
                    self.realTime_Resistance_Graph_set=False
                    self.win.removeItem(self.realTime_Resistance_Graph)
                    self.check_buttom_axix()
                
            #self._parent.voltage_curve.setData(self.voltage_data_array[0::self.divider])
            #self._parent.current_curve.setData(self.current_data_array[0::self.divider])
            #self._parent.resistance_curve.setData(self.resistance_data_array[0::self.divider])

            self._parent.voltage_curve.setData(self.voltage_data_array)
            self._parent.current_curve.setData(self.current_data_array)
            self._parent.resistance_curve.setData(self.resistance_data_array)

            if self.voltage_data_array:
                self.realTime_Voltage_Graph.setXRange(min=self.voltage_data_array[-1]["x"]-self.timeMaxRange, max=self.voltage_data_array[-1]["x"])

            if self.current_data_array:
                self.realTime_Current_Graph.setXRange(min=self.current_data_array[-1]["x"]-self.timeMaxRange, max=self.current_data_array[-1]["x"])

            if self.resistance_data_array:
                self.realTime_Resistance_Graph.setXRange(min=self.resistance_data_array[-1]["x"]-self.timeMaxRange, max=self.resistance_data_array[-1]["x"])




        elif self.graph_Item=="Pattern":
            

            if self.realTime_Voltage_Graph_set:
                self.realTime_Voltage_Graph_set=False
                self.win.removeItem(self.realTime_Voltage_Graph)

            if self.realTime_Current_Graph_set:
                self.realTime_Current_Graph_set=False
                self.win.removeItem(self.realTime_Current_Graph)

            if self.realTime_Resistance_Graph_set:
                self.realTime_Resistance_Graph_set=False
                self.win.removeItem(self.realTime_Resistance_Graph)

            if not self.realTime_Temperature_Graph_set:
                    self.realTime_Temperature_Graph_set=True
                    self.win.addItem(self.realTime_Temperature_Graph,row=0,col=0)

                    self.timeLabel="hour"

                    self.realTime_Temperature_Graph.setLabel(axis='bottom', text='時間', units=self.timeLabel)

            self.pattern_SV_data_array=[]



            self.choose_pattern=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["実行PTN No."].getValue()


            if self.choose_pattern:
                pattern_availible_number=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_実行STEP数".format(self.choose_pattern)].getValue()
            
                self.pattern_SV_data_array.append({"x":0,"y":0})
                for step in range(1,pattern_availible_number+2):
                    XYdata={}
                    XYdata["x"]=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_ステップ累計時間".format(self.choose_pattern,step)].getValue()/60
                    XYdata["y"]=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_SV値".format(self.choose_pattern,step)].getValue()
                    self.pattern_SV_data_array.append(XYdata)
            #not choose_pattern yet 
            else:
                self.pattern_SV_data_array=[]

            self._parent.temp_sv_curve.setData(self.pattern_SV_data_array)
            self._parent.temp_pv_curve.setData(self.pattern_PV_data_array)
            

            # self.realTime_Temperature_Graph_set.setLabel(axis='bottom', text='時間', units="hr")
            # self.realTime_Temperature_Graph_set.setLabel(axis='left', text='温度', units='℃')
            #self.realTimeData_Graph.setLimits(minXRange=0,maxXRange=self.timeMaxRange)




    def graph_setup(self):

        pg.setConfigOptions(background=None)
        self.win = pg.GraphicsLayoutWidget(show=True,parent=self._parent)

        self.row_count=0
        #autoDownsample=True,downsampleMethod="subsample",
        self.realTime_Voltage_Graph = self.win.addPlot(row=1, col=0,clipToView=True)
        self.realTime_Voltage_Graph.setLabel(axis='left', text='電圧', units='V')
        self.realTime_Voltage_Graph.setMouseEnabled(x=True, y=True)
        self.realTime_Voltage_Graph.showGrid(x=True, y=True)
        self.realTime_Current_Graph = self.win.addPlot(row=2, col=0,clipToView=True)
        self.realTime_Current_Graph.setLabel(axis='left', text='電流', units='A')
        self.realTime_Current_Graph.setMouseEnabled(x=True, y=True)
        self.realTime_Current_Graph.showGrid(x=True, y=True)
        self.realTime_Resistance_Graph = self.win.addPlot(row=3, col=0,clipToView=True)
        self.realTime_Resistance_Graph.setLabel(axis='left', text='抵抗', units='Ω')
        self.realTime_Resistance_Graph.setMouseEnabled(x=True, y=True)
        self.realTime_Resistance_Graph.showGrid(x=True, y=True)
        self.realTime_Temperature_Graph = self.win.addPlot(row=4, col=0,clipToView=True)
        self.realTime_Temperature_Graph.setLabel(axis='left', text='温度', units='℃')
        self.realTime_Temperature_Graph.setMouseEnabled(x=True, y=True)
        self.realTime_Temperature_Graph.showGrid(x=True, y=True)

        self.realTime_Voltage_Graph.setLimits(minXRange=self.timeMaxRange,maxXRange=self.timeMaxRange)
        self.realTime_Current_Graph.setLimits(minXRange=self.timeMaxRange,maxXRange=self.timeMaxRange)
        self.realTime_Resistance_Graph.setLimits(minXRange=self.timeMaxRange,maxXRange=self.timeMaxRange)
        #self.realTime_Temperature_Graph.setLimits(minXRange=self.timeMaxRange,maxXRange=self.timeMaxRange)

        
        self._parent.voltage_curve=self.realTime_Voltage_Graph.plot(pen=pg.mkColor(200, 133, 0),
                                                        symbolPen='w',
                                                        symbolBrush=(0,0,0),
                                                        symbolSize=1,
                                                        name="電圧",
                                                        )

        

        self._parent.current_curve=self.realTime_Current_Graph.plot(pen=pg.mkColor(132, 220, 244),
                                                        symbolPen='w',
                                                        symbolBrush=(0,0,0),
                                                        symbolSize=1,
                                                        name="電流",
                                                        )
        

        self._parent.resistance_curve=self.realTime_Resistance_Graph.plot(pen=pg.mkColor(131, 255, 145),
                                                        symbolPen='w',
                                                        symbolBrush=(0,0,0),
                                                        symbolSize=1,
                                                        name="抵抗値",
                                                        )

        self.realTime_Temperature_Graph.addLegend()
        self.pattern_SV_data_array=[]
        self._parent.temp_sv_curve=self.realTime_Temperature_Graph.plot(pen=pg.mkColor(132, 220, 244),
                                                        symbolPen='w',
                                                        symbolBrush=(0,0,0),
                                                        symbolSize=1,
                                                        name="温度SV値",
                                                        )

        self.pattern_PV_data_array=[]
        self._parent.temp_pv_curve=self.realTime_Temperature_Graph.plot(pen=pg.mkColor(200, 133, 0),
                                                        symbolPen='w',
                                                        symbolBrush=(0,0,0),
                                                        symbolSize=1,
                                                        name="温度PV値",
                                                        )

        
        self._parent.ui.load_pages.realtime_grapgLayout.addWidget(self.win, Qt.AlignCenter, Qt.AlignCenter)
        self.realTime_Voltage_Graph_set=False
        self.win.removeItem(self.realTime_Voltage_Graph)
        self.realTime_Current_Graph_set=False
        self.win.removeItem(self.realTime_Current_Graph)
        self.realTime_Resistance_Graph_set=False
        self.win.removeItem(self.realTime_Resistance_Graph)
        self.realTime_Temperature_Graph_set=False
        self.win.removeItem(self.realTime_Temperature_Graph)

        self.graph_Update_request=False

    def two_into_decimal(self,value):

        if value>=32768:
            return (-1)*(65535 + 1 - value)
        else:
            return value

    def realtime_data_Update_Work(self):
        #print("realtime_data_Update_Work")
        while 1:
            time.sleep(0.1)

            

            #self.set_memorypool_register("Modbus Registor Pool - Registor","現在電流値",getItem[-1].current)
            self._parent.ui.load_pages.realtime_Current_lineEdit.setText("{}".format(Quantity(self.realTime_Current,"A").render(prec=4)))
            self._parent.ui.load_pages.realtime_Voltage_lineEdit.setText("{}".format(Quantity(self.realTime_Voltage,"V").render(prec=4)))
            self._parent.ui.load_pages.realtime_Resistor_lineEdit.setText("{}".format(Quantity(self.realTime_Resistor,"Ω").render(prec=4)))
            #self.set_memorypool_register("Modbus Registor Pool - Registor","現在電圧値",self.realTime_Voltage)
            #self.set_memorypool_register("Modbus Registor Pool - Registor","現在電流値",self.realTime_Current)
            #self.set_memorypool_register("Modbus Registor Pool - Registor","現在抵抗値",self.realTime_Resistor)


            if self.realTime_Temp!=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["温度PV値"].getValue():
                self.realTime_Temp=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["温度PV値"].getValue()
                self._parent.ui.load_pages.realtime_Temp_lineEdit.setText("{}".format(Quantity(self.realTime_Temp,"℃").render(prec=4)))

            if self.realTime_Pressure!=self.two_into_decimal(self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["マッフル内圧力"].getValue()):
                data=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["マッフル内圧力"].getValue()
                self.realTime_Pressure=self.two_into_decimal(data)
                self._parent.ui.load_pages.realtime_Pressure_lineEdit.setText("{:.1f} kPa".format(self.realTime_Pressure/10))

            if self.low_pressure!=self.two_into_decimal(self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["減圧"].getValue()):
                data=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["減圧"].getValue()
                self.low_pressure=self.two_into_decimal(data)
            

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定開始"].getValue():
                #self.set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
                if not self.measurement_start:
                    print("測定開始 信号到達",self.measurement_start)
                    self.measurement_start=True
                    measurement_finish_wait_Thread = threading.Thread(target = self.measurement_finish_wait_Work,daemon=True)
                    measurement_finish_wait_Thread.start()

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転開始RST"].getValue():
                # self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",1)
                self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)
                #self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始RST",0)

                
                # time.sleep(0.5)

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定終了RST"].getValue():
                
                # self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
                self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",0)
                #self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了RST",0)
                self.measurement_start=False
                # time.sleep(0.5)

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["実行PTN No.変更RST"].getValue():
                
                # self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",1)
                self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",0)
                
                
                time.sleep(0.5)
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.setEnabled(True)

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["大気圧RST"].getValue():
                # self.set_memorypool_register("Modbus Registor Pool - Registor","大気圧",1)
                self.set_memorypool_register("Modbus Registor Pool - Registor","大気圧",0)
                # time.sleep(0.5)

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転停止RST"].getValue():
                # self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",1)
                self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",0)
                # time.sleep(0.5)
                #self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止RST",0)



    def measurement_finish_wait_Work(self):
        print("測定開始")
        self.eventPool["Auto Run Start"].set()

        self.eventPool["Auto Run finish"].wait()
        self.eventPool["Auto Run finish"].clear()
        self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
        print("測定終了")

    def ultility_Update_Work(self):
        self.AutoMode_pattern_comboBox_contantList=[]

        while 1:
            time.sleep(0.1)

            if self._parent.MMG.memoryPool["System memory"]["Noise_Measurement_status"].getValue():
                self._parent.ui.load_pages.Noisetest_pushButton.blockSignals(True)
                self._parent.ui.load_pages.Noisetest_pushButton.setChecked(True)
            else:
                self._parent.ui.load_pages.Noisetest_pushButton.setChecked(False)
                self._parent.ui.load_pages.Noisetest_pushButton.blockSignals(False)

            if self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_status"].getValue():
                self._parent.ui.load_pages.voltageOutput_pushButton.blockSignals(True)
                self._parent.ui.load_pages.voltageOutput_pushButton.setChecked(True)
            else:
                self._parent.ui.load_pages.voltageOutput_pushButton.setChecked(False)
                self._parent.ui.load_pages.voltageOutput_pushButton.blockSignals(False)

            if self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_trigger"].getValue():
                self._parent.ui.load_pages.manualMeasurement_pushButton.blockSignals(True)
                self._parent.ui.load_pages.manualMeasurement_pushButton.setChecked(True)
            else:
                self._parent.ui.load_pages.manualMeasurement_pushButton.setChecked(False)
                self._parent.ui.load_pages.manualMeasurement_pushButton.blockSignals(False)

            if self.AutoMode_pattern_comboBox_contantList !=self._parent.tempPattern.patternFile_nameList:
                self.AutoMode_pattern_comboBox_contantList=self._parent.tempPattern.patternFile_nameList
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.blockSignals(True)
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.clear()
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.addItems(self.AutoMode_pattern_comboBox_contantList)
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.setCurrentIndex(self.choose_pattern)
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.blockSignals(False)


            if not self._parent.tempPattern.patternFiles==[] and self.AutoMode_pattern_comboBox_contantList:

                if self._parent.tempPattern.patternFiles[self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndex()+1]:
                    gas_mode=self._parent.tempPattern.patternFiles[self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndex()+1].gas_condition
                else:
                    gas_mode==-1

                if gas_mode==-1:
                    gas_mode="未選択"
                elif gas_mode==0:
                    gas_mode="大気"
                elif gas_mode==1:
                    gas_mode="真空"
                elif gas_mode==2:
                    gas_mode="N2置換"
            else:
                gas_mode=""

            self._parent.ui.load_pages.Gas_mode_Label.setText("雰囲気モード:{}".format(gas_mode))
        
            self.ethernetConnecton_icon_active=self._parent.MMG.memoryPool["System memory"]["Ethernet conneciton"].getValue()
            self.usbConnecton_icon_active=self._parent.MMG.memoryPool["System memory"]["GPIB USB conneciton"].getValue()
            self.gPIBConnecton_2635B_icon_active=self._parent.MMG.memoryPool["System memory"]["2635B connection"].getValue()
            self.gPIBConnecton_2657A_icon_active=self._parent.MMG.memoryPool["System memory"]["2657A connection"].getValue()

            

            if self._parent.MMG.memoryPool["System memory"]["Ethernet conneciton"].getValue():
                
                self.ready_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転可"].getValue()
                self.stop_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["停止中"].getValue()
                self.vacuum_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["真空置換中"].getValue()
                self.heating_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["昇温中"].getValue()
                self.keepTemp_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["温度ｷｰﾌﾟ中"].getValue()
                self.testing_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定中"].getValue()
                self.autoRunFinishing_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転終了"].getValue()
                self.error_icon_active=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PLC警報"].getValue()


            else:
                self.ready_icon_active=0
                self.stop_icon_active=0
                self.vacuum_icon_active=0
                self.heating_icon_active=0
                self.keepTemp_icon_active=0
                self.testing_icon_active=0
                self.autoRunFinishing_icon_active=0
                self.error_icon_active=0


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
            if self.autoRunFinishing_icon_active != self._parent.autoRunFinishing_icon._is_active:
                self._parent.autoRunFinishing_icon.set_active(self.autoRunFinishing_icon_active)
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


            
            self.autoRun_logic()

