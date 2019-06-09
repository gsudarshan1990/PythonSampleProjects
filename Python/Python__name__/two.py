import One

print('Top level function for two.py')

One.function1()

if __name__ =='__main__':
    print('two.py is called directly')
else:
    print('two.py is imported')

