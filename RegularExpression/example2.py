import re

try:
    filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox.txt')
except IOError as argument:
    print('could not open the file')
    print(argument)
    exit()

for line in filehandle:
    line=line.rstrip()
    if re.search('From:',line):
        print(line)
