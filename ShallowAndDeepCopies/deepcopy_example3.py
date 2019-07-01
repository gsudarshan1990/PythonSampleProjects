import copy
original=[['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copied_version=original[:]
deeply_copied_version=copy.deepcopy(original)
print('Original')
print(original)
print('Shallow Copied')
print(shallow_copied_version)
print('Deeply Copied')
print(deeply_copied_version)
original.append('Hi there')
original[0].append(['marsupial'])
print('Original')
print(original)
print('Shallow Copied')
print(shallow_copied_version)
print('Deeply Copied')
print(deeply_copied_version)
