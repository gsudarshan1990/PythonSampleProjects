"""
Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
"""

def print_square():
    while True:
        try:
            number1=int(input('Please provide the number to obtain the Square'))
        except:
            print('You have provided the input incorrectly')
        else:
            print('Yes Thank you')
            result=number1**2
            print(result)
            break

print_square()
