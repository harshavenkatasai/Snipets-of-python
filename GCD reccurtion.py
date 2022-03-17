def gcd(a,b):
    if (b==0):
        return a
    
    return gcd(a,a%b)


a=int(input())
b=int(input())
c=gcd(a,b)
print(c)
