string1='Hello world'
type(string1)
print('*'*10)
print(dir(string1))

#Capitalize
string2='abc'
print("using the capitalize function for string 'abc' :"+string2.capitalize())
string3='ABC'
print('using the capitalize function for the string \'ABC\' :'+string3.capitalize())

#Index using find  method
string4='banana'

print('using the find function to find the index  of the letter "n" in the string "banana" '+str(string4.find('n')))
print('using the find function to find the index of the string "na" in the string "banana" '+str(string4.find('n')))
print('using the find function to find the index of the string "z" in the string "banana" '+str(string4.find('z')))

#Upper and lower Case
string6='Hello Bob'
print('Lower case',string6.lower())
print('After the executing the lower function it makes a copy but actual object doesnot change:'+string6)

print('Upper Case:',string6.upper())
print('After the executing the upper() function it makes a copy but actual object doesnot change:'+string6)

#String Replacement
string7='Hello Bob'
string8=string7.replace('Bob','Jane')
print('Replaced String',string8)
print('Acutal String',string7)

#multi replacement
string8=string6.replace('o','X')
print(string8)

#Removing White Space

string9='    Hello Bob'
print('After removing white space from leftside of the string {}:'.format(string9),string9.lstrip())

string10='Hello Bob    '
print('After removing white space from right side of the string {}:'.format(string10).rstrip())

string11='     Hello Bob    '
print('Removing white space from both right side and left side {}:'.format(string11),string11.strip())


string12='Please have a nice day'
print("Checking if the string {} starts with 'Please':".format(string12),string12.startswith('Please'))
print("Checking if the string {} starts with 'please':".format(string12),string12.startswith('please'))

#Finding the String after @ and first space after @'
string13='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
index1=string13.find('@')
print('Find the index of @ in the string "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008:',index1)
index2=string13.find(' ',index1)
print('Find the index of " "(first space) after @ in the string "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008:',index2)
print('String between above two index positions',string13[index1+1:index2])
