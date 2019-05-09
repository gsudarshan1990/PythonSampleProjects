string1 = 'Hello World'
print(string1.upper())
print(string1.lower())
print(string1.split())
string2 ='Hi this is a string'
print(string2.split('i'))

string3='Hello'
string4='There'
print(string3+string4)

string5='123'
a=1

#print(string5+a) provides the type error

print(int(string5)+1)

string6='banana'

print(string6)
print(string6[1])
x=3
print(string6[x-1])

#Index error print(string6[8])

print('length :'+str(len(string6)))

#indexing of the string using while loop

index=0
while index<len(string6):
    letter=string6[index]
    print(index,letter)
    index+=1
else:
    print('String Iteration is completed')

for item in enumerate(string6):
    print(item)

#Counting the number of the letter in the String

count=0
for letter in string6:
    if letter == 'a':
        count+=1
print(count)

string7='Sudarshan Python'

print(string7[0:5])

print(string7[8:9])

print(string7[10:30])

print(string7[10:])
print(string7[:9])


