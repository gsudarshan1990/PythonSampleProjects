def ask_for_integer():
    try:
        number=int(input('Please provide the number'))
    except:
        print('You have provided the wrong number')
    finally:
        print('End of the try/except block')


ask_for_integer()


print('-'*10)
print('Asking till the number is obtained')

def ask_for_integer_until_obtained():
    while True:
        try:
            number=int(input('Please provide the number'))
        except:
            print('you have provided the wrong number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('End of try\except block')

ask_for_integer_until_obtained()
