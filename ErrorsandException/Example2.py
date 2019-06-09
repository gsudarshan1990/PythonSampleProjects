"""
Usage of finally when there is no exception
"""

try:
    result=10+10
except:
    print('You have added wrongly')
finally:
    print('I always run')
    print(result)

"""
Usage of finally when there is exception
"""

print('-'*10)

try:
    result=10+'10'
except:
    print('You have added wrongly')
finally:
    print('I always run')
