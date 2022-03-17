n=int(input())
l=list(map(int,input().strip().split()))
k=[]
for i in range(n):
    mul=1
    for j in range(n):
        if(i!=j):
            mul=mul*l[j]
    k.append(mul)
print(str(k)[1:-1])
