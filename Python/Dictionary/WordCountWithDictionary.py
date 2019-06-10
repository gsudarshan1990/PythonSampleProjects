import string
print(string.punctuation)

filename=input('enter the file name')
counts=dict()
try:
    filehandle=open(filename)
except:
    print('Could not open the file')
    exit()
finally:
    print('try\except block is completed')

for line in filehandle:
    line=line.rstrip()
    str1=' '
    str2=' '
    str3=string.punctuation
    table=line.maketrans(str1,str2,str3)
    line2=line.translate(table)
    print(line2)
    words=line2.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
