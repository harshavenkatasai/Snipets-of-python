k,num = input().split()
num=int(num)
k= int(k)
for i in range(0, num):
    for j in range(0, i+1):
        print(k, end="")
    k = k + 1
    print()
k = k - 2
for i in range(0, num):
    for j in range(0, num-i-1):
        print(k, end="")
    k = k - 1
    print()
