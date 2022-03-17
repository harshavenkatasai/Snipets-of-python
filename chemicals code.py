n=int(input())
l=list(map(int,input().strip().split()))[:n]
l=sorted(l)
l=l[::-1]

if (l[0]+l[1] > l[n-1]*l[n-2]):
    a=l[0]+l[1]
    print(a)
elif (l[0]+l[1] < l[n-1]*l[n-2]):
    a=l[n-1]*l[n-2]
    print(a)
