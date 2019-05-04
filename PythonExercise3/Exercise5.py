"""

MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
"""

def master_yoda(word):
    list=word.split()
    reversed_list=list[::-1]
    reversed_sentence=''
    final_list=" ".join(reversed_list)
    print(final_list)

master_yoda('I am home')
master_yoda('We are ready')
