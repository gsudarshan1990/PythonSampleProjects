original=[['dogs','puppies'],['cats','kittens']]
copied_version=[]
for inner_list in original:
    copied_inner_list=inner_list[:]
    copied_version.append(copied_inner_list)
print('Original Version')
print(original)
print('Coped Version')
print(copied_version)
original[0].append(['cannies'])
print("Original Version")
print(original)
print('Copied Version')
print(copied_version)
