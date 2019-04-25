my_list=[1,2,3,4,5,6,7,8,9,10]

print('printing the elements of the list')
for element in my_list:
    print(element)


print('Priting the even numbers in list')
for num in my_list:
    if num%2 == 0:
        print('{} is even'.format(num))

print('Printing the sum of all numbers in the list')

list_sum =0

for num in my_list:
    list_sum+=num
print(list_sum)



string1='Hello World'
print('String {}'.format(string1))

print('Printing the letters in the String')
for letter in string1:
    print(letter)

print('Working for loops with tuples')

tuple1=(1,2,3)
print('Printing the elements in the tuple')

for item in tuple1:
    print(item)

my_list2=[(1,2),(3,4),(5,6),(7,8)]

for item in my_list2:
    print(item)

for (a,b) in my_list2:
    print(a)

my_list3= [(1,2,3),(4,5,6),(7,8,9)]

for a,b,c in my_list3:
    print(c)

