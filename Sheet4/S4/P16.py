import operator as o
from functools import reduce as r
print(o.add(1,2))

print(r(lambda x,y:x+y,range(100)))

def Sum():
    s=0
    for i in range(100):
        s+=i
    return s
print(Sum())