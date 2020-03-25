#P1:
print("P1")
A=[5,4,8,15,30]
i=0
while i<len(A):
    if(A[i]%5==0):
        print(A[i])
    i+=1

x=[ x for x in A if(x%5==0)]   
print(x)