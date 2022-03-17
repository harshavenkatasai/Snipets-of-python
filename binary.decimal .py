def conbin(n):
    if n>1:
        conbin(n//2)
    print(n%2,end= "")
n= int(input())
conbin(n)
print()
