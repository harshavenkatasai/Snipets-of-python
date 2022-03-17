def re_vowel(string,vowels):
    k=string
    for x in k: 
        if x  in vowels: 
            k = k.replace(x, "$") 
    print(k) 
def re_conconents(string,vowels):
    a=string
    for x in a: 
        if x not in vowels: 
            a = a.replace(x, "#") 
    print(a)   
def re_cap(string):
    print(string.upper()) 
string = "Pavani"
vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U') 
re_vowel(string,vowels)
re_conconents(string,vowels)
re_cap(string)
