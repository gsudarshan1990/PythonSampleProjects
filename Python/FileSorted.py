list=[]
with open('C:/Users/EP833WG/Desktop/python_read_files/animals.txt') as fileobject:
    for line in fileobject:
        list.append(line.rstrip())

print(list)
sortedlist=sorted(list)
print(sortedlist)

with open('C:/Users/EP833WG/Desktop/python_read_files/animals_sorted.txt','w') as fileobjectsecond:
    for animal in sortedlist:
        fileobjectsecond.write(animal+'\n')


