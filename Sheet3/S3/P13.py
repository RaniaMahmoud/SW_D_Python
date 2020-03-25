num=[1,3,4,7,9,11,12,4,5,6]
result=list(map(lambda n : n%2 == 0,num))
print(result)
for res in range(10):
    if result[res]:
        print(num[res],end=" ")
"""         print(res) """

""" list1 = [10, 21, 4, 45, 66, 93, 11]  
even_nos = list(filter(lambda x: (x % 2 == 0), list1))
print("Even numbers in the list: ", even_nos)  
 """