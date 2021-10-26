# -*- coding: utf-8 -*-
from gui_main.gui.uis.pattern_columns.pattern_function import testUnit,testlist
from gpib_manager import GPIB_device_2635B,GPIB_device_2657A,GPIB_Driver,GPIB_package
import threading
import time
import copy

class test_folder_package():

    RT_stage=1
    Temp_stage=2

    def __init__(self,
                 stage=[0,0]
                 ):

        self.stage=stage

class test_profile_package():

    QC_Test=1
    Costomer_Test=2

    def __init__(self,
                 test_times=0,
                 file_name="",
                 date="",
                 condition=1,
                 number="",
                 costomer="",
                 costomerName="",
                 meterialName="",
                 meterial="",
                 mainDia=0,
                 innerDia=0,
                 thinkness=0,
                 gas="",
                 ):
        self.test_times=test_times
        self.file_name=file_name
        self.date=date
        self.condition=condition
        self.number=number
        self.costomer=costomer
        self.costomerName=costomerName
        self.meterialName=meterialName
        self.meterial=meterial
        self.mainDia=mainDia
        self.innerDia=innerDia
        self.thinkness=thinkness
        self.gas=gas


        if self.condition==self.QC_Test:
            self.number=""
            self.costomer=""
            self.costomerName=""

class single_test_unitPackage():

    #If count=-1 mean data stream is finish

    def __init__(self,
                 count=0,
                 time=0,
                 Temperature=0,
                 voltage=0,
                 current=0
                 ):
        self.count=count
        self.time=time
        self.Temperature=Temperature
        self.voltage=voltage
        self.current=current
        self.resistance=voltage/current



def operator_thread(memoryPool,queuePool,eventPool):
    print("fdggfd")
    operator=Operator(memoryPool,queuePool,eventPool)

