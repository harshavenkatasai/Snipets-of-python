n=int(input())
l=[]
for i in range(n):
    s=input()
    ls=len(s)
    k=set(s)
    lk=len(k)
    l.append(ls-lk)
for i in l:
    print(i)
