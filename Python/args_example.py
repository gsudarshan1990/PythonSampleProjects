"""
Define a function that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even
"""

def my_function(*args):
    '''
    function that any number of arguments and returns a list with only even numbers
    :param args: arbitary number of arguments
    :return: list of even numbers
    '''
    length=len(args)
    print(length)
    even_list=[]
    for i in range(0,length):
        if args[i]%2 == 0:
            even_list.append(args[i])
    return even_list

result=my_function(1,2,3,5,8,42,73,78)
print(result)
