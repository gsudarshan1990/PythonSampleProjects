# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'

import re

try:
    filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox-short.txt')
except IOError as argument:
    print('Could not open the file')
    print(argument)
    exit()

count=0
for line in filehandle:
    line=line.rstrip()
    if re.search('F..m:',line):
        print(line)
        count+=1
print(count)
