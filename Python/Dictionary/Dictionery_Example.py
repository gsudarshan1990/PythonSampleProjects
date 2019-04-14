"""
 

Create a dictionary that contains a list of people and one interesting fact about each of them. 
Display each person and their interesting fact to the screen. Next, change a fact about one of 
the people. Also add an additional person and corresponding fact. Display the new list of people 
and facts. Run the program multiple times and notice if the order changes. 

 
"""

FamilyMemebrs_Interstingfacts={'Govindarajan':'Likes to communicate','sudarshan' :'Likes to work more'}

for person,interestingfact in FamilyMemebrs_Interstingfacts.items():
    print('Member :{} , intersting fact: {}'.format(person,interestingfact))

print('-'*20)
print('After changing the fact and adding new member')

FamilyMemebrs_Interstingfacts['sudarshan']='Likes to be perfectionist'
FamilyMemebrs_Interstingfacts['lakshmi']='Likes to learn new things'



for person,interestingfact in FamilyMemebrs_Interstingfacts.items():
    print('Member :{} , intersting fact: {}'.format(person,interestingfact))
