"""
The nested dictionary, pokemon, shows the number of various Pokemon that each person has caught while playing Pokemon Go. Find the total number of rattatas, dittos, and pidgeys caught and assign to the variables r, d, and p respectively.

pokemon = {'Trainer1':
          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
          'Trainer2':
          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
          'Trainer3':
          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
          'Trainer4':
          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}



"""


pokemon = {'Trainer1':
          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
          'Trainer2':
          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
          'Trainer3':
          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
          'Trainer4':
          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}

r=0
d=0
p=0
for outer_dict_key in pokemon:
    for inner_dict_key in pokemon[outer_dict_key]:
        #for second_inner_dict_key in pokemon[outer_dict_key][inner_dict_key]:
            #print(pokemon[outer_dict_key][inner_dict_key][second_inner_dict_key])
        if 'rattatas' in pokemon[outer_dict_key][inner_dict_key]:
            r+=pokemon[outer_dict_key][inner_dict_key]['rattatas']
        if 'ditto' in pokemon[outer_dict_key][inner_dict_key]:
            d+=pokemon[outer_dict_key][inner_dict_key]['ditto']
        if 'pidgey' in pokemon[outer_dict_key][inner_dict_key]:
            p+=pokemon[outer_dict_key][inner_dict_key]['pidgey']
print(r)
print(d)
print(p)
