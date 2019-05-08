def square(num):
    return num**2


#Square of number with Lambda
mylist=[1,2,3,4,5]
print(list(map(lambda num:num**2,mylist)))

#Even numbers with Lambda
mylist2=[1,2,3,4,5,6]
print(list(filter(lambda num:num%2==0,mylist2)))

#First Letter with Lambda
names=['Giraffe','Zebra','Horse']
print(list(map(lambda name:name[0],names)))


#Twice the number

print(list(map(lambda num:2*num,mylist)))

