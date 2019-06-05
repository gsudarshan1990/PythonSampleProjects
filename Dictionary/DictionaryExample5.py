"""
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
"""

dictionary_word=dict()
count=0
filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/words.txt')
for line in filehandle:
   line=line.rstrip()
   words=line.split()
   for word in words:
       dictionary_word[word]='arbitary'
       count+=1

print(dictionary_word)
print(len(dictionary_word))
print(count)
