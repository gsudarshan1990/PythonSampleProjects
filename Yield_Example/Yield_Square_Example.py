def square(number):
    for i in range(number):
        yield i**2

print(square(9))

for number in square(10):
    print(number)
