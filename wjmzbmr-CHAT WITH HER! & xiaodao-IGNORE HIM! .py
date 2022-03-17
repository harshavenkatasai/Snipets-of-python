def lToS(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  

def DorS(arr):
   
    G=[]
    for i in arr:
        if i not in G:
            G.append(i)
    print(lToS(G))
    EorO(lToS(G),arr)

def EorO(G,s):
    a=len(G)
    b=len(s)
    c=b-a
    print(c)
    if c%2!=0:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")
    

s=""
DorS(s)
# second method..........
s=input()
c=0
for i  in range(0,len(s)): 
    for j in range(1,len(s)): 
        if (s[i]==s[j]and i!=j): 
            c+=1 
b=c/2  
if(b%2!=0 or b==1):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
