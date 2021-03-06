# -*- coding: utf-8 -*-
from multiprocessing import Manager
import threading
import time
import os
from operator import *
import csv
import sys
import copy
from main_operator import *
from gui_main.qt_core import *
from gui_main.gui.widgets.py_dialog import *
from registor_manager import *
import datetime
import shutil
import math


class Csv_manager():
    def __init__(self,
                 PoolSemaphore,
                 memoryPool,
                 queuePool,
                 eventPool
                 ):
        self.PoolSemaphore=PoolSemaphore
        self.memoryPool=memoryPool
        self.queuePool=queuePool
        self.eventPool=eventPool

        self.dataRecord_Start=False

        self.main_folder_path=""
        self.csvPath=""

        #reset_Thread = threading.Thread(target = self.reset_Work,daemon=True)
        #reset_Thread.start()

    def startRecord_Manual_CsvFile(self):
        print("startRecord_manual_CsvFile")
        self.dataRecord_Start=True
        Record_manual_Thread = threading.Thread(target = self.record_manual_Work,daemon=True)
        Record_manual_Thread.start()

    def record_manual_Work(self):
        print("record_manual_Work has start")
        
        while self.dataRecord_Start:
            try:
                getItem=self.queuePool["testDataQueue"].get(timeout=0.1)



                with open(self.csv, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([   "{:0>7d}".format(getItem.count),
                                                "{:.3f}".format(getItem.time),
                                                "{:0>3d}".format(getItem.Temperature),
                                                "{:+.5e}".format(getItem.voltage),
                                                "{:+.5e}".format(getItem.current),
                                                "{:+.5e}".format(getItem.resistance),
                                                "{:+.5e}".format(getItem.resistivity)])
                    
            except:
                pass
        print("record_manual_Work has stop")


    def startRecord_CsvFile(self):
        print("startRecord_CsvFile")
        self.dataRecord_Start=True
        Record_Thread = threading.Thread(target = self.record_Work,daemon=True)
        Record_Thread.start()

    

    def record_Work(self):
        print("record_Work has start")
        while self.dataRecord_Start:
            try:
                getItem=self.queuePool["testDataQueue"].get(timeout=0.1)



                with open(self.csv, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([   "{:0>7d}".format(getItem.count),
                                                "{:.3f}".format(getItem.time),
                                                "{:0>3d}".format(getItem.Temperature),
                                                "{:+.5e}".format(getItem.voltage),
                                                "{:+.5e}".format(getItem.current),
                                                "{:+.5e}".format(getItem.resistance),
                                                "{:+.5e}".format(getItem.resistivity)])
                    
            except:
                pass
        print("record_Work has stop")

    def stopRecord_CsvFile(self):
        self.dataRecord_Start=False

    def prepare_NoiseTestCsvFile(self,profile):

        self.profile=profile

        self.csv = os.path.join(self.main_folder_path, "??????????????????????????????.csv")
        with open(self.csv, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(['??????????????????', self.profile.date])
            writer.writerow(['????????????(V)', self.profile.noise_testVoltage])
            writer.writerow(['????????????????????????(A)', self.profile.noise_passLevel])
            writer.writerow(['????????????(min)', self.profile.noise_testTime])


    def prepare_Manual_Single_TestCsvFile(self,profile):

        self.profile=profile

        self.csv = os.path.join(self.main_folder_path, "???????????????????????????.csv")
        with open(self.csv, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(['?????????', self.profile.date])
            writer.writerow(['????????????', self.profile.number])
            if self.profile.mode==2:
                writer.writerow(['?????????', self.profile.costomer])
                writer.writerow(['?????????', self.profile.costomerName])
            writer.writerow(['????????????', self.profile.meterialName])
            writer.writerow(['??????', self.profile.meterial])
            writer.writerow(['????????????(mm)', self.profile.mainDia])
            writer.writerow(['????????????????????????(mm)', self.profile.innerDia])
            writer.writerow(['????????????(mm2)', (((float(self.profile.mainDia)+float(self.profile.innerDia))/2)/2)*(((float(self.profile.mainDia)+float(self.profile.innerDia))/2)/2)*math.pi])
            writer.writerow(['???????????????(mm)', self.profile.thinkness])
            writer.writerow(['????????????(V)', self.profile.voltage])
            writer.writerow("")
            System_memory=self.memoryPool["System memory"]

            if System_memory["AvgHelper_Record_Enabled"].getValue():

                avarage_numbers=0
                avarage_data=0
                got_avarage=False
                for index in range(1,9):
                    if System_memory["AvgHelper_Enable_{}".format(index)].getValue():

                        avarage_numbers+=1
                        avarage_data+=System_memory["AvgHelper_Value_{}".format(index)].getValue()

                        if not got_avarage:
                            got_avarage=True

                        writer.writerow(['?????????'+self._123_to_abc(index),System_memory["AvgHelper_Value_{}".format(index)].getValue()])
                    else:
                        writer.writerow(['?????????'+self._123_to_abc(index),"?????????"])

                if got_avarage:
                    writer.writerow(['???????????????', avarage_data/avarage_numbers])
                    got_avarage=True

                
                writer.writerow("")

    def result_NoiseTestCsvFile(self,text,max,min):
        print("result_NoiseTestCsvFile",text,max,min)
        temp_list=[]
        with open(self.csv) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                temp_list.append(row)

        with open(self.csv, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)
            writer.writerow(['????????????',str(text)])
            writer.writerow(['????????????(A)',str(max)])
            writer.writerow(['????????????(A)',str(min)])
            writer.writerow("")

            for row in temp_list:
                writer.writerow(row)



    
    def prepare_NoiseTestfolder(self):

        System_memory=self.memoryPool["System memory"]
        Modbus_Registor_Pool=self.memoryPool["Modbus Registor Pool - Registor"]

        basepath = "C:/????????????????????????"
        try:
            os.mkdir(basepath)
        except FileExistsError:
            pass

        # Create target Year Directory
        try:
            path = os.path.join(basepath, "?????????????????????")
            os.mkdir(path)
        except FileExistsError:
            pass

        now=datetime.datetime.now()
        try:
            path = os.path.join(path, str("{}???_{}???_{}???_{}???_{}???_{}???".format(now.year,now.month,now.day,now.hour,now.minute,now.second)))
            os.mkdir(path)
        except FileExistsError:
            pass

        self.main_folder_path=path

    def prepare_ManualTest_Mainfolder(self):
        
        System_memory=self.memoryPool["System memory"]
        Modbus_Registor_Pool=self.memoryPool["Modbus Registor Pool - Registor"]

        basepath = "C:/????????????????????????"
        try:
            os.mkdir(basepath)
        except FileExistsError:
            pass



        directory = "{}".format(str(System_memory["??????"].getValue()))
        
        
        # Create target Year Directory
        try:
            path = os.path.join(basepath, directory)
            print(path)
            os.mkdir(path)
        except FileExistsError:
            pass
        
        # Create target Directory
        try:
            os.mkdir(os.path.join(path, "????????????"))
        except FileExistsError:
            pass

        # Create target Directory
        try:
            os.mkdir(os.path.join(path, "????????????"))
        except FileExistsError:
            pass
        
        
        
        if System_memory["????????????"].getValue():
            path = os.path.join(path, "????????????")
            try:
                os.mkdir(path)
            except FileExistsError:
                pass
        else:
            path = os.path.join(path, "????????????")
            try:
                os.mkdir(path)
            except FileExistsError:
                pass
            
        test_number=System_memory["??????????????????"].getValue()
        try:
            path=os.path.join(path, "{}".format(str(test_number)))
            os.mkdir(path)
        except FileExistsError:
            pass

        try:
            path=os.path.join(path, "????????????")
            os.mkdir(path)
        except FileExistsError:
            pass


        now=datetime.datetime.now()
        try:
            path=os.path.join(path, "{}???_{}???_{}???_{}???_{}???_{}???".format(now.year,now.month,now.day,now.hour,now.minute,now.second))
            os.mkdir(path)
        except FileExistsError:
            pass

        self.main_folder_path=path

    def prepare_AutoTest_Mainfolder(self):
        
        System_memory=self.memoryPool["System memory"]
        Modbus_Registor_Pool=self.memoryPool["Modbus Registor Pool - Registor"]

        basepath = "C:/????????????????????????"
        try:
            os.mkdir(basepath)
        except FileExistsError:
            pass



        directory = "{}".format(str(System_memory["??????"].getValue()))
        
        
        # Create target Year Directory
        try:
            path = os.path.join(basepath, directory)
            print(path)
            os.mkdir(path)
        except FileExistsError:
            pass
        
        # Create target Directory
        try:
            os.mkdir(os.path.join(path, "????????????"))
        except FileExistsError:
            pass

        # Create target Directory
        try:
            os.mkdir(os.path.join(path, "????????????"))
        except FileExistsError:
            pass
        
        
        
        if System_memory["????????????"].getValue():
            path = os.path.join(path, "????????????")
            try:
                os.mkdir(path)
            except FileExistsError:
                pass
        else:
            path = os.path.join(path, "????????????")
            try:
                os.mkdir(path)
            except FileExistsError:
                pass
            
            
        test_number=System_memory["??????????????????"].getValue()
        try:
            path=os.path.join(path, "{}".format(str(test_number)))
            os.mkdir(path)
        except FileExistsError:
            pass

        try:
            path=os.path.join(path, "????????????")
            os.mkdir(path)
        except FileExistsError:
            pass


        now=datetime.datetime.now()
        try:
            path=os.path.join(path, "{}???_{}???_{}???_{}???_{}???_{}???".format(now.year,now.month,now.day,now.hour,now.minute,now.second))
            os.mkdir(path)
        except FileExistsError:
            pass

        self.main_folder_path=path
            


    def prepare_Subfolder(self,stage):
        Main_FolderPath=self.memoryPool["System memory"]["Main_FolderPath"].getValue()
        if stage[0]==Test_folder_package.RT_stage:
            path = os.path.join(Main_FolderPath, "RT")
        elif stage[0]==Test_folder_package.Temp_stage:
            path = os.path.join(Main_FolderPath, "{}???".format(stage[1]))
        else:
            return False
        self.subPath=path
        os.mkdir(path)

    def fileMake_Work(self):

        while 1:
            try:
                getItem=self.queuePool["fileMakeQueue"].get(timeout=0.1)

                self.prepare_CsvFile(getItem)
                if self.subFoldergetItem.stage[0]==Test_profile_package.Temp_stage:
                    self.testDataQueue_Work("??????????????????")
                self.testDataQueue_Work("BG????????????")

            except :
                
                if self.dataRecord_Stop:
                    return

    def _123_to_abc(self,number):

        if number==1:
            return "A"
        elif number==2:
            return "B"
        elif number==3:
            return "C"
        elif number==4:
            return "D"
        elif number==5:
            return "E"
        elif number==6:
            return "F"
        elif number==7:
            return "G"
        elif number==8:
            return "H"

    def prepare_Manual_Pattern_TestCsvFile(self,profile):
        self.profile=profile

        self.csv = os.path.join(self.main_folder_path, "???????????????????????????_{}.csv".format(self.profile.file_name))


        with open(self.csv, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(['?????????', self.profile.date])
            writer.writerow(['????????????', self.profile.number])
            if self.profile.mode==2:
                writer.writerow(['?????????', self.profile.costomer])
                writer.writerow(['?????????', self.profile.costomerName])
            writer.writerow(['????????????', self.profile.meterialName])
            writer.writerow(['??????', self.profile.meterial])
            writer.writerow(['????????????(mm)', self.profile.mainDia])
            writer.writerow(['????????????????????????(mm)', self.profile.innerDia])
            writer.writerow(['????????????(mm2)', (((float(self.profile.mainDia)+float(self.profile.innerDia))/2)/2)*(((float(self.profile.mainDia)+float(self.profile.innerDia))/2)/2)*math.pi])
            writer.writerow(['???????????????(mm)', self.profile.thinkness])

            System_memory=self.memoryPool["System memory"]

            if System_memory["AvgHelper_Record_Enabled"].getValue():
                writer.writerow("")

                avarage_numbers=0
                avarage_data=0
                got_avarage=False
                for index in range(1,9):
                    if System_memory["AvgHelper_Enable_{}".format(index)].getValue():

                        avarage_numbers+=1
                        avarage_data+=System_memory["AvgHelper_Value_{}".format(index)].getValue()

                        if not got_avarage:
                            got_avarage=True

                        writer.writerow(['?????????'+self._123_to_abc(index),System_memory["AvgHelper_Value_{}".format(index)].getValue()])
                    else:
                        writer.writerow(['?????????'+self._123_to_abc(index),"?????????"])

                if got_avarage:
                    writer.writerow(['???????????????', avarage_data/avarage_numbers])
                    got_avarage=True
            
            writer.writerow("")
            writer.writerow(['????????????(v)', self.profile.voltage])
            writer.writerow(['???????????????(min)', self.profile.time])
            writer.writerow(['?????????????????????????????????(s)', self.profile.time_sample])
            writer.writerow(['BG ????????????(min)', self.profile.bg_time])
            writer.writerow(['BG ??????????????????????????????(s)', self.profile.bg_time_sample])
            writer.writerow(['Speed', "{}".format(self.profile.speed)])
            writer.writerow(['Filter', "{}".format(self.profile.filter)])
            writer.writerow(['Filter count', self.profile.filter_count])

    def prepare_CsvFile(self,profile):

        self.profile=profile

        self.csvPath = os.path.join(self.main_folder_path, "{}".format(self.profile.folder_name))
        #os.mkdir(self.csvPath)
        try:
            os.mkdir(self.csvPath)
        except FileExistsError:
            pass

        self.csv = os.path.join(self.csvPath, "{}.csv".format(self.profile.file_name))


        with open(self.csv, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(['?????????', self.profile.date])
            writer.writerow(['????????????', self.profile.number])
            if self.profile.mode==2:
                writer.writerow(['?????????', self.profile.costomer])
                writer.writerow(['?????????', self.profile.costomerName])
            writer.writerow(['????????????', self.profile.meterialName])
            writer.writerow(['??????', self.profile.meterial])
            writer.writerow(['????????????(mm)', self.profile.mainDia])
            writer.writerow(['????????????????????????(mm)', self.profile.innerDia])
            writer.writerow(['????????????(mm2)', (((float(self.profile.mainDia)+float(self.profile.innerDia))/2)/2)*(((float(self.profile.mainDia)+float(self.profile.innerDia))/2)/2)*math.pi])
            writer.writerow(['???????????????(mm)', self.profile.thinkness])
            writer.writerow(['???????????????', self.profile.gas])
            System_memory=self.memoryPool["System memory"]

            if System_memory["AvgHelper_Record_Enabled"].getValue():
                writer.writerow("")

                avarage_numbers=0
                avarage_data=0
                got_avarage=False
                for index in range(1,9):
                    if System_memory["AvgHelper_Enable_{}".format(index)].getValue():

                        avarage_numbers+=1
                        avarage_data+=System_memory["AvgHelper_Value_{}".format(index)].getValue()

                        if not got_avarage:
                            got_avarage=True

                        writer.writerow(['?????????'+self._123_to_abc(index),System_memory["AvgHelper_Value_{}".format(index)].getValue()])
                    else:
                        writer.writerow(['?????????'+self._123_to_abc(index),"?????????"])

                if got_avarage:
                    writer.writerow(['???????????????', avarage_data/avarage_numbers])
                    got_avarage=True
            writer.writerow("")
            writer.writerow(['????????????(v)', self.profile.voltage])
            writer.writerow(['???????????????(min)', self.profile.time])
            writer.writerow(['?????????????????????????????????(s)', self.profile.time_sample])
            writer.writerow(['BG ????????????(min)', self.profile.bg_time])
            writer.writerow(['BG ??????????????????????????????(s)', self.profile.bg_time_sample])
            writer.writerow(['Speed', "{}".format(self.profile.speed)])
            writer.writerow(['Filter', "{}".format(self.profile.filter)])
            writer.writerow(['Filter count', self.profile.filter_count])

            
    def record_finish_Work(self,error_code=0):

        with open(self.csv, 'a', newline='') as csvfile:

            writer = csv.writer(csvfile)
            writer.writerow("")

            now=datetime.datetime.now()

            if error_code==1:
                writer.writerow(["??????????????????","","??????","{}???_{}???_{}???_{}???_{}???_{}???".format(now.year,now.month,now.day,now.hour,now.minute,now.second)])
            elif error_code==2:
                writer.writerow(["????????????","???????????????????????????","??????","{}???_{}???_{}???_{}???_{}???_{}???".format(now.year,now.month,now.day,now.hour,now.minute,now.second)])
            elif error_code==3:
                writer.writerow(["????????????","????????????????????????","??????","{}???_{}???_{}???_{}???_{}???_{}???".format(now.year,now.month,now.day,now.hour,now.minute,now.second)])
            elif error_code==4:
                writer.writerow(["????????????","???????????????","??????","{}???_{}???_{}???_{}???_{}???_{}???".format(now.year,now.month,now.day,now.hour,now.minute,now.second)])
            elif error_code==5:
                writer.writerow(["????????????","?????????????????????????????????","??????","{}???_{}???_{}???_{}???_{}???_{}???".format(now.year,now.month,now.day,now.hour,now.minute,now.second)])
            

    def prepare_Record_Header(self,type):

        with open(self.csv, 'a', newline='') as csvfile:

            writer = csv.writer(csvfile)
            writer.writerow("")
            writer.writerow(["{}".format(type)])
            writer.writerow(["????????????","????????????(sec)","?????????","????????????(v)","????????????(A)","?????????(??)","???????????????(?????cm)"])



    def testDataQueue_Work(self,title):

        with open(self.csvPath, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow('')
            writer.writerow(title)
            writer.writerow(['????????????(sec)','??????(???)','????????????(V)','????????????(A)','????????????(??)'])

            process=True
            while 1:
                try:
                    getItem=self.queuePool["testDataQueue"].get(timeout=0.1)
                    process=True
                except :
                    process=False
                    if self.dataRecord_Stop:
                        return

                if abord:
                    if getItem.count==-1:
                        writer.writerow('END')
                        return

                    writer.writerow(getItem.time,getItem.Temperature,getItem.voltage,getItem.current,getItem.resistance)

    

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