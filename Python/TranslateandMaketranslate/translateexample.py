string1='() hello guys and welcome?'
str1='abcde'
str2='12345'
str3='()?'
table=string1.maketrans(str1,str2,str3)
string2=string1.translate(table)
print(string2)
