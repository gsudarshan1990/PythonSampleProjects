nested_list=[['a','b','c'],['d','e'],['f','g','h']]

for outer_item in nested_list:
    print('level1:',outer_item)
    for inner_item in outer_item:
        print("         level2:",inner_item)
