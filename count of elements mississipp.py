s=input()
n=len(s)
c=0
for i  in range(n):
    for j in range(n):
        if (s[i]==s[j]):
            c=c+1
    print(s[i],"-",c)
