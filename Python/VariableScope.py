name='Lion'#Global Variable

def greet():
    #Enclosing Value
    name='Sammy'

    def hello():
        #name='Jack' Local Variable
        print('Hello '+name)
    hello()

greet()
