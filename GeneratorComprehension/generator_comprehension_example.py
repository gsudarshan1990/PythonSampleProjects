mylist=[1,2,3,4,5]

generator_comprehension=(item for item in mylist if item>3)

for i in generator_comprehension:
    print(i)
