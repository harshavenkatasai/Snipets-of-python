n = int(input())
a= n**2
Rev=0
    
while(a > 0):    
    Rem = a %10    
    Rev = (Rev *10) + Rem    
    a = a //10 
b=Rev%10
print(b)
