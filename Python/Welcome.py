#Print the statements

print('Hello, my name is sudarshan and i am new to python i think i will be able to perform my projects in python very well')
print('Good morning')

#Assingement of variables with values
fruit ='apple'
fruit2='orange'

#Printing the variables
print (fruit)
print(fruit2)


#Double quotes inside the single quotes
text1='she said, "That is a great tasting apple!"'
print(text1)

#Double quotes inside the single quotes
text2='"How are you"'
print(text2)

#Single quotes inside the double quotes
text3="That's is a great tasting apple"

print(text3)

#Double quotes using the escape sequence
text4="She said that, \" It is a fantastic year\""
print(text4)

#Single quotes using the escape sequence
text5='she said that \'it is a fantastic year\''
print (text5)

# Strings with indexes
first_letter='apple'[0]
print(first_letter)
last_letter='apple'[4]
print (last_letter)

first_letter1=fruit[0]
print(first_letter1)
last_letter1=fruit[4]
print(last_letter1)
print(fruit[2])

# Length of the Strings- len() function
fruit_len=len(fruit)
print(fruit_len)

print(len(fruit2))
print(len('strawberry'))

#Object methods

fruit3='grape'
print(fruit3.upper())

#Object methods
fruit4='PINEAPPLE'
print(fruit4.lower())

print('I '+'like '+'python.')
print('I'+'like'+'python')

print('s'*10)

first ='I'
middle='like'
last='python'
sentence=first+' '+middle+' '+last
print(sentence)

year =1990
sentence='My name is sudarshan and i was born in the year '
print(sentence+str(year))

print('I {} python this is a {} string'.format('love', 'formatted' ))

print('I {0} {1}. {1} {0}s me'.format('love', 'python'))

first='I'
middle='love'
last='python'
print(str(2)+' {} {} {}'.format(first,middle,last))

version=3

print (str(1)+'. I like python version '+str(version))
print('{}. I like python version {}'.format(2,version))
