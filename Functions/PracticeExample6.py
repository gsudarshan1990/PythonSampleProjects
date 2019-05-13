"""
Write a Python function that checks whether a passed in string is palindrome or not.

"""

def check_palindrome(string1):
    string2=string1[::-1]
    if string1 == string2:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')


check_palindrome('madam')
check_palindrome('nurses')
check_palindrome('helleh')
