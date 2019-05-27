string1='With three words'
list1=string1.split()
print(list1)
print(len(list1))
print(list1[2])
for word in list1:
    print(word)


string2='A lot         of spaces'
list2=string2.split()
print(list2)

string3='first;second;third'
list3=string3.split()
print(list3)

list4=string3.split(';')
print(list4)
print(len(list4))
