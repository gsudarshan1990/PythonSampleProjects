animals=['man','bear','pig']

print(animals[0])
print(animals[1])


animals[0]='lion'
print(animals[0])
print('-'*10)
print(animals[-1])
print(animals[-2])
print(animals[-3])

animals.append('cow')
print(animals[-1])

animals.append('rat')
print(animals[-1])

animals.extend(['duck','whale'])
print(animals)

more_animals=['tiger','elephant']
animals.extend(more_animals)
print(animals)

animals.insert(0,'horse')

print(animals)

animals.insert(2,'Giraffe')
print(animals)

print(animals[1:3])

print(animals[5:7])

print(animals[:3])

print(animals[9:])


print('sudarshan'[1:3])

print('index of \"Giraffe\" is:{}'.format(animals.index('Giraffe')))


try:
    index=animals.index('mangoose')
except:
    index='No information on mangoose'

print(index)

for animal in animals:
    print(animal)


a=10
b=0

try:
    a/b
except:
    print('a cannot divide b since b is 0')


index=0

while index<10:
    print(index)
    index=index+1

animals.sort()
print(animals)

print(len(animals))
print(len(animals[2]))

new_list=['zebra','donkey']
animals.extend(new_list)
print(len(animals))

animals.append('orangutan')
print(len(animals))

animals.insert(4,'cheetah')
print(len(animals))

print(animals)

print('-'*16)

for number in range(10):
    print(number)
print('-'*16)

for number in range(2,5):
        print (number)

for number in range(0,101,2):
    print(number)

print(len(animals))
for number in range(0,len(animals),3):
    print(animals[number])

index=10

while index>0:
    print(index)
    index-=1
print('index of \"rat\":{}'.format(animals.index('rat')))

list1=[1,3,4,5,5]
print(max(list1))

list1.append('all are real numbers')
print(list1)


