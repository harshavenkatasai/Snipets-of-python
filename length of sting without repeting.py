n=int(input())
l=[]
for i in range(n):
    s=input()
    k=set(s)
    l.append(len(k))
for j in l:
    print(j)
