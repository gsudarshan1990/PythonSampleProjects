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

    def __init__(self,mybreed,name,spots):
        self.breed=mybreed
        self.name=name
        self.spots=spots

my_dog=Dog(mybreed='Huskie',name='blackie',spots=True)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
