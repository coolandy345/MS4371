import sqlite3


def loadMemoryPool(memoryPool):

    System_Registor_Database = sqlite3.connect('../Database and Profile/System Registor Structure Database.db')
    cur = System_Registor_Database.cursor()
   
    for row in cur.execute('SELECT * FROM "System Memory Pool" '):
        memoryPool[row[0]]=[row[1],row[2]]

    