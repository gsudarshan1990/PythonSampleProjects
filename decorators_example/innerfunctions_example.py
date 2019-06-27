def hello(name='Jose'):
    print('This is from the hello function')

    def greet():
        return 'This is from the greet function'

    def welcome():
        return 'This is from the welcome function'

    if name == 'Jose':
        return greet
    else:
        return welcome

hello()
my_new_function=hello()
print(my_new_function())
my_new_function=hello('San')
print(my_new_function())
