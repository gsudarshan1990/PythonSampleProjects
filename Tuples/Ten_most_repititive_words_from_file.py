"""
Find the 10 most repititive words

"""
import string
filename=input('Enter the file name')
try:
    filehandle=open(filename)
except IOError as argument:
    print('Could not open the file')
    print(argument)
    exit()
word_dictionary=dict()
for line in filehandle:
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.rstrip()
    words=line.split()
    for word in words:
        word_dictionary[word]=word_dictionary.get(word,0)+1

print(word_dictionary)
list_value_key=list()

for key,value in word_dictionary.items():
    list_value_key.append((value,key))

list_value_key_sorted=sorted(list_value_key,reverse=True)

for key,value in list_value_key_sorted[:10]:
    print(key,value)
