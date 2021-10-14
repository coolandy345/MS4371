import sqlite3
from modbus_TcpServer import ModbusRegistorClass
import sys
import os

import threading

def get_Abs_path(relative):
    if hasattr(sys, '_MEIPASS'):
        join_path=os.path.join(sys._MEIPASS, relative)
        norm_path=os.path.normpath(join_path)
        return 
    join_path=os.path.join(os.path.abspath(os.getcwd()), relative)
    norm_path=os.path.normpath(join_path)
    return norm_path

class memoryUnit():

    def __init__(self,
                 Main_memorypool="",
                 memory_name=""):
        self.Main_memorypool=Main_memorypool
        self.memory_name=memory_name



def memoryWriteThread(memoryPool,queuePool):

    database_relative_path="Database and Profile/System Registor Structure Database.db"
    System_Registor_Database = sqlite3.connect(get_Abs_path(database_relative_path))
    cur = System_Registor_Database.cursor()

    #t = threading.Thread(target = MB_memory_Write_Event_Listener)
    #t = threading.Thread(target = System_memory_Write_Event_Listener)
    #t = threading.Thread(target = System_memory_Write_Event_Listener)
    print(queuePool)
    while 1:
        getItem=memoryUnit()
        getItem=queuePool.get()
        print("getItem = ",getItem)

        test="Update  '{}' set  Value={} where  Registor_Name='{}'".format(getItem.Main_memorypool,memoryPool[getItem.Main_memorypool][getItem.memory_name].value,getItem.memory_name)
        print(test)
        cur.execute(test)

        System_Registor_Database.commit()
         


def loadMemoryPool(memoryPool):


    database_relative_path="Database and Profile/System Registor Structure Database.db"
    
    System_Registor_Database = sqlite3.connect(get_Abs_path(database_relative_path))
    cur = System_Registor_Database.cursor()

    pool={}
    for row in cur.execute('SELECT * FROM "System Memory Pool" '):

        register=ModbusRegistorClass.ModbusPackage(
                               name         =row[0],
                               value        =row[1],
                               comment      =row[2]
                               )
        pool[register.name]=register

    memoryPool["System Memory Pool"]=pool

    pool={}
    for row in cur.execute('SELECT * FROM "Modbus Registor Pool - Coil" '):
        
        register=ModbusRegistorClass.ModbusPackage(number       =row[0],
                               name         =row[1],
                               value        =row[2],
                               comment      =row[3]
                               )
        pool[register.name]=register
    memoryPool["Modbus Registor Pool - Coil"]=pool

    pool={}
    for row in cur.execute('SELECT * FROM "Modbus Registor Pool - Registor" '):

        register=ModbusRegistorClass.ModbusPackage(number       =row[0],
                               name         =row[1],
                               min          =row[2],
                               value        =row[3],
                               max          =row[4],
                               comment      =row[5]
                               )
        pool[register.name]=register

    memoryPool["Modbus Registor Pool - Registor"]=pool

    pool={}
    for row in cur.execute('SELECT * FROM "Test Pattern" '):

        register=ModbusRegistorClass.ModbusPackage(number       =row[0],
                               name         =row[1],
                               min          =row[2],
                               value        =row[3],
                               max          =row[4],
                               comment      =row[5]
                               )
        pool[register.name]=register

    memoryPool["Test Pattern Memory"]=pool

    
    
    System_Registor_Database.commit()
    System_Registor_Database.close()

    
        




    