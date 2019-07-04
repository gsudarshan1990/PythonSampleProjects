word='hello'
mylist1=[letter for letter in word]
print(mylist1)

mylist2=[num for num in range(0,11) if num%2 ==0]
print(mylist2)


num_list=[1,2,3,4,5]

def square(num_list):
    return [num**2 for num in num_list]

print(square(num_list))

def cube(num_list):
    return [num**3 for num in num_list]

print(cube(num_list))



mylist=[1,4,-5, 10,-7,2,3,-1]
list1=[n for n in mylist if n>0]
print(list1)

list2=[n for n in mylist if n<0]
print(list2)

mylist2=['sample','sun','summer','winter','rainy']
list3=[word for word in mylist2 if 's' in word]
print(list3)

mylist3=['tool','table','google','yahoo','microsoft']
list4=[word for word in mylist3 if 't' in word]
print(list4)


mylist5=[1, 4, -5, 10, -7, 2, 3, -1]
list5=[n**2 for n in mylist5 if n>0]
print(list5)
