"""
Write a Python function to multiply all the numbers in a list.
Sample List : [1, 2, 3, -4]
"""

def multiply_numbers_in_list(numbers):
    product=1
    for number in numbers:
        product*=number
    print(product)



numbers=[1,2,3,-4]
multiply_numbers_in_list(numbers)
