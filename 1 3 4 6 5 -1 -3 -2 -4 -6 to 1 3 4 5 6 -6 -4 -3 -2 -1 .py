l=list(map(int,input().strip().split()))
a=[]
b=[]
for i in l:
    if i >=0:
        a.append(i)
    elif i<0:
        b.append(i)
a=sorted(a)
b=sorted(b)
print(a+b)
