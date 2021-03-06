from sqlite3 import connect as sqlite3_connect
from modbus_TcpServer import ModbusRegistorClass
import sys
import os
from time import time,sleep

def get_Abs_path(relative):
    if hasattr(sys, '_MEIPASS'):
        join_path=os.path.join(sys._MEIPASS, relative)
        norm_path=os.path.normpath(join_path)
        return 
    join_path=os.path.join(os.path.abspath(os.getcwd()), relative)
    norm_path=os.path.normpath(join_path)
    return relative

class MemoryUnit():

    def __init__(self,
                 pool_name="",
                 registor_name="",
                 count=1):
        self.pool_name=pool_name
        self.registor_name=registor_name
        self.count=count

def databaseWriteThread_NoModbusLoop(PoolSemaphore,memoryPool,queuePool,eventPool):

    

    database_relative_path="Database and Profile/System Registor Structure Database.db"
    System_Registor_Database = sqlite3_connect(get_Abs_path(database_relative_path))
    cur = System_Registor_Database.cursor()

    while 1:
        getItem=MemoryUnit()
        getItem=queuePool["database_modbusUplaod_Queue"].get()
        
        sleep(0.1)
        
        test="Update  '{}' set  Value='{}' where  Registor_Name='{}'".format(getItem.pool_name,memoryPool[getItem.pool_name][getItem.registor_name].value,getItem.registor_name)

        cur.execute(test)
            
        while not queuePool["database_Uplaod_Queue"].empty():
            getItem=queuePool["database_Uplaod_Queue"].get()
            

            test="Update  '{}' set  Value='{}' where  Registor_Name='{}'".format(getItem.pool_name,memoryPool[getItem.pool_name][getItem.registor_name].value,getItem.registor_name)

            cur.execute(test)
         

        System_Registor_Database.commit()

def databaseWriteThread(PoolSemaphore,memoryPool,queuePool,eventPool):
    

    database_relative_path="Database and Profile/System Registor Structure Database.db"
    System_Registor_Database = sqlite3_connect(get_Abs_path(database_relative_path))
    cur = System_Registor_Database.cursor()

    while 1:
        getItem=MemoryUnit()
        getItem=queuePool["database_Uplaod_Queue"].get()
        queuePool["modbus_Write_Queue"].put(getItem)
        
        sleep(0.1)
        
        test="Update  '{}' set  Value='{}' where  Registor_Name='{}'".format(getItem.pool_name,memoryPool[getItem.pool_name][getItem.registor_name].value,getItem.registor_name)

        cur.execute(test)
            
        while not queuePool["database_Uplaod_Queue"].empty():
            getItem=queuePool["database_Uplaod_Queue"].get()
            queuePool["modbus_Write_Queue"].put(getItem)
            

            test="Update  '{}' set  Value='{}' where  Registor_Name='{}'".format(getItem.pool_name,memoryPool[getItem.pool_name][getItem.registor_name].value,getItem.registor_name)
            #print(test)
            cur.execute(test)
         

        System_Registor_Database.commit()
         


def databaseLoadThread(memoryPool):

    # test_time=time()

    database_relative_path="Database and Profile/System Registor Structure Database.db"
    
    System_Registor_Database = sqlite3_connect(get_Abs_path(database_relative_path))
    cur = System_Registor_Database.cursor()

    memoryPool["Measurement_data"]=None

    pool={}
    
    full_Range_list=list(range(0,10300))
    for row in cur.execute('SELECT * FROM "Modbus Registor Pool - Registor" '):

        register=ModbusRegistorClass.ModbusPackage(number       =row[0],
                               name         =row[1],
                               min              =row[2],
                               value            =row[3],
                               max              =row[4],
                               default          =row[5],
                               volatile_type   =row[6],
                               comment      =row[7]
                               )
        pool[register.name]=register
        
        full_Range_list.remove(row[0])

    for unit in full_Range_list:
        pool["blank_pos_{}".format(unit)]=ModbusRegistorClass.ModbusPackage(name="blank_pos_{}".format(unit),number=unit)

    memoryPool["Modbus Registor Pool - Registor"]=pool

 


    pool={}
    for row in cur.execute('SELECT * FROM "Measurement Pattern" '):

        register=ModbusRegistorClass.ModbusPackage(number       =row[0],
                               name         =row[1],
                               min          =row[2],
                               value        =row[3],
                               max          =row[4],
                               comment      =row[5]
                               )
        pool[register.name]=register

    memoryPool["Measurement Pattern"]=pool

    pool={}
    for row in cur.execute('SELECT * FROM "System memory" '):

        register=ModbusRegistorClass.ModbusPackage(
                               name         =row[0],
                               value        =row[1],
                               comment      =row[2]
                               )
        pool[register.name]=register

    memoryPool["System memory"]=pool




    
    System_Registor_Database.commit()
    System_Registor_Database.close()

    # print(time()-test_time)

    

    




    