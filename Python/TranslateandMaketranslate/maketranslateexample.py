string1='abcde'
dict1={'a':'1','b':'2'}
table=string1.maketrans(dict1)
print(table)


string2='how are you'
str1='aeiou'
str2='12345'
table=string2.maketrans(str1,str2)
print(table)

string3='(( what are you doing?'
str1='aeiou'
str2='12345'
str3='(?'
table=string3.maketrans(str1,str2,str3)
print(table)
