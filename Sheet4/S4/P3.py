import math as m
num=int(input("Enter Number: "))
flag= True
if num>1:
    for i in range (2,int(num/2)+1):
        if num%i == 0:
            print ("notPrime")
            break
    else:
        print("Prime")
else:
    print ("notPrime")
