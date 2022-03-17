import math 
  
def isPerfectSquare(x): 
    sr = math.sqrt(x) 
    return ((sr - math.floor(sr)) == 0) 
  
a=int(input())
if (isPerfectSquare(a)): 
    print("Yes") 
else: 
    print("No")
