counts={'chuck':1,'fred':42,'jan':100}
for key in counts:
    print(key,counts[key])

print('using list(counts) method:',list(counts))
print('using count.keys() method:',counts.keys())
print('using count.values() method:',counts.values())
print('using count.items() method:',counts.items())
