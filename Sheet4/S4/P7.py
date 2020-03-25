list1 = ["M", "na", "i", "Ke"]  
list2 = ["y", "me", "s", "lly"]
list3=[]
for x in list1:
    for y in list2:
        if list1.index(x) == list2.index(y):
            list3.append(x+y)    
print (list3)

