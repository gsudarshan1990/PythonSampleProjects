"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
"""

def old_macdonald(word):
    first_letter_capitalise=word.capitalize()
    print(first_letter_capitalise[0:3]+first_letter_capitalise[3].upper()+first_letter_capitalise[4:])

old_macdonald('macdonald')

