#from ctypes import cdll 
import sys
import time
import ctypes
import usb.core





def check_GPIB_device_insert():
    # find our device
    dev = usb.core.find(idVendor=0x0483, idProduct=0x374B)

    # was it found?
    if dev is None:
        return False
    else:
        return True



class GPIB_device():

    #  Status bit mask in ibsta
    ERR     =0x8000     # Error detected
    TIMO    =0x4000     # Timeout occured
    END     =0x2000     # EOI or EOS detected
    SRQI    =0x1000     # SRQ detected by CIC
    RQS     =0x0800     # Device requested any service
    CMPL    =0x0100     # I/O completed
    LOK     =0x0080     # Local lockout state
    REM     =0x0040     # Remote enable state
    CIC     =0x0020     # Controller-in-Charge state
    ATN     =0x0010     # Attention line asserted
    TACS    =0x0008     # Talker active state
    LACS    =0x0004     # Listener active state
    DTAS    =0x0002     # Device trigger state
    DCAS    =0x0001     # Device clear state


    # Error messages in iberr
    EDVR    =0          # System error
    ECIC    =1          # Function requires GPIB board to be CIC
    ENOL    =2          # Write function detected no Listeners
    EADR    =3          # Interface board not addressed correctly
    EARG    =4          # Invalid argument to function call
    ESAC    =5          # Function requires GPIB board to be SAC
    EABO    =6          # I/O operation aborted
    ENEB    =7          # Non-existent interface board
    EDMA    =8          # Error performing DMA
    EOIP    =10         # I/O operation started before previous operation completed
    ECAP    =11         # No capability for intended operation
    EFSO    =12         # File system operation error
    EBUS    =14         # Command error during device call
    ESTB    =15         # Serial poll status byte lost
    ESRQ    =16         # SRQ remains asserted
    ETAB    =20         # The return buffer is fullS
    ELCK    =21         # Address or board is locked

    S
    # Timeout values and meanings
    T10us   =1          # Timeout of 10 uSec
    T30us   =2          # Timeout of 30 uSec
    T100us  =3          # Timeout of 100 uSec
    T300us  =4          # Timeout of 300 uSec
    T1ms    =5          # Timeout of 1 mSec
    T3ms    =6          # Timeout of 3 mSec
    T10ms   =7          # Timeout of 10 mSec
    T30ms   =8          # Timeout of 30 mSecS
    T100ms  =9          # Timeout of 100 mSec
    T300ms  =10         # Timeout of 300 mSec
    T1s     =11         # Timeout of 1 Sec
    T3s     =12         # Timeout of 3 Sec
    T10s    =13         # Timeout of 10 Sec
    T30s    =14         # Timeout of 30 Sec
    T100s   =15         # Timeout of 100 Sec
    T300s   =16         # Timeout of 300 Sec
    T1000s  =17         # Timeout of 1000 Sec

    def __init__(self,address):
        self.address=address
        self.GPIBdll = ctypes.cdll.LoadLibrary('GPIB-32.dll')


    def initiail_GPIB_device(self):
        Dev=GPIBdll.ibdev(0,self.address,0,8, 1, 0)
        Ret=GPIBdll.ThreadIbsta()
        err=GPIBdll.ThreadIberr()
        print(Ret,err)








        

        send_text = ctypes.create_string_buffer(b"*IDN?",100)
        send_text.value
        GPIBdll.ibwrt(Dev,send_text,len(send_text))
        Ret=GPIBdll.ThreadIbsta()
        err=GPIBdll.ThreadIberr()
        print(Ret,err)

        
        #send_text="Keithley Instruments Inc., Model 2635B, 4490039, 3.3.5                                "
        #print(len(send_text))
        ##GPIBdll.ibrd(int ud, StringBuilder buf, int cnt)
                     
        GPIBdll.ibrd(Dev,send_text, 80)
        cntl=GPIBdll.ThreadIbcntl()
        Ret=GPIBdll.ThreadIbsta()

        err=GPIBdll.ThreadIberr()
        print(cntl,Ret,err,"= ",send_text.value," end")

        for tim in range(1,4):
        
            send_text = ctypes.create_string_buffer(b"beeper.beep(0.1, 2400)",100)
            send_text.value
            GPIBdll.ibwrt(Dev,send_text,len(send_text))
            Ret=GPIBdll.ThreadIbsta()
            err=GPIBdll.ThreadIberr()
            print(Ret,err)

            time.sleep(0.2)

        ibrsp

        #print("get message =",message,cnt)
        #print(Dev,Ret)
