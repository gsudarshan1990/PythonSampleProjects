original=[['dogs','puppies'],['cats','kittens']]
copied_version=original[:]
print(original)
print(copied_version is original)
print(copied_version == original)
original[0].append(['cannies'])
print(original)
print('Now look at copies version')
print(copied_version)
