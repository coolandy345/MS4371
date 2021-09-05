import sqlite3
from modbus_TcpServer import ModbusRegistorClass


def loadMemoryPool(memoryPool):

    System_Registor_Database = sqlite3.connect('../Database and Profile/System Registor Structure Database.db')
    cur = System_Registor_Database.cursor()
   
    pool={}
    for row in cur.execute('SELECT * FROM "System Memory Pool" '):
        pool[row[0]]=row[1]
    memoryPool["System Memory"]=pool

    pool={}
    for row in cur.execute('SELECT * FROM "Modbus Registor Pool - Coil" '):

        register=ModbusRegistorClass.ModbusPackage(number       =row[0],
                               name_sub1    =row[1],
                               value        =row[2],
                               access_type  =row[3],
                               comment      =row[4]
                               )
        pool[register.name]=register
    memoryPool["Modbus Coil Memory"]=pool

    pool={}
    for row in cur.execute('SELECT * FROM "Modbus Registor Pool - Registor" '):

        register=ModbusRegistorClass.ModbusPackage(number       =row[0],
                               name_sub1    =row[1],
                               name_sub2    =row[2],
                               name_sub3    =row[3],
                               min          =row[4],
                               value        =row[5],
                               max          =row[6],
                               access_type  =row[7],
                               comment      =row[8]
                               )
        pool[register.name]=register

    memoryPool["Modbus Registor Memory"]=pool




    