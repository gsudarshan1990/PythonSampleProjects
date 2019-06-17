import re

try:
    file_handle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox-short.txt')
except IOError as argument:
    print('Could not opening the file')
    print(argument)
    exit()
count=0
for line in file_handle:
    line=line.rstrip()
    if re.search('From:',line):
        print(line)
        count += 1
print(count)
