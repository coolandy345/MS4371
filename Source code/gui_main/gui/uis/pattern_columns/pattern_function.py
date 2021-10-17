from gui_main.gui.widgets import *
import copy

class tempUnit():

    temp_unit_type=0
    test_unit_type=1
    End_unit_type=2


    def __init__(
        self,
        Step_Type=0,
        time_hour=0,
        time_min=0,
        SV=0,
        N2_flowRate=0,
        PID_muffle_No=0,
        PID_heater_No=0,
        time_keep=0,
        test_measure_enable=0,
        test_measure_PatternNo=0
        ):
        
        self.Step_Type=Step_Type
        self.time_hour=time_hour
        self.time_min=time_min
        self.SV=SV
        self.N2_flowRate=N2_flowRate
        self.PID_muffle_No=PID_muffle_No
        self.PID_heater_No=PID_heater_No
        self.time_keep=time_keep
        self.test_measure_enable=test_measure_enable
        self.test_measure_PatternNo=test_measure_PatternNo
        

    def print_unit(self):

        print("Step_Type = ",self.Step_Type)
        print("time_hour = ",self.time_hour)
        print("time_min = ",self.time_min)
        print("SV = ",self.SV)
        print("N2_flowRate = ",self.N2_flowRate)
        print("PID_muffle_No = ",self.PID_muffle_No)
        print("PID_heater_No = ",self.PID_heater_No)
        print("time_keep = ",self.time_keep)
        print("test_measure_enable = ",self.test_measure_enable)
        print("test_measure_PatternNo = ",self.test_measure_PatternNo)

class templist():

    def __init__(
        self,
        name="",
        up_asciicode=0,
        down_asciicode=0,
        comment="",
        active=0,
        step_number=0,
        gas_condition=0,
        RT_measure=0,
        ):

        self.name=name
        self.up_asciicode=up_asciicode
        self.down_asciicode=down_asciicode

        if name!="":
            self.name_string2ASC(self.name)
        elif up_asciicode!="" or down_asciicode!="":
            self.name_ASC2string(self.up_asciicode,self.down_asciicode)

        self.comment=comment
        self.active=active
        self.step_number=step_number   ####
        self.gas_condition=gas_condition
        self.RT_measure=RT_measure
        self.units=[]
        self.units.append(None)
        for _step in range(1,21):
            self.units.append(tempUnit())

        self.check_and_adjust()


    def check_and_adjust(self):
        self.checkData()
        self.checkRule()

    #
    #    Function
    #
    def checkData(self):
        for step in range(1,self.step_number+1):

            if(self.units[step].Step_Type==PyTempStep.Temp_Type):
                pass
            elif (self.units[step].Step_Type==PyTempStep.Test_Type):
                if not(step==0 or step==1):
                    self.units[step].SV=self.units[step-1].SV
                pass
            elif (self.units[step].Step_Type==PyTempStep.End_Type):
                pass

        pass


    

    def checkRule(self):
        errorRule=""

        if self.step_number:
            if(self.units[self.step_number].Step_Type!=PyTempStep.End_Type):
                errorRule+="Endステップ未設定"

            if not self.RT_measure:
                if errorRule:
                    errorRule+=" | "
                errorRule+="RT測定未選択"

            if not self.gas_condition:
                if errorRule:
                    errorRule+=" | "
                errorRule+="雰囲気未選択"


        return errorRule
    
    def set_gas_condition(self,gas_condition):
        if self.gas_condition!=gas_condition:
            self.gas_condition=gas_condition
        self.check_and_adjust()
        
    def set_RT_measure(self,RT_measure):
        if self.RT_measure!=RT_measure:
            self.RT_measure=RT_measure
        self.check_and_adjust()

    def set_Comment(self,comment):
        if self.comment!=comment:
            self.comment=comment

        self.check_and_adjust()

    def set_Active(self,active):
        if self.active!=active:
            self.active=active
        self.check_and_adjust()
    
    #
    #    NAME ASCii code modifly
    #     
    def ASCcode_Set(self,up_asciicode,down_asciicode):
        if self.up_asciicode!=up_asciicode or self.down_asciicode!=down_asciicode:
            self.up_asciicode=up_asciicode
            self.down_asciicode=down_asciicode
            self.name_ASC2string(self.up_asciicode,self.down_asciicode)
        self.check_and_adjust()

    def name_ASC2string(self,up_asciicode,down_asciicode):

        self.name=""
        mask=256

        if up_asciicode!="None":
            while up_asciicode:
                asciinum=up_asciicode%mask
                char = chr(asciinum)
                self.name+=char
                up_asciicode=up_asciicode>>8

        if down_asciicode!="None":
            while down_asciicode:

                asciinum=down_asciicode%mask
                char = chr(asciinum)
                self.name+=char
                down_asciicode=down_asciicode>>8

        return self.name
    def name_Set(self,nameString):
        if self.name!=nameString:
            self.name=nameString
            self.name_string2ASC(self.name)
        self.check_and_adjust()


    def name_string2ASC(self,nameString):

        if len(nameString)<=8:



            
            letter_position=0

            for letter in nameString:
                
                asciinum=ord(letter)
                
                #make upper asc
                if letter_position<=3:
                    asciinum=asciinum<<(8*letter_position)
                    self.up_asciicode+=asciinum
                else:
                    asciinum=asciinum<<(8*(letter_position-4))
                    self.down_asciicode+=asciinum

                letter_position+=1

            return self.up_asciicode,self.down_asciicode

        else:
            print("name is too long")
            return ""

    #
    #    Step modifly
    #  
    def setStep(self,step,input):


        self.units[step].Step_Type=input.Step_Type
        self.units[step].SV=input.SV
        self.units[step].N2_flowRate=input.N2_flowRate
        self.units[step].PID_muffle_No=input.PID_muffle_No
        self.units[step].PID_heater_No=input.PID_heater_No
        self.units[step].test_measure_enable=input.test_measure_enable
        self.units[step].test_measure_PatternNo=input.test_measure_PatternNo
        self.units[step].time_hour=input.time_hour
        self.units[step].time_keep=input.time_keep
        self.units[step].time_min=input.time_min

        self.check_and_adjust()

    def getStep(self,step):

        return copy.deepcopy(self.units[step])

    def print_list(self):
        print("name = ",self.name)
        print("comment = ",self.comment)
        print("active = ",self.active)
        print("step_number = ",self.step_number)
        print("gas_condition = ",self.gas_condition)
        print("RT_measure = ",self.RT_measure)

    

