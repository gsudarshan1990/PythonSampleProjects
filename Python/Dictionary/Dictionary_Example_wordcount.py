filename=input('Enter the file name')
if len(filename)<1:
    filename='C:/Users/EP833WG/Desktop/python_read_files/clown.txt'
counts=dict()
try:
    filehandle=open(filename)
except:
    print('File does not exist')
    exit()

for line in filehandle:
    line=line.rstrip()
    #print(line)
    words=line.split()
    #print(words)
    for word in words:
        """
        oldcount=counts.get(word,0)
        print(word,'old',oldcount)
        newcount=oldcount+1
        counts[word]=newcount
        print(word,'new',newcount)
        """

        """
        if word in counts:
            #counts[word]=counts.get(word,0)+1
            counts[word]=counts[word]+1
        else:
            counts[word]=1
            print('***NEW***')
        print(word,counts[word])
        """
        counts[word]=counts.get(word,0)+1
print(counts)

largestnumber=None
largestword=None

for key,value in counts.items():
    if largestnumber is None or value>largestnumber:
        largestnumber=value
        largestword=key
print(largestnumber,largestword)
