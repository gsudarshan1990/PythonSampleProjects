class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name+' says bow bow')

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name+' says meow meow')

mydog=Dog('tommy')
mydog.speak()
mycat=Cat('billy')
mycat.speak()
