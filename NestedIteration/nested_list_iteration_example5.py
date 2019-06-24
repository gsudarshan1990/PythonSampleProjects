"""

Iterate through the list so that if the character ‘m’ is in the string, then it should be added to a new list called m_list
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']

"""
m_list=list()
nested_list=['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']
for first_outer_list_item in nested_list:
    if type(first_outer_list_item) is list:
        for first_inner_list_item in first_outer_list_item:
            if type(first_inner_list_item) is list:
                for second_inner_list_item in first_inner_list_item:
                    if 'm' in second_inner_list_item:
                        m_list.append(second_inner_list_item)
            else:
                if 'm' in first_inner_list_item:
                    m_list.append(first_inner_list_item)
    else:
        if 'm' in first_outer_list_item:
            m_list.append(first_outer_list_item)
print(m_list)
