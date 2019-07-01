def generate_fibonaccci(number):
    a=1
    b=1
    for i in range(number):
        yield a
        a,b=b,a+b

print(generate_fibonaccci(10))

for number in generate_fibonaccci(10):
    print(number)
