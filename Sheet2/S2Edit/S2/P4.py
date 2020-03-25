#P4:
print("P4:")

S = [ 'abc' , 'def' , 'hij' , 'abc' , 'fhg' , 'jkl' , 'jpr' ]
item = str ( input ( "Enter the item to find:" ))
P = [] 
i = 0
for s in S:
    if s == item:
        P = P + [i]
    i = i + 1
if  len (P)> 0:
    print ( "Positions of the entry of an element" , item, "in the list" )
    print (P)
else :
    print ( "Element" , item, "not in the list" ) 






