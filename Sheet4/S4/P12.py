list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
Sub = ["h", "i", "j"]
t=0
for x in list1:
    t+=1
    if t==3:
        for y in x:
            t+=1
            if t==5:
                for z in y:
                    t+=1
                    if t==8:    
                        for q in z:
                            z.extend(Sub)
                            break
print(list1)