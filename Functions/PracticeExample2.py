"""
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""

def ran_check(num,low,high):
    if low<num<high:
        print('{} is between {} and {}'.format(num,low,high))
    else:
        print('{} is not between {} and {}'.format(num,low,high))

ran_check(5,2,7)
ran_check(3,1,10)
