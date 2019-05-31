filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/mbox-short.txt')
for line in filehandle:
    line=line.rstrip()
    if line.startswith('From'):
        words=line.split()
    print(words[2])
