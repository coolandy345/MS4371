import threading
import time
from gui_main.qt_core import *
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *
from registor_manager import *
from quantiphy import Quantity

from pyqtgraph import setConfigOptions as pg_setConfigOptions
from pyqtgraph import GraphicsLayoutWidget as pg_GraphicsLayoutWidget
from pyqtgraph import InfiniteLine as pg_InfiniteLine
from pyqtgraph import SignalProxy as pg_SignalProxy
from pyqtgraph import mkColor as pg_mkColor

import random
import subprocess
import numpy
import math

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
            self.PoolSemaphore.acquire()
            
            # #Wait for 0.01s for any others request
            # time.sleep(0.1)
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
            
            time.sleep(0.01)

            # Collected all  item in this 0.1s
            if not self.queuePool["memory_UploadToMaster_Queue"].empty():
                #Wait for 0.01s for any others request
                time.sleep(0.1)
                
                self.PoolSemaphore.acquire()
                while not self.queuePool["memory_UploadToMaster_Queue"].empty():
                    getItem_list.append(self.queuePool["memory_UploadToMaster_Queue"].get())
            else:
                
                self.PoolSemaphore.acquire()
            
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

            self.PoolSemaphore.release()

            #Send database update request
            for item in getItem_list:
                sendItem=MemoryUnit(item.pool_name,item.registor_name)
                self.queuePool["database_Uplaod_Queue"].put(sendItem)
            
            


            
        
