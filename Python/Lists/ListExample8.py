"""
Exercise 5: Write a program to read through the mail box data and
when you ﬁnd line that starts with “From”, you will split the line into
words using the split function. We are interested in who sent the
message, which is the second word on the From line.
"""

filename=input('enter the file name')
filehandle=open(filename)
count=0
for line in filehandle:
    line=line.rstrip()
    if not line.startswith('From') or line.startswith('From:'):
        continue
    words=line.split()
    count+=1
    print(words[2])
print(f'There are {count} lines')
