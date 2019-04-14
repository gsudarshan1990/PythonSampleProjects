

"""Program to input noun , verb and adjective"""
def user_enter_noun_verb_adjective():
    print('The sentence is:\" Good movie runs forever\"')
    print('please select the noun, verb and adjective and append n for noun , v for verb , a for adjective')
    noun=input('Enter the noun')
    verb = input('Enter the verb')
    adjective=input('Enter the adjective')
    print('Your sentence is: \"{} {} {} forever'.format(adjective,noun,verb))

user_enter_noun_verb_adjective()

