"""
 Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.

['0.8475']
['0.0000']
['0.6178']
['0.0000']
['0.6961']
['0.0000']

"""

import re
filename=input('Enter the file name')

try:
    filehandle=open(filename)
except IOError as argument:
    print('Could not open the file')
    print(argument)
    exit(0)

for line in filehandle:
    line=line.rstrip()
    string1=re.findall('^X\S*: [0-9.]+',line)
    if len(string1)>0:
        second_list=re.findall('[0-9.]+',string1[0])
        print(second_list)


