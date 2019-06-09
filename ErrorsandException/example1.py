"""
Else block runs when there is no exception
"""

try:
    result=10+10
except:
    print('You are trying to add wrongly')
else:
    print('Added Correctly')
    print(result)

"""
Except block runs when there is an exception
"""

print('-'*10)

try:
    result=10+'10'
except:
    print('You are trying to add wrongly')
else:
    print('Added Correctly')
    print(result)



