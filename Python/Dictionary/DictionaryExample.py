"""
Write a function called remove keys(mydict, keylist) that accepts two parameters: a dictionary called mydict and a list
called keylist. remove keys(mydict, keylist) should remove all the keys contained in keylist from mydict and return the
dictionary:

d = { "key1" : "value1", "key2" : "value2", "key3" : "value3", "key4" : "value4" }

"""

dict={ "key1" : "value1", "key2" : "value2", "key3" : "value3", "key4" : "value4" }

def remove_keys(mydict,keylist):
    for keys in keylist:
        del mydict[keys]

print(dict.keys())
keys_list=dict.keys()
list=[]
for keys in keys_list:
    list.append(keys)
remove_keys(dict,list)
print(dict)
