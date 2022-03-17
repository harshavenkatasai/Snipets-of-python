n=int(input())
z=[]
for i in range(n):
    a,b,c=input().split()
    a=bin(int(a))[2:]
    print(a)
    b=int(b)
    c=int(c)
    b=b-1
    c=c
    a=list(a)
    l=len(a)
   
for j in range(b,c):
        
        if (a[j]==0):
            a[j]=1
        elif(a[j]==1):
            a[j]=0
        print(a)
    

#1, 50 2 5, output:-44
