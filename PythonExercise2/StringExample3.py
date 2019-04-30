"""
Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
"""

str='Print every word in this sentence that has an even number of letters'
mylist2=str.split()

for word in mylist2:
    if(len(word)%2 == 0):
        print('length of the word "{}" is "even!"'.format(word))
