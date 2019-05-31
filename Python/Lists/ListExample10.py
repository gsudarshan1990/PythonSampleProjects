"""
Exercise 1: Write a function called chop that takes a list and modiﬁes
it, removing the ﬁrst and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the ﬁrst and last elements.
"""

def chop(list1):
    del list1[0]
    del list1[len(list1)-1]
    print(list1)

list2= ['a', 'b', 'c','d','e','f']
chop(list2)


def middle(list1):
    del list1[0]
    del list1[len(list1) - 1]
    return list1

list2= ['a', 'b', 'c','d','e','f']
list3=middle(list2)
print(list3)

list3=list3+['f']
list3=list3+['g']
list3=list3+['h']
list3=list3+['i']
list3=list3+['j']
print(list3)
