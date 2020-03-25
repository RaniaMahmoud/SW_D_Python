def PT(n):
    t=[1]
    y=[0]
    for x in range(max(n,0)):
        print(t)
        t=[l+r for l,r in zip(t+y,y+t)]
    return n>=1
PT(6)

