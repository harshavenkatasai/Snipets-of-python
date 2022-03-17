n= int(input())
f=0
a=n**2
while (n>0):
    if (n%10 == a%10):
        f=f+1
    n=n/10
    a=a/10
if f<=0:
    print("it is not a automorphic" )
else:
    print("this number is automorphic")
