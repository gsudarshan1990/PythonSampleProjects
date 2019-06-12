filename=input('Enter the file name')
try:
    filehandle=open(filename)
except:
    print('File name is not correct')
    exit()
finally:
    print('Try\Except block is completed')

dict1=dict()
for line in filehandle:
    line=line.rstrip()
    words=line.split()
    if len(words)<3:
        continue
    if not line.startswith('From'):
        continue
    dict1[words[1]]=dict1.get(words[1],0)+1
print(dict1)

list1=list()

for key,value in dict1.items():
    list1.append((value,key))

print(list1)

list2=sorted(list1,reverse=True)

for key,value in list2[0:10]:
    print(key,value)
