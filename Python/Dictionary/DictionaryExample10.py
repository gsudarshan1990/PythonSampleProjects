"""
Calculate the word which occurs most number of times
"""


file_name=input('Enter the file name')
file_handle=open(file_name)
counts=dict()

for line in file_handle:
    line=line.rstrip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

bigword=None
bigcount=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)
