a=[12,34,87]
b=[1,73,93]
c=a+b
print(c)

print(c[1:3])
print(c[:4])
print(c[3:])
print(c[:])


stuff=list()
stuff.append(99)
stuff.append('book')
print(stuff)
stuff.append('cookie')
print(stuff)


list3=[12,35,28,91,36,57]

print(12 in list3)
print(17 in list3)
print(21 not in list3)


sample_list=['Joseph','Glenn','Sally']
sample_list.sort()
print(sample_list)


list4=[12,32,28,68,36,57]

print('length',len(list4))
print('minimum',min(list4))
print('maximum',max(list4))
print('sum',sum(list4))
print('average',(sum(list4)/len(list4)))


#calculate the average of numbers with list

num_list=list()
while True:
    inp=input('Enter the number and "done" to stop')
    if inp == 'done':
        break
    value=float(inp)
    num_list.append(value)

average=sum(num_list)/len(num_list)
print(average)
