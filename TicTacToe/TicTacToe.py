
#Create a board

def test_board(board):
    print(' | | ')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' | | ')
    print('-|-|-')
    print(' | | ')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(' | | ')
    print('-|-|-')
    print(' | | ')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(' | | ')

#test_list=['#','X','','O','O','O','X','O','X','O']
#test_board(test_list)

def choose_marker():
    marker=''
    while (marker!='X') and (marker!='O'):
        marker=input('please choose between "X" or "O"')
    player1=marker

    if player1 == 'X':
        player2='O'
    elif player1 == 'O':
        player2 ='X'
    return (player1,player2)

#print(choose_marker())


def place_marker(test_list,marker,position):
    test_list[position]=marker

#place_marker(test_list,'$',8)
#test_board(test_list)

def win_check(test_list,marker):


    return (test_list[1] == test_list[2] == test_list[3]!='') or \
    (test_list[4] == test_list[5] == test_list[6]!='') or \
    (test_list[7] == test_list[8] == test_list[9]!='') or \
    (test_list[1] == test_list[4] == test_list[7]!='') or \
    (test_list[2] == test_list[5] == test_list[8]!='') or \
    (test_list[3] == test_list[6] == test_list[9]!='') or \
    (test_list[1] == test_list[5] == test_list[9]!='')  or \
    (test_list[3] == test_list[5] == test_list[7]!='')

#print('-'*10)
#test_board(test_list)
#print(win_check(test_list,'X'))

import random

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == ' '

#print(space_check(test_list,4))

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False #if board has space
    return True #if the board is full

#print(full_board_check(test_list))

def player_choice(board):
    position = 0
    list2=[1,2,3,4,5,6,7,8,9]
    while position not in list2:
        if not space_check(board,position):
            position=int(input('Choose the position(1-9)'))

    return position
#player_choice(test_list)


def replay():
    choice=input('Enter "Yes" if you want to play again and if do want to play again enter "NO"')
    if choice == 'Yes':
        return True
    elif choice == 'No':
        return False


print('Welcome to Tic Tac Toe Game')

def check_full(board):
    for i in range(1,10):
        if check_index(board,i):
            return False
    return True

def check_index(board,position):
    return board[position] == ''

while True:
    test_list=['']*10
    player1_marker,player2_marker=choose_marker()
    inp=input('Do you want to play ? y or n')
    if inp == 'y':
        game_on=True
    else:
        game_on=False

    turn=choose_first()
    while game_on:
        if turn == 'Player 1':
            print('Player1')
            test_board(test_list)
            position = player_choice(test_list)
            place_marker(test_list, player1_marker, position)
            if win_check(test_list, player1_marker):
                print('Player 1 has won the game')
                print(test_board(test_list))
                game_on = False
            else:
                if check_full(test_list):
                    print('Game is Tied')
                    game_on = False
                else:
                    turn = 'Player 2'
        elif turn == 'Player 2':
            print('Player 2')
            test_board(test_list)
            position = player_choice(test_list)
            place_marker(test_list, player2_marker, position)
            if win_check(test_list, player2_marker):
                print('Player 2 has won the game')
                print(test_list)
                game_on = False
            else:
                if check_full(test_list):
                    print('Game is Tied')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break

