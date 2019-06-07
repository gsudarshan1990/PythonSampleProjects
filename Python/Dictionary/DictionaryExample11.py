filename=input('Enter the file name')
filehandle=open(filename)
count=dict()
for line in filehandle:
    line=line.rstrip()
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1

print(count)
