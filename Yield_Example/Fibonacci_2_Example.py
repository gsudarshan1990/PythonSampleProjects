def generate_fibonacci(number):
    a=1
    b=1

    for i in range(number):
        yield a
        a,b=b,a+b

g=generate_fibonacci(10)

for i in range(10):
    print(next(g))
