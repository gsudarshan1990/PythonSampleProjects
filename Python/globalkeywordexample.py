#in the below no global key word is used

x =50

def func(x):
    print(x)
    x=100
    print('the value of x changed from 50 to {}'.format(x))

func(x)
print('The value of x after changing in the fuction didnot get effect outside the function'+str(x)) #Since no global keywoard is used the change in function does not effect initial initialization


x=50
def func():
    global x
    print(x)

    x=100
    print('The value of x changed from 50 to {}'.format(x))

func()
print(x)
