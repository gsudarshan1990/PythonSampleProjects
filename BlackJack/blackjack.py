import random

suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing=True

class Card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank+' of '+self.suit


class Deck():

    def __init__(self):
        self.deck=list()
        for suit in suits:
            for rank in ranks:
                card=Card(suit,rank)
                self.deck.append(card)

    def __str__(self):
        for i in self.deck:
            print(i)
        return ''

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card=self.deck.pop()
        return single_card

#test_deck=Deck()
#print(test_deck)


class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]

        if card.rank == 'Ace':
            self.aces+=1

    def adjust_for_aces(self):

        if self.value>21 and self.aces:
            self.value-=10
            self.aces-=1

"""
test_hand=Hand()
test_deck.shuffle()
pulled_card=test_deck.deal()
print(pulled_card)
test_hand.add_card(pulled_card)
print(test_hand.value)
"""

class Chips():

    def __init__(self,total=100):
        self.total=total
        self.bet=0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet=int(input('Enter the bet?'))
        except:
            print('Please provide the integer')
        else:
            if chips.bet>chips.total:
                print('Sorry you dont have enough chips. you have:{}'.format(chips.total))
            else:
                break


def hit(test_deck,test_hand):
    single_card=test_deck.deal()
    test_hand.add_card(single_card)
    test_hand.adjust_for_aces()

def hit_or_stand(test_deck,test_hand):
    global playing

    while True:
        option = input('Enter hit or Stand? h or s')

        if option[0].lower() == 'h':
            hit(test_deck,test_hand)

        elif option[0].lower() == 's':
            print('Player Stands')
            playing = False
        else:
            print('Please enter the correct option which is h or s. Currently you have entered inappropriate option')
            continue

        break

def player_wins(player,dealer,chips):
    print('Player Wins')
    chips.win_bet()

def player_busts(player,dealer,chips):
    print('Player Lost')
    chips.lose_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer Wins, Player Lost')
    chips.lose_bet()

def dealer_busts(player,dealer,chips):
    print('Player wins,Dealer Lost')
    chips.win_bet()

def push(player,dealer):
    print('Player and Dealer tie!')


def show_some(player,dealer):
    print('Dealer Hand')
    print('Print One Hidden Card')
    print(dealer.cards[1])
    print('\n')
    print('Player Hand')
    for card in player.cards:
        print(card)


def show_all(player,dealer):
    print('Dealer Hand')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Player Hand')
    for card in player.cards:
        print(card)


while True:
    #Print the Opening the Statement

    print('Welcome to Black Jack')

    #Create Deck, shuffle and add two cards

    deck=Deck()
    deck.shuffle()

    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #Create the player chips

    player_chips=Chips()


    #take bet

    take_bet(player_chips)

    #show the cards

    show_some(player_hand,dealer_hand)

    while playing:

        #hit or stand
        hit_or_stand(deck,player_hand)

        #Show some of the cards

        show_some(player_hand,dealer_hand)

        #If the Player busts
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break


        #if the player has not busted

        if player_hand.value<=21:

                while dealer_hand.value<player_hand.value:
                    hit(deck,dealer_hand)

                show_all(player_hand,dealer_hand)

        #Different Scenarios

        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

        #Inform the total number of chips

        print('The Total number of chips {}'.format(player_chips.total))

        #Check whether user want to play the game again

        new_game=input('Please let us know if you want to play the game again? y/n')

        if new_game[0].lower() == 'y':
            playing=True
            continue
        else:
            print('Thank you for the playing')
            break
