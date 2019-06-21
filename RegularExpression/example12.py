"""
# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero

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
    searched_line=re.findall('^From .* ([0-9][0-9]:[0-9][0-9])',line)
    if len(searched_line)>0:
        print(searched_line)
