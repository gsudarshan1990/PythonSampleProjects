mylist=[1,2,3,4,5]

generator_comprehension=(item for item in mylist if item>3)

for i in generator_comprehension:
    print(i)

mylist1=[1,4,-5,10,-7,2,3,-1]

generator=(n for n in mylist1 if n>0)

for number in generator:
    print(number)
