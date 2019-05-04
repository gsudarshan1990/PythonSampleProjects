"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

"""

def paper_doll(word):
    formatted_word=''
    for i in range(0,len(word)):
        formatted_word=formatted_word+word[i]*3
    print(formatted_word)

paper_doll('Hello')
paper_doll('Mississippi')
