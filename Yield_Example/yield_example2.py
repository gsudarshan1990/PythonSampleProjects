my_list=[1,2,3,4,5]

def square(mylist):
    for number in mylist:
        yield  number**2

for square_number in square(my_list):
    print(square_number)
