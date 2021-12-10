import copy
import ctypes
import threading
import time

import usb.core
from registor_manager import *

from .gpib_manager import (GPIB_device_2635B, GPIB_device_2657A, GPIB_Driver,
                           GPIB_package)


def set_memorypool_register(memoryPool,
                                                queuePool,
                                                memorypool_name,
                                                registor_name,
                                                value):
        
        if memoryPool[memorypool_name][registor_name].getValue()!=value:

            sub_memorypool=copy.deepcopy(memoryPool[memorypool_name])
            sub_memorypool[registor_name].setValue(value)

            memoryPool[memorypool_name]=sub_memorypool
            sendItem=MemoryUnit(memorypool_name,registor_name)
            #print("sendItem",sendItem.pool_name,sendItem.registor_name)
            queuePool["database_Uplaod_Queue"].put(sendItem)
            queuePool["memory_DownlaodToGUI_request_Queue"].put(sendItem)
            

def GPIB_USB_interface_connnection_Work(PoolSemaphore,memorypool,queuePool):
    
    # find our device
    connection=False
    set_memorypool_register(memorypool,queuePool,"System memory","GPIB USB conneciton",0)
    while 1:
        # was it found?
        dev = usb.core.find(idVendor=0x06CE, idProduct=0x8314)
        if dev is None:
            if connection!=False:
                connection = False
                set_memorypool_register(memorypool,queuePool,"System memory","GPIB USB conneciton",0)
        else:
            if connection!=True:
                connection = True
                set_memorypool_register(memorypool,queuePool,"System memory","GPIB USB conneciton",1)

        time.sleep(1)


def gpib_Thread(PoolSemaphore,memoryPool,queuePool):

    
    
    gPIB_Driver=GPIB_Driver(PoolSemaphore,memoryPool,queuePool)
    
    #GPIB connnection Thread create 
    gPIB_USB_interface_connnection_Thread = threading.Thread(target = GPIB_USB_interface_connnection_Work,daemon=True,args = (PoolSemaphore,memoryPool,queuePool))
    gPIB_USB_interface_connnection_Thread.start()
    