class testUnit():

    def __init__(
        self,
        voltage=0,
        ):
        self.voltage=voltage

    def print_unit(self):

        print("Step_Type = ",self.Step_Type)
        print("voltage = ",self.voltage)

        
class testlist():
    def __init__(
        self,
        name="",
        comment="",
        active=0,
        step_number=0,
        test_time=0,
        test_sampletime=0,
        BG0_test_time=0,
        BG_test_time=0,
        BG_sampletime=0,

        ):
        
        self.name=name
        self.comment=comment
        self.active=active
        self.step_number=step_number
        self.test_time=test_time
        self.test_sampletime=test_sampletime
        self.BG0_test_time=BG0_test_time
        self.BG_test_time=BG_test_time
        self.BG_sampletime=BG_sampletime
        self.units=[]
        self.units.append(None)
        for _step in range(1,9):
            self.units.append(testUnit())

        self.check_and_adjust()

    def check_and_adjust(self):
        self.checkData()
        self.checkRule()

    def checkData(self):
        pass

    def checkRule(self):
        errorRule=""

        return errorRule


    def set_Name(self,name):
        if self.name!=name:
            self.name=name

        self.check_and_adjust()

    def set_Comment(self,comment):
        if self.comment!=comment:
            self.comment=comment

        self.check_and_adjust()

    def set_Active(self,active):
        if self.active!=active:
            self.active=active

        self.check_and_adjust()

    def set_Step_number(self,step_number):
        if self.step_number!=step_number:
            self.step_number=step_number

        self.check_and_adjust()

    def set_Test_time(self,test_time):
        if self.test_time!=test_time:
            self.test_time=test_time

        self.check_and_adjust()

    def set_Test_sampletime(self,test_sampletime):
        if self.test_sampletime!=test_sampletime:
            self.test_sampletime=test_sampletime

        self.check_and_adjust()

    def set_BG0_test_time(self,BG0_test_time):
        if self.BG0_test_time!=BG0_test_time:
            self.BG0_test_time=BG0_test_time

        self.check_and_adjust()

    def set_BG_test_time(self,BG_test_time):
        if self.BG_test_time!=BG_test_time:
            self.BG_test_time=BG_test_time

        self.check_and_adjust()

    def set_BG_sampletime(self,BG_sampletime):
        if self.BG_sampletime!=BG_sampletime:
            self.BG_sampletime=BG_sampletime

        self.check_and_adjust()


    def setStep(self,step,input):

        self.units[step].voltage=input.voltage

        self.check_and_adjust()

    def getStep(self,step):

        return copy.deepcopy(self.units[step])

    def print_list(self):
        print("name = ",self.name)
        print("comment = ",self.comment)
        print("active = ",self.active)
        print("step_number = ",self.step_number)
        print("test_time = ",self.test_time)
        print("test_sampletime = ",self.test_sampletime)
        print("BG0_test_time = ",self.BG0_test_time)
        print("BG_test_time = ",self.BG_test_time)
        print("BG_sampletime = ",self.BG_sampletime)
