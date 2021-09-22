#/usr/bin/python
# --------------------------------------------------------------------------- # 
# System module import
# --------------------------------------------------------------------------- # 
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

# --------------------------------------------------------------------------- # 
# local module import
# --------------------------------------------------------------------------- # 
from registor_manager import *

import sys
import os
import time

from modbus_TcpServer import *
from gui_main import*

from gui_main.qt_core import *

import pprint

def hello():
        time.sleep(1)

def shotdown_entire_app(future):
    print("shotdown_entire_app")
    for process in executor._processes.values():
        process.kill()


if __name__ == "__main__":
    input("wait")
    #MemoryPoolManager=Manager()
    #MemoryPool = MemoryPoolManager.dict()
    #loadMemoryPool(MemoryPool)
    #print(MemoryPool)
    input("wait")
    #with ProcessPoolExecutor(max_workers=10) as executor:
    #    executor.submit(run_async_server,MemoryPool)
    #    Gui_future = executor.submit(initial_GUI,MemoryPool)
    #    Gui_future.add_done_callback(shotdown_entire_app)









  

    