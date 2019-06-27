def hello():
    print('This is the hello function')

def other(some_other_function):
    print('Some other code')
    some_other_function()


other(hello)
