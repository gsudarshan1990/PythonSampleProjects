def new_decorator_function(original_function):

    def wrap_function():
        print('Some code before the original function')

        original_function()

        print('Some Code after the original function')

    return wrap_function

def new_function():
    print('This is the original function')

my_function=new_decorator_function(new_function)
my_function()
