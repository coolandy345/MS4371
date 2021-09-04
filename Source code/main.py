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

from modbus_TcpServer import *
from gui_main import*

def hello():
        time.sleep(1)

def shotdown_entire_app(future):
    print("shotdown_entire_app")
    for process in executor._processes.values():
        process.kill()


if __name__ == "__main__":
    MemoryPoolManager=Manager()
    MemoryPool = MemoryPoolManager.dict()
    loadMemoryPool(MemoryPool)
    
    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.submit(run_async_server)
        Gui_future = executor.submit(initial_GUI)
        Gui_future.add_done_callback(shotdown_entire_app)




  

    