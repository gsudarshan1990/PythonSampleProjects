"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""


def has_33(list):
    instance_of_three=0
    for i in range(0,len(list)):
        if (3 == list[i]) and i!=len(list)-1:
            instance_of_three=i
    if (3 == list[instance_of_three]) and (3 == list[instance_of_three+1]):
        print(True)
    else:
        print(False)


has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])
