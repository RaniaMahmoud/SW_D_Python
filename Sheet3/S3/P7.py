lAph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def stringProg(s,x):
    total=0
    l1=set(s)
    for i in l1:
        for j in lAph:
            if i==j:
                total=total+1
    return total
s= "The quice brown fox jumps over the lazy dog"
t=stringProg(s,len(s))
if 26 == t:
    print("yes")
else:
    print("Not")
