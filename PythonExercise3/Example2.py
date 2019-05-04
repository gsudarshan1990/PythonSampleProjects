"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""

def animal_crackers(string):
    list=string.split()
    if len(list) == 2:
        if list[0][0] == list[1][0]:
            print(True)
        else:
            print(False)


animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')
