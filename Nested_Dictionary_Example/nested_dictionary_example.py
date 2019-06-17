info={'personal_data':
          {'name':'Lauren',
           'age':20,
           'major':'information science',
            'physical-features':
               {
                   'color':
                       {
                           'eye':'blue',
                           'hair':'brown'
                       },
                   'height':"5\'8"
               }
             },
           'other':
               {
                   'favorite_colors':['purple','green','blue'],
                   'intersted_in':['social_media','intellectual property','copyright','music','books']
               }
      }

descendant_dict=info['personal_data']
print(descendant_dict)
second_descendant_dict=descendant_dict['physical-features']
print(second_descendant_dict)
third_descendant_dict=second_descendant_dict['color']
print(third_descendant_dict)
