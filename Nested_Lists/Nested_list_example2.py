"""
Extract the word 'willow' from the below list
['bagel','cream cheese',breakfast','grits','eggs','bacon',[34,9,73,[]],[['willow','birch','elm'],'apple','peach','cherry']]
"""

given_list=['bagel','cream cheese','breakfast','grits','eggs','bacon',[34,9,73,[]],[['willow','birch','elm'],'apple','peach','cherry']]
print('Obtaining the 7th index')
print(given_list[7])
item_one=given_list[7]
item_two=item_one[0]
print(item_two)
item_three=item_two[0]
print(item_three)
print('Another Way')
print('given_list[7][0][0]:',given_list[7][0][0])
