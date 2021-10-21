#!/usr/bin/env python
"""
Pymodbus Asynchronous Server Example
--------------------------------------------------------------------------

The asynchronous server is a high performance implementation using the
twisted library as its backend.  This allows it to scale to many thousands
of nodes which can be helpful for testing monitoring software.
"""
# --------------------------------------------------------------------------- # 
# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.version import version
from pymodbus.server.asynchronous import StartTcpServer,StopServer
from twisted.internet import reactor
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import (ModbusRtuFramer,
                                  ModbusAsciiFramer,
                                  ModbusBinaryFramer)
from pymodbus.datastore import ModbusSparseDataBlock
from registor_manager import *
from twisted.internet.task import LoopingCall

#from ..registor_manager import databaseLoadThread,databaseWriteThread,MemoryUnit

import random

import threading
# --------------------------------------------------------------------------- # 
# configure the service logging
# --------------------------------------------------------------------------- # 
import logging
import time
import socket
import copy


#FORMAT = ('%(asctime)-15s %(threadName)-15s'
#          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
#logging.basicConfig(format=FORMAT)
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)



class CustomDataBlock(ModbusSparseDataBlock):
    """ A datablock that stores the new value in memory
    and performs a custom action after it has been stored.
    """
    def __init__(self,memorypool,queuepool):
        #super().__init__()
        
        self.memorypool=memorypool
        self.queuepool=queuepool
        self.register_namedict={}
        self.register_dict={}
        self.register_shift=1
        #get dict
        self.get_register_dict()

        super().__init__(self.register_dict)

        ethernet_connection_thread = threading.Thread(target = self.ethernet_connection_Work,daemon=True)
        ethernet_connection_thread.start()

        database_update_thread = threading.Thread(target = self.database_update_Work,daemon=True)
        database_update_thread.start()


    def get_register_dict(self):
        self.register_dict={}

        for unit in self.memorypool["Modbus Registor Pool - Registor"].values():
            self.register_namedict[unit.registor_number+self.register_shift]=unit.name
            self.register_dict[unit.registor_number+self.register_shift]=unit.getValue()

    def getValues(self, address, count=1):
        super(CustomDataBlock, self).getValues(address, count)
        self.set_Ethernet_Connection()

    def ethernet_connection_Work(self):
        while 1:

            if self.memorypool["System memory"]["Ethernet conneciton check pool"].getValue():
                sub_memorypool=copy.deepcopy(self.memorypool["System memory"])
                sub_memorypool["Ethernet conneciton check pool"].setValue(0)
                self.memorypool["System memory"]=sub_memorypool

                sub_memorypool=copy.deepcopy(self.memorypool["System memory"])
                sub_memorypool["Ethernet conneciton"].setValue(1)
                self.memorypool["System memory"]=sub_memorypool

            else:
                sub_memorypool=copy.deepcopy(self.memorypool["System memory"])
                sub_memorypool["Ethernet conneciton"].setValue(0)
                self.memorypool["System memory"]=sub_memorypool

            time.sleep(1)
        

    def set_Ethernet_Connection(self):

        sub_memorypool=copy.deepcopy(self.memorypool["System memory"])
        sub_memorypool["Ethernet conneciton check pool"].setValue(1)
        self.memorypool["System memory"]=sub_memorypool


        
    def setValues(self, address, value):
        
        self.set_Ethernet_Connection()
        """ Sets the requested values of the datastore

        :param address: The starting address
        :param values: The new values to be set
        """
        super(CustomDataBlock, self).setValues(address, value)

        # whatever you want to do with the written value is done here,
        # however make sure not to do too much work here or it will
        # block the server, espectially if the server is being written
        # to very quickly

        if isinstance(value, list):
            address_temp=address
            for val in value:
                registor_name=self.register_namedict[address_temp]
                self.set_memorypool_register(registor_name,val)
                address_temp+=1
        else:
            registor_name=self.register_namedict[address]
            self.set_memorypool_register(registor_name,value)


    def set_memorypool_register(self,registor_name,value):

        if self.memorypool["Modbus Registor Pool - Registor"][registor_name].getValue()!=value:

            sub_memorypool=copy.deepcopy(self.memorypool["Modbus Registor Pool - Registor"])
            sub_memorypool[registor_name].setValue(value)

            self.memorypool["Modbus Registor Pool - Registor"]=sub_memorypool
            sendItem=MemoryUnit("Modbus Registor Pool - Registor",registor_name)
            self.queuepool["memory_Write_Queue"].put(sendItem)

    def database_update_Work(self):
    
        while 1:
            getItem=MemoryUnit()
            getItem=self.queuepool["modbus_Write_Queue"].get()

            if getItem.Main_memorypool=="Modbus Registor Pool - Registor":
                unit=self.memorypool["Modbus Registor Pool - Registor"][getItem.memory_name]
                self.register_dict[unit.registor_number+self.register_shift]=unit.getValue()



        

    #def getValues(self, address, count=1):

    #    super(CustomDataBlock, self).getValues(address, count)
    #    print("getValues",address,count)



#def database_update_threadJob(a):

#    while 1:
#        print("database_update_threadJob")
#        context  = a
#        context[0x01].setValues(0x03,1,[5])
#        time.sleep(1)



def run_async_server(memorypool,queuePool):
    
    block  = CustomDataBlock(memorypool,queuePool)
    #print(block.getValues(10, count=10))

    #block  = ModbusSequentialDataBlock(0, [17]*100)
    store  = ModbusSlaveContext(di=block, co=block, hr=block, ir=block)
    context = ModbusServerContext(slaves=store, single=True)

    # ----------------------------------------------------------------------- # 
    # initialize the server information
    # ----------------------------------------------------------------------- # 
    # If you don't set this or any fields, they are defaulted to empty strings.
    # ----------------------------------------------------------------------- # 
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'MOTOYAMA CO .,LTD'
    identity.ProductCode = 'MS4371'
    identity.VendorUrl = 'https://www.motoyama.co.jp/'
    identity.ProductName = 'MS4371 - Modbus Server'
    identity.ModelName = 'Modbus Server'
    identity.MajorMinorRevision = version.short()
    
    # ----------------------------------------------------------------------- # 
    # run the server you want
    # ----------------------------------------------------------------------- # 
    # TCP Server
    local_IP_address=socket.gethostbyname(socket.gethostname())
    StartTcpServer(context, identity=identity, address=(local_IP_address, 502))
    

if __name__ == "__main__":


    run_async_server()

