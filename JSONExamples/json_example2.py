import json

def pretty(obj):
    return json.dumps(obj)

d={'key1':{'c':True,'a':90,5:50},'key2':{'b':3,'c':'yes'}}
print(d)
print('-'*10)
print(pretty(d))
