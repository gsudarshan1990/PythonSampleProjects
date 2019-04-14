class Square:
    def __init__(self,side):
        self.side = side

    def print_side(self):
        print(self.side)

    def __add__(squareone,squaretwo):
        return ((4*squareone.side)+(4*squaretwo.side))

square1=Square(5)
square2=Square(6)
square1.print_side()
square2.print_side()
print('Addition of two squares',square1+square2)
