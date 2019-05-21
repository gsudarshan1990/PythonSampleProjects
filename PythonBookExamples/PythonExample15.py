"""
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
"""


hours=input('Enter the hours')
rate=input('Enter the rate')
total_pay=0
try:
    int_hours=int(hours)
    float_rate=float(rate)
    if int_hours>40:
        initial_pay=40*float_rate
        extra_hours=int_hours-40
        extra_pay=extra_hours*((float_rate)*1.5)
    total_pay=initial_pay+extra_pay
    print('Pay:',total_pay)
except:
    print('Enter the numeric numbers')

