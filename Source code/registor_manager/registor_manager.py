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

    
        




    