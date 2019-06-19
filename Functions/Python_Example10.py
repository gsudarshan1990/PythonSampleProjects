

def gold_room():
    print('This room is full of gold,enter the number to take the gold')
    next=input('Enter the number and should be 0 or 1')
    if "0" in next or "1" in next:
        how_much_gold=input('how much gold do you want to take')
    else:
        print('Please enter the number')

    if int(how_much_gold)<50:
        print('You are not greedy and you win')
    else:
        print('You are greedy and you lose')

def bear_room():
    print('This is bear room')
    print('This bear has some honey')
    print('The bear is in front of another door')
    print('How are you going to move the bear')
    print('From the above enter the options')
    bear_moved=False

    while True:
        next=input('Enter the option')

        if next == 'take honey':
           dead('The bear looks at you and you are finished')
        elif next =='taunt bear' and not bear_moved:
            print('The bear has moved')
            bear_moved=True
        elif next =='taunt bear' and bear_moved:
            print('The bear has not moved')
        elif next == 'open door' and bear_moved:
            gold_room()
        else:
            print('You have entered the wrong option')
def dead():
    pass
