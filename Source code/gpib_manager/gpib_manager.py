#from ctypes import cdll 
import sys
import time
import ctypes

import usb.core



def check_GPIB_device_insert():

    # find our device
    dev = usb.core.find(idVendor=0x0403, idProduct=0x6001)

    # was it found?
    if dev is None:
        raise ValueError('Device not found')
        return False
    else:
        return True



class Gpib_device():

    def __init__(self,
                 address
                 
                 
                 
                 
                 ):










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

        for tim in range(1,4):
        
            send_text = ctypes.create_string_buffer(b"beeper.beep(0.1, 2400)",100)
            send_text.value
            mydll.ibwrt(Dev,send_text,len(send_text))
            Ret=mydll.ThreadIbsta()
            err=mydll.ThreadIberr()
            print(Ret,err)

            time.sleep(0.2)

        ibrsp

        #print("get message =",message,cnt)
        #print(Dev,Ret)
