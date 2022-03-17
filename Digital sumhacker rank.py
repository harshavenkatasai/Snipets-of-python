n,s=input().split()
n=int(n)
s=int(s)
l=[]
for i in range(10,100):
    get_sum = 0
    for digit in str(i):   
      get_sum += int(digit)
      if (get_sum == s):
        l.append(i)
k=l[:-10]
print(*k, sep=' ')
