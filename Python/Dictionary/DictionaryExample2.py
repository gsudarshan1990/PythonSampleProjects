"""
When we iterate through a dictionary using a for loop, we actually iterate over the keys:
Modify the code above to print just the keys associated to values that are greater than 1.
d = { "key1":1, "key2":2, "key3":1, "key4":3, "key5":1, "key6":4, "key7":2 }
"""

dict ={ "key1":1, "key2":2, "key3":1, "key4":3, "key5":1, "key6":4, "key7":2 }


for keys in dict:
    if (dict[keys]>1):
        print('keys',keys,'value=',dict[keys])
