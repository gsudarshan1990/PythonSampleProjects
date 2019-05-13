"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
"""

def unique_element_list(list2):
    set2=set(list2)
    print(set2)
    print(list(set2))

list1=[1,1,1,1,2,2,3,3,3,3,4,5]
unique_element_list(list1)
