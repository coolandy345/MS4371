# -*- coding: utf-8 -*-
from gui_main.gui.uis.pattern_columns.pattern_function import testUnit,testlist
from gpib_manager import GPIB_device_2635B,GPIB_device_2657A,GPIB_Driver,GPIB_package
import threading
import time
import copy
from gpib_manager import *
from registor_manager import *
from quantiphy import Quantity
from csv_manager import  *
import datetime
import random

class Test_folder_package():

    RT_stage=1
    Temp_stage=2

    def __init__(self,
                 stage=[0,0]
                 ):

        self.stage=stage

class Test_profile_package():
    
    QC_Test=1
    Costomer_Test=2

    def __init__(self,
                 date="",
                 folder_name="",
                 file_name="",
                 mode=0,
                 number="",
                 costomer="",
                 costomerName="",
                 meterialName="",
                 meterial="",
                 mainDia=0,
                 innerDia=0,
                 thinkness=0,
                 gas="",
                 voltage=0,
                 time=0,
                 time_sample=0,
                 bg_time=0,
                 bg_time_sample=0,
                 speed="",
                 filter="",
                 filter_count=0,
                 ):
        self.date=date
        self.folder_name=folder_name
        self.file_name=file_name
        self.mode=mode
        self.number=number
        self.costomer=costomer
        self.costomerName=costomerName
        self.meterialName=meterialName
        self.meterial=meterial
        self.mainDia=mainDia
        self.innerDia=innerDia
        self.thinkness=thinkness
        self.gas=gas

        self.voltage=voltage
        self.time=time
        self.bg_time=bg_time
        self.speed=speed
        self.filter=filter

        if not self.time:
            self.time_sample=0
        else:
            self.time_sample=time_sample

        if not self.bg_time:
            self.bg_time_sample=0
        else:
            self.bg_time_sample=bg_time_sample

        if self.filter=="なし":
            self.filter_count=0
        else:
            self.filter_count=filter_count

        if self.mode==self.QC_Test:
            self.number=""
            self.costomer=""
            self.costomerName=""

class Single_data_unitPackage():

    #If count=-1 mean data stream is finish

    def __init__(self,
                 time=0,
                 count=0,
                 Temperature=0,
                 voltage=0,
                 current=0,
                 resistance=0,
                 resistivity=0

                 ):
        self.time=time
        self.count=count
        self.Temperature=Temperature
        self.voltage=voltage
        self.current=current
        self.resistance=resistance
        self.resistivity=resistivity




