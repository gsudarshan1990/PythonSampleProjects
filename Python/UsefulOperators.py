#Range Example

for num in range(0,10,2):
    print(num)

index_count=0

"""
for letter in 'abcde':
    print('For index {} the letter is {}'.format(index_count,letter))
    index_count+=1
"""
#Enumerate returns a tuple

word='Google'
for item in enumerate(word):
    print(item)

#Perform the tuple Unpacking
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('-'*10)

#zip

mylist1=[1,2,3]
mylist2=['a','b','c']

for item in zip(mylist1,mylist2):
    print(item)

#minimum and maximum

mylist3=[10,20,30,40,50]

print('min='+str(min(mylist3)))
print('max='+str(max(mylist3)))

#in keyword

print('a' in 'abcde')
print('f' in 'abcde')
print(10 in mylist3)

#in keyword works with keys

dict1={'abc':123}

print('abc' in dict1)

#Shuffle
print("*"*5+'Shuffle Example'+'*'*8)
mylist4=[1,2,3,4,5,6,7,8,9,10]
print('Printing list before Shuffle')
print(mylist4)
print('Printing list after shuffle')
from random import shuffle
shuffle(mylist4)
print(mylist4)


#Randint Example

from random import randint
print(randint(0,100))
