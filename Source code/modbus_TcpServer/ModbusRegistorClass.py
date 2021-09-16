class ModbusPackage():
    def __init__(self,
                 number=0,
                 name="",
                 min=0,
                 value=0,
                 max=1,
                 access_type=0,
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
        self.access_type=access_type
        self.comment=comment

    def getValue():
        return self.value

    def setValue(value):
        if value >self.max:
            value=self.max
            print("Set too large value to this registor ,Register number = ",number)
        elif value<self.min:
            value=self.min
            print("Set too small value to this registor ,Register number = ",number)

        self.value=value

    def getName():
        return self.name

    def getNumber():
        return self.number






