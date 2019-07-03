
def func():
    print('Calling function')

def log_calls(argument_func):
    def wrapper():
        name=argument_func.__name__
        print(f'Before {name} is called')
        argument_func()
        print(f'After {name} is called')
    return wrapper


func=log_calls(func)
func()

@log_calls
def new_func():
    print('Good Morning')
