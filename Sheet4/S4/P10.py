list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
l=[x for x in list1 if x != ""]
print (l)
r= list(filter(None,list1))
print(r)