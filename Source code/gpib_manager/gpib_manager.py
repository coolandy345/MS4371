# -*- coding: utf-8 -*-

#from ctypes import cdll 
import sys
import time
import ctypes
import threading
import time
from registor_manager import *
import copy






class GPIB_package():

    init_type=0
    send_type=1
    read_type=2


    def __init__(self,
                 type=0,
                 command="",
                 name="",
                 address=0,
                 result="",
                 error_message=[]
                 ):
        self.type=type
        self.command=command
        self.name=name
        self.address=address
        self.result=result
        self.error_message=error_message

class GPIB_Driver():
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


    ERR_dict={
        0:"System error",
        1:"Function requires GPIB board to be CIC",
        2:"Write function detected no Listeners",
        3:"Interface board not addressed correctly",
        4:"Invalid argument to function call",
        5:"Function requires GPIB board to be SAC",
        6:"I/O operation aborted",
        7:"Non-existent interface board",
        8:"Error performing DMA",
        10:"I/O operation started before previous operation completed",
        11:"No capability for intended operation",
        12:"File system operation error",
        14:"Command error during device call",
        15:"Serial poll status byte lost",
        16:"SRQ remains asserted",
        20:"The return buffer is fullS",
        21:"Address or board is locked"
        }

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


    def __init__(self,memoryPool,queuePool):
        self.GPIB = ctypes.cdll.LoadLibrary('GPIB-32.dll')


        
        
        self.memoryPool=memoryPool
        self.queuePool=queuePool
        self.dev_descriptor={}

        queue_Thread = threading.Thread(target = self.queue_Work,daemon=True)
        queue_Thread.start()

    def queue_Work(self):
        while 1:
            
            self.getItem=self.queuePool["GPIB_send_queue"].get()
            
            error_code=0
            getMessage=None
            
            if self.getItem.type==GPIB_package.init_type:
                error_code=self.initiail_GPIB_device()
            elif  self.getItem.type==GPIB_package.send_type:
                error_code=self.send_Command(self.getItem.command)
            elif  self.getItem.type==GPIB_package.read_type:
                error_code,getMessage=self.request_Command()

            error_message=self.err_check(error_code)
            
            sendItem=GPIB_package(     type=self.getItem.type,
                                                                 command=self.getItem.command,
                                                                 name=self.getItem.name,
                                                                 result=getMessage,
                                                                 error_message=error_message)

            self.queuePool["GPIB_{}_queue".format(self.getItem.name)].put(sendItem)
            

    
    def initiail_GPIB_device(self):
        byte_string="GPIB0".encode("utf8")
        self.send_buffer= ctypes.create_string_buffer(byte_string)
        self.board_descriptor=self.GPIB.ibfindW(self.send_buffer)
        self.GPIB.ibdma(self.board_descriptor,1)

        self.dev_descriptor[self.getItem.name]=self.GPIB.ibdev(0,self.getItem.address,0,self.T30ms, 1, 0)
        self.GPIB.ibclr(self.dev_descriptor[self.getItem.name])
        Ret=self.GPIB.ThreadIbsta()
        err=self.GPIB.ThreadIberr()
        if ((Ret & self.ERR) != 0):
            return err
        else:
            return 0

    def request_Command(self):

        error=0
        
        error,result=self.get_Value()
        return error,result

    def err_check(self,error_code):
        list=[]
        for bit in self.ERR_dict.keys():

            if ((error_code & 1<<bit) != 0):
                list.append(self.ERR_dict[bit])

        return list


    def send_Command(self,command):
        test=time.time()
        byte_string=command.encode("utf8")
        self.send_buffer= ctypes.create_string_buffer(byte_string)

        self.GPIB.ibwrt(self.dev_descriptor[self.getItem.name],self.send_buffer,self.send_buffer._length_)
        
        Ret=self.GPIB.ThreadIbsta()
        err=self.GPIB.ThreadIberr()
        
        if ((Ret & self.ERR) != 0):
            return err
        else:
            return 0

    def get_Value(self):

        read_buffer= ctypes.create_string_buffer(1000)
        self.GPIB.ibrd(self.dev_descriptor[self.getItem.name],read_buffer,read_buffer._length_)
        Ret=self.GPIB.ThreadIbsta()
        err=self.GPIB.ThreadIberr()
        
        
        if ((Ret & self.ERR) != 0):
            return err,None
        else:
            result=read_buffer.value.decode("utf8")
            return 0,result

