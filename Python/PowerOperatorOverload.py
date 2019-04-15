"""
Create a class called Square and perform the following tasks -
(i) Create two objects for this class squareOne and
squareTwo
(ii) Find the result of side of squareOne to the power of side
of squareTwo

While performing SquareOne ** SquareTwo, you need to
overload __pow__() method

"""


class Square:
    def __init__(self,side):
        self.side =side

    def __pow__(square1,square2):
        return square1.side**square2.side

squareone=Square(2)
squaretwo=Square(4)
print(squareone**squaretwo)

