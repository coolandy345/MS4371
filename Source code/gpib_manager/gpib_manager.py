from ctypes import cdll 
import sys


class Gpib_manager():

    def __init__(self):
        print("import GPIB-32.dll")
        mydll = cdll.LoadLibrary('GPIB-32.dll')

        Dev=mydll.ibdev(0, 24, 0,11, 1, 0)
        Ret=mydll.ThreadIbsta()
        print(Dev,Ret)


        mydll.ibwrtfA(Dev,"*IDN?",len("*IDN?"))
        Ret=mydll.ThreadIbsta()
        print(Dev,Ret)

        message=""
        mydll.ibrd(Dev, message, 50);
        cnt=mydll.ThreadIbcntl()
        print("get message =",message,cnt)
        Ret=mydll.ThreadIbsta()
        print(Dev,Ret)
