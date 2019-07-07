d={}

d['a']=1
d['b']=2
d['c']=3
d['d']=4
d['e']=5

print(d)

for key,value in d.items():
    print(key,value)
from collections import OrderedDict

d1=OrderedDict()
d1['a']=1
d1['b']=2
d1['c']=3
d1['d']=4
d1['e']=5

print(d1)

for key,value in d1.items():
    print(key,value)


d2={}
d2['a']=1
d2['b']=2

d3={}
d3['b']=2
d3['a']=1

print(d2 == d3)


d4=OrderedDict()
d4['a']=1
d4['b']=2

d5=OrderedDict()
d5['b']=2
d5['a']=1

print(d4 == d5)
