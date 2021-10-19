from .gpib_manager import GPIB_device_2635B,GPIB_device_2657A
from registor_manager import *
import copy
import threading
import time
import usb.core



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

def GPIB_connnection_Work(memorypool,queuePool):
    
    connection=False
    while 1:
        # find our device
        dev = usb.core.find(idVendor=0x0483, idProduct=0x374B)

        # was it found?
        if dev is None:
            if connection!=False:
                connection = False
                set_memorypool_register(memorypool,queuePool,"System memory","GPIB USB conneciton",0)
                print("GPIB USB disconneciton")
        else:
            if connection!=True:
                connection = True
                set_memorypool_register(memorypool,queuePool,"System memory","GPIB USB conneciton",1)
                print("GPIB USB conneciton")

        time.sleep(1)


def gpib_Thread(memoryPool,queuePool):
    
    #GPIB connnection Thread create 
    GPIB_connnection_Thread = threading.Thread(target = GPIB_connnection_Work,args = (memoryPool,queuePool))
    GPIB_connnection_Thread.start()

    #GPIB device class create 
    gpib_2635B_manager=GPIB_device_2635B(memoryPool,queuePool)
    gpib_2657A_manager=GPIB_device_2657A(memoryPool,queuePool)








