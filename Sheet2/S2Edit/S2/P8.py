
#P8:
print("P8:")

lis1=[1,2,5,15]
lis2=[4,8,9,13]
l3=[]
i=0
while i<4:
    if lis1[i]%2 == 0:
        l3=lis1+[i]
    elif lis2[i]%2 != 0:
        l3=lis2+[i]
    i+=1
print(l3)
