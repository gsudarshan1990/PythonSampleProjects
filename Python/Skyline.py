"""
Dene a function called myfunc that takes in a string, and returns a matching string where
every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming
string only contains letters, and don't worry about numbers, spaces or punctuation. The
output string can start with either an uppercase or lowercase letter, so long as letters alternate
throughout the string.

"""

def myfunc(word):
    length=len(word)
    string=''
    for i in range(0,length):
        if i%2==0:
            string=string+word[i].lower()
        else:
            string = string + word[i].upper()
    return string

result=myfunc('sudarshan')
print(result)
