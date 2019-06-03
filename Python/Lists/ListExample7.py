"""
Exercise 4: Download a copy of the ﬁle www.py4e.com/code3/romeo.txt.
Write a program to open the ﬁle romeo.txt and read it line by line. For
each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word
is not in the list, add it to the list. When the program completes, sort
and print the resulting words in alphabetical order.
"""

filename=input('enter the file name')
filehandle=open(filename)
words_list=list()
for line in filehandle:
    line=line.rstrip()
    print(line)
    words=line.split()
    for word in words:
        if len(words_list) == 0 or word not in words_list:
            words_list.append(word)
words_list.sort()
print(words_list)

