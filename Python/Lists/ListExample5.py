filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox-short.txt')
for line in filehandle:
    line=line.rstrip()
    words=line.split()
    #print('Words:',words)
    #First Guardian
    """
    if line == '':
        print('Skip line')
        continue
    """
    #Guardian Second
    """
    if len(words)<1:
        continue
    """
    #Compound Guardian
    if len(words)<3 or words[0]!='From':
        #print('Ignore')
        continue
    print(words[2])
