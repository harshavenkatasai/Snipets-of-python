def reverse(n):
    Reverse = 0    
    while(n > 0):    
        Reminder = n %10    
        Reverse = (Reverse *10) + Reminder    
        n = n //10
    
    return Reverse 
def square(n):
    a=0
    a=n**2
    return a 
def squareroot(n):
    return (n**0.5)


n=int(input())
a=square(n)
a=reverse(a)
a=squareroot(a)
a=reverse(a)
if (a==n):
    print("%d adam number"%n)
else:
    print("%d Not adam"%n)
