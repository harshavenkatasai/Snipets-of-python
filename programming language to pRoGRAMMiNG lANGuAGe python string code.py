ef dupe(s):
    l=[]
    for i in range(0, len(s)):  
        count = 1  
        for j in range(i+1, len(s)):  
            if(s[i] == s[j] and s[i] != ' '):  
                count = count + 1  
                s = s[:j] + '0' + s[j+1:]  
   
        if(count > 1 and s[i] != '0'):  
            l.append(s[i]) 
    return l
def lToS(s):  
    str1 = ""  
    
    for ele in s:  
        str1 += ele   
    return str1
s="programming language"
a=lToS(dupe(s))
s=list(s)
for i in range(len(s)):
    for j in a:
        if s[i]==j:
            s[i]=j.upper()

print(lToS(s))     
