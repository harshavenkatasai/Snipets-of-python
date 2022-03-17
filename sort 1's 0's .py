def arraymake():
    c=0
    l1=int(input())
    l=list(map(int,input().split(' ')))
    
    for i in range(l1):
        if l[i]==0:
            c=c+1
    return c

n=int(input())
m=[]
for i in range(n):
    k=arraymake()
    m.append(k)
for j in range(n):
    print(m[j])