class GPIB_device():
    def __init__(self,memoryPool,queuePool,address,name):
        
        self.address=address
        self.connection = False
        self.dev_descriptor=0
        self.device_IDN=""
        self.name=name
        self.memoryPool=memoryPool
        self.queuePool=queuePool

        self.test=0
        
        self.set_memorypool_register("System memory","{} connection".format(self.name),0)
        
        connnection_check_Thread = threading.Thread(target = self.connnection_check_Work,daemon=True)
        connnection_check_Thread.start()

    def initiail_GPIB_device(self):

        sendItem=GPIB_package(
                type=GPIB_package.init_type,
                command="",
                name=self.name,
                address=self.address
            )
        
        self.queuePool["GPIB_send_queue"].put(sendItem)
        getItem=self.queuePool["GPIB_{}_queue".format(self.name)].get()

        #If we have any error code
        if len(getItem.error_message):
            self.connect_action(False)
            print("Fail init device at adress {} Error is {}".format(self.address,getItem.error_message))
            return getItem.error_message
        else:
            print("secess init GPIB device at {}".format(self.name))
            self.connect_action(True)
            self.send_Command("reset()")
            self.send_Command("*CLS")
            self.send_Command("beeper.beep(0.1, 2400)")
            return None

    
    def connect_action(self,connect):

        self.connection=connect
        self.set_memorypool_register("System memory","{} connection".format(self.name),self.connection)


        
         #if self.connection!=connect:

         #    self.connection=connect
         #    if self.connection:
         #       self.set_memorypool_register("System memory","{} connection".format(self.name),1)
         #       print("{} connection".format(self.name),1)
         #    else:
         #       self.set_memorypool_register("System memory","{} connection".format(self.name),0)
         #       print("{} connection".format(self.name),0)

    def connnection_check_Work(self):
        
        while 1:
            #print("connnection_check_Loop time1 is ",time.time()-test)
            
            if self.connection:
                pass
                #self.send_Command("*IDN?")
                #result,error_code=self.read_Command()
                ##print("get connection check message of  {} -- result is {} , errorcode is {}".format(self.name,result,error_code))
                ##If we have any error code
                #if len(error_code):
                #    self.connect_action(False)
                #else:
                #    self.device_IDN=result
                #    self.connect_action(True)
            else:
                #print("fail connection check at {}".format(self.name))
                self.initiail_GPIB_device()
            
            #print("connnection_check_Work time3 is ",time.time()-test)
            time.sleep(1)

    def  send_Command(self,messgae):
        if not self.connection:
            return "No connection"

        sendItem=GPIB_package(
                type=GPIB_package.send_type,
                command=messgae,
                name=self.name,
                address=self.address
            )
        
        self.queuePool["GPIB_send_queue"].put(sendItem)
        getItem=self.queuePool["GPIB_{}_queue".format(self.name)].get()
        #If we have any error code
        if len(getItem.error_message):
            self.connect_action(False)
        else:
            self.device_IDN=getItem.result
            self.connect_action(True)

        return getItem.error_message

    def  read_Command(self):
        if not self.connection:
            return "","No connection"

        sendItem=GPIB_package(
                type=GPIB_package.read_type,
                name=self.name,
                address=self.address
            )
        
        self.queuePool["GPIB_send_queue"].put(sendItem)
        getItem=self.queuePool["GPIB_{}_queue".format(self.name)].get()
        #If we have any error code
        if len(getItem.error_message):
            self.connect_action(False)
            return "",getItem.error_message
        else:
            self.device_IDN=getItem.result
            self.connect_action(True)
            return getItem.result , getItem.error_message

        


    def set_memorypool_register(self,memorypool_name,registor_name,value):
        
        if self.memoryPool[memorypool_name][registor_name].getValue()!=value:

            sub_memorypool=copy.deepcopy(self.memoryPool[memorypool_name])
            sub_memorypool[registor_name].setValue(value)

            self.memoryPool[memorypool_name]=sub_memorypool
            sendItem=MemoryUnit(memorypool_name,registor_name)
            self.queuePool["database_Uplaod_Queue"].put(sendItem)
            self.queuePool["memory_DownlaodToGUI_request_Queue"].put(sendItem)


        

class GPIB_device_2635B(GPIB_device):
    def __init__(self,memoryPool,queuePool):
        self.memoryPool=memoryPool
        self.queuePool=queuePool
        
        super().__init__(memoryPool,queuePool,address=self.memoryPool["System memory"]["2635B GPIB address"].getValue(),name="2635B")


    

class GPIB_device_2657A(GPIB_device):
    def __init__(self,memoryPool,queuePool):
        self.memoryPool=memoryPool
        self.queuePool=queuePool

        super().__init__(memoryPool,queuePool,address=self.memoryPool["System memory"]["2657A GPIB address"].getValue(),name="2657A")



