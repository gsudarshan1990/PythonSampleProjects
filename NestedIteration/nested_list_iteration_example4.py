"""
Reading the nested list with different items of different type
[1,2,['a','b','c'],['d','e'],['f','g','h']]

"""

nested1=[1,2,['a','b','c'],['d','e'],['f','g','h']]
for outer_list_item in nested1:
    print('level1:')
    """
    Iterating through the below code will produce the error
    for inner_list in outer_list:
        print('      level2:',inner_list)
    """
    if type(outer_list_item) is list:
        for inner_list_item in outer_list_item:
            print('          level2:'+inner_list_item)
    else:
        print('          level2:',outer_list_item)
