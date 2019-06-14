"""
Exercise 3: Write a program that reads a ﬁle and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z.

"""

import string
filename=input('Enter the file name')

try:
    filehandle=open(filename)
except IOError as argument:
    print(argument)
    print('Default File Opening')
    filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/romeo-2.txt')

letter_dictionary=dict()
for line in filehandle:
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.rstrip()
    words=line.split()
    for word in words:
        word=word.lower()
        for letter in word:
            letter_dictionary[letter]=letter_dictionary.get(letter,0)+1

#print(letter_dictionary)
Flipped_list=list()
for key,value in letter_dictionary.items():
    Flipped_list.append((value,key))

sorted_list=sorted(Flipped_list,reverse=True)
print(sorted_list)