class Operator():

    def __init__(self,
                 memoryPool,
                 queuePool,
                 eventPool
                 ):
        self.memoryPool=memoryPool
        self.queuePool=queuePool
        self.eventPool=eventPool
        
        print("1")

        self.gpib_2635B=GPIB_device_2635B(memoryPool,queuePool)
        print("2")
        self.gpib_2657A=GPIB_device_2657A(memoryPool,queuePool)

        print("3")
        auto_Run_Start_Thread = threading.Thread(target = self.auto_Run_Start_Work,daemon=True)
        auto_Run_Start_Thread.start()

        stop_Thread = threading.Thread(target = self.stop_Work,daemon=True)
        stop_Thread.start()

        while 1:
            pass

    def stop_Work(self):
        while 1:
            self.eventPool["GPIB Stop"].wait()
            self.eventPool["GPIB Stop"].clear()

            self.stop=True
            print("GPIB stop")

    def set_memorypool_register(self,
                                                memorypool_name,
                                                registor_name,
                                                value):
        
        if self.memoryPool[memorypool_name][registor_name].getValue()!=value:

            sub_memorypool=copy.deepcopy(self.memoryPool[memorypool_name])
            sub_memorypool[registor_name].setValue(value)

            self.memoryPool[memorypool_name]=sub_memorypool
            sendItem=MemoryUnit(memorypool_name,registor_name)
            queuePool["database_Uplaod_Queue"].put(sendItem)
            queuePool["memory_DownlaodToGUI_request_Queue"].put(sendItem)

    def auto_Run_Start_Work(self):
        while 1:
            #get event Start Run Auto run
            self.eventPool["Auto Run Start"].wait()
            self.eventPool["Auto Run Start confirm"].set()
            self.stop=False

            Modbus_Registor_Pool=self.memoryPool["Modbus Registor Pool - Registor"]


            #check if PLC is ok to start
            #check if PLC is stop
            if Modbus_Registor_Pool["運転可"].getValue() and Modbus_Registor_Pool["停止中"].getValue():

                #Tell PLC start pattern and PLC will reset this
                set_memorypool_register("Modbus Registor Pool - Registor","運転開始",1)
            
                #check if there is any test pattern at future pattern step
                operate_PTN_number=Modbus_Registor_Pool["実行PTN No.変更"].getValue()

                test_pattern_listInPTN=[]

                if Modbus_Registor_Pool["PTNData_{}_RT計測".format(operate_PTN_number)].getValue():
                    test_pattern_listInPTN.append("RT")

                for step in range(1,Modbus_Registor_Pool["PTNData_{}_実行STEP数".format(operate_PTN_number)].getValue()+1):
                    if Modbus_Registor_Pool["PTNData_{}_STEP_{}_STEP情報".format(operate_PTN_number,step)].getValue()==2:
                        #this is a test pattern
                        test_pattern=Modbus_Registor_Pool["PTNData_{}_STEP_{}_測定パターン".format(operate_PTN_number,step)].getValue()
                        test_pattern_listInPTN.append(test_pattern)

                #print(test_pattern_listInPTN)
                
                Measurement_Pattern=self.memoryPool["Measurement Pattern"]
                #if yes
                for test_pattern_no in test_pattern_listInPTN:


                    test_pattern=testlist()
                    if test_pattern_no=="RT":
                        #prepare test profile and send script to GPIB device
                        test_pattern.active=Measurement_Pattern["PTNData_{}_パターン有効".format(test_pattern_no)].getValue(),
                        test_pattern.BG0_test_time=Measurement_Pattern["PTNData_{}_BG0測定時間".format(test_pattern_no)].getValue(),
                        test_pattern.BG_sampletime=Measurement_Pattern["PTNData_{}_BG測定sampletime".format(test_pattern_no)].getValue()
                            
                    else:
                        #prepare test profile and send script to GPIB device
                        
                        test_pattern.name=Measurement_Pattern["PTNData_{}_名称".format(test_pattern_no)].getValue(),
                        test_pattern.comment=Measurement_Pattern["PTNData_{}_註記".format(test_pattern_no)].getValue(),
                        test_pattern.active=Measurement_Pattern["PTNData_{}_パターン有効".format(test_pattern_no)].getValue(),
                        test_pattern.step_number=Measurement_Pattern["PTNData_{}_実行STEP数".format(test_pattern_no)].getValue(),
                        test_pattern.test_time=Measurement_Pattern["PTNData_{}_測定時間".format(test_pattern_no)].getValue(),
                        test_pattern.test_sampletime=Measurement_Pattern["PTNData_{}_測定sampletime".format(test_pattern_no)].getValue(),
                        test_pattern.BG0_test_time=Measurement_Pattern["PTNData_{}_BG0測定時間".format(test_pattern_no)].getValue(),
                        test_pattern.BG_test_time=Measurement_Pattern["PTNData_{}_BG測定時間".format(test_pattern_no)].getValue(),
                        test_pattern.BG_sampletime=Measurement_Pattern["PTNData_{}_BG測定sampletime".format(test_pattern_no)].getValue()
                            
                        units=[]
                        for unit in range(1,test_pattern.step_number+1):
                            unit=testUnit(
                                voltage=Measurement_Pattern["PTNData_{}_STEP_{}_電圧".format(test_pattern_no,unit)].getValue()
                                )
                            units.append(unit)
                        test_pattern.units=units



                    self.GPIB_device_ScriptPrepare(test_pattern)

                    self.abort=False
                    #Wait PLC tell us if we can start to test
                    while not self.eventPool["Test approve"].wait(0.1):
                        #If we got stop signal
                        if self.stop:
                            self.abort=True
                            break
                    self.eventPool["Test approve"].clear()

                    #If we got stop signal stop this auto start
                    if self.abort:
                        break

                    
                    #start test 
                    #print("PLC allow us to start measurment")
                    
                    #               - tell csv_manager get ready

                    #               - send trigger to GPIB device to start script
                    self.GPIB_device_startScript()
                    #               - initial measure data retrive Thread
                    GPIB_data_retrive_Thread = threading.Thread(target = self.GPIB_data_retrive_Work,daemon=True)
                    GPIB_data_retrive_Thread.start()

                    while not self.eventPool["GPIB_Test_Finish"].wait(0.1):
                        #If we got stop signal
                        if self.stop:
                            self.abort=True
                            break
                    self.eventPool["GPIB_Test_Finish"].clear()

                    #If we got stop signal stop this auto start
                    if self.abort:
                        break

                    #Tell PLC we had finish measurement test 
                    set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)


            
        #clear  Start Run Auto run event
        self.eventPool["Auto Run Start"].clear()

    def GPIB_device_ScriptPrepare(self,patten):
        #reset all gpib device include TSP-Link device
            #-reset()
            #-node[1].errorqueue.clear()
            #-node[2].errorqueue.clear()
            #-node[1].status.reset()
            #-node[2].status.reset()
            #-tsplink.reset()
            #-node[1].dataqueue.clear()
            #-node[1].display.clear()
            #-node[1].display.setcursor(1, 1)
            #-node[1].display.settext("Prepare")
            #-node[1].display.setcursor(2, 1)
            #-node[1].display.settext("Wait to start PTN.1")
            #-node[2].display.clear()
            #-node[2].display.setcursor(1, 1)
            #-node[2].display.settext("Prepare")
            #-node[2].display.setcursor(2, 1)
            #-node[2].display.settext("Wait to start PTN.1")


        #prepare test pattern to script

        #send script to TSP-Link Master

            #-loadscript testProfile

            #-tsplink.trigger[0].reset()
            #-tsplink.trigger[1].reset()
            #-tsplink.trigger[2].reset()
            #-tsplink.trigger[3].reset()

            #-node[1].smua.reset()
            #-node[1].smua.nvbuffer1.clear()
            #-node[1].smua.nvbuffer1.collecttimestamps = 1
            #-node[1].smua.nvbuffer1.timestampresolution=0.000001     if total time is short then 70minute
            #-node[1].smua.nvbuffer1.timestampresolution=0.000010     if total time is bigger then 70minute
            #-node[1].smua.trigger.initiate()
            #-node[1].smua.trigger.autoclear = 1
            #-node[1].smua.trigger.measure.i(smua.nvbuffer1)
            #-node[1].smua.trigger.measure.stimulus=tsplink.trigger[1].EVENT_ID
            #-node[1].tsplink.trigger[2].stimulus=smua.trigger.MEASURE_COMPLETE_EVENT_ID
            
            #-node[2].smua.reset()
            #-node[2].smua.nvbuffer1.clear()
            #-node[2].smua.nvbuffer1.collecttimestamps = 1
            #-node[2].smua.nvbuffer1.timestampresolution=0.000001     if total time is short then 70minute
            #-node[2].smua.nvbuffer1.timestampresolution=0.000010     if total time is bigger then 70minute
            #-node[2].smua.trigger.initiate()
            #-node[2].smua.trigger.autoclear = 1
            #-node[2].smua.trigger.measure.v(smua.nvbuffer1)
            #-node[2].smua.trigger.measure.stimulus=tsplink.trigger[1].EVENT_ID
            #-node[2].tsplink.trigger[3].stimulus=smua.trigger.MEASURE_COMPLETE_EVENT_ID
            #-
            #-
            #-node[1].trigger.timer[0].reset()                                                                          //Set sync timer
            #-node[1]trigger.timer[0].clear()
            #-node[1]trigger.timer[0].count= 測定回数
            #-node[1]trigger.timer[0].delay= サンプリング周期
            #-node[1]trigger.timer[0].stimulus=tsplink.trigger[0].EVENT_ID
            #-node[1]tsplink.trigger[1].stimulus=trigger.timer[0].EVENT_ID
            #-
            #-
            #-
            #-node[1]trigger.blender[1].reset()                                                                      //Set blender
            #-node[1]trigger.blender[1].stimulus[1]=tsplink.trigger[2].EVENT_ID
            #-node[1]trigger.blender[1].stimulus[2]=tsplink.trigger[3].EVENT_ID
            #-
            #-
            #-node[1].smua.source.func = smua.OUTPUT_DCVOLTS                    //output high voltage
            #-node[1].smua.source.autorangev = smua.AUTORANGE_ON
            #-node[1].smua.source.levelv = 測定電圧
            #-node[1].smua.source.limiti = 20e-3 
            #-node[1].smua.measure.rangei = 20e-3
            #-node[1].smua.source.output = smua.OUTPUT_ON
            #-
            #-
            #-node[1].tsplink.trigger[0].assert()                                                           //start measurement loop
            #-
            #-for count 1,測定回数 do
            #-  node[1].trigger.blender[1].wait()
            #-  node[1].current_name=node[1].smua.nvbuffer1.measurefunctions[N]
            #-  node[1].current_time=node[1].smua.nvbuffer1.timestamps[count]
            #-  node[1].current_value=node[1].smua.nvbuffer1.readings[count]
            #-  node[1].voltage_name=node[2].smua.nvbuffer1.measurefunctions[N]
            #-  node[1].voltage_time=node[2].smua.nvbuffer1.timestamps[count]
            #-  node[1].voltage_value=node[2].smua.nvbuffer1.readings[count]
            #-
            #-  node[1].sendItem={count,current_name,current_time,current_value,voltage_name,voltage_time,voltage_value}
            #-
            #-  node[1].dataqueue.add(sendItem)
            #-
            #-node[1].dataqueue.add(-1)
            #-
            #-tsplink.trigger[0].assert()
            #-
            #-node[1].smua.source.output = smua.OUTPUT_OFF                          //TurnOFF high voltage
            #-
            #-endscript
        pass

    def GPIB_device_startScript(self):
        #send GPIB command to TSP-Master
        self.gpib_2657A.send_Command("testProfile.run()")

    def GPIB_data_retrive_Work(self):
        #send GPIB command to get Voltage and Current
        self.measurement_data=[]
        while 1:
            result,error_message=self.gpib_2657A.read_Command("node[1].print(dataqueue.next())")
            if not error_message:
                if result==-1:
                    self.eventPool["GPIB_Test_Finish"].set()
                    break
                else:
                    #save the result back to array
                    #result={
                    #count,
                    #current_name,
                    #current_time,
                    #current_value,
                    #voltage_name,
                    #voltage_time,
                    #voltage_value}
                    #result="1,currnet,3,4,voltage,6,7"
                    #print(result)
                    
                    result_list=list(result.split(","))
                    print(result_list)

                    data_pachage=single_test_unitPackage(
                            count=int(result_list[0]),
                            time=float(result_list[2]),
                            Temperature=float(self.memoryPool["Modbus Registor Pool - Registor"]["温度PV値"].getValue()),
                            voltage=float(result_list[6]),
                            current=float(result_list[3])
                        )
                    self.measurement_data.append(data_pachage)
                    self.memoryPool["Measurement_data"]=self.measurement_data
                    self.eventPool["CSV_Data_arrive"].set()
                    self.eventPool["GUI_Data_arrive"].set()
                    

            time.sleep(0.5)
            if self.stop:
                break

                    


    def csv_prepare(self):

        #send subFolderMake command to csv_manager and sub folder should be ready
        #put subFolderMake command to queue
        self.queuePool["subFolderMakeQueue"].put()

