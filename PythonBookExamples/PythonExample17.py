"""
Exercise 6: Rewrite your pay computation with time-and-a-half for over-
time and create a function called computepay which takes two parameters
(hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""


def calculate(int_hours,int_rate):
    total_pay=0
    if int_hours>40:
        extra_hours=int_hours-40
        extra_rate=int_rate*1.5
        initial_pay=40*10
        extra_pay=extra_hours*extra_rate
        total_pay=initial_pay+extra_pay
    return total_pay



hours=input('Enter the hours')
rate=input('Enter the rate')
try:
    int_hours=int(hours)
    int_rate=int(rate)
except:
    print('Your input is wrong please enter the number')
print(calculate(int_hours,int_rate))



