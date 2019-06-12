x=('Glenn','Sally','Joseph')
print(x[2])

values=(1,9,2)
print(max(values))

for value in values:
    print(value)


(x,y)=(4,'fred')
print(y)

(a,b)=(99,88)
print(b)


dict1={'a':10,'d':40,'c':30,'b':20}
print(dict1.items())

print(sorted(dict1.items()))


for key,value in sorted(dict1.items()):
    print(key,value)

list1=list()
for key,value in dict1.items():
    list1.append((value,key))

print(list1)

print(sorted(list1))
print(sorted(list1,reverse=True))
