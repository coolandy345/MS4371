#from ctypes import cdll 
import sys
import time
import ctypes


class Gpib_manager():

    def __init__(self):

        mydll = ctypes.cdll.LoadLibrary('GPIB-32.dll')

        Dev=mydll.ibdev(0,24,0,8, 1, 0)
        Ret=mydll.ThreadIbsta()
        err=mydll.ThreadIberr()
        print(Ret,err)

        send_text = ctypes.create_string_buffer(b"*IDN?",100)
        send_text.value
        mydll.ibwrt(Dev,send_text,len(send_text))
        Ret=mydll.ThreadIbsta()
        err=mydll.ThreadIberr()
        print(Ret,err)

        
        #send_text="Keithley Instruments Inc., Model 2635B, 4490039, 3.3.5                                "
        #print(len(send_text))
        ##mydll.ibrd(int ud, StringBuilder buf, int cnt)
                     
        mydll.ibrd(Dev,send_text, 80)
        cntl=mydll.ThreadIbcntl()
        Ret=mydll.ThreadIbsta()
        err=mydll.ThreadIberr()
        print(cntl,Ret,err,"= ",send_text.value," end")

        
        send_text = ctypes.create_string_buffer(b"beeper.beep(0.5, 2400)",100)
        send_text.value
        mydll.ibwrt(Dev,send_text,len(send_text))
        Ret=mydll.ThreadIbsta()
        err=mydll.ThreadIberr()
        print(Ret,err)



        

        #print("get message =",message,cnt)
        #print(Dev,Ret)
