n=int(input())
a=0
for i in range(1,n):
    if (n%i==0):
        a=a+i
if a>n:
    print("Yes the number is abonded")
else:
    ("No the number is not abonded")
