""" import random as r
lAph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lUper=[(str(x)).upper() for x in lAph ]
lSympol=['*','-',',',':',';','*','^','@','!','$','#','%','(',')','=','+','/']
lNumber=[0,1,2,3,4,5,6,7,8,9]
def pas(l1,l2,l3,l4):
    x1=r.choice(l1)
    x2=r.choice(l2)
    x3=r.choice(l3)
    x4=str(r.choice(l4))
    return x1+x2+x3+x4
print(pas(lAph,lUper,lSympol,lNumber))
 """
import string
import random
t=''
num=int(input('How many characters in your password?'))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
for x in range(num+1):
    t+=random.choice(s)
print(t)

""" def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?')))) """