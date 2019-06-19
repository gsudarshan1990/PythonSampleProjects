import re

string1="guru99, eduction is fun"

lst=re.findall(r'^\w+',string1)
print(lst)


string2='we are splitting the words'

lst=re.split(r'\s',string2)
print(lst)
