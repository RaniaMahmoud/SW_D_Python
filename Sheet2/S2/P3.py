#P3:
print("P3:")
l1=["sat","tasa","asd"]
l2=[]
c='t'
n=3
i=0
while i<n:
    j=0
    k=0
    while j<len(l1[i]):
        if l1[i][j]==c:
            k+=1
        j+=1
    l2=l2+[k]
    
    i+=1
    
print(l2)
