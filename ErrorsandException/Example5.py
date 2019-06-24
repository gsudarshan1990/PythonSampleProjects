"""
Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0

z = x/y
"""


try:
    x=5
    y=0
    z=x/y
except ZeroDivisionError as argument:
    print('You attempted to divide by zero')
    print(argument)
finally:
    print('All done')
