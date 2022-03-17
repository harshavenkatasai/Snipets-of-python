def fact(z):
    if (z>=1):
        return z*fact(z-1)
    else:
        return 1
a,b=input().split()
a=int(a)
b=int(b)
if a>b:
    s=a
    p=b
elif (a<b):
    s=b
    p=a
else:
    s=a
    p=b
npr= (fact(s)/fact(s-p))
npr=int(npr)
print(npr)
