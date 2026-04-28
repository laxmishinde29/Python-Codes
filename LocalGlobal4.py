No = 11     

def fun():    
    global No = 21
    print("Value of No from Fun is : ",No)      #11
    No = No + 1         #  12
    print("Value of No from Fun is : ",No)      #12

print("Value of No is :",No)        #11
fun()
print("Value of No is :",No)        #21