def square(num):
    return num**2

mylist=[1,2,3,4,5]

for item in map(square,mylist):
    print(item)

print(list(map(square,mylist)))


def cube(num):
    return num**3

print(list(map(cube,mylist)))



