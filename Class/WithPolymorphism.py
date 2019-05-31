class Animal():
    def __init__(self,name):
        print('I am an animal')
        self.name=name
    def speak(self):
        raise NotImplementedError('Subclass did not implement this function')

class Dog(Animal):
    def speak(self):
        print(self.name+' say bow bow')

class Cat(Animal):
    def speak(self):
        print(self.name+' Says meow meow')

myDog=Dog('fred')
myDog.speak()
myCat=Cat('Billy')
myCat.speak()
