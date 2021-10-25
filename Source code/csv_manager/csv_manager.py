# -*- coding: utf-8 -*-
from multiprocessing import Manager
import threading
import time
import os
from operator import *
import csv

def csv_manager_thread(memoryPool,queuePool,eventPool):
	csv_manager=Csv_manager(memoryPool,queuePool,eventPool)


class Csv_manager():
    def __init__(self,
                 memoryPool,
                 queuePool,
                 eventPool
                 ):
        self.memoryPool=memoryPool
        self.queuePool=queuePool
        self.eventPool=eventPool

        self.dataRecord_Stop=False

        self.subPath=""
        self.csvPath=""

        reset_Thread = threading.Thread(target = self.reset_Work,daemon=True)
        reset_Thread.start()

        self.subFolderMake_Thread = threading.Thread(target = self.subFolderMake_Work,daemon=True)
        self.subFolderMake_Thread.start()

    def reset_Work(self):
        while 1:
            self.eventPool["Record stop"].wait()
            self.dataRecord_Stop=True

    def subFolderMake_Work(self):
        while 1:
            self.dataRecord_Stop=False
            self.subFoldergetItem=self.queuePool["subFolderMakeQueue"].get()

            self.prepare_Subfolder(self.subFoldergetItem.stage)
            self.fileMake_Work()

            

    def prepare_Subfolder(self):
        Main_FolderPath=self.memoryPool["System memory"]["Main_FolderPath"].getValue()
        if self.subFoldergetItem.stage[0]==test_profile_package.RT_stage:
            path = os.path.join(Main_FolderPath, "RT")
        elif self.subFoldergetItem.stage[0]==test_profile_package.Temp_stage:
            path = os.path.join(Main_FolderPath, "{}℃".format(self.subFoldergetItem.stage[1]))
        else:
            return False
        self.subPath=path
        os.mkdir(path)

    def fileMake_Work(self):

        process=True
        while 1:
            try:
                getItem=self.queuePool["fileMakeQueue"].get(0.1)
                process=True
            except :
                process=False
                if self.dataRecord_Stop:
                    return

            if process:
                self.prepare_CsvFile(getItem)
                if self.subFoldergetItem.stage[0]==test_profile_package.Temp_stage:
                    self.testDataQueue_Work("抵抗測定結果")
                self.testDataQueue_Work("BG測定結果")

    def prepare_CsvFile(self,profile):

        self.csvPath = os.path.join(self.subPath, "{}".format(profile.file_name))
        with open(self.csvPath, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(['測定日', profile.date])
            writer.writerow(['依頼測定番号', profile.date])
            writer.writerow(['依頼元', profile.date])
            writer.writerow(['依頼者', profile.date])
            writer.writerow(['試料名称', profile.date])
            writer.writerow(['材料', profile.date])
            writer.writerow(['主電極径(mm)', profile.date])
            writer.writerow(['ガード電極の内径(mm)', profile.date])
            writer.writerow(['材料の厚さ(mm)', profile.date])
            writer.writerow(['測定雰囲気', profile.date])

            

    def testDataQueue_Work(self,title):

        with open(self.csvPath, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow('')
            writer.writerow(title)
            writer.writerow(['経過時間(sec)','温度(℃)','印加電圧(V)','測定電流(A)','測定抵抗(Ω)'])

            process=True
            while 1:
                try:
                    getItem=self.queuePool["testDataQueue"].get(0.1)
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

    

