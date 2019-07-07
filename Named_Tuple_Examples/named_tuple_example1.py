t=(1,2,3)
print(t[0])

from collections import namedtuple

Dog=namedtuple('Dog','age breed name')
sam=Dog(age=2,breed='Lab',name='Sammy')
print(sam.age)
print(sam.breed)
print(sam.name)

Cat=namedtuple('Cat','fur claws name')
kitten=Cat(fur='Fuzzy',claws=False,name='kitten')
print(kitten)
print(kitten[0])
print(kitten[1])
print(kitten[2])

Student=namedtuple('Student','name age dateofbirth')
student1=Student(name='Rahul',age=15,dateofbirth='1st July 2004')
print(student1)
print(student1.age)
print(student1.name)
print(student1.dateofbirth)


Person=namedtuple('Person','name age gender')
bob=Person(name='Bob',age=30,gender='male')
jane=Person(name='Jane',age=25,gender='male')

print(bob)
print(jane)
