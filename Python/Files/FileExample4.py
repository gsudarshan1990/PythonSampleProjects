"""
Write a program to read through a file and print  the contents of the file(line by line) all in uppercase
"""

fname=input('Enter the file name')
filehandle=open(fname)
for line in filehandle:
    line=line.rstrip()
    print(line.upper())
