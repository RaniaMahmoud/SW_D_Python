from functools import reduce as r
def simulateReduce(L1):
    return r(lambda x,y:x+y,L1)
l1=[5,8,6,1,3,4]
print(simulateReduce(l1))