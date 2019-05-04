"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19

"""

def blackjack(a,b,c):
    total=sum((a,b,c))
    if  total<=21:
        print(total)
    else:
        if (a==11) or (b==11)or(c==11):
            total-=10
            print(total)
        else:
            print('BUST')

blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)


