#/usr/bin/python
# --------------------------------------------------------------------------- # 
# System module import
# --------------------------------------------------------------------------- # 
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager,Queue

# --------------------------------------------------------------------------- # 
# local module import
# --------------------------------------------------------------------------- # 

import sys
import os
import time

from modbus_TcpServer import *
from registor_manager import *
from gui_main import*

from gui_main.qt_core import *
from csv_manager import *


from main_operator import *

import ctypes
import csv


def shotdown_entire_app(future):
    print("shotdown_entire_app")
    for process in executor._processes.values():
        process.kill()


if __name__ == "__main__":

    MemoryPoolManager=Manager()
    MemoryPool = MemoryPoolManager.dict()

    QueuePool={}
    QueuePool["modbus_Write_Queue"]=MemoryPoolManager.Queue()
    QueuePool["database_Uplaod_Queue"]=MemoryPoolManager.Queue()
    QueuePool["database_modbusUplaod_Queue"]=MemoryPoolManager.Queue()

    

    QueuePool["memory_DownlaodToGUI_request_Queue"]=MemoryPoolManager.Queue()
    QueuePool["memory_UploadToMaster_Queue"]=MemoryPoolManager.Queue()

    QueuePool["GPIB_send_queue"]=MemoryPoolManager.Queue()
    QueuePool["GPIB_2635B_queue"]=MemoryPoolManager.Queue()
    QueuePool["GPIB_2657A_queue"]=MemoryPoolManager.Queue()

    QueuePool["subFolderMakeQueue"]=MemoryPoolManager.Queue()
    QueuePool["fileMakeQueue"]=MemoryPoolManager.Queue()
    QueuePool["testDataQueue"]=MemoryPoolManager.Queue()

    EventPool={}
    EventPool["Auto Run Start"]=MemoryPoolManager.Event()
    EventPool["Auto Run finish"]=MemoryPoolManager.Event()
    
    EventPool["Noise Measure Start"]=MemoryPoolManager.Event()
    
    EventPool["Test approve"]=MemoryPoolManager.Event()
    EventPool["GPIB_Test_Finish"]=MemoryPoolManager.Event()
    EventPool["CSV_Data_arrive"]=MemoryPoolManager.Event()
    EventPool["GUI_Data_arrive"]=MemoryPoolManager.Event()
    
    EventPool["Database_data_Initial"]=MemoryPoolManager.Event()
    EventPool["CSV stop"]=MemoryPoolManager.Event()
    EventPool["GPIB Stop"]=MemoryPoolManager.Event()

    EventPool["Test Event1"]=MemoryPoolManager.Event()
    EventPool["Test Event2"]=MemoryPoolManager.Event()

    
    databaseLoadThread(MemoryPool)
    ##memoryWriteThread(MemoryPool,QueuePool)
    #initial_GUI(MemoryPool,QueuePool,EventPool)
    #gpib_Thread(MemoryPool,QueuePool)
    #operator_thread(MemoryPool,QueuePool,EventPool)
    #run_async_server(MemoryPool,QueuePool)

    with ProcessPoolExecutor(max_workers=10) as executor:
        
        executor.submit(csv_manager_thread,MemoryPool,QueuePool,EventPool)
        executor.submit(run_async_server,MemoryPool,QueuePool)
        executor.submit(databaseWriteThread,MemoryPool,QueuePool,EventPool)
        executor.submit(databaseWriteThread_NoModbusLoop,MemoryPool,QueuePool,EventPool)

        executor.submit(operator_thread,MemoryPool,QueuePool,EventPool)

        Gui_future = executor.submit(initial_GUI,MemoryPool,QueuePool,EventPool)
        Gui_future.add_done_callback(shotdown_entire_app)





  

    