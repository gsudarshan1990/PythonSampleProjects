"""
Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

hours=input('Enter the hours')
rate=input('Enter the rate')

int_hours=int(hours)
float_rate=float(rate)
total_pay=0
if int_hours>40:
    initial_pay=40*float_rate
    extra_hours=int_hours-40
    extra_pay=extra_hours*((float_rate)*1.5)
total_pay=initial_pay+extra_pay
print('Pay:',total_pay)
