class ModbusPackage():
    def __init__(self,
                 number=0,
                 name="",
                 min=0,
                 value=0,
                 max=1,
                 default=0,
                 volatile_type=0,
                 comment=""
                 ):
        self.registor_number=number
        self.name=name
        self.min=min
        if not value==None:
            self.value=value
        else:
            self.value=self.min
        self.max=max
        self.default=default
        self.volatile_type=volatile_type
        self.comment=comment

        if self.volatile_type:
            self.value=self.default

    def print_Package_Contant(self):
        print("self.registor_number =",self.registor_number)
        print("self.name =",self.name)
        print("self.min =",self.min)
        print("self.value =",self.value)
        print("self.max =",self.max)
        print("self.access_type =",self.access_type)
        print("self.comment =",self.comment)

    def getValue(self):
        if isinstance(self.value, int):
            return self.value
        else:
            return 0

    def setValue(self,value):
        
        if type(self.max)=="NoneType" and type(self.min)=="NoneType":
            if value >self.max:
                value=self.max
                print("Set too large value to this registor ,Register number = ",self.registor_number)
                return
            elif value<self.min:
                value=self.min
                print("Set too small value to this registor ,Register number = ",self.registor_number)
                return
        
        self.value=value

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number






