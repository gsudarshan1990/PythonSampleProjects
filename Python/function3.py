def get_name():
    name=input('Enter the name')
    return name

def say_name(name):
    print('Hi {}'.format(name))

def greetings():
    name=get_name()
    say_name(name)

greetings()
