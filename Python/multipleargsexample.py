def print_two(*args):
    arg1,arg2=args
    print(f'The two arguments are {arg1} and {arg2}')

def print_two_arguments(arg1,arg2):
    print(f'The two arguments are {arg1} and {arg2}')

def print_one_argument(arg1):
    print(f'One argument are {arg1}')

def print_no_agrument():
    print('No argument')

print_two("first","second")
print_two_arguments("third","fourth")
print_one_argument("five")
print_no_agrument()
