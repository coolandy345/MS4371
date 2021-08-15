
# --------------------------------------------------------------------------- # 
# System module import
# --------------------------------------------------------------------------- # 
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager
from modbusTcpServer import ModbusTcpServer

# --------------------------------------------------------------------------- # 
# local module import
# --------------------------------------------------------------------------- # 
from registor_manager import RegistorManager
import time

def hello():
    while 1:
        print("Hello")
        time.sleep(1)

if __name__ == "__main__":

    #Memory Prepare
    MemoryPoolManager=Manager()
    MemoryPool = MemoryPoolManager.dict()
    RegistorManager.loadMemoryPool(MemoryPool)
    
    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.submit(ModbusTcpServer.run_async_server)
        executor.submit(hello)
        print(MemoryPool)