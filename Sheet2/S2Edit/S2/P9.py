
#P9: n <= 10000
import math as m
print("P9:")
n=10000
p=True
for i in range(2,int(m.sqrt(n)+1)):
    if (n % i == 0):
        p=False
        break    
if p:
    print("prime")
else:
    print("notPrime")