class Main_utility_manager(QWidget):
    def __init__( 
            self, 
            parent = None,
            PoolSemaphore=None,
            queuePool={},
            eventPool={}
    ):
        super().__init__()

        self._parent=parent
        self.PoolSemaphore=PoolSemaphore
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

        self.graph_Item="Pattern"
        
        self.AutoMode_pattern_comboBox_contantList=[]
        self.Manual_Measurement_pattern_comboBox_contantList=[]

        self.timeUnit=1
        self.current_time_unit=1
        self.timeLabel="s"
        self.timeMaxRange=10
        self.timeMinRange=1
        self.divider=1

        self.PV_Record_Start=False
        self.collect_PV_Data_array_start=False

        self.graph_Update_request=False

        self.dataRecord_Start=False
        
        self.utility_setup()

        self.realTime_Temp=0
        self.realTime_Pressure=0
        self.realTime_Voltage=0
        self.realTime_Current=0
        self.realTime_Resistor=0

        self.low_pressure=0

        self.data_semaphore=threading.Semaphore()
        self.temp_data_array=[]
        self.data_array_depth=0

        self.temp_graph_data_array=[]
        # self.voltage_graph_data_array=[]
        # self.current_graph_data_array=[]
        # self.resistance_graph_data_array=[]

        self.voltage_data_array     =numpy.zeros(shape=(100000000, 2),dtype='f')
        self.current_data_array     =numpy.zeros(shape=(100000000, 2),dtype='f')
        self.resistance_data_array  =numpy.zeros(shape=(100000000, 2),dtype='f')
        self.temp_sv_data_array     =numpy.zeros(shape=(100000000, 2),dtype='f')
        self.temp_pv_data_array     =numpy.zeros(shape=(100000000, 2),dtype='f')

        


        self.measurement_start=False


        self.set_setting_Transfer_request=False
        self.set_setting_Transfer_enable=False
        self.set_setting_Transfer_value=0


        self.graph_Update_timer=QTimer()
        self.graph_Update_timer.timeout.connect(self.graph_Update_Work)
        self.graph_Update_timer.start(30)

        self.ultility_Update_timer=QTimer()
        self.ultility_Update_timer.timeout.connect(self.ultility_Update_Work)
        self.ultility_Update_timer.start(10)


        realtime_data_Update_Thread = threading.Thread(target = self.realtime_data_Update_Work,daemon=True)
        realtime_data_Update_Thread.start()

        setting_transfer_Thread = threading.Thread(target = self.setting_transfer_Work,daemon=True)
        setting_transfer_Thread.start()

        self.startup_check_dialog()
        
        self.set_memorypool_register("Modbus Registor Pool - Registor","測定可",0)
        self.set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
        self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
        self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",1)
        self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)

    def startup_check_dialog(self):
        subprocess2 = subprocess.Popen("ipconfig", shell=True, stdout=subprocess.PIPE)
        subprocess_return = subprocess2.stdout.read()
        get_string=subprocess_return.decode("Shift JIS")
        get_ethernet_interface=get_string.find("イーサネット アダプター イーサネット")
        if get_ethernet_interface==-1:
            self.lunchOptionDialog("イーサネット・インターフェースは未検出です。パソコンを再起動してください。",PyDialog.error_type)
            self.close_app()
            return
        
        get_correct_IP_address=get_string.find("IPv4 アドレス . . . . . . . . . . . .: 192.168.0.40")

        if get_correct_IP_address==-1:
            self.lunchOptionDialog("イーサネットIPアドレスは不正確です。192.168.0.40 に設定してください。",PyDialog.error_type)
            os.system('netsh interface ip set address "イーサネット" static 192.168.0.40 255.255.255.0 192.168.0.1')
            self.close_app()
            return

        if not self._parent.MMG.memoryPool["System memory"]["GPIB USB conneciton"].getValue():
            self.lunchOptionDialog("GPIB-USBインターフェースは未検出です、接続状況をご確認ください。",PyDialog.error_type)
            self.close_app()
            return

        if not self._parent.MMG.memoryPool["System memory"]["2657A connection"].getValue():
            self.lunchOptionDialog("Keithey 2657A & 2635B は通信異常です。GPIB-USBインターフェースを挿し直し、接続状況をご確認ください。",PyDialog.error_type)
            self.close_app()
            return
        



        

    def close_app(self):
        self.timer2=QTimer()
        self.timer2.timeout.connect(self.close_app_work)
        self.timer2.start(100)
        
    def close_app_work(self):
        print("close_app from GUI")
        self._parent.close()


    def lunchOptionDialog(self,message,type):

        '''
        PyDialog.error_type
        PyDialog.warning_2_type
        PyDialog.warning_3_type
        '''

        diag = PyDialog(type,message)
        return(str(diag.exec()))

    def lunchMessageDialog(self,title,message):
        diag = PyMessageDialog(title,message)
        return(str(diag.exec()))

    def autoRun_logic(self):
        
        #If we got ethernet access
        if self.ethernetConnecton_icon_active:
            
            self._parent.ui.load_pages.remoteConnect_pushButton.setEnabled(True)

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
                self._parent.ui.load_pages.Noise_Measurement_Start_pushButton.setEnabled(True)
            else:
                self._parent.ui.load_pages.Noise_Measurement_Start_pushButton.setEnabled(False)
                

        else:
            self._parent.ui.load_pages.Noise_Measurement_Start_pushButton.setEnabled(True)


            if self._parent.ui.load_pages.remoteConnect_pushButton.isEnabled() or self._parent.ui.load_pages.remoteConnect_pushButton.isChecked():
                self._parent.ui.load_pages.remoteConnect_pushButton.blockSignals(True)
                self._parent.ui.load_pages.remoteConnect_pushButton.setEnabled(False)
                self._parent.ui.load_pages.remoteConnect_pushButton.setChecked(False)
                self._parent.ui.load_pages.remoteConnect_pushButton.blockSignals(False)
                self.set_memorypool_register("Modbus Registor Pool - Registor","リモート",0)

        # if not self.usbConnecton_icon_active or not self.gPIBConnecton_2657A_icon_active:
        #     if not self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PC警報"].getValue():
        #         self.set_memorypool_register("Modbus Registor Pool - Registor","PC警報",1)

        #if PLC is allow us to start
        if (self.ready_icon_active and self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["リモート"].getValue()):

            #Disbale FreeGas flow
            if self._parent.ui.load_pages.gasFreeflow_pushButton.isEnabled():
                self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(False)
                self._parent.ui.load_pages.gasFreeflow_pushButton.setChecked(False)

            #Enable manual mode check pushbutton
            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
                self._parent.ui.load_pages.btn_ManaualMode.setEnabled(True)
                self._parent.ui.load_pages.btn_ManaualMode.setVisible(True)

            #Stop collect PV temperature data
            if self.PV_Record_Start:
                    self.PV_Record_Start=False

            #Enable conent editable
            self._parent.testfile_manager.set_content_Editeable(True)

            #Enbale AutoRun
            self._parent.ui.load_pages.autostart_pushButton.setText("運転開始")

            if not self._parent.ui.load_pages.autostart_pushButton.isEnabled():
                
                if self._parent.ui.load_pages.AutoMode_pattern_comboBox.isEnabled():
                    self._parent.ui.load_pages.autostart_pushButton.blockSignals(False)
                    self._parent.ui.load_pages.autostart_pushButton.setEnabled(True)

            #Enbale pattern be choose
            # if not self._parent.ui.load_pages.AutoMode_pattern_comboBox.isEnabled():
            #     self._parent.ui.load_pages.AutoMode_pattern_comboBox.setEnabled(True)

            #Disbale EMS stop
            if self._parent.ui.load_pages.eMSstop_pushButton.isEnabled():
                self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(False)

        #if PLC is not allow us to start
        else:

            #if PLC is at Running state
            if (self.vacuum_icon_active or
                self.heating_icon_active or
                self.keepTemp_icon_active or
                self.testing_icon_active or
                self.autoRunFinishing_icon_active):

                self._parent.ui.load_pages.autostart_pushButton.setText("運転中")

                #Disbale FreeGas flow
                if self._parent.ui.load_pages.gasFreeflow_pushButton.isEnabled():
                    self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(False)
                    self._parent.ui.load_pages.gasFreeflow_pushButton.setChecked(False)

                #Disable conent editable
                self._parent.testfile_manager.set_content_Editeable(False)

                #Disable manual mode check pushbutton
                self._parent.ui.load_pages.btn_ManaualMode.setEnabled(False)
                self._parent.ui.load_pages.btn_ManaualMode.setVisible(False)

                #Start collecting PV temperature
                if not self.PV_Record_Start:
                    self.PV_Record_Start=True
                    collect_PV_Data_array_Thread = threading.Thread(target = self.collect_PV_Data_array,daemon=True)
                    collect_PV_Data_array_Thread.start()


                #Enbale EMS stop
                if not self._parent.ui.load_pages.eMSstop_pushButton.isEnabled():
                    self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(True)

                    
            #if PLC is not at Running state also PLC is not allow to start
            else:

                self._parent.ui.load_pages.autostart_pushButton.setText("準備中")

                #Enable manual mode check pushbutton
                if not self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
                    self._parent.ui.load_pages.btn_ManaualMode.setEnabled(True)
                    self._parent.ui.load_pages.btn_ManaualMode.setVisible(True)

                if self.realTime_Pressure<self.low_pressure:
                    #Disbale FreeGas flow
                    if not self._parent.ui.load_pages.gasFreeflow_pushButton.isEnabled():
                        self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(True)
                        self._parent.ui.load_pages.gasFreeflow_pushButton.setChecked(False)
                else:
                    #Disbale FreeGas flow
                    if self._parent.ui.load_pages.gasFreeflow_pushButton.isEnabled():
                        self._parent.ui.load_pages.gasFreeflow_pushButton.setEnabled(False)
                        self._parent.ui.load_pages.gasFreeflow_pushButton.setChecked(False)

                if self.PV_Record_Start:
                    self.PV_Record_Start=False

                #Disbale EMS stop
                if self._parent.ui.load_pages.eMSstop_pushButton.isEnabled():
                    self._parent.ui.load_pages.eMSstop_pushButton.setEnabled(False)

            #Disbale AutoRun
            if self._parent.ui.load_pages.autostart_pushButton.isEnabled():
                self._parent.ui.load_pages.autostart_pushButton.blockSignals(True)
                self._parent.ui.load_pages.autostart_pushButton.setEnabled(False)


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
        self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",1)

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

        self.PoolSemaphore.acquire()
        
        # if self._parent.MMG.memoryPool[pool_name][registor_name].getValue()!=value:
        self._parent.MMG.memoryPool[pool_name][registor_name].setValue(value)
        sendItem=MemoryUnit(pool_name,registor_name)
        self.queuePool["memory_UploadToMaster_Queue"].put(sendItem)

        self.PoolSemaphore.release()

    def maxmin(self,max,min,data):
        if data>=max:
            return max,True
        elif data<=min:
            return min,True
        else:
            return data,False

    def btn_callback(self):

        btn_name=self.sender().objectName()

        # print(btn_name)v

        if btn_name == "btn_AutoMode":
            self._parent.ui.load_pages.stackedWidget.setCurrentWidget(self._parent.ui.load_pages.page_AutoOperate)

        if btn_name == "Resistor_checkBox":
            self.graph_Update_request=True
            self.check_buttom_axix()
            
        if btn_name == "Voltage_checkBox":
            self.graph_Update_request=True
            self.check_buttom_axix()
        
        if btn_name == "Current_checkBox":
            self.graph_Update_request=True
            self.check_buttom_axix()


        elif btn_name == "Noise_Measurement_Start_pushButton":
            self._parent.ui.load_pages.Noise_Measurement_Start_pushButton.blockSignals(True)
            self._parent.ui.load_pages.btn_AutoMode.setEnabled(False)
            self._parent.ui.load_pages.btn_AutoMode.setVisible(False)

            data_receive_Thread = threading.Thread(target = self.noise_measurement_finish_wait_Work,daemon=True)
            data_receive_Thread.start()

        elif btn_name == "Measurement_Mode_comboBox":
            index=self._parent.ui.load_pages.Measurement_Mode_comboBox.currentIndex()
            self._parent.ui.load_pages.stackedWidget_2.setCurrentIndex(index)

        elif btn_name == "Noise_Measurement_Voltage_lineEdit":
            data=float(self._parent.ui.load_pages.Noise_Measurement_Voltage_lineEdit.text())
            data,err=self.maxmin(1000,0,data)
            if err:
                self._parent.ui.load_pages.Noise_Measurement_Voltage_lineEdit.setText(str(data))

            self.set_memorypool_register("System memory","Noise_Measurement_Voltage",data)
            self.noise_Measurement_Voltage=data

        elif btn_name == "Noise_Measurement_Time_lineEdit":
            data=float(self._parent.ui.load_pages.Noise_Measurement_Time_lineEdit.text())
            data,err=self.maxmin(60,0.1,data)
            if err:
                self._parent.ui.load_pages.Noise_Measurement_Time_lineEdit.setText(str(data))

            self.set_memorypool_register("System memory","Noise_Measurement_Time",data)
            self.noise_Measurement_Time=data


        elif btn_name == "Noise_Measurement_Current_lineEdit":
            data=float(self._parent.ui.load_pages.Noise_Measurement_Current_lineEdit.text())
            data,err=self.maxmin(1000,0,data)
            if err:
                self._parent.ui.load_pages.Noise_Measurement_Current_lineEdit.setText(str(data))

            self.set_memorypool_register("System memory","Noise_Measurement_Current",data)
            self.noise_Measurement_Current=data

        elif btn_name == "Measurement_Stop_pushButton":
            self._parent.ui.load_pages.Measurement_Stop_pushButton.blockSignals(True)
            
            self.set_memorypool_register("System memory","測定異常コード",3)
            self.eventPool["Measure Stop"].set()
            # self._parent.ui.load_pages.btn_AutoMode.setEnabled(True)
            # self._parent.ui.load_pages.btn_AutoMode.setVisible(True)

        elif btn_name == "btn_ManaualMode":
            self._parent.ui.load_pages.stackedWidget.setCurrentWidget(self._parent.ui.load_pages.page_ManaulOperate)

        elif btn_name == "autostart_pushButton":
            self._parent.ui.load_pages.autostart_pushButton.blockSignals(True)
            # self._parent.ui.load_pages.autostart_pushButton.setEnabled(False)

            self.measurement_start=False
            self.eventPool["Measure Stop"].clear()



            self.set_memorypool_register("Modbus Registor Pool - Registor","実行STEP No.",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.",int(self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndex()+1))
            
            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",1)
            time.sleep(0.2)
            
            self.set_memorypool_register("System memory","Auto_Measurement_status",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",1)

            time.sleep(0.01)

            self.measurement_PenddingWait_Thread = threading.Thread(target = self.measurement_PenddingWait_Work,daemon=True)
            self.measurement_PenddingWait_Thread.start()

            

            #Check all condition to start sequence
                # Lock parameter setting
                # Prepare folder to recorda
                # Tell PLC to start pattern


        elif btn_name == "remoteConnect_pushButton":
            self.remoteConnect_signal=True
            set=self._parent.ui.load_pages.remoteConnect_pushButton.isChecked()
            self.set_memorypool_register("Modbus Registor Pool - Registor","リモート",int(set))
            self.measurement_start=False
            self.set_memorypool_register("System memory","測定異常コード",3)
            self.eventPool["Measure Stop"].set()
            self.dataRecord_Start=False
            
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)


        

        elif btn_name == "gasFreeflow_pushButton":
            # Set Gas registor to memory bus
            self.set_memorypool_register("Modbus Registor Pool - Registor","大気圧",1)

        elif btn_name == "eMSstop_pushButton":
            # self._parent.ui.load_pages.eMSstop_pushButton.blockSignals(True)
            self.set_memorypool_register("System memory","測定異常コード",3)
            self.eventPool["Measure Stop"].set()
            self.dataRecord_Start=False
            
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
            self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",1)
            self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)


        elif btn_name == "Manual_Measurement_SingleMode_comboBox":
            manual_mode=self._parent.ui.load_pages.Manual_Measurement_SingleMode_comboBox.currentText()
            self.set_memorypool_register("System memory","Manual_Measurement_Single_Mode",manual_mode)

        elif btn_name == "Manual_Measurement_PatternMode_comboBox":
            manual_PaPattern_No=self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.currentIndex()
            self.set_memorypool_register("System memory","Manual_Measurement_Pattern_Number",manual_PaPattern_No)

        elif btn_name == "Manual_Measurement_SingleMode_pushButton":
            self.set_memorypool_register("System memory","Manual_Measurement_Mode","Single")
            self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setText("電圧印加")
            # self._parent.ui.load_pages.Manual_Measurement_SingleVoltage_lineEdit.setVisible(True)

        elif btn_name == "Manual_Measurement_PatternMode_pushButton":
            self.set_memorypool_register("System memory","Manual_Measurement_Mode","Pattern")
            self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setText("パターン測定")
            # self._parent.ui.load_pages.Manual_Measurement_SingleVoltage_lineEdit.setVisible(False)

        elif btn_name == "Manual_Measurement_Trigger_pushButton":
            self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.blockSignals(True)
            self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setChecked(True)

            self.set_memorypool_register("System memory","Manual_Measurement_trigger",1)

            #self.eventPool["Test Event2"].set()
             # Read valtage and current from gpib device

        elif btn_name == "Manual_Measurement_Start_pushButton":
            self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.blockSignals(True)
            self._parent.ui.load_pages.btn_AutoMode.setEnabled(False)
            self._parent.ui.load_pages.btn_AutoMode.setVisible(False)

            data_receive_Thread = threading.Thread(target = self.manual_measurement_finish_wait_Work,daemon=True)
            data_receive_Thread.start()

            

        elif btn_name == "Manual_Measurement_SingleVoltage_lineEdit":
            # Set output voltage limit
            # self.set_memorypool_register("System memory","Manual_Measurement_Voltage",float(self._parent.ui.load_pages.Manual_Measurement_SingleVoltage_lineEdit.text()))

            data=float(self._parent.ui.load_pages.Manual_Measurement_SingleVoltage_lineEdit.text())
            data,err=self.maxmin(2000,-2000,data)
            if err:
                self._parent.ui.load_pages.Manual_Measurement_SingleVoltage_lineEdit.setText(str(data))

            self.set_memorypool_register("System memory","Manual_Measurement_Voltage",data)

        elif btn_name == "AutoMode_pattern_comboBox":

            #choose pattern
            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.",int(self._parent.ui.load_pages.AutoMode_pattern_comboBox.currentIndex()+1))
            self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",1)

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["リモート"].getValue():
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.setCursor(QCursor(Qt.BusyCursor))
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.setEnabled(False)
                self._parent.ui.load_pages.autostart_pushButton.setEnabled(False)

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
            # self.starttime=time.time()
            time_unitChange=False

            index=self._parent.ui.load_pages.timeUnit_comboBox.currentText()

            if index=="1s/div":

                if not self.timeUnit==1:
                    time_unitChange=True

                self.timeUnit=1
                self.timeLabel="s"
                self.timeMaxRange=10
                self.divider=1
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
            elif index=="10s/div":

                if not self.timeUnit==1:
                    time_unitChange=True

                self.timeUnit=1
                self.timeLabel="s"
                self.timeMaxRange=100
                self.divider=1
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
            elif index=="30s/div":
                
                if not self.timeUnit==1:
                    time_unitChange=True

                self.timeUnit=1
                self.timeLabel="s"
                self.timeMaxRange=300
                self.divider=3
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
            elif index=="1min/div":
                
                if not self.timeUnit==60:
                    time_unitChange=True
                    
                self.timeUnit=60
                self.timeLabel="min"
                self.timeMaxRange=10
                self.divider=6
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)

            elif index=="10min/div":
                
                if not self.timeUnit==60:
                    time_unitChange=True
                    
                self.timeUnit=60
                self.timeLabel="min"
                self.timeMaxRange=100
                self.divider=60
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)

            elif index=="30min/div":
                
                if not self.timeUnit==60:
                    time_unitChange=True
                    
                self.timeUnit=60
                self.timeLabel="min"
                self.timeMaxRange=300
                self.divider=180
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)


            elif index=="1h/div":
                
                if not self.timeUnit==3600:
                    time_unitChange=True
                    
                self.timeUnit=3600
                self.timeLabel="hour"
                self.timeMaxRange=10
                self.divider=360
                
                self.realTime_Voltage_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Current_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
                self.realTime_Resistance_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
    
            if time_unitChange:
                self.graph_timeUnitData_adjust()

            self.graph_Update_request=True

            self.check_buttom_axix()

            

    def data_receive_Work(self):

        self._parent.ui.load_pages.timeUnit_comboBox.setCurrentIndex(0)

        self.data_array_depth=0

        pressure_testnumber=10000

        start_time=0

        # self.data_semaphore.acquire()

        # self.current_time_unit=self.timeUnit

        # time_array=numpy.linspace(0,3600*24/self.timeUnit,num=pressure_testnumber).reshape(pressure_testnumber,1)
                                    
        # ran_array1=numpy.random.rand(pressure_testnumber,1).reshape(pressure_testnumber,1)
        # ran_array2=numpy.random.rand(pressure_testnumber,1).reshape(pressure_testnumber,1)
        # ran_array3=numpy.random.rand(pressure_testnumber,1).reshape(pressure_testnumber,1)

        # self.voltage_data_array[0:pressure_testnumber,0:1]=time_array
        # self.voltage_data_array[0:pressure_testnumber,1:2]=ran_array1
        # self.current_data_array[0:pressure_testnumber,0:1]=time_array
        # self.current_data_array[0:pressure_testnumber,1:2]=ran_array2
        # self.resistance_data_array[0:pressure_testnumber,0:1]=time_array
        # self.resistance_data_array[0:pressure_testnumber,1:2]=ran_array3

        # self.data_array_depth=pressure_testnumber

        # start_time=float(time_array[-1])
        # print(start_time)
        
        # self.data_semaphore.release()

        # self.timeUnit=1
        while self.dataRecord_Start:
            try:
                getItem=self.queuePool["GUI_DataQueue"].get(timeout=0.1)


                # print("GUI_DataQueue",getItem)
                self.realTime_Voltage=getItem[-1].voltage
                self.realTime_Current=getItem[-1].current
                self.realTime_Resistor=getItem[-1].resistance

                # print("12",self.realTime_Voltage,self.realTime_Current,self.realTime_Resistor)
                
                for data in getItem:
                    # print("GUI_DataQueue",data.time,data.voltage,data.current,)
                    

                    self.data_semaphore.acquire()
                    data_time=(data.time+start_time)/self.timeUnit
                    self.current_data_array[self.data_array_depth]=numpy.array([data_time,data.current])
                    self.voltage_data_array[self.data_array_depth]=numpy.array([data_time,data.voltage])
                    self.resistance_data_array[self.data_array_depth]=numpy.array([data_time,data.resistance])
                    self.data_semaphore.release()

                    self.data_array_depth+=1


                
                self.graph_Update_request=True



            except:
                pass

        print("data_receive_Work is finish")


    def measurement_PenddingWait_Work(self):
        last_step=-1

        while self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転開始"].getValue():

            current_step=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["実行STEP No."].getValue()

            if not last_step==current_step:

                last_step=current_step
                current_pattern=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["実行PTN No."].getValue()
                if current_step==0:
                    hasMeasurement=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_RT計測".format(current_pattern,current_step)].getValue()
                    self.holding_time=10
                else:
                    hasMeasurement=self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_測定有".format(current_pattern,current_step)].getValue()
                    self.holding_time=10+self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PTNData_{}_STEP_{}_キープ時間".format(current_pattern,current_step)].getValue()*60

                if hasMeasurement:

                    self.eventPool["Auto Measure Request"].clear()
                    time.sleep(0.01)

                    self.measurement_startTimer_Thread = threading.Thread(target = self.measurement_startTimer_Work,daemon=True)
                    self.measurement_startTimer_Thread.start()

                    self.eventPool["Auto Measure Request"].wait()
                    self.eventPool["Auto Measure Request"].clear()

                    if not self.measurement_start:
                        print("測定開始 信号到達",self.measurement_start)
                        self.measurement_start=True
                        measurement_finish_wait_Thread = threading.Thread(target = self.measurement_finish_wait_Work,daemon=True)
                        measurement_finish_wait_Thread.start()
                

            time.sleep(0.1)

    def measurement_startTimer_Work(self):

        self.set_memorypool_register("System memory","測定異常コード",0)
        time.sleep(self.holding_time)


        if not self.measurement_start:
            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
                self.set_memorypool_register("System memory","測定異常コード",2)
            else:
                self.set_memorypool_register("System memory","測定異常コード",4)

            self.eventPool["Auto Measure Request"].set()


    def utility_setup(self):

        self.graph_setup()

        self._parent.ui.load_pages.btn_AutoMode.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.btn_ManaualMode.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.Measurement_Stop_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.Noise_Measurement_Start_pushButton.clicked.connect(self.btn_callback)

        self._parent.ui.load_pages.Noise_Measurement_Voltage_lineEdit.setValidator(QDoubleValidator())
        data=self._parent.MMG.memoryPool["System memory"]["Noise_Measurement_Voltage"].getValue()
        self._parent.ui.load_pages.Noise_Measurement_Voltage_lineEdit.setText("{}".format(data))
        self._parent.ui.load_pages.Noise_Measurement_Voltage_lineEdit.editingFinished.connect(self.btn_callback)
        self._parent.ui.load_pages.Noise_Measurement_Time_lineEdit.setValidator(QDoubleValidator())
        data=self._parent.MMG.memoryPool["System memory"]["Noise_Measurement_Time"].getValue()
        self._parent.ui.load_pages.Noise_Measurement_Time_lineEdit.setText("{}".format(data))
        self._parent.ui.load_pages.Noise_Measurement_Time_lineEdit.editingFinished.connect(self.btn_callback)
        self._parent.ui.load_pages.Noise_Measurement_Current_lineEdit.setValidator(QDoubleValidator())
        data=self._parent.MMG.memoryPool["System memory"]["Noise_Measurement_Current"].getValue()
        self._parent.ui.load_pages.Noise_Measurement_Current_lineEdit.setText("{}".format(data))
        self._parent.ui.load_pages.Noise_Measurement_Current_lineEdit.editingFinished.connect(self.btn_callback)

        self._parent.ui.load_pages.Resistor_checkBox.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.Voltage_checkBox.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.Current_checkBox.clicked.connect(self.btn_callback)
        
        self._parent.ui.load_pages.Measurement_Mode_comboBox.currentIndexChanged.connect(self.btn_callback)
        index=self._parent.ui.load_pages.Measurement_Mode_comboBox.currentIndex()
        self._parent.ui.load_pages.stackedWidget_2.setCurrentIndex(index)
        
        self._parent.ui.load_pages.remoteConnect_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.gasFreeflow_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.autostart_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.eMSstop_pushButton.clicked.connect(self.btn_callback)


        
        self._parent.ui.load_pages.Manual_Measurement_SingleVoltage_lineEdit.setValidator(QDoubleValidator())
        data=self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Voltage"].getValue()
        self._parent.ui.load_pages.Manual_Measurement_SingleVoltage_lineEdit.setText("{}".format(data))
        self._parent.ui.load_pages.Manual_Measurement_SingleVoltage_lineEdit.editingFinished.connect(self.btn_callback)

        data=self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Single_Mode"].getValue()
        self._parent.ui.load_pages.Manual_Measurement_SingleMode_comboBox.setCurrentText("{}".format(data))
        self._parent.ui.load_pages.Manual_Measurement_SingleMode_comboBox.currentIndexChanged.connect(self.btn_callback)

        data=self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Pattern_Number"].getValue()
        self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.setCurrentIndex(data)
        self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.currentIndexChanged.connect(self.btn_callback)


        self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.clicked.connect(self.btn_callback)
        self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.clicked.connect(self.btn_callback)

        
        data=self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Mode"].getValue()
        if data=="Single":
            self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.setChecked(True)
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.setChecked(False)
            self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setText("電圧印加")
        elif data=="Pattern":
            self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.setChecked(False)
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.setChecked(True)
            self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setText("パターン測定")



        self._parent.ui.load_pages.graphItem_combobox.currentIndexChanged.connect(self.btn_callback)

        self._parent.ui.load_pages.graphItem_combobox.setCurrentIndex(1)
        self._parent.ui.load_pages.timeUnit_comboBox.currentIndexChanged.connect(self.btn_callback)

        self._parent.ui.load_pages.realtime_Pressure_lineEdit.setText("0 kPa")
        self._parent.ui.load_pages.realtime_Temp_lineEdit.setText("0 ℃")
        
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

    def graph_timeUnitData_adjust(self):

        time_convert_constant=self.current_time_unit/self.timeUnit
        
        self.data_semaphore.acquire()
        self.voltage_data_array[0:self.data_array_depth,0:1]*=time_convert_constant
        self.current_data_array[0:self.data_array_depth,0:1]*=time_convert_constant
        self.resistance_data_array[0:self.data_array_depth,0:1]*=time_convert_constant
        self.data_semaphore.release()

        self.current_time_unit=self.timeUnit

    def graph_update(self):

        if self.graph_Item=="Measure_Data":

            if self.realTime_Temperature_Graph_set:
                self.realTime_Temperature_Graph_set=False
                self.win.removeItem(self.realTime_Temperature_Graph)
                self.realTime_Temperature_Graph.showLabel("bottom", show=False)

                self.check_buttom_axix()

            self.realTime_Voltage_Graph_bottomAxis.setTickSpacing(self.timeMaxRange/10,self.timeMaxRange/100)
            self.realTime_Current_Graph_bottomAxis.setTickSpacing(self.timeMaxRange/10,self.timeMaxRange/100)
            self.realTime_Resistance_Graph_bottomAxis.setTickSpacing(self.timeMaxRange/10,self.timeMaxRange/100)

            
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


            sucess,pos,index=self.get_data_from_view(self.voltage_data_array[self.data_array_depth-1][0]-1.1*self.timeMaxRange,False)

            skip_gap=1
            gap=(self.data_array_depth-index)
            if gap >5000:
                skip_gap=math.ceil(gap/5000)

            self._parent.voltage_curve.setData(self.voltage_data_array[index:self.data_array_depth:skip_gap])
            self._parent.current_curve.setData(self.current_data_array[index:self.data_array_depth:skip_gap])
            self._parent.resistance_curve.setData(self.resistance_data_array[index:self.data_array_depth:skip_gap])

            if self.data_array_depth>0:
                self.realTime_Voltage_Graph.setXRange(min=self.voltage_data_array[self.data_array_depth-1][0]-1.1*self.timeMaxRange, max=self.voltage_data_array[self.data_array_depth-1][0]+0.1*self.timeMaxRange)
                self.realTime_Current_Graph.setXRange(min=self.current_data_array[self.data_array_depth-1][0]-1.1*self.timeMaxRange, max=self.current_data_array[self.data_array_depth-1][0]+0.1*self.timeMaxRange)
                self.realTime_Resistance_Graph.setXRange(min=self.resistance_data_array[self.data_array_depth-1][0]-1.1*self.timeMaxRange, max=self.resistance_data_array[self.data_array_depth-1][0]+0.1*self.timeMaxRange)




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

                    self.timeLabel="s"

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


    def adjust_graph_and_data(self):
        # print(self.realTime_Voltage_Graph.viewRange())

        xrange=self.realTime_Voltage_Graph.viewRange()[0]

        sucess,pos,start_index=self.get_data_from_view(xrange[0])
        sucess,pos,end_index=self.get_data_from_view(xrange[1])

        if sucess:
            skip_gap=1
            gap=(end_index-start_index)
            if gap >=5000:
                skip_gap=math.ceil(gap/5000)

            self._parent.voltage_curve.setData(self.voltage_data_array[start_index:end_index+1:skip_gap])
            self._parent.current_curve.setData(self.current_data_array[start_index:end_index+1:skip_gap])
            self._parent.resistance_curve.setData(self.resistance_data_array[start_index:end_index+1:skip_gap])

    def realTime_Voltage_Graph_mouse_move(self,evt):

        self.adjust_graph_and_data()

        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.realTime_Voltage_Graph.sceneBoundingRect().contains(pos):
            mousePoint = self.realTime_Voltage_Graph_vb.mapSceneToView(pos)
            index = int(mousePoint.x())
            # if index > 0 and index < len(data1):
            #     label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % (mousePoint.x(), data1[index], data2[index]))
            
            sucess,pos,index = self.get_data_from_view(mousePoint.x())

            if sucess:
                self.realTime_Voltage_Graph_vLine.setPos(pos)
                self.realTime_Current_Graph_vLine.setPos(pos)
                self.realTime_Resistance_Graph_vLine.setPos(pos)


    def realTime_Current_Graph_mouse_move(self,evt):

        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.realTime_Current_Graph.sceneBoundingRect().contains(pos):
            mousePoint = self.realTime_Current_Graph_vb.mapSceneToView(pos)
            index = int(mousePoint.x())
            # if index > 0 and index < len(data1):
            #     label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % (mousePoint.x(), data1[index], data2[index]))
            
            sucess,pos,index = self.get_data_from_view(mousePoint.x())

            if sucess:
                self.realTime_Voltage_Graph_vLine.setPos(pos)
                self.realTime_Current_Graph_vLine.setPos(pos)
                self.realTime_Resistance_Graph_vLine.setPos(pos)

    def realTime_Resistance_Graph_mouse_move(self,evt):

        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.realTime_Resistance_Graph.sceneBoundingRect().contains(pos):
            mousePoint = self.realTime_Resistance_Graph_vb.mapSceneToView(pos)
            index = int(mousePoint.x())
            # if index > 0 and index < len(data1):
            #     label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % (mousePoint.x(), data1[index], data2[index]))
            
            sucess,pos,index = self.get_data_from_view(mousePoint.x())

            if sucess:
                self.realTime_Voltage_Graph_vLine.setPos(pos)
                self.realTime_Current_Graph_vLine.setPos(pos)
                self.realTime_Resistance_Graph_vLine.setPos(pos)

    def get_data_from_view(self,pos,real_make=True):

        if (    self.realTime_Voltage_Graph_set or 
                self.realTime_Current_Graph_set or 
                self.realTime_Resistance_Graph_set ):
                

            Finded_close_pos=False
            most_clost_index=0
            short_distance=9999999999 

            temp_array=numpy.hsplit(self.voltage_data_array, 2)

            temp_array=numpy.reshape(temp_array[0][:self.data_array_depth],self.data_array_depth)

            most_clost_index=numpy.searchsorted(temp_array, pos)

            distance_a=abs(self.voltage_data_array[most_clost_index][0]-pos)
            distance_b=abs(self.voltage_data_array[most_clost_index-1][0]-pos)

            if most_clost_index>0 and distance_a>distance_b:
                most_clost_index-=1

            Finded_close_pos=True

            # for data in self.voltage_data_array:

            #     distance=abs(data[0]-pos)
            #     if distance<short_distance:
            #         Finded_close_pos=True
            #         most_clost_index=index
            #         short_distance=distance

            #     index+=1

            if Finded_close_pos:


                if real_make:
                    self.realTime_Voltage=self.voltage_data_array[most_clost_index][1]
                    self.realTime_Current=self.current_data_array[most_clost_index][1]
                    self.realTime_Resistor=self.resistance_data_array[most_clost_index][1]

                return True,self.voltage_data_array[most_clost_index][0],most_clost_index

            else:
                return None,None,0
        
        else:

            return None,None,0

    def graph_setup(self):

        pg_setConfigOptions(background=None)
        self.win = pg_GraphicsLayoutWidget(show=True,parent=self._parent)


        self.row_count=0
        #autoDownsample=True,downsampleMethod="subsample",
        self.realTime_Voltage_Graph = self.win.addPlot(row=1, col=0,clipToView=True)
        self.realTime_Voltage_Graph_vLine = pg_InfiniteLine(angle=90, movable=False)
        self.realTime_Voltage_Graph.addItem(self.realTime_Voltage_Graph_vLine, ignoreBounds=True)
        self.realTime_Voltage_Graph_vb = self.realTime_Voltage_Graph.vb
        self.realTime_Voltage_Graph_proxy = pg_SignalProxy(self.realTime_Voltage_Graph.scene().sigMouseMoved, rateLimit=60, slot=self.realTime_Voltage_Graph_mouse_move)
        self.realTime_Voltage_Graph.enableAutoRange('x',0.95)
        self.realTime_Voltage_Graph.setLabel(axis='left', text='電圧', units='V')
        self.realTime_Voltage_Graph.setMouseEnabled(x=True, y=True)
        self.realTime_Voltage_Graph.showGrid(x=True, y=True)

        
        self.realTime_Voltage_Graph.setMenuEnabled(False)

        self.realTime_Current_Graph = self.win.addPlot(row=2, col=0,clipToView=True)
        self.realTime_Current_Graph_vLine = pg_InfiniteLine(angle=90, movable=False)
        self.realTime_Current_Graph.addItem(self.realTime_Current_Graph_vLine, ignoreBounds=True)
        self.realTime_Current_Graph_vb = self.realTime_Current_Graph.vb
        self.realTime_Current_Graph_proxy = pg_SignalProxy(self.realTime_Current_Graph.scene().sigMouseMoved, delay=0.01 , rateLimit=60, slot=self.realTime_Current_Graph_mouse_move)
        self.realTime_Current_Graph.enableAutoRange('x',0.95)
        self.realTime_Current_Graph.setLabel(axis='left', text='電流', units='A')
        self.realTime_Current_Graph.setMouseEnabled(x=True, y=True)
        self.realTime_Current_Graph.showGrid(x=True, y=True)
        
        self.realTime_Current_Graph.setMenuEnabled(False)

        self.realTime_Resistance_Graph = self.win.addPlot(row=3, col=0,clipToView=True)
        self.realTime_Resistance_Graph_vLine = pg_InfiniteLine(angle=90, movable=False)
        self.realTime_Resistance_Graph.addItem(self.realTime_Resistance_Graph_vLine, ignoreBounds=True)
        self.realTime_Resistance_Graph_vb = self.realTime_Resistance_Graph.vb
        self.realTime_Resistance_Graph_proxy = pg_SignalProxy(self.realTime_Resistance_Graph.scene().sigMouseMoved, rateLimit=60, slot=self.realTime_Resistance_Graph_mouse_move)
        self.realTime_Resistance_Graph.enableAutoRange('x',0.95)
        self.realTime_Resistance_Graph.setLabel(axis='left', text='抵抗', units='Ω')
        self.realTime_Resistance_Graph.setMouseEnabled(x=True, y=True)
        self.realTime_Resistance_Graph.showGrid(x=True, y=True)
        self.realTime_Resistance_Graph.setMenuEnabled(False)

        self.realTime_Temperature_Graph = self.win.addPlot(row=4, col=0,clipToView=True)
        self.realTime_Temperature_Graph.setLabel(axis='left', text='温度', units='℃')
        self.realTime_Temperature_Graph.setMouseEnabled(x=True, y=True)
        self.realTime_Temperature_Graph.showGrid(x=True, y=True)
        self.realTime_Temperature_Graph.setMenuEnabled(False)

        self.realTime_Voltage_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
        self.realTime_Current_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
        self.realTime_Resistance_Graph.setLimits(minXRange=0.01*self.timeMaxRange,maxXRange=1.1*self.timeMaxRange)
        #self.realTime_Temperature_Graph.setLimits(minXRange=self.timeMaxRange,maxXRange=self.timeMaxRange)

        

        self._parent.voltage_curve=self.realTime_Voltage_Graph.plot(pen=pg_mkColor(200, 133, 0),
                                                        name="電圧",
                                                        )

        self.realTime_Voltage_Graph_bottomAxis=self.realTime_Voltage_Graph.getAxis("bottom")
        self.realTime_Voltage_Graph_bottomAxis.enableAutoSIPrefix(False)
        

        self._parent.current_curve=self.realTime_Current_Graph.plot(pen=pg_mkColor(132, 220, 244),
                                                        name="電流",
                                                        )

        self.realTime_Current_Graph_bottomAxis=self.realTime_Current_Graph.getAxis("bottom")
        self.realTime_Current_Graph_bottomAxis.enableAutoSIPrefix(False)
        

        self._parent.resistance_curve=self.realTime_Resistance_Graph.plot(pen=pg_mkColor(131, 255, 145),
                                                        name="抵抗値",
                                                        )

        self.realTime_Resistance_Graph_bottomAxis=self.realTime_Resistance_Graph.getAxis("bottom")
        self.realTime_Resistance_Graph_bottomAxis.enableAutoSIPrefix(False)

        self.realTime_Temperature_Graph.addLegend()
        self.pattern_SV_data_array=[]
        self._parent.temp_sv_curve=self.realTime_Temperature_Graph.plot(pen=pg_mkColor(132, 220, 244),
                                                        name="温度SP値",
                                                        )

        self.pattern_PV_data_array=[]
        self._parent.temp_pv_curve=self.realTime_Temperature_Graph.plot(pen=pg_mkColor(200, 133, 0),
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
                self.eventPool["Auto Measure Request"].set()


                # if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
                #     if not self.measurement_start:
                #         print("測定開始 信号到達",self.measurement_start)
                #         self.measurement_start=True
                #         measurement_finish_wait_Thread = threading.Thread(target = self.measurement_finish_wait_Work,daemon=True)
                #         measurement_finish_wait_Thread.start()



            if self.ethernetConnecton_icon_active and not self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
                self.set_memorypool_register("System memory","測定異常コード",4)
                self.eventPool["Measure Stop"].set()

            if self.error_icon_active:
                if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転開始"].getValue():
                    self.set_memorypool_register("System memory","測定異常コード",5)
                    self.eventPool["Measure Stop"].set()
                    
                    self.dataRecord_Start=False
                    
                    self.set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
                    self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
                    self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",1)
                    self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)


            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転開始RST"].getValue():
                self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始",0)
                # time.sleep(0.5)
                self.set_memorypool_register("Modbus Registor Pool - Registor","運転開始RST",0)

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["運転停止RST"].getValue():
                self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止",0)
                # time.sleep(0.5)
                self.set_memorypool_register("Modbus Registor Pool - Registor","運転停止RST",0)

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定終了RST"].getValue():
                self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",0)
                # time.sleep(0.5)
                self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了RST",0)

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["実行PTN No.変更RST"].getValue():
                time.sleep(1)
                self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更",0)
                self.set_memorypool_register("Modbus Registor Pool - Registor","実行PTN No.変更RST",0)
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.setEnabled(True)
                self._parent.ui.load_pages.AutoMode_pattern_comboBox.setCursor(QCursor(Qt.ArrowCursor))
                

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["大気圧RST"].getValue():
                self.set_memorypool_register("Modbus Registor Pool - Registor","大気圧",0)
                # time.sleep(0.5)
                self.set_memorypool_register("Modbus Registor Pool - Registor","大気圧RST",0)

            if self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PC警報RST"].getValue():
                self.set_memorypool_register("Modbus Registor Pool - Registor","PC警報",0)
                # time.sleep(0.5)
                self.set_memorypool_register("Modbus Registor Pool - Registor","PC警報RST",0)


            

    def noise_measurement_finish_wait_Work(self):
        # print("ノイズ測定開始")
        self.dataRecord_Start=True
        data_receive_Thread = threading.Thread(target = self.data_receive_Work,daemon=True)
        data_receive_Thread.start()
        self.eventPool["Noise Measure Start"].set()
        self.eventPool["Noise Measure finish"].clear()
        self.eventPool["Noise Measure finish"].wait()
        self.eventPool["Noise Measure finish"].clear()
        self.dataRecord_Start=False
        self.measurement_start=False
        # print("ノイズ測定終了")
        
    def manual_measurement_finish_wait_Work(self):

        print("手動測定開始")
        self.dataRecord_Start=True
        data_receive_Thread = threading.Thread(target = self.data_receive_Work,daemon=True)
        data_receive_Thread.start()

        mode=self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Mode"].getValue()
        if mode =="Single":
            self.eventPool["Manual Measure Single Start"].set()
            self.eventPool["Manual Measure Single finish"].clear()
            self.eventPool["Manual Measure Single finish"].wait()
            self.eventPool["Manual Measure Single finish"].clear()

        elif mode =="Pattern":
            self.eventPool["Manual Measure Pattern Start"].set()
            self.eventPool["Manual Measure Pattern finish"].clear()
            self.eventPool["Manual Measure Pattern finish"].wait()
            self.eventPool["Manual Measure Pattern finish"].clear()

        self.dataRecord_Start=False
        self.measurement_start=False
        
        self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.blockSignals(False)
        # print("手動測定終了")

    def measurement_finish_wait_Work(self):
        # print("測定開始")
        self.dataRecord_Start=True
        data_receive_Thread = threading.Thread(target = self.data_receive_Work,daemon=True)
        data_receive_Thread.start()
        self.eventPool["Auto Measure Start"].set()
        self.eventPool["Auto Measure finish"].clear()
        self.eventPool["Auto Measure finish"].wait()
        self.eventPool["Auto Measure finish"].clear()
        self.set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
        self.set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)
        self.dataRecord_Start=False
        self.measurement_start=False
        # print("測定終了")

    

    def ultility_Update_Work(self):

        #if any Measurement is taking place
        #enable Stop button
        #prevent user go to others mode
        if ( self._parent.MMG.memoryPool["System memory"]["Noise_Measurement_Active"].getValue() or 
            self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Active"].getValue()    ):
            self._parent.ui.load_pages.Measurement_Stop_pushButton.blockSignals(False)
            self._parent.ui.load_pages.Measurement_Stop_pushButton.setChecked(False)
            self._parent.ui.load_pages.Measurement_Stop_pushButton.setEnabled(True)
            self._parent.ui.load_pages.Measurement_Mode_comboBox.setEnabled(False)
            self._parent.ui.load_pages.btn_AutoMode.setEnabled(False)
            self._parent.ui.load_pages.btn_AutoMode.setVisible(False)
        else:
            #We dont need to stop/abort any measurement
            self._parent.ui.load_pages.Measurement_Stop_pushButton.blockSignals(True)
            self._parent.ui.load_pages.Measurement_Stop_pushButton.setChecked(False)
            self._parent.ui.load_pages.Measurement_Stop_pushButton.setEnabled(False)

            #We should allow to switch to Auto mode
            self._parent.ui.load_pages.btn_AutoMode.setEnabled(True)
            self._parent.ui.load_pages.btn_AutoMode.setVisible(True)

            #if PLC tell us not to do measurement
            if self.ethernetConnecton_icon_active and not self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
        
                self._parent.ui.load_pages.Measurement_Mode_comboBox.setEnabled(False)
                self._parent.ui.load_pages.Noise_Measurement_Start_pushButton.setEnabled(False)

            #if we are free to process any measurement
            else:
                self._parent.ui.load_pages.Measurement_Mode_comboBox.setEnabled(True)

        #if Noise Measurement is ongoing
        #Disable Noise_Measurement_Start_pushButton from over load method
        #Prevent any test paremeter changed
        if self._parent.MMG.memoryPool["System memory"]["Noise_Measurement_Active"].getValue():
            self._parent.ui.load_pages.Noise_Measurement_Start_pushButton.blockSignals(True)
            self._parent.ui.load_pages.Noise_Measurement_Start_pushButton.setChecked(True)
            self._parent.ui.load_pages.Noise_Measurement_Voltage_lineEdit.setEnabled(False)
            self._parent.ui.load_pages.Noise_Measurement_Time_lineEdit.setEnabled(False)
            self._parent.ui.load_pages.Noise_Measurement_Current_lineEdit.setEnabled(False)
        else:
            self._parent.ui.load_pages.Noise_Measurement_Start_pushButton.setChecked(False)
            self._parent.ui.load_pages.Noise_Measurement_Start_pushButton.blockSignals(False)
            self._parent.ui.load_pages.Noise_Measurement_Voltage_lineEdit.setEnabled(True)
            self._parent.ui.load_pages.Noise_Measurement_Time_lineEdit.setEnabled(True)
            self._parent.ui.load_pages.Noise_Measurement_Current_lineEdit.setEnabled(True)

        #if Manual Measurement is ongoing
        if self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Active"].getValue():

            self._parent.ui.load_pages.Manual_Measurement_SingleVoltage_lineEdit.setEnabled(False)
            self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.blockSignals(True)
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.blockSignals(True)
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.setEnabled(False)

            #Check which measeurement mode are we
            Manual_Measurement_Mode=self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Mode"].getValue()
            if Manual_Measurement_Mode=="Single":
                self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.setChecked(True)
                self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.setEnabled(True)
                self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.setChecked(False)
                self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.setEnabled(False)


                #if voltage is already output and data is incomeing
                if self.ethernetConnecton_icon_active and not self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setChecked(False)
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(False)
                    self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setChecked(False)
                    self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setEnabled(False)
                else:
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setChecked(True)
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(True)
                    if self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Ready"].getValue():
                        if self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_trigger"].getValue():
                            self._parent.ui.load_pages.Manual_Measurement_SingleMode_comboBox.setEnabled(False)
                            self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.setEnabled(False)
                            self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.blockSignals(True)
                            self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setChecked(True)
                            self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setEnabled(True)
                        else:
                            self._parent.ui.load_pages.Manual_Measurement_SingleMode_comboBox.setEnabled(True)
                            self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.setEnabled(True)
                            self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.blockSignals(False)
                            self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setChecked(False)
                            self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setEnabled(True)
                    else:
                        self._parent.ui.load_pages.Manual_Measurement_SingleMode_comboBox.setEnabled(True)
                        self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setChecked(False)
                        self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setEnabled(False)

        



            elif Manual_Measurement_Mode=="Pattern":
                self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.setChecked(False)
                self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.setEnabled(False)
                self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.setChecked(True)
                self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.setEnabled(True)
                self._parent.ui.load_pages.Manual_Measurement_SingleMode_comboBox.setEnabled(True)

                if self.ethernetConnecton_icon_active and not self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setChecked(False)
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(False)
                else:
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setChecked(True)
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(True)


        #if Manual Measurement is not ongoing
        else:
            self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setEnabled(False)

            self._parent.ui.load_pages.Manual_Measurement_SingleVoltage_lineEdit.setEnabled(True)
            self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.blockSignals(False)
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.blockSignals(False)
            self._parent.ui.load_pages.Manual_Measurement_SingleMode_comboBox.setEnabled(True)
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.setEnabled(True)


            #Check which measeurement mode are we
            Manual_Measurement_Mode=self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Mode"].getValue()
            if Manual_Measurement_Mode=="Single":
                self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.setChecked(True)#
                self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.setEnabled(True)#
                self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.setChecked(False)#
                self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.setEnabled(True)#


                if self.ethernetConnecton_icon_active and not self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
                    
                    # print("1")
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setChecked(False)#
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(False)#
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.blockSignals(True)
                else:
                    
                    # print("2")
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setChecked(False)#
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(True)#
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.blockSignals(False)



            elif Manual_Measurement_Mode=="Pattern":
                self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.setChecked(False)#
                self._parent.ui.load_pages.Manual_Measurement_SingleMode_pushButton.setEnabled(True)#
                self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.setChecked(True)#
                self._parent.ui.load_pages.Manual_Measurement_PatternMode_pushButton.setEnabled(True)#

                if self.ethernetConnecton_icon_active and not self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
                
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setChecked(False)#
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(False)#
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.blockSignals(True)
                else:
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setChecked(False)#
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(True)#
                    self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.blockSignals(False)



            # #Check which measeurement mode are we looking at
            # Manual_Measurement_Mode=self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Mode"].getValue()
            # if Manual_Measurement_Mode=="Single":
            #     if self.ethernetConnecton_icon_active and not self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
            #         self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(False)
            #     else:
            #         self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(True)
            #         self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.blockSignals(False)

            # elif Manual_Measurement_Mode=="Pattern":
            #     self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.setEnabled(False)
            #     self._parent.ui.load_pages.Manual_Measurement_Start_pushButton.blockSignals(True)

            #     if self.ethernetConnecton_icon_active and not self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["測定可"].getValue():
            #         self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setEnabled(False)
            #     else:
            #         print("2")
            #         self._parent.ui.load_pages.Manual_Measurement_Trigger_pushButton.setEnabled(True)

                

        

        if self.AutoMode_pattern_comboBox_contantList !=self._parent.tempPattern.patternFile_nameList:
            self.AutoMode_pattern_comboBox_contantList=self._parent.tempPattern.patternFile_nameList
            self._parent.ui.load_pages.AutoMode_pattern_comboBox.blockSignals(True)
            self._parent.ui.load_pages.AutoMode_pattern_comboBox.clear()
            self._parent.ui.load_pages.AutoMode_pattern_comboBox.addItems(self.AutoMode_pattern_comboBox_contantList)
            self._parent.ui.load_pages.AutoMode_pattern_comboBox.setCurrentIndex(self.choose_pattern)
            self._parent.ui.load_pages.AutoMode_pattern_comboBox.blockSignals(False)

        if self.Manual_Measurement_pattern_comboBox_contantList !=self._parent.testPattern.patternFile_nameList:
            self.Manual_Measurement_pattern_comboBox_contantList=self._parent.testPattern.patternFile_nameList
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.blockSignals(True)
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.clear()
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.addItems(self.Manual_Measurement_pattern_comboBox_contantList)
            choose_test_pattern=self._parent.MMG.memoryPool["System memory"]["Manual_Measurement_Pattern_Number"].getValue()
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.setCurrentIndex(choose_test_pattern)
            self._parent.ui.load_pages.Manual_Measurement_PatternMode_comboBox.blockSignals(False)

        if not self._parent.tempPattern.patternFiles==[] and self.AutoMode_pattern_comboBox_contantList:

            gas_mode=0
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



