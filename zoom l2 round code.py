l=list(map(int,input("Enter the nubles : ").strip().split()))
n=len(l)
s=[]
for i in range(0, n, 2):
    a=l[i]
    b=l[i+1]
    s.append(a+b)
c=min(s)
for i in range(len(s)):
    if s[i]==c:
        print("jar",i+1)
