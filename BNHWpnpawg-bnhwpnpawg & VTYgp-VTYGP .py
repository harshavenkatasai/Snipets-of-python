s="BNHWpnpawg"
u=0
l=0
for i in s:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
if l>u:
    s=s.lower()
elif u>l:
    s=s.upper()
print(s)
