a=input()
n=len(a)
c=0
for i in range(n-1):
    if a[i-1]==a[i+1]:
        c=c+1
print(c)
