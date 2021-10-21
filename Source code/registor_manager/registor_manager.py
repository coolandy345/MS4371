import sqlite3
from modbus_TcpServer import ModbusRegistorClass
import sys
import os
import time
import threading

def get_Abs_path(relative):
    if hasattr(sys, '_MEIPASS'):
        join_path=os.path.join(sys._MEIPASS, relative)
        norm_path=os.path.normpath(join_path)
        return 
    join_path=os.path.join(os.path.abspath(os.getcwd()), relative)
    norm_path=os.path.normpath(join_path)
    return norm_path

class MemoryUnit():

    def __init__(self,
                 Main_memorypool="",
                 memory_name=""):
        self.Main_memorypool=Main_memorypool
        self.memory_name=memory_name



def databaseWriteThread(memoryPool,queuePool):

    database_relative_path="Database and Profile/System Registor Structure Database.db"
    System_Registor_Database = sqlite3.connect(get_Abs_path(database_relative_path))
    cur = System_Registor_Database.cursor()

    while 1:
        getItem=MemoryUnit()
        getItem=queuePool["memory_Write_Queue"].get()
        queuePool["modbus_Write_Queue"].put(getItem)
        time.sleep(0.5)
        
        if not memoryPool[getItem.Main_memorypool][getItem.memory_name].volatile_type:
            test="Update  '{}' set  Value='{}' where  Registor_Name='{}'".format(getItem.Main_memorypool,memoryPool[getItem.Main_memorypool][getItem.memory_name].value,getItem.memory_name)
            #print(test)
            cur.execute(test)
            #memoryPool[getItem.Main_memorypool][getItem.memory_name].print_Package_Contant()
            
        while not queuePool["memory_Write_Queue"].empty():
            getItem=queuePool["memory_Write_Queue"].get()
            queuePool["modbus_Write_Queue"].put(getItem)

            if not memoryPool[getItem.Main_memorypool][getItem.memory_name].volatile_type:
                test="Update  '{}' set  Value='{}' where  Registor_Name='{}'".format(getItem.Main_memorypool,memoryPool[getItem.Main_memorypool][getItem.memory_name].value,getItem.memory_name)
                #print(test)
                cur.execute(test)

                #memoryPool[getItem.Main_memorypool][getItem.memory_name].print_Package_Contant()
         

        System_Registor_Database.commit()
         


def databaseLoadThread(memoryPool):


    database_relative_path="Database and Profile/System Registor Structure Database.db"
    
    System_Registor_Database = sqlite3.connect(get_Abs_path(database_relative_path))
    cur = System_Registor_Database.cursor()

    

    pool={}
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

    datalist=[]
    for row in cur.execute('SELECT * FROM "Read Measurement Data" '):

        register=ModbusRegistorClass.MeasurePackage(
                                time                =row[0],
                                valtage         =row[1],
                                current         =row[2],
                                resistor         =row[3],
                                duration               =row[4],
                                temperature           =row[5]
                               )
        datalist.append(register)

    memoryPool["Read Measurement Data"]=datalist

    
    System_Registor_Database.commit()
    System_Registor_Database.close()

    
        




    