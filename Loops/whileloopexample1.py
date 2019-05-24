n=5
while n>0:
    print(n)
    n-=1
print('loop completed')

"""
while True:
    inp=input('Enter some information and done to stop the loop')
    if inp == 'done':
        break
    print(inp)
print('loop completed')
"""

while True:
    inp=input('Enter the information and done to stop the loop')
    if inp[0] == '#':
        continue
    if inp == 'done':
        break
    print(inp)
print('loop completed')

count=0
list1=[3, 41, 12, 9, 74, 15]
for value in list1:
    count+=1
print(count)

total=0
list1=[3, 41, 12, 9, 74, 15]
for number in list1:
    total+=number
print(total)

largest=None
list1=[3, 41, 12, 9, 74, 15]
for number in list1:
    if largest is None or number>largest:
        largest=number
print(largest)


smallest=None
list1=[3, 41, 12, 9, 74, 15]
for number in list1:
    if smallest is None or number<smallest:
        smallest=number
print(smallest)
