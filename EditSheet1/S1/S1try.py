import calendar as c
from datetime import datetime as t
from datetime import date as d
from datetime import timedelta as td

""" m=c.month(2020,3)
print(m)
cl=c.calendar(2020,m=2)
print (cl) """

""" tnow=t.now()
tim1=tnow.strftime("%H:%M:%S")
tim2=tnow.strftime("%d-%m-%y")
print(tim1," ",tim2) """

""" age = int(input("Enter your age:"))
hundred = int((100-age) + t.now().year)
print(hundred) """
""" 
fn="Ran"
Ln="mah"
print(Ln[::-1],"",fn[::-1]) 
exam_st_date=(7,3,2020)
print("%i/%i/%i"%exam_st_date) """

print((d(2020,7,10) - d(2020,7,5)).days)