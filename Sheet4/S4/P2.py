a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
l=[]
if len(a) >=len(b):
    for i in b :
        for j in a:
            if i==j:
                l=l+[j]
else:
    for i in b :
        for j in a:
            if i==j:
                l=l+[j]
print(list(dict.fromkeys(l)))