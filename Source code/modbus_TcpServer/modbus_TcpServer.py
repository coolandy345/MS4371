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


#FORMAT = ('%(asctime)-15s %(threadName)-15s'
#          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
#logging.basicConfig(format=FORMAT)
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)



class CustomDataBlock(ModbusSparseDataBlock):
    """ A datablock that stores the new value in memory
    and performs a custom action after it has been stored.
    """

    def setValues(self, address, value):
        """ Sets the requested values of the datastore

        :param address: The starting address
        :param values: The new values to be set
        """
        super(CustomDataBlock, self).setValues(address, value)

        # whatever you want to do with the written value is done here,
        # however make sure not to do too much work here or it will
        # block the server, espectially if the server is being written
        # to very quickly
        print("wrote {} to {}".format(value, address))

    #def getValues(self, address, count=1):

    #    super(CustomDataBlock, self).getValues(address, count)
    #    print("getValues",address,count)

def database_update_threadJob(modbus_context,memorypool,queuePool):
    
    while 1:
        getItem=MemoryUnit()
        getItem=queuePool["modbus_Write_Queue"].get()

        context  = a
        context[0x01].setValues(0x03,1,[5])

#def database_update_threadJob(a):

#    while 1:
#        print("database_update_threadJob")
#        context  = a
#        context[0x01].setValues(0x03,1,[5])
#        time.sleep(1)



def run_async_server(memorypool,queuePool):
    

    block  = CustomDataBlock([0]*400)
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

    #t = threading.Thread(target = database_update_threadJob,args = (i,))
    t = threading.Thread(target = database_update_threadJob,args = (context,memorypool,queuePool))
    t.start()

    # TCP Server
    local_IP_address=socket.gethostbyname(socket.gethostname())
    StartTcpServer(context, identity=identity, address=(local_IP_address, 502))

    
    # TCP Server with deferred reactor run

    # from twisted.internet import reactor
    # StartTcpServer(context, identity=identity, address=("localhost", 5020),
    #                defer_reactor_run=True)
    # reactor.run()

    # Server with RTU framer
    # StartTcpServer(context, identity=identity, address=("localhost", 5020),
    #                framer=ModbusRtuFramer)

    # UDP Server
    # StartUdpServer(context, identity=identity, address=("127.0.0.1", 5020))

    # RTU Server
    # StartSerialServer(context, identity=identity,
    #                   port='/dev/ttyp0', framer=ModbusRtuFramer)

    # ASCII Server
    # StartSerialServer(context, identity=identity,
    #                   port='/dev/ttyp0', framer=ModbusAsciiFramer)

    # Binary Server
    # StartSerialServer(context, identity=identity,
    #                   port='/dev/ttyp0', framer=ModbusBinaryFramer)


if __name__ == "__main__":


    run_async_server()

