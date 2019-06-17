nested1=[['a','b','c'],['d','e'],['f','g','h']]
print('*'*5+'Part One'+'*'*5)
nested1[0].append('z')
nested1[1].append('w')
print(nested1[0])
print(len(nested1))
nested1.append(['i'])
for sample_list in nested1:
    print(sample_list)
print('*'*5+'Part Two'+'*'*5)
y=nested1[1]
print(y)
print(y[0])
print(nested1[1][0])
print('*'*5+'Part Three'+'*'*5)
nested1[1]=[1,2,3]
for sample_list in nested1:
    print(sample_list)
nested1[1][0]=100
print(nested1[1])
