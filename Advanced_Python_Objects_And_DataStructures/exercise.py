"""
 Convert 1024 to binary and hexadecimal representation
"""

print(hex(1024))
print(bin(1024))


"""
Round 5.23222 to two decimal places
"""

print(round(5.23222,2))

"""
Check if every letter in the string s is lower case
s = 'hello how are you Mary, are you feeling okay?'
"""

import string
s = 'hello how are you Mary, are you feeling okay?'
modified_string=s.translate(s.maketrans('','',string.punctuation))
print(modified_string)
words=modified_string.split()
for word in words:
    for letter in word:
        if(letter.islower()):
          continue
        else:
            print(letter+' is not lower')
            print('Every letter is not lower')

"""
How many times does the letter 'w' show up in the string below?

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
"""
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
count=s.count('w')
print(count)

"""
Problem 5: Find the elements in set1 that are not in set2:

:
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
"""

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print(set1.difference(set2))

"""


Problem 6: Find all elements that are in either set:
"""
print(set1.union(set2))


"""
Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.
"""

dict={x:x**3 for x in range(5)}
print(dict)


"""
Problem 8: Reverse the list below:

list1 = [1,2,3,4]

"""

list1 = [1,2,3,4]
list1.reverse()
print(list1)


"""
Problem 9: Sort the list below:

list2 = [3,4,2,5,1]
"""

list2 = [3,4,2,5,1]
list2.sort()
print(list2)
