s=input()
x,y=(0,0)
for i in s:
    if (i=="L"):
        x=x-1
    elif (i=="D"):
        y=y-1
    elif(i=="U"):
        y=y+1
    elif (i=="R"):
        x=x+1
print("(%d,%d)"%(x,y))
