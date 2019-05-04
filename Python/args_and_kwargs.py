#Function without args

def add_numbers(a,b,c,d,e,f):
    return sum((a,b,c,d,e,f))

result=add_numbers(1,2,3,4,5,6)
print(result)

#Error will be obtaining when we use 7 arguments instead of 6


def add_numbers(*args):
    print(args)
    print(sum(args))

print('The following results are obtained without changing the function definition')
print('Initially only 5 arguments is passed')
add_numbers(1,2,3,4,5)
print('Ten arguments is passed')
add_numbers(1,2,3,4,5,6,7,8,9,10)


print('*'*10)
print('Usage of **kwargs')
print('*'*10)

def my_function(**kwargs):
    print(kwargs)
    print(kwargs['fruit'])

my_function(fruit='apple',vegetable='Tomato')


def function(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I like {} {}'.format(args[0],kwargs['food']))


function(10,20,30,40,fruit='orange',food='rice')
