"""
Count occurence of each word in the sentence
text=the clown ran after the car and the car into the tent and the tent fell down on the clown and the car
"""

count=dict()
text=input('Enter the text')

words=text.split()
print('Words:',words)
for word in words:
    count[word]=count.get(word,0)+1
print(count)
