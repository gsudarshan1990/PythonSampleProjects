def check_even(num):
    return num%2 == 0

mylist=[1,2,3,4,5,6]

print(list(filter(check_even,mylist)))
