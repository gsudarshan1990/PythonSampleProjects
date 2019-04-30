"""
Use List Comprehension to create a list of the first letters of every word in the string below:
str='Create a list of the first letters of every word in this string'
"""

str='Create a list of the first letters of every word in this string'

mylist3=str.split()

list4=[word[0] for word in mylist3]
print(list4)
