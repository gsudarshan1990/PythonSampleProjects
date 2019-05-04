"""

MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""

def makes_twenty(a,b):
    if (a==20) or (b==20):
        print(True)
    else:
        result=sum((a,b))
        if result==20:
            print(True)
        else:
            print(False)


makes_twenty(20,10)
makes_twenty(12,8)
makes_twenty(2,3)
