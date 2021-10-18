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


from gpib_manager import Gpib_manager



def test_A(memoryPool):

    for i in range(10):
        print("Send signal")
        memoryPool["EvevtPool"]["MB_memory_Write_Event"][0].set()
        time.sleep(0.2)

def test_B(memoryPool):

    while 1:
        memoryPool["EvevtPool"]["MB_memory_Write_Event"][0].wait()
        memoryPool["EvevtPool"]["MB_memory_Write_Event"][0].clear()
        print("get event")


def shotdown_entire_app(future):
    print("shotdown_entire_app")
    for process in executor._processes.values():
        process.kill()

if __name__ == "__main__":

    #MemoryPoolManager=Manager()
    #MemoryPool = MemoryPoolManager.dict()

    #QueuePool={}
    #QueuePool["modbus_Write_Queue"]=MemoryPoolManager.Queue()
    #QueuePool["memory_Write_Queue"]=MemoryPoolManager.Queue()
    #QueuePool["memory_refresh_Queue"]=MemoryPoolManager.Queue()

    gpib_manager=Gpib_manager()
    #databaseLoadThread(MemoryPool)
    ##memoryWriteThread(MemoryPool,QueuePool)
    ##initial_GUI(MemoryPool,QueuePool)

    ##with ProcessPoolExecutor(max_workers=10) as executor:
    ##    #test_A_future = executor.submit(test_A,MemoryPool)
    ##    #test_B_future = executor.submit(test_B,MemoryPool)
    ##    executor.submit(databaseWriteThread,MemoryPool,QueuePool)
    ##    Gui_future = executor.submit(initial_GUI,MemoryPool,QueuePool)
    ##    Gui_future.add_done_callback(shotdown_entire_app)

    #with ProcessPoolExecutor(max_workers=10) as executor:
    #    executor.submit(run_async_server,MemoryPool,QueuePool)
    #    executor.submit(databaseWriteThread,MemoryPool,QueuePool)
    #    Gui_future = executor.submit(initial_GUI,MemoryPool,QueuePool)
    #    Gui_future.add_done_callback(shotdown_entire_app)









  

    