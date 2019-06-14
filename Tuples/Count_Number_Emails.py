"""
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195

"""

filename=input('Enter the file name')
try:
    filehandle=open(filename)
except IOError as argument:
    print(argument)
    if filename == '':
        print('According to argument empty file doesnot exist')
    else:
        print(f'According to argument {filename} file doesnot exist')
    exit()
email_dictionary=dict()
for line in filehandle:
    line=line.rstrip()
    words=line.split()
    if len(words)<3:
        continue
    if not line.startswith('From'):
        continue
    email_dictionary[words[1]]=email_dictionary.get(words[1],0)+1

print(email_dictionary)

Flipped_list=list()
for key,value in email_dictionary.items():
    Flipped_list.append((value,key))

sorted_list=sorted(Flipped_list,reverse=True)

print(sorted_list[0])
