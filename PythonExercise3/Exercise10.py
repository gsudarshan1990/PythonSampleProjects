"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
"""

def summer_69(list):
    index_of_6=0
    index_of_9=0
    total=0
    for i,j in zip(range(0,len(list)),range(0,len(list))):
        if list[i] == 6:
            index_of_6=i
        if list[j] == 9:
            index_of_9=j
    if (index_of_6 == 0) and (index_of_9==0):
        total=sum(tuple(list))
    else:
        list2=list[:index_of_6]+list[index_of_9+1:]
        total=sum(tuple(list2))
    print(total)

summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])


