#System module import
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

#local module import
from registor_manager import RegistorManager

if __name__ == "__main__":

    SystemMemoryPool=Manager()
    ns = SystemMemoryPool.Namespace()
    RegistorManager.loadMemoryPool(ns)

    with ProcessPoolExecutor(max_workers=10) as executor:
        print("hello")