num_list=[1,2,3,4,5]

def square(num_list):
    result_list=[]
    for num in num_list:
        result_list.append(num**2)
    return result_list

print(square(num_list))



def  square(num_list):
    for num in num_list:
        yield num**2

for number in square(num_list):
    print(number)


def cube(num_list):
    result=[]
    for num in num_list:
        result.append(num**3)
    return result

print(cube(num_list))

def cube_by_yield(num_list):
    for num in num_list:
        yield num**3

for num in cube_by_yield(num_list):
    print(num)
