import json

a_string='\n\n\n{\n"resultCount":25, \n "results":[\n{"WrapperType":"track","kind":"podcast","collectionId":10892}]}'

print(a_string)

d=json.loads(a_string)
print(d.keys())

for value in d:
    print(d[value])
