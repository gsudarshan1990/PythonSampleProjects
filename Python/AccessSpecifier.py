class Car:
    numberOfWheels = 4
    _color='Black'
    __year=2017

class Bmw(Car):
    def __init__(self):
        print('The color of the car is {}'.format(self._color))

car=Car()
print('number of wheels in the car is ',car.numberOfWheels)
bmw=Bmw()
print('The year of manufacture is ',car._Car__year)
