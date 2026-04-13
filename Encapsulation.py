class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
        print("Object gets created succesfully")

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans

    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans

obj1 = Arithmatic(11,10)
obj2 = Arithmatic(21,20)

Ret = obj1.Addition()
print(Ret)

Ret = obj2.Substraction()
print(Ret)

#binding characteristics and behaviour together (if code contain class it is inheritance)
#magic method = call back method