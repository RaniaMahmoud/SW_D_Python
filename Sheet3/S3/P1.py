def palin(s):
    if s==s[::-1]:
        return True
    else:
        return False

s=input("Enter String: ")
if(palin(s)):
    print("pal")
else:
    print("not")