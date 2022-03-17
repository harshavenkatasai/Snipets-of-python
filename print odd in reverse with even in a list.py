n=int(input())
a=[]
b=[]
c=[]
l=list(map(int, input().split()))
for i in l:
    if (i%2==0):
        a.append(i)
    elif (i%2!=0):
        b.append(i)
a=sorted(a)
# print(a)
b=sorted(b)
# print(b)
b.reverse()
# print(b)
c=b+a
print(*c, sep=' ')
