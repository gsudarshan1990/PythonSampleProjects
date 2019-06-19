import re

filename=input('Enter the file name')

try:
    filehandle=open(filename)
except IOError as argument:
    print('Could not Open the file')
    print(argument)
    exit(0)

for line in filehandle:
    line=line.rstrip()
    lst=re.findall('\S+@\S+',line)
    if len(lst)>0:
        print(lst)
