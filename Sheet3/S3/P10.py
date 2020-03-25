num=int(input("Enter Number: "))

def perfectNum(num):
    total=0
    for i in range (1,num):
        if num%i == 0:
            total=total+i
            print(i)
    return total

if perfectNum(num) == num:
    print("isPerfect")
else:
    print("NotPerfect")    