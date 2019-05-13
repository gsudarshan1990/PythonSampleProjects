"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
"""

def string_with_lower_and_upper_case(string):
    count_lower=0
    count_upper=0
    print(ord('a'))
    print(ord('z'))
    for letter in string:
        if ord('a')<=ord(letter)<=ord('z'):
            count_lower+=1
        elif ord('A')<=ord(letter)<=ord('Z'):
            count_upper+=1
    print('No: of lower case letter is {}'.format(count_upper))
    print('No: of upper case letter is {}'.format(count_lower))

string_with_lower_and_upper_case('Hello Mr. Rogers, how are you this fine Tuesday?')
