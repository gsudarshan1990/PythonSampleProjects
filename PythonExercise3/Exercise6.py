"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True

"""


def almost_there(number):
    number1 = 100-number
    number2 = 200-number
    if (abs(number1)<=10) or (abs(number2)<=10):
        print(True)
    else:
        print(False)

almost_there(90)
almost_there(104)
almost_there(150)
almost_there(209)
