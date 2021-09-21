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

    
        




    