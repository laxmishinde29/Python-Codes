class Parent:
    def __init__(self):             #constructor of parent
        print("Inside Parent Constructor")
        self.No1 = 10
        self.No2 = 20

    def fun(self):
        print("Inside Fun method of parent",self.No1, self.No2)

class child(Parent):
    def __init__(self):              #parent constructor
        super().__init__()           #parent la call karnya sathi
        print("Inside child constructor")
        self.A = 11
        self.B = 21

    def sun(self):
        print("Inside sun method of child",self.A, self.B, self.No1, self.No2)

cobj = child()

print(cobj.No1)     #10
print(cobj.No2)     #20

print(cobj.A)       #11
print(cobj.B)       #21

cobj.fun()
cobj.sun()
