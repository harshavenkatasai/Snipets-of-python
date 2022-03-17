def arraymake():
    c=[]
    total=0
    l1,l2=input().split(" ")
    l1=int(l1)
    l2=int(l2)
    if (l1%2==0 or l2%2==0):
        
        
        lno=list(map(int,input().split(' ')))
        lf=list(map(int,input().split(' ')))
        for i in range(l1):
            if lno[i]%2==1:
                c.append(lf[i])
        for ele in range(0, len(c)):
            total = total + c[ele]
        return total
    

n=int(input())
m=[]
for i in range(n):
    m.append(arraymake())
for j in range(len(m)):
    print(m[j])
