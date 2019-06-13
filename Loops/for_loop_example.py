the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quaters']

for number in the_count:
    print('the number ',number)

for fruit in fruits:
    print('The fruit type is ',fruit)

for i in change:
    print(i)

empty_list=list()

for number in range(6):
    empty_list.append(number)

for number in empty_list:
    print(number)
