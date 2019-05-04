"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
"""

def spy_game(list):
    count=list.count(0)
    first_occurence_of_zero=0
    last_occurence_of_zero=0
    first_occurence_of_seven=0
    if count == 2:
        first_occurence_of_zero=list.index(0)
        last_occurence_of_zero=len(list)-1-list[::-1].index(0)
    first_occurence_of_seven=list.index(7)
    if (first_occurence_of_zero<last_occurence_of_zero<first_occurence_of_seven):
        print(True)
    else:
        print(False)





spy_game([1,2,4,0,0,7,5])
spy_game([1, 0, 2, 4, 0, 5, 7])
spy_game([1,7,2,0,4,5,0])

