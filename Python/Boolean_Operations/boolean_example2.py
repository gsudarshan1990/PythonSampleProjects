people = 30
cars = 40
buses = 15

if cars>people:
    print('We should take cars')
elif cars<people:
    print('We should not take cars')
else:
    print('We cannot decide')

if buses > cars:
    print('There are too many buses')
elif buses<cars:
    print('We should take buses')
else:
    print('We cannot decide')

if people>buses:
    print('We should take buses')
else:
    print('We cannot decide')
