"""
Exercise 4: Add code to the above program to ﬁgure out who has the
most messages in the ﬁle. After all the data has been read and the dic-
tionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to ﬁnd who has
the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195

"""

filename=input('Enter the file name')

try:
    filehandle=open(filename)
except:
    print('your file name is wrong')
    exit()

counts=dict()
for line in filehandle:
    line=line.rstrip()
    words=line.split()
    if len(words)<3:
        continue
    if not line.startswith('From'):
        continue
    counts[words[1]]=counts.get(words[1],0)+1

print(counts)

list1=list()

for key,value in counts.items():
    list1.append((value,key))
"""
print(max(list1))
"""

sorted_list=sorted(list1,reverse=True)
(time,name)=sorted_list[0]
print('The name is:',name)
print('Number of times is:',time)


