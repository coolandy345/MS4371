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

                 ノイズ測定判定基準=0,
                 ノイズ測定時間=0,
                 ノイズ測定電圧=0

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

        self.ノイズ測定判定基準=ノイズ測定判定基準
        self.ノイズ測定時間=ノイズ測定時間
        self.ノイズ測定電圧=ノイズ測定電圧


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

        self.temperature=0
        
        self.csv_manager=Csv_manager(memoryPool,queuePool,eventPool)

        #self.gpib_2635B=GPIB_device_2635B(memoryPool,queuePool)
        self.gpib_2657A=GPIB_device_2657A(memoryPool,queuePool)

        self.gpib_2657A_control=False

        auto_Run_Start_Thread = threading.Thread(target = self.auto_Run_Start_Work,daemon=True)
        auto_Run_Start_Thread.start()

        start_noise_measurement_Thread = threading.Thread(target = self.start_noise_measurement,daemon=True)
        start_noise_measurement_Thread.start()

        get_temp_Thread = threading.Thread(target = self.get_temp_Work,daemon=True)
        get_temp_Thread.start()


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
        

    def get_temp_Work(self):
        while 1:
            time.sleep(0.2)
            self.temperature=self.memoryPool["Modbus Registor Pool - Registor"]["温度PV値"].getValue()

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
        while not self.eventPool["Test approve"].wait(timeout=0.1):
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

        while not self.eventPool["GPIB_Test_Finish"].wait(timeout=0.1):
            #If we got stop signal
            if self.stop:
                return False
        self.eventPool["GPIB_Test_Finish"].clear()

    def stop_measurement(self):
        self.script_stop=False
        #get event Start Run Auto run
        self.eventPool["Measure Stop"].wait()
        #clear  Start Run Auto run event
        self.eventPool["Measure Stop"].clear()
        self.script_stop=True

    def start_noise_measurement(self):
        
        while 1:
            #get event Start Run Auto run
            self.eventPool["Noise Measure Start"].wait()
            #clear  Start Run Auto run event
            self.eventPool["Noise Measure Start"].clear()

            self.noise_measurement_voltage=self.memoryPool["System memory"]["Noise_Measurement_Voltage"].getValue()
            self.noise_measurement_current=1e-12*self.memoryPool["System memory"]["Noise_Measurement_Current"].getValue()
            self.noise_measurement_time=60*self.memoryPool["System memory"]["Noise_Measurement_Time"].getValue()

            print("start_noise_measurement",self.noise_measurement_voltage,self.noise_measurement_current,self.noise_measurement_time)

            stop_noise_measurement_Thread = threading.Thread(target = self.stop_measurement,daemon=True)
            stop_noise_measurement_Thread.start()

            self.script_stop=False

            self.gpib_2657A.send_Command("abort")
            self.gpib_2657A.send_Command("*CLS")
            self.gpib_2657A.send_Command("reset()")
            self.gpib_2657A.send_Command("node[1].smua.reset()")
            self.gpib_2657A.send_Command("node[2].smua.reset()")
            
            self.gpib_2657A.send_Command("node[2].display.clear()")
            self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[2].display.settext(\"Uploading script\")")

            self.gpib_2657A.send_Command("node[1].display.clear()")
            self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[1].display.settext(\"Uploading script\")")
            
            
            self.gpib_2657A.send_Command("loadscript Noise_Measurement")
            

            self.gpib_2657A.send_Command("reset()")
            self.gpib_2657A.send_Command("node[1].beeper.beep(0.1, 2400)")

            self.gpib_2657A.send_Command("node[2].display.clear()")
            self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[2].display.settext(\"Noise Test Start\")")

            self.gpib_2657A.send_Command("node[1].display.clear()")
            self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[1].display.settext(\"Noise Test Start\")")

            self.gpib_2657A.send_Command("delay(1)")   #10
            
            
            self.gpib_2657A.send_Command("node[1].display.clear()")
            self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[1].display.settext(\"Setting...\")")
            
            self.gpib_2657A.send_Command("node[1].display.setcursor(2, 1)")
            self.gpib_2657A.send_Command("node[1].display.settext(\"Voltage... {}\")".format(Quantity(float(self.noise_measurement_voltage),"V").render(prec=4)))

            self.gpib_2657A.send_Command("node[2].display.clear()")
            self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("node[2].display.settext(\"Setting...\")")
            
            
            self.gpib_2657A.send_Command("node[1].smua.reset()")
            self.gpib_2657A.send_Command("node[1].smua.measure.nplc = 1")   #20
            self.gpib_2657A.send_Command("node[1].smua.measure.autorangev = smua.AUTORANGE_ON")
            self.gpib_2657A.send_Command("node[1].smua.measure.count = 1")
            self.gpib_2657A.send_Command("node[1].smua.measure.delay = 0")

            self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.clear()")
            self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.appendmode = 1")
            self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.collecttimestamps = 1")
            self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.fillmode = 0")

            self.gpib_2657A.send_Command("node[1].smua.source.func = smua.OUTPUT_DCVOLTS")
            self.gpib_2657A.send_Command("node[1].smua.source.offmode = smua.OUTPUT_ZERO")
            self.gpib_2657A.send_Command("node[1].smua.source.rangev = 1500")    #30
            self.gpib_2657A.send_Command("node[1].smua.source.levelv = {}".format(self.noise_measurement_voltage))
            self.gpib_2657A.send_Command("node[1].smua.source.limiti = 1e-6")

            
            self.gpib_2657A.send_Command("node[2].smua.reset()")
            self.gpib_2657A.send_Command("node[2].smua.measure.nplc = 1")
            self.gpib_2657A.send_Command("node[2].smua.measure.autorangei = smua.AUTORANGE_ON")
            self.gpib_2657A.send_Command("node[2].smua.measure.count = 1")
            self.gpib_2657A.send_Command("node[2].smua.measure.delay = 0")
            
            self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.clear()")
            self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.appendmode = 1")
            self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.collecttimestamps = 1")   #40
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
            self.gpib_2657A.send_Command("node[2].display.smua.measure.func = display.MEASURE_DCAMPS")   #50
            
            self.gpib_2657A.send_Command("test_time={}".format(self.noise_measurement_time))
            self.gpib_2657A.send_Command("over_current={}".format(self.noise_measurement_current))
            self.gpib_2657A.send_Command("under_current={}".format(-1*self.noise_measurement_current))
            self.gpib_2657A.send_Command("max_current=0")
            self.gpib_2657A.send_Command("min_current=0")

            self.gpib_2657A.send_Command("search_count=0")
            self.gpib_2657A.send_Command("search_index=1")
            self.gpib_2657A.send_Command("search_burst=2")

            self.gpib_2657A.send_Command("loop_start=true")
            self.gpib_2657A.send_Command("overcurrent=false")
            self.gpib_2657A.send_Command("undercurrent=false")

            
            self.gpib_2657A.send_Command("time_up=false")
            
            
            self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.clear()")
            self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.clear()")
            #While loop
            self.gpib_2657A.send_Command("while loop_start do")

            #Measurement Current & Voltage
            self.gpib_2657A.send_Command("  node[1].smua.measure.overlappedv(node[1].smua.nvbuffer1)")
            self.gpib_2657A.send_Command("  node[2].smua.measure.overlappedi(node[2].smua.nvbuffer1)")
            #Waitting Measurement complete
            self.gpib_2657A.send_Command("  waitcomplete()")
            self.gpib_2657A.send_Command("  voltage_data=node[1].smua.nvbuffer1.readings[node[1].smua.nvbuffer1.n]")
            self.gpib_2657A.send_Command("  current_data=node[2].smua.nvbuffer1.readings[node[2].smua.nvbuffer1.n]")
            self.gpib_2657A.send_Command("  current_time=node[2].smua.nvbuffer1.timestamps[node[2].smua.nvbuffer1.n]")


            #Times up Check
            self.gpib_2657A.send_Command("  if search_count>=search_burst then")
            self.gpib_2657A.send_Command("      printbuffer(search_index,node[2].smua.nvbuffer1.n,   node[1].smua.nvbuffer1.timestamps,   node[1].smua.nvbuffer1.statuses,  node[1].smua.nvbuffer1.readings,   node[2].smua.nvbuffer1.timestamps,   node[2].smua.nvbuffer1.statuses,  node[2].smua.nvbuffer1.readings) ")
            self.gpib_2657A.send_Command("      search_index=node[2].smua.nvbuffer1.n+1")
            self.gpib_2657A.send_Command("      search_count=0")
            self.gpib_2657A.send_Command("  else")   #70
            self.gpib_2657A.send_Command("      search_count=search_count+1")
            self.gpib_2657A.send_Command("  end")
            
            #Max Current record
            self.gpib_2657A.send_Command("  if current_data>max_current then")   #60
            self.gpib_2657A.send_Command("      max_current=current_data")
            self.gpib_2657A.send_Command("  end")

            #Min Current record
            self.gpib_2657A.send_Command("  if current_data<min_current then")   #60
            self.gpib_2657A.send_Command("      min_current=current_data")
            self.gpib_2657A.send_Command("  end")

            

            #Over current Check
            self.gpib_2657A.send_Command("  if current_data>over_current then")
            self.gpib_2657A.send_Command("      overcurrent=true")
            self.gpib_2657A.send_Command("  else")
            self.gpib_2657A.send_Command("      overcurrent=false")
            self.gpib_2657A.send_Command("  end")

            #Under current Check
            self.gpib_2657A.send_Command("  if current_data<under_current then")
            self.gpib_2657A.send_Command("      undercurrent=true")
            self.gpib_2657A.send_Command("  else")
            self.gpib_2657A.send_Command("      undercurrent=false")
            self.gpib_2657A.send_Command("  end")

            #Times up Check
            self.gpib_2657A.send_Command("  if current_time>test_time then")
            self.gpib_2657A.send_Command("      time_up=true")
            self.gpib_2657A.send_Command("  else")   #70
            self.gpib_2657A.send_Command("      time_up=false")
            self.gpib_2657A.send_Command("  end")

            self.gpib_2657A.send_Command("  if overcurrent or undercurrent or time_up then")

            
            self.gpib_2657A.send_Command("      if search_count>0 then")
            self.gpib_2657A.send_Command("          printbuffer(search_index,node[2].smua.nvbuffer1.n,   node[1].smua.nvbuffer1.timestamps,   node[1].smua.nvbuffer1.statuses,  node[1].smua.nvbuffer1.readings,   node[2].smua.nvbuffer1.timestamps,   node[2].smua.nvbuffer1.statuses,  node[2].smua.nvbuffer1.readings) ")
            self.gpib_2657A.send_Command("      end")
            self.gpib_2657A.send_Command("      break")
            self.gpib_2657A.send_Command("  end")

            self.gpib_2657A.send_Command("end")
            #While loop end

            self.gpib_2657A.send_Command("node[1].smua.source.output = 0")
            self.gpib_2657A.send_Command("node[1].smua.reset()")
            self.gpib_2657A.send_Command("node[2].smua.source.output = 0")
            self.gpib_2657A.send_Command("node[2].smua.reset()")


            #self.gpib_2657A.send_Command("printbuffer(1, node[2].smua.nvbuffer1.n, node[2].smua.nvbuffer1) ")

            

            #check overcurrent or  undercurrent is happened or not
            self.gpib_2657A.send_Command("if overcurrent then")
                #Over current Fail
            self.gpib_2657A.send_Command("  text=string.format(\"Fail | %.4e A\",max_current)")
            self.gpib_2657A.send_Command("  node[1].display.clear()")
            self.gpib_2657A.send_Command("  node[1].display.setcursor(1, 1)")   #80
            self.gpib_2657A.send_Command("  node[1].display.settext(text)")
            self.gpib_2657A.send_Command("  node[2].display.clear()")
            self.gpib_2657A.send_Command("  node[2].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("  node[2].display.settext(text)")

            self.gpib_2657A.send_Command("elseif undercurrent then")
                #under current Fail
            self.gpib_2657A.send_Command("  text=string.format(\"Fail | %.4e A\",min_current)")
            self.gpib_2657A.send_Command("  node[1].display.clear()")
            self.gpib_2657A.send_Command("  node[1].display.setcursor(1, 1)")   #80
            self.gpib_2657A.send_Command("  node[1].display.settext(text)")
            self.gpib_2657A.send_Command("  node[2].display.clear()")
            self.gpib_2657A.send_Command("  node[2].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("  node[2].display.settext(text)")


            self.gpib_2657A.send_Command("else")
                #Time up Success
            self.gpib_2657A.send_Command("  bigger=max_current+min_current")
            self.gpib_2657A.send_Command("  if bigger>=0 then")
            self.gpib_2657A.send_Command("      text=string.format(\"Pass | %.4e A\",max_current)")
            self.gpib_2657A.send_Command("  else")
            self.gpib_2657A.send_Command("      text=string.format(\"Pass | %.4e A\",min_current)")
            self.gpib_2657A.send_Command("  end")

            self.gpib_2657A.send_Command("  node[1].display.clear()")
            self.gpib_2657A.send_Command("  node[1].display.setcursor(1, 1)")
            self.gpib_2657A.send_Command("  node[1].display.settext(text)")
            self.gpib_2657A.send_Command("  node[2].display.clear()")
            self.gpib_2657A.send_Command("  node[2].display.setcursor(1, 1)")   #90
            self.gpib_2657A.send_Command("  node[2].display.settext(text)")

            self.gpib_2657A.send_Command("end")

            self.gpib_2657A.send_Command("print(\"finish\")")
            
            self.gpib_2657A.send_Command("if overcurrent or undercurrent then")
            self.gpib_2657A.send_Command("  print(\"fail\",max_current,min_current)")
            self.gpib_2657A.send_Command("else")
            self.gpib_2657A.send_Command("  print(\"pass\",max_current,min_current)")
            self.gpib_2657A.send_Command("end")



            self.gpib_2657A.send_Command("node[1].display.setcursor(2, 1)")
            self.gpib_2657A.send_Command("node[1].display.settext(\"Please press TRG confirm\")")


            self.gpib_2657A.send_Command("beeper.beep(0.2, 2400)")
            self.gpib_2657A.send_Command("delay(0.3)")
            self.gpib_2657A.send_Command("beeper.beep(0.2, 2400)")   #100
            self.gpib_2657A.send_Command("delay(0.3)")
            self.gpib_2657A.send_Command("beeper.beep(0.2, 2400)")

            
            self.gpib_2657A.send_Command("node[1].display.trigger.wait(300)")   #10
            self.gpib_2657A.send_Command("beeper.beep(0.2, 2400)")

            self.gpib_2657A.send_Command("node[1].display.screen = display.SMUA")
            self.gpib_2657A.send_Command("node[1].display.smua.measure.func = display.MEASURE_DCVOLTS")
            
            self.gpib_2657A.send_Command("node[2].display.screen = display.SMUA")
            self.gpib_2657A.send_Command("node[2].display.smua.measure.func = display.MEASURE_DCAMPS")   #50
            
            self.gpib_2657A.send_Command("reset()")
            self.gpib_2657A.send_Command("node[1].smua.reset()")
            self.gpib_2657A.send_Command("node[2].smua.reset()")

            self.gpib_2657A.send_Command("endscript")

            if not self.script_stop:
                self.gpib_2657A.send_Command("Noise_Measurement.run()")

            stop_noise_measurement_Thread = threading.Thread(target = self.data_retrive_Work,daemon=True)
            stop_noise_measurement_Thread.start()

    def data_retrive_Work(self):
        time.sleep(1)

        pass_="不合格"
        max_current=0
        min_current=0


        
        self.csv_manager.prepare_NoiseTestfolder()

        profile=Test_profile_package(
                                    date=datetime.datetime.now(),
                                    ノイズ測定判定基準=self.noise_measurement_current,
                                     ノイズ測定時間=self.noise_measurement_time/60,
                                     ノイズ測定電圧=self.noise_measurement_voltage,
                                )
        
        #Prepare Main Path
        self.csv_manager.prepare_NoiseTestCsvFile(profile)
        
        self.csv_manager.prepare_Record_Header("ノイズ測定")
        self.csv_manager.startRecord_CsvFile()
        
        
        while not self.script_stop:

            text=self.gpib_2657A.read_Command()

            if text[0]=="finish":
                self.gpib_2657A.send_Command("reset()")
                text=self.gpib_2657A.read_Command()

                data_list=[]
                for data in text[0].split("\t"):
                    data_list.append(data)

                self.csv_manager.result_NoiseTestCsvFile(data_list[0],data_list[1],data_list[2])
                


                print("stop_measurement")
                return
            elif text[0]:
                #print(text[0])
                data_list=[]

                data_package_list=[]

                for data in text[0].split(","):
                    data_list.append(float(data))

                index =0

                for count in range(0,int(len(data_list)/6)):
                    voltage_timestemp=data_list[index]
                    voltage_status=data_list[index+1]
                    voltage_value=data_list[index+2]
                    current_timestemp=data_list[index+3]
                    current_status=data_list[index+4]
                    current_value=data_list[index+5]

                    index+=6
                    if current_value!=0:
                        resistance=voltage_value/current_value
                    else:
                        resistance=0

                    datapackage=Single_data_unitPackage(
                        time=current_timestemp,
                         count=0,
                         Temperature=self.temperature,
                         voltage=voltage_value,
                         current=current_value,
                         resistance=resistance,
                         resistivity=0,
                    )

                    data_package_list.append(datapackage)
                    
                
                self.queuePool["testDataQueue"].put(datapackage)
                self.queuePool["GUI_DataQueue"].put(data_package_list)
                time.sleep(0.01)
            else:
                time.sleep(0.2)

        self.gpib_2657A.send_Command("abort")

        self.gpib_2657A.send_Command("node[1].display.clear()")
        self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
        self.gpib_2657A.send_Command("node[1].display.settext(\"Stop\")")

        self.gpib_2657A.send_Command("node[2].display.clear()")
        self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
        self.gpib_2657A.send_Command("node[2].display.settext(\"Stop\")")

        
        self.gpib_2657A.send_Command("*CLS")

        
        time.sleep(0.1)

        self.gpib_2657A.send_Command("beeper.beep(0.1, 2550)")
        time.sleep(0.1)
        self.gpib_2657A.send_Command("beeper.beep(0.1, 2550)")   #100
        time.sleep(0.1)
        self.gpib_2657A.send_Command("beeper.beep(0.1, 2550)")   #100
        time.sleep(0.1)

        time.sleep(1)

        self.gpib_2657A.send_Command("reset()")
        self.gpib_2657A.send_Command("node[1].smua.reset()")
        self.gpib_2657A.send_Command("node[2].smua.reset()")

        self.gpib_2657A.send_Command("node[1].display.screen = display.SMUA")
        self.gpib_2657A.send_Command("node[1].display.smua.measure.func = display.MEASURE_DCVOLTS")
            
        self.gpib_2657A.send_Command("node[2].display.screen = display.SMUA")
        self.gpib_2657A.send_Command("node[2].display.smua.measure.func = display.MEASURE_DCAMPS")   #50

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

            print("Auto Run Start 1")
            Modbus_Registor_Pool=self.memoryPool["Modbus Registor Pool - Registor"]
            System_memory=self.memoryPool["System memory"]
            Measurement_Pattern=self.memoryPool["Measurement Pattern"]
            

            #Prepare Main Path
            self.csv_manager.prepare_Mainfolder()
            
            print("Auto Run Start 2")

            if System_memory["評価試験"].getValue():
                mode=Test_profile_package.QC_Test
            else:
                mode=Test_profile_package.Costomer_Test


            #check pattern & step
            pattern_number=Modbus_Registor_Pool["実行PTN No."].getValue()
            step_number=Modbus_Registor_Pool["実行STEP No."].getValue()

            print("Auto Run Start 3")

            folder_name=""
            if step_number:
                test_pattern_number=Modbus_Registor_Pool["PTNData_{}_STEP_{}_測定パターン".format(pattern_number,step_number)].getValue()+1
                folder_name="{}℃_step_{}".format(Modbus_Registor_Pool["PTNData_{}_STEP_{}_SV値".format(pattern_number,step_number)].getValue(),step_number)
            else:
                test_pattern_number=Modbus_Registor_Pool["PTNData_{}_RT測定パターン".format(pattern_number)].getValue()+1
                folder_name="RT_step_0"

            test_step_count=Measurement_Pattern["PTNData_{}_実行STEP数".format(test_pattern_number)].getValue()

            step_list=[]
            if Measurement_Pattern["PTNData_{}_BG0測定時間".format(test_pattern_number)].getValue():
                step_list=range(0,test_step_count+1)
            else:
                step_list=range(1,test_step_count+1)
            print("Auto Run Start 4")
            for step in step_list:
                
                script_voltage=0
                script_time=0
                script_sample_time=0
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
                print("Auto Run Start 5")
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

                print("Auto Run Start 6")
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
                print("Auto Run Start 7")
                #Prepare Main Path
                self.csv_manager.prepare_CsvFile(profile)

                for type in measuretype:
                    print("Auto Run Start 8")
                    #Prepare CSV Header
                    self.csv_manager.prepare_Record_Header(type)

                    #starting listen data arrive
                    self.csv_manager.startRecord_CsvFile()
                    
                    if type=="抵抗測定結果":
                        script_voltage=voltage
                        script_time=_time
                        script_sample_time=Measurement_Pattern["PTNData_{}_測定sampletime".format(test_pattern_number)].getValue()
                    elif type=="BG測定結果":
                        script_voltage=0
                        script_time=bg_time
                        script_sample_time=Measurement_Pattern["PTNData_{}_BG測定sampletime".format(test_pattern_number)].getValue()

                    #------------------------------------------------------------------------------------------------------
                    print("start_normal_measurement",script_voltage,script_time,script_sample_time)

                    #stop_noise_measurement_Thread = threading.Thread(target = self.stop_measurement,daemon=True)
                    #stop_noise_measurement_Thread.start()
            
                    #self.gpib_2657A.send_Command("abort")
                    #self.gpib_2657A.send_Command("reset()")
                    #self.gpib_2657A.send_Command("node[1].smua.reset()")
                    #self.gpib_2657A.send_Command("node[2].smua.reset()")
                    #self.gpib_2657A.send_Command("*CLS")
            
                    #self.gpib_2657A.send_Command("node[2].display.clear()")
                    #self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
                    #self.gpib_2657A.send_Command("node[2].display.settext(\"Uploading script\")")

                    #self.gpib_2657A.send_Command("node[1].display.clear()")
                    #self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
                    #self.gpib_2657A.send_Command("node[1].display.settext(\"Uploading script\")")
            
            
                    #self.gpib_2657A.send_Command("loadscript Noise_Measurement")
            

                    #self.gpib_2657A.send_Command("reset()")
                    #self.gpib_2657A.send_Command("node[1].beeper.beep(0.1, 2400)")

                    #self.gpib_2657A.send_Command("node[2].display.clear()")
                    #self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
                    #self.gpib_2657A.send_Command("node[2].display.settext(\"Noise Test Start\")")

                    #self.gpib_2657A.send_Command("node[1].display.clear()")
                    #self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
                    #self.gpib_2657A.send_Command("node[1].display.settext(\"Noise Test Start\")")

                    #self.gpib_2657A.send_Command("delay(1)")   #10
            
            
                    #self.gpib_2657A.send_Command("node[1].display.clear()")
                    #self.gpib_2657A.send_Command("node[1].display.setcursor(1, 1)")
                    #self.gpib_2657A.send_Command("node[1].display.settext(\"Setting...\")")
            
                    #self.gpib_2657A.send_Command("node[1].display.setcursor(2, 1)")
                    #self.gpib_2657A.send_Command("node[1].display.settext(\"Voltage... {}\")".format(Quantity(float(self.noise_measurement_voltage),"V").render(prec=4)))

                    #self.gpib_2657A.send_Command("node[2].display.clear()")
                    #self.gpib_2657A.send_Command("node[2].display.setcursor(1, 1)")
                    #self.gpib_2657A.send_Command("node[2].display.settext(\"Setting...\")")
            
            
                    #self.gpib_2657A.send_Command("node[1].smua.reset()")
                    #self.gpib_2657A.send_Command("node[1].smua.measure.nplc = 1")   #20
                    #self.gpib_2657A.send_Command("node[1].smua.measure.autorangev = smua.AUTORANGE_ON")
                    #self.gpib_2657A.send_Command("node[1].smua.measure.count = 1")
                    #self.gpib_2657A.send_Command("node[1].smua.measure.delay = 0")

                    #self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.clear()")
                    #self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.appendmode = 1")
                    #self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.collecttimestamps = 1")
                    #self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.fillmode = 0")

                    #self.gpib_2657A.send_Command("node[1].smua.source.func = smua.OUTPUT_DCVOLTS")
                    #self.gpib_2657A.send_Command("node[1].smua.source.offmode = smua.OUTPUT_ZERO")
                    #self.gpib_2657A.send_Command("node[1].smua.source.rangev = 1500")    #30
                    #self.gpib_2657A.send_Command("node[1].smua.source.levelv = {}".format(self.noise_measurement_voltage))
                    #self.gpib_2657A.send_Command("node[1].smua.source.limiti = 1e-6")

            
                    #self.gpib_2657A.send_Command("node[2].smua.reset()")
                    #self.gpib_2657A.send_Command("node[2].smua.measure.nplc = 1")
                    #self.gpib_2657A.send_Command("node[2].smua.measure.autorangei = smua.AUTORANGE_ON")
                    #self.gpib_2657A.send_Command("node[2].smua.measure.count = 1")
                    #self.gpib_2657A.send_Command("node[2].smua.measure.delay = 0")
            
                    #self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.clear()")
                    #self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.appendmode = 1")
                    #self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.collecttimestamps = 1")   #40
                    #self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.fillmode = 0")


                    #self.gpib_2657A.send_Command("node[2].smua.source.func = smua.OUTPUT_DCVOLTS")
                    #self.gpib_2657A.send_Command("node[2].smua.source.offmode = smua.OUTPUT_ZERO")
                    #self.gpib_2657A.send_Command("node[2].smua.source.levelv = 0")
                    #self.gpib_2657A.send_Command("node[2].smua.source.rangev = 200e-3")
                    #self.gpib_2657A.send_Command("node[2].smua.source.limiti = 1e-9")

                    #self.gpib_2657A.send_Command("node[2].smua.source.output = 1")
                    #self.gpib_2657A.send_Command("node[1].smua.source.output = 1")
            
                    #self.gpib_2657A.send_Command("node[1].display.screen = display.SMUA")
                    #self.gpib_2657A.send_Command("node[1].display.smua.measure.func = display.MEASURE_DCVOLTS")
            
                    #self.gpib_2657A.send_Command("node[2].display.screen = display.SMUA")
                    #self.gpib_2657A.send_Command("node[2].display.smua.measure.func = display.MEASURE_DCAMPS")   #50
            
                    #self.gpib_2657A.send_Command("test_time={}".format(self.noise_measurement_time))
                    #self.gpib_2657A.send_Command("over_current={}".format(self.noise_measurement_current))
                    #self.gpib_2657A.send_Command("under_current={}".format(-1*self.noise_measurement_current))
                    #self.gpib_2657A.send_Command("max_current=0")
                    #self.gpib_2657A.send_Command("min_current=0")

                    #self.gpib_2657A.send_Command("search_count=0")
                    #self.gpib_2657A.send_Command("search_index=1")
                    #self.gpib_2657A.send_Command("search_burst=2")

                    #self.gpib_2657A.send_Command("loop_start=true")
                    #self.gpib_2657A.send_Command("overcurrent=false")
                    #self.gpib_2657A.send_Command("undercurrent=false")

            
                    #self.gpib_2657A.send_Command("time_up=false")
            
            
                    #self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.clear()")
                    #self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.clear()")
                    ##While loop
                    #self.gpib_2657A.send_Command("while loop_start do")

                    ##Measurement Current & Voltage
                    #self.gpib_2657A.send_Command("  node[1].smua.measure.overlappedv(node[1].smua.nvbuffer1)")
                    #self.gpib_2657A.send_Command("  node[2].smua.measure.overlappedi(node[2].smua.nvbuffer1)")
                    ##Waitting Measurement complete
                    #self.gpib_2657A.send_Command("  waitcomplete()")
                    #self.gpib_2657A.send_Command("  voltage_data=node[1].smua.nvbuffer1.readings[node[1].smua.nvbuffer1.n]")
                    #self.gpib_2657A.send_Command("  current_data=node[2].smua.nvbuffer1.readings[node[2].smua.nvbuffer1.n]")
                    #self.gpib_2657A.send_Command("  current_time=node[2].smua.nvbuffer1.timestamps[node[2].smua.nvbuffer1.n]")


                    ##Times up Check
                    #self.gpib_2657A.send_Command("  if search_count>=search_burst then")
                    #self.gpib_2657A.send_Command("      printbuffer(search_index,node[2].smua.nvbuffer1.n,   node[1].smua.nvbuffer1.timestamps,   node[1].smua.nvbuffer1.statuses,  node[1].smua.nvbuffer1.readings,   node[2].smua.nvbuffer1.timestamps,   node[2].smua.nvbuffer1.statuses,  node[2].smua.nvbuffer1.readings) ")
                    #self.gpib_2657A.send_Command("      search_index=node[2].smua.nvbuffer1.n+1")
                    #self.gpib_2657A.send_Command("      search_count=0")
                    #self.gpib_2657A.send_Command("  else")   #70
                    #self.gpib_2657A.send_Command("      search_count=search_count+1")
                    #self.gpib_2657A.send_Command("  end")
            
                    ##Max Current record
                    #self.gpib_2657A.send_Command("  if current_data>max_current then")   #60
                    #self.gpib_2657A.send_Command("      max_current=current_data")
                    #self.gpib_2657A.send_Command("  end")

                    ##Min Current record
                    #self.gpib_2657A.send_Command("  if current_data<min_current then")   #60
                    #self.gpib_2657A.send_Command("      min_current=current_data")
                    #self.gpib_2657A.send_Command("  end")

            

                    ##Over current Check
                    #self.gpib_2657A.send_Command("  if current_data>over_current then")
                    #self.gpib_2657A.send_Command("      overcurrent=true")
                    #self.gpib_2657A.send_Command("  else")
                    #self.gpib_2657A.send_Command("      overcurrent=false")
                    #self.gpib_2657A.send_Command("  end")

                    ##Under current Check
                    #self.gpib_2657A.send_Command("  if current_data<under_current then")
                    #self.gpib_2657A.send_Command("      undercurrent=true")
                    #self.gpib_2657A.send_Command("  else")
                    #self.gpib_2657A.send_Command("      undercurrent=false")
                    #self.gpib_2657A.send_Command("  end")

                    ##Times up Check
                    #self.gpib_2657A.send_Command("  if current_time>test_time then")
                    #self.gpib_2657A.send_Command("      time_up=true")
                    #self.gpib_2657A.send_Command("  else")   #70
                    #self.gpib_2657A.send_Command("      time_up=false")
                    #self.gpib_2657A.send_Command("  end")

                    #self.gpib_2657A.send_Command("  if overcurrent or undercurrent or time_up then")

            
                    #self.gpib_2657A.send_Command("      if search_count>0 then")
                    #self.gpib_2657A.send_Command("          printbuffer(search_index,node[2].smua.nvbuffer1.n,   node[1].smua.nvbuffer1.timestamps,   node[1].smua.nvbuffer1.statuses,  node[1].smua.nvbuffer1.readings,   node[2].smua.nvbuffer1.timestamps,   node[2].smua.nvbuffer1.statuses,  node[2].smua.nvbuffer1.readings) ")
                    #self.gpib_2657A.send_Command("      end")
                    #self.gpib_2657A.send_Command("      break")
                    #self.gpib_2657A.send_Command("  end")

                    #self.gpib_2657A.send_Command("end")
                    ##While loop end

                    #self.gpib_2657A.send_Command("node[1].smua.source.output = 0")
                    #self.gpib_2657A.send_Command("node[1].smua.reset()")
                    #self.gpib_2657A.send_Command("node[2].smua.source.output = 0")
                    #self.gpib_2657A.send_Command("node[2].smua.reset()")


                    ##self.gpib_2657A.send_Command("printbuffer(1, node[2].smua.nvbuffer1.n, node[2].smua.nvbuffer1) ")

            

                    ##check overcurrent or  undercurrent is happened or not
                    #self.gpib_2657A.send_Command("if overcurrent then")
                    #    #Over current Fail
                    #self.gpib_2657A.send_Command("  node[1].display.clear()")
                    #self.gpib_2657A.send_Command("  node[1].display.setcursor(1, 1)")   #80
                    #self.gpib_2657A.send_Command("  node[1].display.settext(\"Fail \")")
                    #self.gpib_2657A.send_Command("  node[2].display.clear()")
                    #self.gpib_2657A.send_Command("  node[2].display.setcursor(1, 1)")
                    #self.gpib_2657A.send_Command("  node[2].display.settext(\"Fail \")")

            
                    #self.gpib_2657A.send_Command("elseif undercurrent then")
                    #    #under current Fail
                    #self.gpib_2657A.send_Command("  node[1].display.clear()")
                    #self.gpib_2657A.send_Command("  node[1].display.setcursor(1, 1)")   #80
                    #self.gpib_2657A.send_Command("  node[1].display.settext(\"Fail \")")
                    #self.gpib_2657A.send_Command("  node[2].display.clear()")
                    #self.gpib_2657A.send_Command("  node[2].display.setcursor(1, 1)")
                    #self.gpib_2657A.send_Command("  node[2].display.settext(\"Fail \")")


                    #self.gpib_2657A.send_Command("else")
                    #    #Time up Success
                    #self.gpib_2657A.send_Command("  node[1].display.clear()")
                    #self.gpib_2657A.send_Command("  node[1].display.setcursor(1, 1)")
                    #self.gpib_2657A.send_Command("  node[1].display.settext(\"Pass \")")
                    #self.gpib_2657A.send_Command("  node[2].display.clear()")
                    #self.gpib_2657A.send_Command("  node[2].display.setcursor(1, 1)")   #90
                    #self.gpib_2657A.send_Command("  node[2].display.settext(\"Pass \")")

                    #self.gpib_2657A.send_Command("end")

                    #self.gpib_2657A.send_Command("print(\"finish\")")
            
                    #self.gpib_2657A.send_Command("if overcurrent or undercurrent then")
                    #self.gpib_2657A.send_Command("  print(\"fail\",max_current,min_current)")
                    #self.gpib_2657A.send_Command("else")
                    #self.gpib_2657A.send_Command("  print(\"pass\",max_current,min_current)")
                    #self.gpib_2657A.send_Command("end")


                    #self.gpib_2657A.send_Command("node[1].display.setcursor(2, 1)")

                    #self.gpib_2657A.send_Command("bigger=max_current+min_current")
                    #self.gpib_2657A.send_Command("if bigger>=0 then")
                    #self.gpib_2657A.send_Command("  text=string.format(\"Max current = %e A\",max_current)")
                    #self.gpib_2657A.send_Command("else")
                    #self.gpib_2657A.send_Command("  text=string.format(\"Max current = %e A\",min_current)")
                    #self.gpib_2657A.send_Command("end")

                    #self.gpib_2657A.send_Command("node[1].display.settext(text)")
                    #self.gpib_2657A.send_Command("node[2].display.setcursor(2, 1)")
                    #self.gpib_2657A.send_Command("node[2].display.settext(text)")

                    #self.gpib_2657A.send_Command("beeper.beep(0.2, 2400)")
                    #self.gpib_2657A.send_Command("delay(0.3)")
                    #self.gpib_2657A.send_Command("beeper.beep(0.2, 2400)")   #100
                    #self.gpib_2657A.send_Command("delay(0.3)")
                    #self.gpib_2657A.send_Command("beeper.beep(0.2, 2400)")

            
                    #self.gpib_2657A.send_Command("delay(5)")   #10

                    #self.gpib_2657A.send_Command("endscript")

                    #if not self.script_stop:
                    #    self.gpib_2657A.send_Command("Noise_Measurement.run()")


                    ##------------------------------------------------------------------------------------------------------

                    #while not self.script_stop:

                    #    text=self.gpib_2657A.read_Command()

                    #    if text[0]=="finish":
                    #        self.gpib_2657A.send_Command("reset()")
                    #        text=self.gpib_2657A.read_Command()

                    #        data_list=[]
                    #        for data in text[0].split("\t"):
                    #            data_list.append(data)

                    #        self.csv_manager.result_NoiseTestCsvFile(data_list[0],data_list[1],data_list[2])
                
                    #        break
                    #    elif text[0]:
                    #        #print(text[0])
                    #        data_list=[]

                    #        data_package_list=[]

                    #        for data in text[0].split(","):
                    #            data_list.append(float(data))

                    #        index =0

                    #        for count in range(0,int(len(data_list)/6)):
                    #            voltage_timestemp=data_list[index]
                    #            voltage_status=data_list[index+1]
                    #            voltage_value=data_list[index+2]
                    #            current_timestemp=data_list[index+3]
                    #            current_status=data_list[index+4]
                    #            current_value=data_list[index+5]

                    #            index+=6
                    #            if current_value!=0:
                    #                resistance=voltage_value/current_value
                    #            else:
                    #                resistance=0

                    #            datapackage=Single_data_unitPackage(
                    #                time=current_timestemp,
                    #                 count=0,
                    #                 Temperature=self.temperature,
                    #                 voltage=voltage_value,
                    #                 current=current_value,
                    #                 resistance=resistance,
                    #                 resistivity=0,
                    #            )

                    #            data_package_list.append(datapackage)
                    
                
                    #        self.queuePool["testDataQueue"].put(datapackage)
                    #        self.queuePool["GUI_DataQueue"].put(data_package_list)
                    #        time.sleep(0.01)
                    #    else:
                    #        time.sleep(0.2)

                    #print("stop_measurement")
                    #self.gpib_2657A.send_Command("abort")
                    #self.gpib_2657A.send_Command("reset()")
                    #self.gpib_2657A.send_Command("node[1].smua.reset()")
                    #self.gpib_2657A.send_Command("node[2].smua.reset()")

                    #self.gpib_2657A.send_Command("node[2].smua.source.output = 0")
                    #self.gpib_2657A.send_Command("node[1].smua.source.output = 0")
                    #self.gpib_2657A.send_Command("*CLS")
                    
                    
                    #starting listen data arrive
                    self.csv_manager.stopRecord_CsvFile()
                    

            self.eventPool["Auto Run finish"].set()



            

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
        self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.collectsourcevalues = 1")
        self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.collecttimestamps = 1")
        self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.timestampresolution=0.000001")     #if total time is short then 70minute
        #self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.timestampresolution=0.000010")     #if total time is bigger then 70minute
        self.gpib_2657A.send_Command("node[1].smua.trigger.initiate()")
        self.gpib_2657A.send_Command("node[1].smua.trigger.autoclear = 1")
        self.gpib_2657A.send_Command("node[1].smua.trigger.measure.i(smua.nvbuffer1)")
        self.gpib_2657A.send_Command("node[1].smua.trigger.measure.stimulus=tsplink.trigger[1].EVENT_ID")
        self.gpib_2657A.send_Command("node[1].tsplink.trigger[2].stimulus=smua.trigger.MEASURE_COMPLETE_EVENT_ID")
            
        self.gpib_2657A.send_Command("node[2].smua.reset()")
        self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.clear()")
        self.gpib_2657A.send_Command("node[1].smua.nvbuffer1.collectsourcevalues = 1")
        self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.collecttimestamps = 1")
        self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.timestampresolution=0.000001")     #if total time is short then 70minute
        #self.gpib_2657A.send_Command("node[2].smua.nvbuffer1.timestampresolution=0.000010")    #if total time is bigger then 70minute
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

