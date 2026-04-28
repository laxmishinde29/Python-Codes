#polymorphism

class Parent:
    def __init__(self):             #constructor of parent
        print("Inside Parent Constructor")
        

    def fun(self):
        print("Inside Fun method of parent")

class child(Parent):
    def __init__(self):              #parent constructor
        super().__init__()           #parent la call karnya sathi
        print("Inside child constructor")
       

    def fun(self):
        super().fun()
        print("Inside fun method of child")

cobj = child()

cobj.fun()
