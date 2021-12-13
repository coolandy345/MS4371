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
    def __init__(self,PoolSemaphore,memorypool,queuepool,eventPool):
        #super().__init__()
        
        self.PoolSemaphore=PoolSemaphore
        self.memorypool=memorypool
        self.Modbuspool=self.memorypool["Modbus Registor Pool - Registor"]
        self.queuepool=queuepool
        self.eventPool=eventPool
        self.register_namedict={}
        self.register_dict={}
        self.register_shift=1

        self.update_lock=False
        self.start_upload=False

        self.ethernet_connection=False
        self.ethernet_connection_pool=False

        self.MainPool_update_Request=False
        self.MainPool_update_namelist=[]

        self.set_memorypool_register("System memory","Ethernet conneciton",False)
        
        #get dict
        self.get_register_dict()

        self.Modbus_debug=True
        #print(self.register_dict)

        super().__init__(self.register_dict)
        
        ethernet_connection_thread = threading.Thread(target = self.ethernet_connection_Work,daemon=True)
        ethernet_connection_thread.start()

        database_update_thread = threading.Thread(target = self.modbusDatabase_update_Work,daemon=True)
        database_update_thread.start()

        
    def get_register_dict(self):
        self.register_dict={}
        self.PoolSemaphore.acquire(timeout=1)
        for unit in self.memorypool["Modbus Registor Pool - Registor"].values():
            self.register_namedict[unit.registor_number+self.register_shift]=unit.name
            self.register_dict[unit.registor_number+self.register_shift]=unit.getModbusValue()
        self.PoolSemaphore.release()


    def getValues(self, address, count):
        self.ethernet_connection_pool=True
        registor_name=self.register_namedict[address]

        if self.Modbus_debug:
            pass
            #value_list=[]
            #if add in range(0,count):
            #registor_name=self.register_namedict[address+add]
            #value_list.append(self.Modbuspool[registor_name].getValue())
            #print("modbus read - ","[{}]".format(address-self.register_shift),registor_name,count,self.Modbuspool[registor_name].getValue())

        if address-self.register_shift==0:
            self.start_upload=True
            self.eventPool["Setting_upload_toPLC_Start"].set()

        elif address-self.register_shift==10000:
            self.start_upload=False
            self.eventPool["Setting_upload_toPLC_Finish"].set()

        if self.start_upload:
            self.queuepool["Setting_upload_toPLC_Queue"].put(address/100)


        return super().getValues(address, count)

    def ethernet_connection_Work(self):
        while 1:

            if self.ethernet_connection_pool != self.ethernet_connection:
                
                self.ethernet_connection=self.ethernet_connection_pool
                self.set_memorypool_register("System memory","Ethernet conneciton",self.ethernet_connection)

            self.ethernet_connection_pool=False

            time.sleep(1)

    def set_memorypool_register(self,pool_name,registor_name,value):
        
        self.PoolSemaphore.acquire(timeout=1)
        if self.memorypool[pool_name][registor_name].getValue()!=value:

            sub_memorypool=copy.deepcopy(self.memorypool[pool_name])
            sub_memorypool[registor_name].setValue(value)
            self.memorypool[pool_name]=sub_memorypool
            sendItem=MemoryUnit(pool_name,registor_name)
            self.queuepool["database_Uplaod_Queue"].put(sendItem)
            self.queuepool["memory_DownlaodToGUI_request_Queue"].put(sendItem)
        self.PoolSemaphore.release()
        
    def MainDatabase_upload_Work(self):
            #test=time.time()
            
                
            local_namelist=[]
            #Remove void item in  MainPool_update_namelist
            for name in self.MainPool_update_namelist:
                if name.find('blank_pos') == -1:
                    local_namelist.append(name)

            self.MainPool_update_namelist=[]

            #Remove Duplicates From poolNameList
            local_namelist = list(dict.fromkeys(local_namelist))
            
            self.PoolSemaphore.acquire(timeout=1)
            tempPool=self.memorypool["Modbus Registor Pool - Registor"]

            for name in local_namelist:
                tempPool[name].setValue(self.Modbuspool[name].getValue())
                    #We get aviaible data
            self.memorypool["Modbus Registor Pool - Registor"]=tempPool
            self.PoolSemaphore.release()
            for name in local_namelist:
                sendItem=MemoryUnit("Modbus Registor Pool - Registor",name)
                self.queuepool["database_modbusUplaod_Queue"].put(sendItem)
                self.queuepool["memory_DownlaodToGUI_request_Queue"].put(sendItem)
                
            #print(time.time()-test)
            



    def modbus_setValues_Work(self,address,value):
        
        self.ethernet_connection_pool=True
        
        
        if isinstance(value, list):

            registor_name_first=self.register_namedict[address]
            
            address_temp=address
            change=False
            change_contant_dict={}

            for val in value:
                registor_name=self.register_namedict[address_temp]
                if val!=self.Modbuspool[registor_name].getValue():
                    self.Modbuspool[registor_name].setValue(val)
                    self.MainPool_update_namelist.append(registor_name)
                    change_contant_dict["[{}]{}".format(address_temp-self.register_shift,registor_name)]=val
                    if self.Modbus_debug:
                        pass
                        #print("modbus write - ","[{}]".format(address_temp-self.register_shift),registor_name,val)
                    change=True
                address_temp+=1
            if change:
                if self.Modbus_debug:
                    print("modbus write from PLC - ","数量{}".format(len(self.MainPool_update_namelist)),change_contant_dict)

                self.MainDatabase_upload_Work()
                #self.MainPool_update_Request=True

                
        else:
            change=False
            registor_name=self.register_namedict[address]
            if value!=self.Modbuspool[registor_name].getValue():
                
                self.Modbuspool[registor_name].setValue(value)
                self.MainPool_update_namelist.append(registor_name)
                change=True
            if change:
                if self.Modbus_debug:
                    print("modbus write from PLC - ","[{}]".format(address-self.register_shift),registor_name,value)
                self.MainDatabase_upload_Work()
                #self.MainPool_update_Request=True
            


        
    def setValues(self, address, value):
        
        """ Sets the requested values of the datastore

        :param address: The starting address
        :param values: The new values to be set
        """
        super(CustomDataBlock, self).setValues(address, value)
        if self.Modbus_debug:
            registor_name=self.register_namedict[address]
            #print("modbus write - ","[{}]".format(address-self.register_shift),registor_name,"-",value)

        # whatever you want to do with the written value is done here,
        # however make sure not to do too much work here or it will
        # block the server, espectially if the server is being written
        # to very quickly
        #while self.update_lock:
        #    pass

        self.modbus_setValues_Work(address,value)

        #modbus_setValues_thread = threading.Thread(target = self.modbus_setValues_Work,daemon=True,args=[address,value])
        #modbus_setValues_thread.start()
        
        


    

    def modbusDatabase_update_Work(self):
    
        while 1:
            getItem=MemoryUnit()
            getItem=self.queuepool["modbus_Write_Queue"].get()


            if getItem.pool_name=="Modbus Registor Pool - Registor":
                unit=self.memorypool["Modbus Registor Pool - Registor"][getItem.registor_name]
                self.register_dict[unit.registor_number+self.register_shift]=unit.getModbusValue()
                #self.setValues(unit.registor_number+self.register_shift, unit.getModbusValue())

                registor_name=self.register_namedict[unit.registor_number+self.register_shift]
                if self.Modbus_debug:
                    print("modbus update from PC - ","[{}]".format(unit.registor_number),registor_name,unit.getModbusValue())

                super(CustomDataBlock, self).setValues(unit.registor_number+self.register_shift, unit.getModbusValue())

                #self.memorypool["Modbus Registor Pool - Registor"]
                self.Modbuspool[getItem.registor_name].setValue(unit.value)
                #self.Modbuspool=self.memorypool["Modbus Registor Pool - Registor"]

                if (unit.registor_number<=9999 or 
                    (unit.registor_number<=10229 and unit.registor_number>=10200)):
                
                    registor_name=self.register_namedict[10160+self.register_shift]
                    if self.Modbus_debug:
                        print("modbus update write - ","[10160]".format(10160),registor_name,1)
                    super(CustomDataBlock, self).setValues(10160+self.register_shift, 1)
                




def run_async_server(PoolSemaphore,memorypool,queuePool,eventPool):
    
    block  = CustomDataBlock(PoolSemaphore,memorypool,queuePool,eventPool)
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
    StartTcpServer(context, identity=identity, address=(local_IP_address, 506))
    

if __name__ == "__main__":


    run_async_server()

