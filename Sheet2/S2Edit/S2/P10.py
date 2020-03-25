#P10:
print("P10:")
def fib(x):
    n1=0
    n2=1
    n3=1
    print(n1)
    print(n2)
    for i in range(2,x):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3


x=int(input("Enter Number:"))
fib(x)

