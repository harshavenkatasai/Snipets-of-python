n=int(input())
l=[]
for i in range(n):
    s=input()
    revs=s[::-1]
    # print(revs)
    if s==revs:
        l.append("Yes")
    else:
        l.append("No")
for i in l:
    print(i)
