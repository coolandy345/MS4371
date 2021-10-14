import sqlite3
from modbus_TcpServer import ModbusRegistorClass
import sys
import os

def get_Abs_path(relative):
    if hasattr(sys, '_MEIPASS'):
        join_path=os.path.join(sys._MEIPASS, relative)
        norm_path=os.path.normpath(join_path)
        return 
    join_path=os.path.join(os.path.abspath(os.getcwd()), relative)
    norm_path=os.path.normpath(join_path)
    return norm_path

def memoryWriteThread(memoryPool):

    database_relative_path="Database and Profile/System Registor Structure Database.db"
    System_Registor_Database = sqlite3.connect(get_Abs_path(database_relative_path))
    cur = System_Registor_Database.cursor()

    while 1:
        memoryPool["EvevtPool"]["MB_memory_Write_Event"]["Event"].wait()
        memoryPool["EvevtPool"]["MB_memory_Write_Event"]["Event"].clear()

        registor_name= memoryPool["EvevtPool"]["MB_memory_Write_Event"]["Registor"]

        Table_name="Modbus Registor Pool - Registor"

        test="Update  '{}' set  Value={} where  Registor_Name='{}'".format(Table_name,memoryPool["Modbus Registor Memory"][registor_name].value,registor_name)
        cur.execute(test)

        System_Registor_Database.commit()
         


def loadMemoryPool(memoryPool):


    database_relative_path="Database and Profile/System Registor Structure Database.db"
    
    System_Registor_Database = sqlite3.connect(get_Abs_path(database_relative_path))
    cur = System_Registor_Database.cursor()

    pool={}
    for row in cur.execute('SELECT * FROM "System Memory Pool" '):
        pool[row[0]]=row[1]
    memoryPool["System Memory"]=pool

    pool={}
    for row in cur.execute('SELECT * FROM "Modbus Registor Pool - Coil" '):
        
        register=ModbusRegistorClass.ModbusPackage(number       =row[0],
                               name         =row[1],
                               value        =row[2],
                               comment      =row[3]
                               )
        pool[register.name]=register
    memoryPool["Modbus Coil Memory"]=pool

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

    memoryPool["Modbus Registor Memory"]=pool

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

    
        




    