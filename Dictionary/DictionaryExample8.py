"""
Count the number of letters in word
"""

word = 'brontosaurus'
count={}
for letter in word:
    if letter in count:
        count[letter]=count[letter]+1
    else:
        count[letter]=1
print(count)

print('another method')
count1=dict()
for letter in word:
    count1[letter]=count.get(letter,0)+1
print(count)
