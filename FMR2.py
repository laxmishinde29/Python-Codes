def CheckEven(No):
    return (No % 2 == 0)

def Incerment(No):
    return No+1

def main():
    Data = [11,10,15,20,27,30]
    print("Actual Data is :",Data)

    FData = list(filter(CheckEven, Data))
    print("Data after filter is : ",FData)

    MData = list(map(Incerment, Data))
    print("Data after mapping is :",MData)

if __name__ == "__main__":
    main()