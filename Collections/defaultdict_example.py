from collections import defaultdict

d={}
d['k1']=1
print(d['k1'])
#print(d['k2'])


dict1=defaultdict(object)
print(dict1['one'])

dict2=defaultdict(lambda :0)
dict2['two']=2
print(dict2['one'])
print(dict2)
