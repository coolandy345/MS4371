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


from gpib_manager import *

import ctypes


def shotdown_entire_app(future):
    print("shotdown_entire_app")
    for process in executor._processes.values():
        process.kill()


if __name__ == "__main__":

    MemoryPoolManager=Manager()
    MemoryPool = MemoryPoolManager.dict()

    QueuePool={}
    QueuePool["modbus_Write_Queue"]=MemoryPoolManager.Queue()
    QueuePool["memory_Write_Queue"]=MemoryPoolManager.Queue()
    QueuePool["memory_refresh_Queue"]=MemoryPoolManager.Queue()

    
    databaseLoadThread(MemoryPool)

    ##memoryWriteThread(MemoryPool,QueuePool)
    #initial_GUI(MemoryPool,QueuePool)


    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.submit(gpib_Thread,MemoryPool,QueuePool)
        executor.submit(run_async_server,MemoryPool,QueuePool)
        executor.submit(databaseWriteThread,MemoryPool,QueuePool)
        Gui_future = executor.submit(initial_GUI,MemoryPool,QueuePool)
        Gui_future.add_done_callback(shotdown_entire_app)


  

    