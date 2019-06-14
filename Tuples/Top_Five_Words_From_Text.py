filename=input('Enter the file name')
try:
    filehandle=open(filename)
except IOError as argument:
    print(argument)
    filehandle=open('C:/Users/EP833WG/Desktop/python_read_files/clown.txt')

word_dictionary=dict()

for line in filehandle:
    line=line.rstrip()
    words =line.split()
    for word in words:
        word_dictionary[word]=word_dictionary.get(word,0)+1

#print(word_dictionary)

temporary_list=list()
for key,value in word_dictionary.items():
    temporary_list.append((value,key))

#print('Flipped',temporary_list)

sorted_list=sorted(temporary_list,reverse=True)
#print(sorted_list)

for value,key in sorted_list[:5]:
    print(key,value)
