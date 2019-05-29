from sys import argv

script, user_name=argv
prompt='>'

print('The name of the this file is {} and your name is {}'.format(script,user_name))
print ('Answer the following question')
print('Do you like me {}'.format(user_name))
like=input(prompt)
print('where do you live {}'.format(user_name))
live=input(prompt)
print('what kind of computer you have?')
computer=input(prompt)

print('So you {} {},  you live at {}, and you have {} computer'.format(like,user_name,live,computer))
