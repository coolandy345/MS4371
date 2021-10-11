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




def hello():
    test=0
    while 1:
        print(test)
        time.sleep(0.1)
        test+=1


def shotdown_entire_app(future):
    print("shotdown_entire_app")
    for process in executor._processes.values():
        process.kill()

if __name__ == "__main__":

    MemoryPoolManager=Manager()
    MemoryPool = MemoryPoolManager.dict()
    loadMemoryPool(MemoryPool)
    initial_GUI(MemoryPool)

    #with ProcessPoolExecutor(max_workers=10) as executor:
    #    executor.submit(run_async_server,MemoryPool)
    #    executor.submit(hello)
    #    Gui_future = executor.submit(initial_GUI,MemoryPool)
    #    Gui_future.add_done_callback(shotdown_entire_app)









  

    