

def say_hi():
    print('Hi! Welcome to python functions')

def program_to_add_two_numbers():
    data1=input('Enter the first value')
    data2=input('Enter the second value')
    data3=int(data1)+int(data2)
    print(data3)

def say_hi_from_command_line(name):
    print('Hello {} how are you'.format(name))


def say_hi_from_command_line(name='sudarshan'):
    print('Hello {} how are you'.format(name))

def say_hi_multiple_arguments(firstname,lastname):
    print('Hello {} {}. How are you'.format(firstname,lastname))

say_hi_multiple_arguments('sudarshan','Govindarajan')

def Check_even_or_odd(number):
    """This program is for determining whether a  number is even or odd"""
    if number%2 == 0:
        return 'EVEN'
    else:
        return 'ODD'



print(Check_even_or_odd(8))


