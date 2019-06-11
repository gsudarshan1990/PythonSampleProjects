word='hello'
mylist1=[letter for letter in word]
print(mylist1)

mylist2=[num for num in range(0,11) if num%2 ==0]
print(mylist2)


num_list=[1,2,3,4,5]

def square(num_list):
    return [num**2 for num in num_list]

print(square(num_list))

def cube(num_list):
    return [num**3 for num in num_list]

print(cube(num_list))
