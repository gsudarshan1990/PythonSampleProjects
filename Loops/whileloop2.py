while True:
    inp=input('Enter the line')
    if inp.startswith('#'):
        continue
    if inp=='done':
        break
    print(inp)
