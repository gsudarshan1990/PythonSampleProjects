"""
Exercise 3: Write a program to read through a mail log, build a his-
togram using a dictionary to count how many messages have come from
each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

"""

filename=input('Enter the file name')
counts=dict()
try:
    filehandle=open(filename)
except:
    print('You have entered wrong file name')
    exit()

for line in filehandle:
    line=line.rstrip()
    #print(line)
    words=line.split()
    if len(words)<3:
        continue
    if  not line.startswith('From'):
        continue
    words=line.split()
    counts[words[1]]=counts.get(words[1],0)+1
print(counts)


