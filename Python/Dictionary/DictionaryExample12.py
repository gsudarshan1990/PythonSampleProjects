counts={ 'chuck' : 1 , 'annie' : 42, 'jan': 100}

for key in counts:
    print(key,counts[key])

print('-'*10)

for key in counts:
    if counts[key]>10:
        print(key,counts[key])
print('-'*10)
list1=list(counts.keys())
list1.sort()
for key in list1:
    print(key,counts[key])
