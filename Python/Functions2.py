
#Creating a Sample function for Salutation
def print_hello(name):
    '''
    This function prints the name
    :param name: name
    :return: no return type
    '''
    print("Hello "+name)

#Calling the function
print_hello("sudarshan")

#Creating a function with return value
def add_two_numbers(num1,num2):
    return num1+num2

#Calling the function and storing the result value
result=add_two_numbers(5,11)
#Printing the result
print(result)

#Using the Help function to get information about the function
help(print_hello)

#Check whether the word 'Dog' is present in the string

mystring='Dog is a pet animal'

def dog_check(string):
    '''
    Check whether word exists in a String
    :param string: a string is provided
    :return: Boolean
    '''
    if 'Dog' in string:
        return True
    else:
        return False

result=dog_check(mystring)
print(result)

#Above function is written in a simple way
def dog_check(string):
    return 'Dog' in string

print(dog_check(mystring))


#Example of Pig Latin
"""
if word starts with vowel, add 'ay' to end
if word does not start with vowel, put first letter at the end,then add 'ay'
Example:
word->ordway
apple->appleay
"""

def pig_latin(word):
    first_letter=word[0]
    list_vowels=['a','e','i','o','u']
    presence_of_vowel=first_letter in list_vowels
    if presence_of_vowel:
        word=word+'ay'
    else:
        word=word[1:]+word[0]+'ay'
    print(word)

pig_latin('word')
pig_latin('apple')




