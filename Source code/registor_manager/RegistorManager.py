import sqlite3
from multiprocessing import Manager

def loadMemoryPool(namespace):

    System_Registor_Database = sqlite3.connect('../Database and Profile/System Registor Structure Database.db')
    cur = System_Registor_Database.cursor()
    
    Dict={}
    for row in cur.execute('SELECT * FROM "System Memory Pool"'):
        Dict[row[0]]=[row[1],row[2]]

    print(Dict)
    print(Dict["CR1"])