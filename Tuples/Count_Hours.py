"""
Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by ﬁnding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

"""
filename=input('Enter the file name')
try:
    filehandle=open(filename)
except IOError as argument:
    print(argument)
    if filename == '':
        print('According to argument empty file doesnot exist')
    else:
        print(f'According to argument {filename} file doesnot exist')
    exit()
hour_dictionary=dict()
for line in filehandle:
    line=line.rstrip()
    words=line.split()
    if len(words)<3:
        continue
    if not line.startswith('From'):
        continue
    #print(words[5])
    hours,minutes,seconds=words[5].split(':')
    #print(hours)
    if hours in hour_dictionary:
        hour_dictionary[hours]=hour_dictionary[hours]+1
    else:
        hour_dictionary[hours]=1

for key,value in hour_dictionary.items():
    print(key,value)
