def temp_convert(value):
    return int(value)

try:
    temp_convert('xyz')
except ValueError as argument:
    print('Could not convert the number',argument)
