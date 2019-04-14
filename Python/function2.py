def check_positive_or_negative():
    data=input('Enter the number')
    if int(data)<0:
        return 'NEGATIVE'
    else:
        return 'POSITIVE'

print(check_positive_or_negative())
