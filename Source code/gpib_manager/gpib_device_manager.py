from .gpib_manager import GPIB_device_2635B,GPIB_device_2657A,GPIB_Driver,GPIB_package
from registor_manager import *
import copy
import threading
import time
import usb.core
import ctypes


def set_memorypool_register(Main_memorypool,
                                                QueuePool,
                                                memorypool_name,
                                                registor_name,
                                                value):
        
        if Main_memorypool[memorypool_name][registor_name].getValue()!=value:

            sub_memorypool=copy.deepcopy(Main_memorypool[memorypool_name])
            sub_memorypool[registor_name].setValue(value)

            Main_memorypool[memorypool_name]=sub_memorypool
            sendItem=MemoryUnit(memorypool_name,registor_name)
            QueuePool["memory_Write_Queue"].put(sendItem)

def GPIB_USB_interface_connnection_Work(memorypool,queuePool):
    
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


def gpib_Thread(memoryPool,queuePool):

    gPIB_Driver=GPIB_Driver(memoryPool,queuePool)
    
    #GPIB connnection Thread create 
    gPIB_USB_interface_connnection_Thread = threading.Thread(target = GPIB_USB_interface_connnection_Work,args = (memoryPool,queuePool))
    gPIB_USB_interface_connnection_Thread.start()

    #GPIB device class create 
    gpib_2635B_manager=GPIB_device_2635B(memoryPool,queuePool)
    gpib_2657A_manager=GPIB_device_2657A(memoryPool,queuePool)








