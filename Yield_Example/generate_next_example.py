def simple_generate():
    for i in range(3):
        yield i

g=simple_generate()
print(next(g))
print(next(g))
print(next(g))
