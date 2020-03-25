num=int(input("Enter Number: "))
n1=0
n2=1
n3=0
l=[]
l.append(n1)
l.append(n2)
for i in range(num+1):
    n3=n1+n2
    l.append(n3)
    n1=n2
    n2=n3
print(l)
