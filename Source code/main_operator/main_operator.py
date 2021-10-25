# -*- coding: utf-8 -*-
from gpib_manager import GPIB_device_2635B,GPIB_device_2657A,GPIB_Driver,GPIB_package
import threading
import time

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
                 time=0,
                 Temperature=0,
                 voltage=0,
                 current=0,
                 resistance=0,
                 ):
        self.time=time
        self.Temperature=Temperature
        self.voltage=voltage
        self.current=current
        self.resistance=resistance



def operator_thread(memoryPool,queuePool,eventPool):
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


        gpib_2635B=GPIB_device_2635B(memoryPool,queuePool)
        gpib_2657A=GPIB_device_2657A(memoryPool,queuePool)


    def auto_Run_Start():
        self.eventPool["Auto Run Start"].wait()
        #get event Start Run Auto run

        #check if PLC is ok to start
        #check if PLC is stop

        #Tell PLC start pattern and PLC will reset this

            #check if there is any test pattern at future pattern step
            #if yes
                #prepare test profile and send script to GPIB device
                #                                                                                     
                #Wait PLC tell us if we can start to test
                #start test 
                #               - send trigger to GPIB device to start script
                #               - initial measure data retrive Thread
                #               - tell csv_manager get ready
                #Tell PLC we had finish measurement test 
            #if no
                #wait PLC tell us all pattern is finish

    def GPIB_data_retrive_Work(self):
        #send GPIB command to get Voltage and Current

        #-node[1].print(dataqueue.next())
        #save the result back to array

        pass

    def GPIB_device_prepare(self):
        #reset all gpib device include TSP-Link device
            #-reset()
            #-errorqueue.clear()
            #-status.reset()
            #-tsplink.reset()
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
            #-content
            #-endscript
        pass

    def GPIB_device_startScript(self):
        #send GPIB command to TSP-Master
        #-testProfile.run()
        pass

    def csv_prepare(self):

        #send subFolderMake command to csv_manager and sub folder should be ready
        #put subFolderMake command to queue
        self.queuePool["subFolderMakeQueue"].put()

