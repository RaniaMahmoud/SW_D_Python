
#P5:
print("P5:")
import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = (b * b) - (4 * a * c)

if(d > 0):
    root1 = (-b + math.sqrt(d) / (2 * a))
    root2 = (-b - math.sqrt(d) / (2 * a))
    print("Two Distinct Real Roots Exists: root1 = {} and root2 = {}".format(root1, root2))
elif(d == 0):
    root1 = root2 = -b / (2 * a)
    print("Two Equal and Real Roots Exists: root1 = {} and root2 = {}".format(root1, root2))
elif(d < 0):
    root1 = root2 = -b / (2 * a)
    i = math.sqrt(-d) / (2 * a)
    x=root1+i
    y=root1-i
    print("Two Distinct Complex Roots Exists: root1 = {} and root2 = {}".format(x, y))
