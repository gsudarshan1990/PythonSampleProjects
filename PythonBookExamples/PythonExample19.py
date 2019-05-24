"""
Exercise 1: Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.
"""

list1=list()
while True:
    inp=input('Enter the number')
    if inp == 'done':
        break
    try:
        number=float(inp)
        list1.append(number)
    except:
        print('Invalid Input')

print('total',sum(list1))
print('count',len(list1))
print('average',(sum(list1)/len(list1)))
