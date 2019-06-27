def hello():
    print('This statement is from the hello function')
    return None

print(hello)
hello()

greet=hello
print(greet)
greet()
del hello
greet()

