n=int(input())
s=0
l=list(map(int,input().split()))
a=min(l)
print(a)
while(n>0):
    n1 = n % 10;
    s=s+n1
    n1 = n / 10;

print(s)

