class Sample():
    pass

my_sample=Sample()
print(type(my_sample))


class Dog():

    def __init__(self,breed):
        self.breed = breed

my_dog=Dog(breed='Lab')
print(type(my_dog))


class Dog():

    species='mammal'

    def __init__(self,mybreed,name,spots):
        self.breed=mybreed
        self.name=name
        self.spots=spots

my_dog=Dog(mybreed='Huskie',name='blackie',spots=True)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)


class Dog():
    species='mammal'

    def __init__(self,breed,name):
        self.breed=breed
        self.name=name

    def bark(self,number):
        print('WOOF! my name is {} and number is {}'.format(self.name,number))

my_dog=Dog(breed='Huskie',name='Frankie')
print(my_dog.breed)
print(my_dog.species)
print(my_dog.name)
my_dog.bark(10)
