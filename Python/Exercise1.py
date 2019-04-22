"""
What is the type of the result of the expression 3 + 1.5 + 4?
What would you use to find a number’s square root, as well as its square?
# Square root:
# Square:
Strings
Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
# Print out 'e' using indexing
Reverse the string 'hello' using slicing:
s ='hello'
# Reverse the string using slicing
Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'
# Print out the 'o'

# Method 1:
# Method 2:
Lists
Build this list [0,0,0] two separate ways.
# Method 1:
# Method 2:
Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
Sort the list below:
list4 = [5,3,4,6,1]
Dictionaries
Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
# Grab 'hello'
d = {'k1':{'k2':'hello'}}
# Grab 'hello'
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
Can you sort a dictionary? Why or why not?
Tuples
What is the major difference between tuples and lists?
How do you create a tuple?
Sets
What is unique about a set?
Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]


"""


import math

print(3+1.5+4)
number =25
number =6
print(math.sqrt(25))
print(math.pow(number,2))

S='hello'
print(S[1])

print(S[::-1])

len=len(S)
print(S[len-1])
print(S[-1])

list1=[0,0,0]
list2= []
list2.append(0)
list2.append(0)
list2.append(0)

print(list1)
print(list2)

list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)

list4=[5,3,4,6,1]
list4.sort()
print(list4)

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])

t1=(0,1,'hello')
print(t1)


list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))
