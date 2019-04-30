"""
Use for, .split(), and if to create a Statement that will print out words that start with 's'
st = 'Print only the words that start with s in this sentence'
"""

str='Print only the words that start with s in this sentence'

mylist1=str.split()

for word in mylist1:
    if word[0]=='s':
        print(word)
