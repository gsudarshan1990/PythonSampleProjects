for number in [5,4,3,2,1]:
    print(number)
print('Blastsoff')

friends=['Joseph','Glen','Sally']
for friend in friends:
    print('Hello '+friend)
print(friends[1])

lotto=[2,14,26,41,63]
print(lotto)
lotto[2]=28
print(lotto)


#String are not mutable
"""
string1='Banana'
string1[0]='b'  Not possible
"""

string1='Banana'
print(string1.lower())


greet='Hello Sudarshan'
print(len(greet))

list2=[1,33,'Sudarshan',99]
print(len(list2))


friends=['Joseph','Glen','Sally']
for i in range(len(friends)):
    print(str(i)+":"+friends[i])

