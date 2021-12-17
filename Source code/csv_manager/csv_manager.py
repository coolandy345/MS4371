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

        self.csv = os.path.join(self.main_folder_path, "ノイズ測定結果データ.csv")
        with open(self.csv, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(['測定実施時刻', self.profile.date])
            writer.writerow(['測定電圧(V)', self.profile.ノイズ測定電圧])
            writer.writerow(['測定判定基準電流(A)', self.profile.ノイズ測定判定基準])
            writer.writerow(['測定時間(min)', self.profile.ノイズ測定時間])


    def prepare_ManualTestCsvFile(self,profile):

        self.profile=profile

        self.csv = os.path.join(self.main_folder_path, "手動測定結果データ.csv")
        with open(self.csv, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(['測定日', self.profile.date])
            writer.writerow(['測定番号', self.profile.number])
            if self.profile.mode==2:
                writer.writerow(['依頼元', self.profile.costomer])
                writer.writerow(['依頼者', self.profile.costomerName])
            writer.writerow(['試料名称', self.profile.meterialName])
            writer.writerow(['材料', self.profile.meterial])
            writer.writerow(['主電極径(mm)', self.profile.mainDia])
            writer.writerow(['ガード電極の内径(mm)', self.profile.innerDia])
            writer.writerow(['電極面積(mm2)', (((float(self.profile.mainDia)+float(self.profile.innerDia))/2)/2)*(((float(self.profile.mainDia)+float(self.profile.innerDia))/2)/2)*math.pi])
            writer.writerow(['材料の厚さ(mm)', self.profile.thinkness])
            writer.writerow(['測定電圧(V)', self.profile.voltage])
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
            writer.writerow(['合格判定',str(text)])
            writer.writerow(['最大電流(A)',str(max)])
            writer.writerow(['最小電流(A)',str(min)])
            writer.writerow("")

            for row in temp_list:
                writer.writerow(row)



    
    def prepare_NoiseTestfolder(self):

        System_memory=self.memoryPool["System memory"]
        Modbus_Registor_Pool=self.memoryPool["Modbus Registor Pool - Registor"]

        basepath = "C:/高温抵抗測定結果"
        try:
            os.mkdir(basepath)
        except FileExistsError:
            pass

        # Create target Year Directory
        try:
            path = os.path.join(basepath, "ノイズ測定結果")
            os.mkdir(path)
        except FileExistsError:
            pass

        now=datetime.datetime.now()
        try:
            path = os.path.join(path, str("{}年_{}月_{}日_{}時_{}分_{}秒".format(now.year,now.month,now.day,now.hour,now.minute,now.second)))
            os.mkdir(path)
        except FileExistsError:
            pass

        self.main_folder_path=path

    def prepare_ManualTest_Mainfolder(self):
        
        System_memory=self.memoryPool["System memory"]
        Modbus_Registor_Pool=self.memoryPool["Modbus Registor Pool - Registor"]

        basepath = "C:/高温抵抗測定結果"
        try:
            os.mkdir(basepath)
        except FileExistsError:
            pass



        directory = "{}".format(str(System_memory["年度"].getValue()))
        
        
        # Create target Year Directory
        try:
            path = os.path.join(basepath, directory)
            print(path)
            os.mkdir(path)
        except FileExistsError:
            pass
        
        # Create target Directory
        try:
            os.mkdir(os.path.join(path, "評価試験"))
        except FileExistsError:
            pass

        # Create target Directory
        try:
            os.mkdir(os.path.join(path, "依頼測定"))
        except FileExistsError:
            pass
        
        
        
        if System_memory["評価試験"].getValue():
            path = os.path.join(path, "評価試験")
            try:
                os.mkdir(path)
            except FileExistsError:
                pass
        else:
            path = os.path.join(path, "依頼測定")
            try:
                os.mkdir(path)
            except FileExistsError:
                pass
            
        test_number=System_memory["依頼測定番号"].getValue()
        try:
            path=os.path.join(path, "{}".format(str(test_number)))
            os.mkdir(path)
        except FileExistsError:
            pass

        try:
            path=os.path.join(path, "手動測定")
            os.mkdir(path)
        except FileExistsError:
            pass


        now=datetime.datetime.now()
        try:
            path=os.path.join(path, "{}年_{}月_{}日_{}時_{}分_{}秒".format(now.year,now.month,now.day,now.hour,now.minute,now.second))
            os.mkdir(path)
        except FileExistsError:
            pass

        self.main_folder_path=path

    def prepare_AutoTest_Mainfolder(self):
        
        System_memory=self.memoryPool["System memory"]
        Modbus_Registor_Pool=self.memoryPool["Modbus Registor Pool - Registor"]

        basepath = "C:/高温抵抗測定結果"
        try:
            os.mkdir(basepath)
        except FileExistsError:
            pass



        directory = "{}".format(str(System_memory["年度"].getValue()))
        
        
        # Create target Year Directory
        try:
            path = os.path.join(basepath, directory)
            print(path)
            os.mkdir(path)
        except FileExistsError:
            pass
        
        # Create target Directory
        try:
            os.mkdir(os.path.join(path, "評価試験"))
        except FileExistsError:
            pass

        # Create target Directory
        try:
            os.mkdir(os.path.join(path, "依頼測定"))
        except FileExistsError:
            pass
        
        
        
        if System_memory["評価試験"].getValue():
            path = os.path.join(path, "評価試験")
            try:
                os.mkdir(path)
            except FileExistsError:
                pass
        else:
            path = os.path.join(path, "依頼測定")
            try:
                os.mkdir(path)
            except FileExistsError:
                pass
            
            
        test_number=System_memory["依頼測定番号"].getValue()
        try:
            path=os.path.join(path, "{}".format(str(test_number)))
            os.mkdir(path)
        except FileExistsError:
            pass

        try:
            path=os.path.join(path, "自動測定")
            os.mkdir(path)
        except FileExistsError:
            pass


        now=datetime.datetime.now()
        try:
            path=os.path.join(path, "{}年_{}月_{}日_{}時_{}分_{}秒".format(now.year,now.month,now.day,now.hour,now.minute,now.second))
            os.mkdir(path)
        except FileExistsError:
            pass

        self.main_folder_path=path
            


    def prepare_Subfolder(self,stage):
        Main_FolderPath=self.memoryPool["System memory"]["Main_FolderPath"].getValue()
        if stage[0]==Test_folder_package.RT_stage:
            path = os.path.join(Main_FolderPath, "RT")
        elif stage[0]==Test_folder_package.Temp_stage:
            path = os.path.join(Main_FolderPath, "{}℃".format(stage[1]))
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
                    self.testDataQueue_Work("抵抗測定結果")
                self.testDataQueue_Work("BG測定結果")

            except :
                
                if self.dataRecord_Stop:
                    return

            

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

            writer.writerow(['測定日', self.profile.date])
            writer.writerow(['測定番号', self.profile.number])
            if self.profile.mode==2:
                writer.writerow(['依頼元', self.profile.costomer])
                writer.writerow(['依頼者', self.profile.costomerName])
            writer.writerow(['試料名称', self.profile.meterialName])
            writer.writerow(['材料', self.profile.meterial])
            writer.writerow(['主電極径(mm)', self.profile.mainDia])
            writer.writerow(['ガード電極の内径(mm)', self.profile.innerDia])
            writer.writerow(['電極面積(mm2)', (((float(self.profile.mainDia)+float(self.profile.innerDia))/2)/2)*(((float(self.profile.mainDia)+float(self.profile.innerDia))/2)/2)*math.pi])
            writer.writerow(['材料の厚さ(mm)', self.profile.thinkness])
            writer.writerow(['測定雰囲気', self.profile.gas])
            writer.writerow("")
            writer.writerow(['測定電圧(v)', self.profile.voltage])
            writer.writerow(['主測定時間(min)', self.profile.time])
            writer.writerow(['主測定サンプリング周期(s)', self.profile.time_sample])
            writer.writerow(['BG 測定時間(min)', self.profile.bg_time])
            writer.writerow(['BG 測定サンプリング周期(s)', self.profile.bg_time_sample])
            writer.writerow(['Speed', "{}".format(self.profile.speed)])
            writer.writerow(['Filter', "{}".format(self.profile.filter)])
            writer.writerow(['Filter count', self.profile.filter_count])

            


    def prepare_Record_Header(self,type):

        with open(self.csv, 'a', newline='') as csvfile:

            writer = csv.writer(csvfile)
            writer.writerow("")
            writer.writerow(["{}".format(type)])
            writer.writerow(["測定次数","経過時間(sec)","温度℃","印加電圧(v)","測定電流(A)","抵抗値(Ω)","体積抵抗率(Ω・cm)"])



    def testDataQueue_Work(self,title):

        with open(self.csvPath, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow('')
            writer.writerow(title)
            writer.writerow(['経過時間(sec)','温度(℃)','印加電圧(V)','測定電流(A)','測定抵抗(Ω)'])

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