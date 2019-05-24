"""
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
"""

numbers=list()
while True:
    inp=input('Enter the number')
    if inp == 'done':
        break
    try:
        value=int(inp)
        numbers.append(value)
    except:
        print('Invalid Input Enter the correct numbers')
print(numbers)

largest=None
for number in numbers:
    if largest is None or number>largest:
        largest=number
smallest=None
for number in numbers:
    if smallest is None or number<smallest:
        smallest=number
print('largest',largest)
print('smallest',smallest)

