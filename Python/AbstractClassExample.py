
from abc import ABCMeta,abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass


class Square:
    side=4
    def area(self):
        print('Area of the Square is ',self.side*self.side)


class Rectangle:
    length=5
    width=10
    def area(self):
        print('area of the rectange is ',self.length*self.width)

square=Square()
rectangle = Rectangle()
square.area()
rectangle.area()

