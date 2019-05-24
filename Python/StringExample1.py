string1='banana'
print(string1[1])
print(string1[0])


index=0
while index<len(string1):
    print(string1[index])
    index=index+1


for char in string1:
    print(char)


s='Monty Python'
print(s[0:5])
print(s[6:len(s)])

fruit='banana'
print(fruit[:3])
print(fruit[3:])

#count of 'a' in banana

count=0
fruit='banana'
for letter in fruit:
    if letter == 'a':
        count=count+1
print(count)


def count_letter(fruit,letter):
    count=0
    for index in fruit:
        if index == letter:
            count=count+1
    print(count)

count_letter('banana','a')


print('a' in 'banana')
print('seed' in 'banana')

word='banana'
if word == 'banana':
    print('both the words are same')

word1='apple'
word2='orange'

if word1<word:
    print('Apple come Before Banana')
if word2>word:
    print('Oragne comes after banana')

stuff='Hello World'
print(type(stuff))
print(dir(stuff))

string1='Good Morning'
print(dir(string1))

list1=[1,2,3]
print(dir(list1))
list1.append(4)
print(list1)

print(help(stuff.capitalize()))


string2='banana'
string3=string2.upper()
print(string3)
index_of_a=string2.find('a')
print(index_of_a)

print(string2.find('na'))
print(string2.find('na',3))

line='    Here we go   '
print(line.strip())
print(line.rstrip())


line='Have a nice day'
print(line.startswith('Have'))
print(line.startswith('h'))


data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
initial_position=data.find('@')
space=data.find(' ',initial_position)
print(initial_position)
print(space)
print(data[initial_position+1:space])
