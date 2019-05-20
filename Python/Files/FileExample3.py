"""
#Reading from the file
filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox.txt')
for line in filehandle:
    print(line)
"""

#Count of the line

filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox.txt')
count=0
for line in filehandle:
    count+=1
print('Line Count:'+str(count))
print('This file handle function does not read new line')



filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox-short.txt')
line=filehandle.read()
print(len(line))
print('This file handle function reads the new line')


filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox-short.txt')
for line in filehandle:
    if line.startswith('From'):
        print(line)



filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox-short.txt')
for line in filehandle:
    line=line.rstrip()
    if line.startswith('From'):
        print(line)
print('*'*10)
print('*'*10)
print('*'*10)
print('*'*10)
print('*'*10)
filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox-short.txt')
for line in filehandle:
    line=line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)


fname=input('Enter the file name')
filehandle=open(fname)
count=0
for line in filehandle:
    line=line.rstrip()
    if line.startswith('Subject:'):
        count+=1
print('The lines start with "Subject" is:'+str(count))

fname=input('Enter the file name')
filehandle=open(fname)
count=0
for line in filehandle:
    line=line.rstrip()
    if line.startswith('Subject:'):
        count+=1
print('The lines start with "Subject" is:'+str(count))
import time
time.sleep(5)

fhandle= open('C:/Users/EP833WG/Desktop/python_read_files/mbox-short.txt')
for line in fhandle:
    line=line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)


fname=input('Enter the filename')
try:
    fhandle=open(fname)
except:
    print('File name provided is wrong')
