
def add_decorator(argument_func):
     def wrapper(*args,**kwargs):
        name=argument_func.__name__
        print(f'before {name} is called')
        r=argument_func(*args,**kwargs)
        print(f'after {name} is called')
        return r
     return wrapper

@add_decorator
def add_function(a,b):
    return a+b

print(add_function(2,4))
