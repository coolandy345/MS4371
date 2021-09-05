class ModbusPackage():
    def __init__(self,
                 number=0,
                 name_sub1="",
                 name_sub2="",
                 name_sub3="",
                 min=0,
                 value=0,
                 max=1,
                 access_type=0,
                 comment=""
                 ):
        self.registor_number=number
        self.name=""
        if type(name_sub1)==type(self.name) and name_sub1!="":
            self.name+=name_sub1
        if type(name_sub2)==type(self.name) and name_sub2!="":
            self.name+="_"+name_sub2
        if type(name_sub3)==type(self.name) and name_sub3!="":
            self.name+="_"+name_sub3
        self.name_sub1=name_sub1
        self.name_sub2=name_sub2
        self.name_sub3=name_sub3
        self.min=min
        if not value==None:
            self.value=value
        else:
            self.value=self.min
        self.max=max
        self.access_type=access_type
        self.comment=comment

    def getValue():
        return self.value

    def setValue(value):
        if value >self.max:
            value=self.max
            print("Set too large value to this registor")
        elif value<self.min:
            value=self.min
            print("Set too small value to this registor")

        self.value=value

    def getName():
        return self.name

    def getNumber():
        return self.number






