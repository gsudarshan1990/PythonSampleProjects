my_list=['one', 'two', 'three']
print(my_list)
another_list=['four', 'five', 'six']
print(another_list)
new_list = my_list + another_list
print(new_list)
new_list[0]='ONE ALL CAPS'
print(new_list)
new_list.append('seven')
new_list.append('eight')
print(new_list)
value1=new_list.pop()
print(new_list)
value2=new_list.pop()
print(new_list)
print(value1)
print(value2)
value3= new_list.pop(0)
print(new_list)
print(value3)

my_new_list=['one', 'two','three', 'four']
my_new_list.sort()
print(my_new_list)
my_new_list.reverse()
print(my_new_list)