def operator_thread(memoryPool,queuePool,eventPool):
    gpib_Thread(memoryPool,queuePool)

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
        
        self.csv_manager=Csv_manager(memoryPool,queuePool,eventPool)

        #self.gpib_2635B=GPIB_device_2635B(memoryPool,queuePool)
        self.gpib_2657A=GPIB_device_2657A(memoryPool,queuePool)

        self.gpib_2657A_control=False

        auto_Run_Start_Thread = threading.Thread(target = self.auto_Run_Start_Work,daemon=True)
        auto_Run_Start_Thread.start()

        start_noise_measurement_Thread = threading.Thread(target = self.start_noise_measurement,daemon=True)
        start_noise_measurement_Thread.start()

        stop_noise_measurement_Thread = threading.Thread(target = self.stop_noise_measurement,daemon=True)
        stop_noise_measurement_Thread.start()


        test1_Thread=threading.Thread(target = self.test_Work1,daemon=True)
        test1_Thread.start()

        test2_Thread=threading.Thread(target = self.test_Work2,daemon=True)
        test2_Thread.start()

        stop_Thread = threading.Thread(target = self.stop_Work,daemon=True)
        stop_Thread.start()

        #TSP_check_Thread = threading.Thread(target = self.TSP_check_Work,daemon=True)
        #TSP_check_Thread.start()


        self.set_memorypool_register("Modbus Registor Pool - Registor","PC Boot",0)

        self.set_memorypool_register("Modbus Registor Pool - Registor","PC Boot",1)


    #def TSP_check_Work(self):
    #    self.
    #    pass
        

    def test_Work1(self):
        
        while 1:
            self.eventPool["Test Event1"].wait()
            self.eventPool["Test Event1"].clear()
            print("Test Event1 trigger")

            self.gpib_2657A.send_Command("loadscript testProfile")
            
            self.gpib_2657A.send_Command("reset()")
            
            self.gpib_2657A.send_Command("tsplink.reset() ")
            self.gpib_2657A.send_Command("dataqueue.clear()  ")
            

            self.gpib_2657A.send_Command("for element = 1, 3 do ")
            self.gpib_2657A.send_Command("beeper.beep(0.1, 2400)")
            self.gpib_2657A.send_Command("sendItem={element, node[1].tsplink.node,node[2].tsplink.node}")
            self.gpib_2657A.send_Command("dataqueue.add(sendItem)  ")
            self.gpib_2657A.send_Command("end")


            self.gpib_2657A.send_Command(" print(\"access queue now\") ")
 
            self.gpib_2657A.send_Command("while dataqueue.count > 0 do  ")
            self.gpib_2657A.send_Command(" x = dataqueue.next()  ")
            self.gpib_2657A.send_Command(" print(x[1],x[2],x[3]) ")
            self.gpib_2657A.send_Command("end")

            self.gpib_2657A.send_Command(" print(\"finial\") ")
 


            #self.gpib_2657A.send_Command("  node[1].sendItem={ver1,ver2}")
            #self.gpib_2657A.send_Command("  node[1].print(sendItem)")
            #self.gpib_2657A.send_Command("end)")

            self.gpib_2657A.send_Command("endscript")

            self.gpib_2657A.send_Command("testProfile.run()")
            pass


    def test_Work2(self):
        while 1:
            self.eventPool["Test Event2"].wait()
            self.eventPool["Test Event2"].clear()
            print("Test Event2 trigger")


            message,errorcode=self.gpib_2657A.read_Command()
            if errorcode:
                print("GPIB Read エラー発生",errorcode)
            else:
                print(type(message.split('\t')),message.split('\t'))
            #result_list=list(result.split(","))
            time.sleep(1)
            
            pass

    def stop_Work(self):
        while 1:
            self.eventPool["GPIB Stop"].wait()
            self.eventPool["GPIB Stop"].clear()

            self.stop=True
            print("GPIB EMS stop")

            self.gpib_2657A.send_Command("reset()")


    def set_memorypool_register(self,
                                                memorypool_name,
                                                registor_name,
                                                value):

        if self.memoryPool[memorypool_name][registor_name].getValue()!=value:
            sub_memorypool=copy.deepcopy(self.memoryPool[memorypool_name])
            sub_memorypool[registor_name].setValue(value)
            
            self.memoryPool[memorypool_name]=sub_memorypool
            sendItem=MemoryUnit(memorypool_name,registor_name)
            
            self.queuePool["database_Uplaod_Queue"].put(sendItem)
            self.queuePool["memory_DownlaodToGUI_request_Queue"].put(sendItem)

    def measurement_initial(
                                self,
                                voltage=0,
                                test_time=0,
                                sample_time=0
                            ):
        self.GPIB_device_ScriptPrepare(voltage,test_time,sample_time)

        #Wait PLC tell us if we can start to test
        while not self.eventPool["Test approve"].wait(0.1):
            #If we got stop signal
            if self.stop:
                return False

        #Get PLC approve to process
        #print("PLC allow us to start measurment")
        self.eventPool["Test approve"].clear()
        set_memorypool_register("Modbus Registor Pool - Registor","測定開始",0)
        
        #               - send trigger to GPIB device to start script
        self.GPIB_device_startScript()
        #               - initial measure data retrive Thread
        GPIB_data_retrive_Thread = threading.Thread(target = self.GPIB_data_retrive_Work,daemon=True)
        GPIB_data_retrive_Thread.start()

        while not self.eventPool["GPIB_Test_Finish"].wait(0.1):
            #If we got stop signal
            if self.stop:
                return False
        self.eventPool["GPIB_Test_Finish"].clear()

    def stop_noise_measurement(self):
        while 1:
            #get event Start Run Auto run
            self.eventPool["Noise Measure Stop"].wait()
            #clear  Start Run Auto run event
            self.eventPool["Noise Measure Stop"].clear()
            print("stop")
            self.noise_stop=True

    def start_noise_measurement(self):
        test_voltage=1000
        over_current=5e-12
        test_time=1

        while 1:
            #get event Start Run Auto run
            self.eventPool["Noise Measure Start"].wait()
            #clear  Start Run Auto run event
            self.eventPool["Noise Measure Start"].clear()

            print("start")
            self.noise_stop=False
            
            self.gpib_2657A.send_Command("loadscript Noise_Measurement")
            

            self.gpib_2657A.send_Command("reset()")
            self.gpib_2657A.send_Command("tsplink.reset()")
            self.gpib_2657A.send_Command("beeper.beep(0.1, 2400)")

            self.gpib_2657A.send_Command("node[2].display.clear()")
            self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[2].display.settext(\"Noise Test Start\")")

            self.gpib_2657A.send_Command("node[1].display.clear()")
            self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[1].display.settext(\"Noise Test Start\")")

            
            self.gpib_2657A.send_Command("delay(1)")
            
            
            self.gpib_2657A.send_Command("node[1].display.clear()")
            self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[1].display.settext(\"Setting...\")")
            
            self.gpib_2657A.send_Command("node[1].display.setcursor(2, 1)")
            self.gpib_2657A.send_Command("node[1].display.settext(\"Voltage... {}\")".format(Quantity(float(test_voltage),"V").render(prec=4)))

            self.gpib_2657A.send_Command("node[2].display.clear()")
            self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[2].display.settext(\"Setting...\")")
            
            
            self.gpib_2657A.send_Command("node[1].smua.reset()")
            self.gpib_2657A.send_Command("node[1].smua.measure.nplc = 1")
            self.gpib_2657A.send_Command("node[1].smua.measure.autorangev = smua.AUTORANGE_ON")
            self.gpib_2657A.send_Command("node[1].smua.measure.count = 1")
            self.gpib_2657A.send_Command("node[1].smua.measure.delay = 0")

            self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.clear()")
            self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.appendmode = 1")
            self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.collecttimestamps = 0")
            self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.fillmode = 0")

            self.gpib_2657A.send_Command("node[1].smua.source.func = smua.OUTPUT_DCVOLTS")
            self.gpib_2657A.send_Command("node[1].smua.source.rangev = 1500")
            self.gpib_2657A.send_Command("node[1].smua.source.levelv = {}".format(test_voltage))
            self.gpib_2657A.send_Command("node[1].smua.source.limiti = 1e-6")

            
            self.gpib_2657A.send_Command("node[2].smua.reset()")
            self.gpib_2657A.send_Command("node[2].smua.measure.nplc = 1")
            self.gpib_2657A.send_Command("node[2].smua.measure.autorangei = smua.AUTORANGE_ON")
            self.gpib_2657A.send_Command("node[2].smua.measure.count = 1")
            self.gpib_2657A.send_Command("node[2].smua.measure.delay = 0")
            self.gpib_2657A.send_Command("node[2].tsplink.trigger[0].stimulus = smua.trigger.MEASURE_COMPLETE_EVENT_ID")
            

            self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.clear()")
            self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.appendmode = 1")
            self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.collecttimestamps = 0")
            self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.fillmode = 0")


            self.gpib_2657A.send_Command("node[2].smua.source.func = smua.OUTPUT_DCVOLTS")
            self.gpib_2657A.send_Command("node[2].smua.source.offmode = smua.OUTPUT_ZERO")
            self.gpib_2657A.send_Command("node[2].smua.source.levelv = 0")
            self.gpib_2657A.send_Command("node[2].smua.source.rangev = 200e-3")
            self.gpib_2657A.send_Command("node[2].smua.source.limiti = 1e-9")
            


            self.gpib_2657A.send_Command("node[2].smua.source.output = 1")
            self.gpib_2657A.send_Command("node[1].smua.source.output = 1")
            

            self.gpib_2657A.send_Command("node[1].display.screen = display.SMUA")
            self.gpib_2657A.send_Command("node[1].display.smua.measure.func = display.MEASURE_DCVOLTS")
            
            self.gpib_2657A.send_Command("node[2].display.screen = display.SMUA")
            self.gpib_2657A.send_Command("node[2].display.smua.measure.func = display.MEASURE_DCAMPS")
            

            
            self.gpib_2657A.send_Command("delay(1)")

            
            
            self.gpib_2657A.send_Command("test_time={}".format(test_time))
            self.gpib_2657A.send_Command("over_current={}".format(over_current))
            self.gpib_2657A.send_Command("max_current=0")
            
            self.gpib_2657A.send_Command("timer.reset()")
            #While loop
            self.gpib_2657A.send_Command("while not_oc and not_time_up do")

            #Measurement Current & Voltage
            self.gpib_2657A.send_Command("voltage_data=node[1].smua.measure.v()")
            self.gpib_2657A.send_Command("current_data=node[2].smua.measure.i()")

            #Waitting Measurement complete
            self.gpib_2657A.send_Command("tsplink.trigger[0].wait(10)")
            
            #Max Current Check
            self.gpib_2657A.send_Command("if current_data>max_current then")
            self.gpib_2657A.send_Command("max_current=current_data")
            self.gpib_2657A.send_Command("end")

            #Over current Check
            self.gpib_2657A.send_Command("if current_data>over_current then")
            self.gpib_2657A.send_Command("not_oc=0")
            self.gpib_2657A.send_Command("else")
            self.gpib_2657A.send_Command("not_oc=1")
            self.gpib_2657A.send_Command("end")

            #Times up Check
            self.gpib_2657A.send_Command("if timer.measure.t()>test_time then")
            self.gpib_2657A.send_Command("not_time_up=0")
            self.gpib_2657A.send_Command("else")
            self.gpib_2657A.send_Command("not_time_up=1")
            self.gpib_2657A.send_Command("end")
            
            self.gpib_2657A.send_Command("end")
            #While loop end

            self.gpib_2657A.send_Command("node[1].smua.source.output = 0")
            self.gpib_2657A.send_Command("node[1].smua.reset()")
            self.gpib_2657A.send_Command("node[2].smua.source.output = 0")
            self.gpib_2657A.send_Command("node[2].smua.reset()")

            #check overcurrent is happened or not
            self.gpib_2657A.send_Command("if not current_data then")
                #Over current Fail
            self.gpib_2657A.send_Command("node[1].display.clear()")
            self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[1].display.settext(\"Fail \")")
            self.gpib_2657A.send_Command("node[2].display.clear()")
            self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[2].display.settext(\"Fail \")")

            self.gpib_2657A.send_Command("else")
                #Time up Success
            self.gpib_2657A.send_Command("node[1].display.clear()")
            self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[1].display.settext(\"Pass \")")
            self.gpib_2657A.send_Command("node[2].display.clear()")
            self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[2].display.settext(\"Pass \")")

            self.gpib_2657A.send_Command("end")

            self.gpib_2657A.send_Command("node[1].display.setcursor(2, 1)")
            self.gpib_2657A.send_Command("node[1].text=string.format('Max Current = %f',max_current)")
            self.gpib_2657A.send_Command("node[1].display.settext(node[1].text)")
            self.gpib_2657A.send_Command("node[2].display.setcursor(2, 1)")
            self.gpib_2657A.send_Command("node[2].display.settext(node[1].text)")

            self.gpib_2657A.send_Command("beeper.beep(0.2, 2400)")
            self.gpib_2657A.send_Command("delay(0.3)")
            self.gpib_2657A.send_Command("beeper.beep(0.2, 2400)")
            self.gpib_2657A.send_Command("delay(0.3)")
            self.gpib_2657A.send_Command("beeper.beep(0.2, 2400)")

            self.gpib_2657A.send_Command("endscript")

            self.gpib_2657A.send_Command("Noise_Measurement.run()")

    def data_stream_work(self):
        #self.data_stream_start=False
        while self.data_stream_start:
            #return random.random()
            datapackage=Single_data_unitPackage(
                    time=random.random(),
                     count=random.random(),
                     Temperature=random.random(),
                     voltage=random.random(),
                     current=random.random(),
                     resistance=random.random(),
                     resistivity=random.random(),
                )
            self.queuePool["testDataQueue"].put(datapackage)
            self.queuePool["GUI_DataQueue"].put(datapackage)

            

            time.sleep(0.01)

    def stop_data_stream(self):
        #get event Start Run Auto run
        self.eventPool["data_stream_stop"].wait()
        #clear  Start Run Auto run event
        self.eventPool["data_stream_stop"].clear()

        
        print("stop_data_stream")

        self.data_stream_start=False

        

    def start_data_stream(self):
        #get event Start Run Auto run
        self.eventPool["data_stream_start"].wait()
        #clear  Start Run Auto run event
        self.eventPool["data_stream_start"].clear()

        print("start_data_stream")

        self.data_stream_start=True
        data_stream_Thread = threading.Thread(target = self.data_stream_work,daemon=True)
        data_stream_Thread.start()



    def auto_Run_Start_Work(self):
        while 1:
            #get event Start Run Auto run
            self.eventPool["Auto Run Start"].wait()
            #clear  Start Run Auto run event
            self.eventPool["Auto Run Start"].clear()


            Modbus_Registor_Pool=self.memoryPool["Modbus Registor Pool - Registor"]
            System_memory=self.memoryPool["System memory"]
            Measurement_Pattern=self.memoryPool["Measurement Pattern"]
            

            #Prepare Main Path
            self.csv_manager.prepare_Mainfolder()

            if System_memory["評価試験"].getValue():
                mode=Test_profile_package.QC_Test
            else:
                mode=Test_profile_package.Costomer_Test


            #check pattern & step
            pattern_number=Modbus_Registor_Pool["実行PTN No."].getValue()
            step_number=Modbus_Registor_Pool["実行STEP No."].getValue()

            

            folder_name=""
            if step_number:
                test_pattern_number=Modbus_Registor_Pool["PTNData_{}_STEP_{}_測定パターン".format(pattern_number,step_number)].getValue()+1
                folder_name="{}℃".format(Modbus_Registor_Pool["PTNData_{}_STEP_{}_SV値".format(pattern_number,step_number)].getValue())
            else:
                test_pattern_number=Modbus_Registor_Pool["PTNData_{}_RT測定パターン".format(pattern_number)].getValue()+1
                folder_name="RT"

            test_step_count=Measurement_Pattern["PTNData_{}_実行STEP数".format(test_pattern_number)].getValue()

            step_list=[]
            if Measurement_Pattern["PTNData_{}_BG0測定時間".format(test_pattern_number)].getValue():
                step_list=range(0,test_step_count+1)
            else:
                step_list=range(1,test_step_count+1)

            for step in step_list:

                step_name=""
                if step==0:
                    step_name="BG0"
                    voltage=0
                    _time=0
                    bg_time=Measurement_Pattern["PTNData_{}_BG0測定時間".format(test_pattern_number)].getValue()
                    measuretype=["BG測定結果"]

                else:
                    step_name="測定NO-{}".format(step)
                    voltage=Measurement_Pattern["PTNData_{}_STEP_{}_電圧".format(test_pattern_number,step)].getValue()
                    bg_time=Measurement_Pattern["PTNData_{}_BG測定時間".format(test_pattern_number)].getValue()
                    _time=Measurement_Pattern["PTNData_{}_測定時間".format(test_pattern_number)].getValue()
                    measuretype=["抵抗測定結果","BG測定結果"]

                gas=Modbus_Registor_Pool["PTNData_{}_測定雰囲気".format(pattern_number)].getValue()

                if gas==1:
                    gas="大気"
                elif gas==2:
                    gas="真空"
                elif gas==4:
                    gas="N2置換"

                speed=Measurement_Pattern["PTNData_{}_speed".format(test_pattern_number)].getValue()
                if speed==0:
                    speed="Normal (1PLC)"
                elif speed==1:
                    speed="Hi Accuracy (10PLC)"

                filter=Measurement_Pattern["PTNData_{}_filter_type".format(test_pattern_number)].getValue()
                if filter==0:
                    filter="なし"
                elif filter==1:
                    filter="平均(repeating)"
                elif filter==2:
                    filter="移動平均(moving)"
                elif filter==3:
                    filter="中央値(Median)"


                profile=Test_profile_package(
                                    date=datetime.datetime.now(),
                                    folder_name=folder_name,
                                    file_name=step_name,
                                    mode=mode,
                                    gas=gas,
                                    number=System_memory["依頼測定番号"].getValue(),
                                    costomer=System_memory["依頼元"].getValue(),
                                    costomerName=System_memory["依頼者"].getValue(),
                                    meterialName=System_memory["試料名称"].getValue(),
                                    meterial=System_memory["材料"].getValue(),
                                    mainDia=System_memory["主電極径(mm)"].getValue(),
                                    innerDia=System_memory["ガード電極の内径(mm)"].getValue(),
                                    thinkness=System_memory["試料の厚さ(mm)"].getValue(),
                                    
                                    voltage=voltage,
                                    time=_time,
                                    time_sample=Measurement_Pattern["PTNData_{}_測定sampletime".format(test_pattern_number)].getValue(),
                                    bg_time=bg_time,
                                    bg_time_sample=Measurement_Pattern["PTNData_{}_BG測定sampletime".format(test_pattern_number)].getValue(),
                                    speed=speed,
                                    filter=filter,
                                    filter_count=Measurement_Pattern["PTNData_{}_filter_count".format(test_pattern_number)].getValue(),

                                )

                #Prepare Main Path
                self.csv_manager.prepare_CsvFile(profile)

                for type in measuretype:

                    #Prepare CSV Header
                    self.csv_manager.prepare_Record_Header(type)

                    #starting listen data arrive
                    self.csv_manager.startRecord_CsvFile()


                    self.start_data_stream()
                    self.stop_data_stream()
                    
                    #starting listen data arrive
                    self.csv_manager.stopRecord_CsvFile()
                    

            self.eventPool["Auto Run finish"].set()


            ##check if PLC is ok to start
            ##check if PLC is stop
            #if Modbus_Registor_Pool["運転可"].getValue() and Modbus_Registor_Pool["停止中"].getValue():

            #    #Tell PLC start pattern and PLC will reset this
            #    set_memorypool_register("Modbus Registor Pool - Registor","運転開始",1)
            
            #    #check if there is any test pattern at future pattern step
            #    operate_PTN_number=Modbus_Registor_Pool["実行PTN No.変更"].getValue()

            #    test_pattern_listInPTN=[]

            #    if Modbus_Registor_Pool["PTNData_{}_RT計測".format(operate_PTN_number)].getValue():
            #        test_pattern_listInPTN.append("RT")

            #    for step in range(1,Modbus_Registor_Pool["PTNData_{}_実行STEP数".format(operate_PTN_number)].getValue()+1):
            #        if Modbus_Registor_Pool["PTNData_{}_STEP_{}_STEP種類".format(operate_PTN_number,step)].getValue()==2:
            #            #this is a test pattern
            #            test_pattern=Modbus_Registor_Pool["PTNData_{}_STEP_{}_測定パターン".format(operate_PTN_number,step)].getValue()
            #            test_pattern_listInPTN.append(test_pattern)

            #    #print(test_pattern_listInPTN)
                
            #    Measurement_Pattern=self.memoryPool["Measurement Pattern"]
            #    #if yes
            #    for test_pattern_no in test_pattern_listInPTN:


            #        test_pattern=testlist()
            #        if test_pattern_no=="RT":
            #            #prepare test profile and send script to GPIB device
            #            test_pattern.active=Measurement_Pattern["PTNData_{}_パターン有効".format(test_pattern_no)].getValue(),
            #            test_pattern.BG0_test_time=Measurement_Pattern["PTNData_{}_BG0測定時間".format(test_pattern_no)].getValue(),
            #            test_pattern.BG_sampletime=Measurement_Pattern["PTNData_{}_BG測定sampletime".format(test_pattern_no)].getValue()
                            
            #        else:
            #            #prepare test profile and send script to GPIB device
                        
            #            test_pattern.name=Measurement_Pattern["PTNData_{}_名称".format(test_pattern_no)].getValue(),
            #            test_pattern.comment=Measurement_Pattern["PTNData_{}_註記".format(test_pattern_no)].getValue(),
            #            test_pattern.active=Measurement_Pattern["PTNData_{}_パターン有効".format(test_pattern_no)].getValue(),
            #            test_pattern.step_number=Measurement_Pattern["PTNData_{}_実行STEP数".format(test_pattern_no)].getValue(),
            #            test_pattern.test_time=Measurement_Pattern["PTNData_{}_測定時間".format(test_pattern_no)].getValue(),
            #            test_pattern.test_sampletime=Measurement_Pattern["PTNData_{}_測定sampletime".format(test_pattern_no)].getValue(),
            #            test_pattern.BG0_test_time=Measurement_Pattern["PTNData_{}_BG0測定時間".format(test_pattern_no)].getValue(),
            #            test_pattern.BG_test_time=Measurement_Pattern["PTNData_{}_BG測定時間".format(test_pattern_no)].getValue(),
            #            test_pattern.BG_sampletime=Measurement_Pattern["PTNData_{}_BG測定sampletime".format(test_pattern_no)].getValue()
                            
            #            units=[]
            #            for unit in range(1,test_pattern.step_number+1):
            #                unit=testUnit(
            #                    voltage=Measurement_Pattern["PTNData_{}_STEP_{}_電圧".format(test_pattern_no,unit)].getValue()
            #                    )
            #                units.append(unit)
            #            test_pattern.units=units



            #        #               - tell csv_manager get ready
            #        if test_pattern_no=="RT":
            #            test_folder_package=Test_folder_package([Test_folder_package.RT_stage,0])
            #            self.queuePool["subFolderMakeQueue"].put(test_folder_package)

            #        else:
            #            test_folder_package=Test_folder_package([Test_folder_package.Temp_stage,0])
            #            self.queuePool["subFolderMakeQueue"].put(test_folder_package)

            #        self.measurement_initial()
            #         #Tell PLC we had finish measurement test 
            #        set_memorypool_register("Modbus Registor Pool - Registor","測定終了",1)

            

    def GPIB_device_ScriptPrepare(self,voltage,test_time,sample_time):
        #reset all gpib device include TSP-Link device

        self.gpib_2657A.send_Command("reset()")
        self.gpib_2657A.send_Command("node[1].errorqueue.clear()")
        self.gpib_2657A.send_Command("node[2].errorqueue.clear()")
        self.gpib_2657A.send_Command("node[1].status.reset()")
        self.gpib_2657A.send_Command("node[2].status.reset()")
        self.gpib_2657A.send_Command("tsplink.reset()")
        self.gpib_2657A.send_Command("node[1].dataqueue.clear()")
        self.gpib_2657A.send_Command("node[1].display.clear()")
        self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
        self.gpib_2657A.send_Command("node[1].display.settext(\"Prepare\")")
        self.gpib_2657A.send_Command("node[1].display.setcursor(2, 1)")
        self.gpib_2657A.send_Command("node[1].display.setcursor(2, 1)")
        self.gpib_2657A.send_Command("node[1].display.settext(\"Wait to start PTN.1\")")
        self.gpib_2657A.send_Command("node[2].display.clear()")
        self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
        self.gpib_2657A.send_Command("node[2].display.settext(\"Prepare\")")
        self.gpib_2657A.send_Command("node[2].display.setcursor(2, 1)")
        self.gpib_2657A.send_Command("node[2].display.settext(\"Wait to start PTN.1\")")
        #prepare test pattern to script
        #send script to TSP-Link Master

        #-loadscript testProfile
        self.gpib_2657A.send_Command("loadscript testProfile")
        self.gpib_2657A.send_Command("tsplink.trigger[0].reset()")
        self.gpib_2657A.send_Command("tsplink.trigger[1].reset()")
        self.gpib_2657A.send_Command("tsplink.trigger[2].reset()")
        self.gpib_2657A.send_Command("tsplink.trigger[3].reset()")

        self.gpib_2657A.send_Command("node[1].smua.reset()")
        self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.clear()")
        self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.collecttimestamps = 1")
        self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.timestampresolution=0.000001")     #if total time is short then 70minute
        self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.timestampresolution=0.000010")     #if total time is bigger then 70minute
        self.gpib_2657A.send_Command("node[1].smua.trigger.initiate()")
        self.gpib_2657A.send_Command("node[1].smua.trigger.autoclear = 1")
        self.gpib_2657A.send_Command("node[1].smua.trigger.measure.i(smua.nvbuffer1)")
        self.gpib_2657A.send_Command("node[1].smua.trigger.measure.stimulus=tsplink.trigger[1].EVENT_ID")
        self.gpib_2657A.send_Command("node[1].tsplink.trigger[2].stimulus=smua.trigger.MEASURE_COMPLETE_EVENT_ID")
            
        self.gpib_2657A.send_Command("node[2].smua.reset()")
        self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.clear()")
        self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.collecttimestamps = 1")
        self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.timestampresolution=0.000001")     #if total time is short then 70minute
        self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.timestampresolution=0.000010")    #if total time is bigger then 70minute
        self.gpib_2657A.send_Command("node[2].smua.trigger.initiate()")
        self.gpib_2657A.send_Command("node[2].smua.trigger.autoclear = 1")
        self.gpib_2657A.send_Command("node[2].smua.trigger.measure.v(smua.nvbuffer1)")
        self.gpib_2657A.send_Command("node[2].smua.trigger.measure.stimulus=tsplink.trigger[1].EVENT_ID")
        self.gpib_2657A.send_Command("node[2].tsplink.trigger[3].stimulus=smua.trigger.MEASURE_COMPLETE_EVENT_ID")

        self.gpib_2657A.send_Command("node[1].trigger.timer[0].reset()")                                                                         #//Set sync timer
        self.gpib_2657A.send_Command("node[1]trigger.timer[0].clear()")
        self.gpib_2657A.send_Command("node[1]trigger.timer[0].count= 測定回数")
        self.gpib_2657A.send_Command("node[1]trigger.timer[0].delay= サンプリング周期")
        self.gpib_2657A.send_Command("node[1]trigger.timer[0].stimulus=tsplink.trigger[0].EVENT_ID")
        self.gpib_2657A.send_Command("node[1]tsplink.trigger[1].stimulus=trigger.timer[0].EVENT_ID")

        self.gpib_2657A.send_Command("node[1]trigger.blender[1].reset()")                                                                      #//Set blender
        self.gpib_2657A.send_Command("node[1]trigger.blender[1].stimulus[1]=tsplink.trigger[2].EVENT_ID")
        self.gpib_2657A.send_Command("node[1]trigger.blender[1].stimulus[2]=tsplink.trigger[3].EVENT_ID")

        self.gpib_2657A.send_Command("node[1].smua.source.func = smua.OUTPUT_DCVOLTS")                   #//output high voltage
        self.gpib_2657A.send_Command("node[1].smua.source.autorangev = smua.AUTORANGE_ON")
        self.gpib_2657A.send_Command("node[1].smua.source.levelv = 測定電圧")
        self.gpib_2657A.send_Command("node[1].smua.source.limiti = 20e-3 ")
        self.gpib_2657A.send_Command("node[1].smua.measure.rangei = 20e-3")
        self.gpib_2657A.send_Command("node[1].smua.source.output = smua.OUTPUT_ON")

        self.gpib_2657A.send_Command("node[1].tsplink.trigger[0].assert()")                                                           #//start measurement loop

        self.gpib_2657A.send_Command("for count 1,測定回数 do")
        self.gpib_2657A.send_Command("  node[1].trigger.blender[1].wait()")
        self.gpib_2657A.send_Command("  node[1].current_name=node[1].smua.nvbuffer1.measurefunctions[N")
        self.gpib_2657A.send_Command("  node[1].current_time=node[1].smua.nvbuffer1.timestamps[count]")
        self.gpib_2657A.send_Command("  node[1].current_value=node[1].smua.nvbuffer1.readings[count]")
        self.gpib_2657A.send_Command("  node[1].voltage_name=node[2].smua.nvbuffer1.measurefunctions[N]")
        self.gpib_2657A.send_Command("  node[1].voltage_time=node[2].smua.nvbuffer1.timestamps[count]")
        self.gpib_2657A.send_Command("  node[1].voltage_value=node[2].smua.nvbuffer1.readings[count]")

        self.gpib_2657A.send_Command("  node[1].sendItem={count,current_name,current_time,current_value,voltage_name,voltage_time,voltage_value}")

        self.gpib_2657A.send_Command("  node[1].print(sendItem)")
        self.gpib_2657A.send_Command("end)")

        self.gpib_2657A.send_Command("node[1].smua.source.output = smua.OUTPUT_OFF")                         #//TurnOFF high voltage
        self.gpib_2657A.send_Command("node[1].print(\"finish\")")
        self.gpib_2657A.send_Command("endscript")

    def GPIB_device_startScript(self):
        #send GPIB command to TSP-Master
        self.gpib_2657A.send_Command("testProfile.run()")

    def GPIB_data_retrive_Work(self):
        #send GPIB command to get Voltage and Current
        self.measurement_data=[]
        while 1:
            result,error_message=self.gpib_2657A.read_Command()
            if not error_message:
                if result==-"finish":
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

                    data_pachage=Single_data_unitPackage(
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

