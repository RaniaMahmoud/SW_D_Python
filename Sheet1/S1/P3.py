#P3:
from datetime import timedelta as t
from datetime import date as d
print ("P3:")
nam = str(input("Enter your name:"))
age = int(input("Enter your age:"))
##calc = 2020+(100-age)
d1=d(2014,7,2)
calc=d1+t(days=100)
#print("\n")
print("In {} you will be 100 years old".format(calc.year))
print ("\n")

