"""
Exercise 1: Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression:

Enter a regular expression: java$
"""


import re

filename=input('Enter the file name')

try:
    filehandle=open(filename)
except IOError as argument:
    print('Could not open the file')
    print(argument)
    exit(0)
count=0
for line in filehandle:
    line=line.rstrip()
    result=re.findall(r'java$',line)
    if len(result)>0:
        print(result)
    count+=1
print(count)
