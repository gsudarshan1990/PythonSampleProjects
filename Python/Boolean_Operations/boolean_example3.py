print('You have entered a dark room with two doors. Do you want to go through door 1 or door 2')

door_number=int(input('>enter the option'))

if door_number == 1:
    print('There is a bear eating the cake. What do you do?')
    print('1. Take the Cake')
    print('2. Scream at the bear')

    your_answer=int(input('>enter the option'))

    if your_answer == 1:
        print('bear eats your face. Good job!')
    elif your_answer == 2:
        print('bear eats your legs, Good Job!')
    else:
        print('bear ran away')

elif door_number == 2:
    print('You stare through retina into the endless abyss')
    print('1.Blue berries')
    print('2.Yellow Jacket Clothespins')
    print('3. Understanding revolvers yelling melodies')

    your_answer=input('>enter the option')

    if your_answer == 1 or your_answer == 2:
        print('your body survives')
    else:
        print('Eyes Cannot Survive')
else:
    print('You Stumble down and fall')
