def without_generate_cube(n):
    result=[]
    for i in range(n):
        result.append(i**3)
    return result

print(without_generate_cube(10))

def generate_cube(n):
    for i in range(n):
        yield i**3

for number in generate_cube(10):
    print(number)


