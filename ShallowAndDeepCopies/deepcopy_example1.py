original=[['dogs','puppies'],['cats','kittens']]
copied_version=[]
for inner_list in original:
    copied_inner_list=[]
    for item in inner_list:
        copied_inner_list.append(item)
    copied_version.append(copied_inner_list)
print(original)
print(copied_version)
original[0].append(['cannies'])
print('After appending')
print(original)
print(copied_version)
