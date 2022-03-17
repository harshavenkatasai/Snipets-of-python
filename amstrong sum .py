def amstrong(n):
    s=0
    
    n=str(n)
    ln=len(n)
    print(ln)
    n=int(n)
    while(n>0):
        a=n%10
        s=s+(a**ln)
        n=n/10
    if (s==n):
        print("Y")
        return 0
    else:
        return 1

n=int(input())
add=0
c=amstrong(n)
if (c==0):
    print("Yes")
  
elif(c==1):
    print("No")
    
