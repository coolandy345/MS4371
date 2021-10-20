#from ctypes import cdll 
import sys
import time
import ctypes
import threading
import time
from registor_manager import *

class GPIB_device():

    #  Status bit mask in ibsta
    ERR     =0x8000     # Error detected
    TIMO    =0x4000     # Timeout occured
    END     =0x2000     # EOI or EOS detected
    SRQI    =0x1000     # SRQ detected by CIC
    RQS     =0x0800     # self.gpib_device requested any service
    CMPL    =0x0100     # I/O completed
    LOK     =0x0080     # Local lockout state
    REM     =0x0040     # Remote enable state
    CIC     =0x0020     # Controller-in-Charge state
    ATN     =0x0010     # Attention line asserted
    TACS    =0x0008     # Talker active state
    LACS    =0x0004     # Listener active state
    DTAS    =0x0002     # self.gpib_device trigger state
    DCAS    =0x0001     # self.gpib_device clear state


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
        self.GPIB = ctypes.cdll.LoadLibrary('GPIB-32.dll')
        self.connection = False
        self.dev_descriptor=0
        
        if self.initiail_GPIB_device():
            self.send_Command("beeper.beep(0.1, 2400)")

        connnection_check_Thread = threading.Thread(target = self.connnection_check_Work)
        connnection_check_Thread.start()


    def initiail_GPIB_device(self):

        self.dev_descriptor=self.GPIB.ibdev(0,self.address,0,self.T100ms, 1, 0)
        Ret=self.GPIB.ThreadIbsta()
        err=self.GPIB.ThreadIberr()
        if ((Ret & self.ERR) != 0):
            #print("initiail fail with numer {} device".format(self.address))
            self.connection = False
            return False
        else:
            self.connection = True
            return True

    def request_Command(self,command):
        if self.send_Command(command):
            result = self.get_Value()
            self.connection = True
        else:
            result = False
            self.connection = False
        return result

    def send_Command(self,command):
        if not self.connection:
            if self.initiail_GPIB_device():
                return False

        byte_string=command.encode("utf8")
        send_buffer= ctypes.create_string_buffer(byte_string)
        self.GPIB.ibwrt(self.dev_descriptor,send_buffer,send_buffer._length_)
        Ret=self.GPIB.ThreadIbsta()
        err=self.GPIB.ThreadIberr()
        if ((Ret & self.ERR) != 0):
            #print("fail send data to numer {} device".format(self.address))
            self.connection = False
            return False
        else:
            self.connection = True
            return True

    def get_Value(self):

        read_buffer= ctypes.create_string_buffer(100)

        self.GPIB.ibrd(self.dev_descriptor,read_buffer,read_buffer._length_)

        #cntl=self.GPIB.ThreadIbcntl()
        Ret=self.GPIB.ThreadIbsta()
        err=self.GPIB.ThreadIberr()
        if ((Ret & self.ERR) != 0):
            #print("fail retrive result from numer {} device".format(self.address))
            self.connection = False
            return False
        else:
            result=read_buffer.value.decode("utf8")
            self.connection = True
            return result


    def connnection_check_Work(self):
        
        while 1:
            #int ibln (int ud, int pad, int sad, short *listen)
            read_buffer= ctypes.create_string_buffer(100)
            self.GPIB.ibln(self.dev_descriptor,self.address,self.GPIB.NO_SAD,read_buffer)
            result=read_buffer.value.decode("utf8")
            print(result)
            #self.set_memorypool_register("System memory","2635B connection",self.request_Command("*IDN?"))
            time.sleep(0.5)

        

class GPIB_device_2635B(GPIB_device):
    def __init__(self,memoryPool,queuePool):
        super().__init__(self.memoryPool["System memory"]["2635B GPIB address"].getValue())

        self.memoryPool=memoryPool
        self.queuePool=queuePool

        

    def set_memorypool_register(self,memorypool_name,registor_name,value):
        
        if self.memoryPool[memorypool_name][registor_name].getValue()!=value:

            sub_memorypool=copy.deepcopy(self.memoryPool[memorypool_name])
            sub_memorypool[registor_name].setValue(value)

            self.memoryPool[memorypool_name]=sub_memorypool
            sendItem=MemoryUnit(memorypool_name,registor_name)
            self.queuePool["memory_Write_Queue"].put(sendItem)


    

class GPIB_device_2657A(GPIB_device):
    def __init__(self,memoryPool,queuePool):
        super().__init__(self.memoryPool["System memory"]["2657A GPIB address"].getValue())

        self.memoryPool=memoryPool
        self.queuePool=queuePool

    def initial_device(self):
        self.initiail_GPIB_device()
        self.send_Command("smua.reset()")


    def set_memorypool_register(self,memorypool_name,registor_name,value):
        
        if self.memoryPool[memorypool_name][registor_name].getValue()!=value:

            sub_memorypool=copy.deepcopy(self.memoryPool[memorypool_name])
            sub_memorypool[registor_name].setValue(value)

            self.memoryPool[memorypool_name]=sub_memorypool
            sendItem=MemoryUnit(memorypool_name,registor_name)
            self.queuePool["memory_Write_Queue"].put(sendItem)


