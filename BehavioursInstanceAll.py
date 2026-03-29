class Demo:
    No = 10

    def __init__(self,A,B):  #instant variable
        self.Value1 = A
        self.Value2 = B

    def fun(self):          #instant method
        print("Inside instance method fun :",self.Value1, self.Value2)

    @classmethod
    def sun(cls):
        print("Inside class method :",cls.No)

    @staticmethod
    def gun():
        print("Inside static method gun",Demo.No)

Demo.sun()
print("Class variable No :",Demo.No)

obj = Demo(11,21)

obj.fun()
print("Instance in variable :",obj.Value1,obj.Value2)

Demo.gun()