
dictionery_phonenumber={'sudarshan':'9378153277','father':'9840579546'}
sudarshan_contactnumber=dictionery_phonenumber['sudarshan']
father_contactnumber=dictionery_phonenumber['father']

print('contact numbe of sudarshan is {}'.format(sudarshan_contactnumber))
print('contact number of father is {}'.format(father_contactnumber))

print('After changing the sudarshan contact number')
print('-'*20)

dictionery_phonenumber['sudarshan']='9176320342'
print('contact number of sudarshan is {}'.format(dictionery_phonenumber['sudarshan']))

dictionery_phonenumber['mother']='9176221358'
print(dictionery_phonenumber)
print('Total number of contents in dictionery is '+str(len(dictionery_phonenumber)))

print('-'*20)
print('Inserting the new contact number of sonu')

dictionery_phonenumber['sonu']='9030117843'
print(dictionery_phonenumber)

print('Deleting a contact number from the dictionery')
print('-'*20)

del dictionery_phonenumber['sonu']
print(dictionery_phonenumber)

del dictionery_phonenumber['sudarshan']

print('Dictionery can store the values of multiple data types')
dictionery_phonenumber['sudarshan']=['9176320342','9962111378']


print(dictionery_phonenumber)
print(dictionery_phonenumber['sudarshan'])

for phonenumber in dictionery_phonenumber['sudarshan']:
    print(phonenumber)

print('Printing a single phone number form multiple phone numbers')

if 'sudarshan' in dictionery_phonenumber.keys():
    print(dictionery_phonenumber['sudarshan'][0])

if 'sonu' in dictionery_phonenumber.keys():
    print('sonu is available in the dictionery')
else:
    print('sonu is not available')

print(dictionery_phonenumber['sudarshan'][0])

print('sudarshan' in dictionery_phonenumber.keys())

print('9840579546' in dictionery_phonenumber.values())


for people in dictionery_phonenumber:
    print(dictionery_phonenumber[people])

for people,numbers in dictionery_phonenumber.items():
    print(' The person {} has the phone number {}'.format(people,phonenumber) )
