from itertools import permutations as pers
def lToS(s): 
    
    str1 = "" 
    
    for ele in s: 
        str1 += ele  
    return str1 

def Per(str):
    l=[]
    perL = pers(str)
    for p in list(perL):
        l.append(lToS(p))
    return l

s = input()
a=Per(s)
for i in a:
    print(i)
