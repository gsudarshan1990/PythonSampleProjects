days_Of_The_week=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
print(days_Of_The_week)
firstday=days_Of_The_week[0]
print(firstday)

list1=list(days_Of_The_week)
print(list1)

print(type(list1))
print(type(days_Of_The_week))

animals_list=['lion','dog', 'giraffe']
animals_tuple=tuple(animals_list)

print(type(animals_list))
print(type(animals_tuple))

for days in days_Of_The_week:
    print(days.upper())

Weekends=['Satuday','Sunday']
(sat,sun)=Weekends
print(sat)
print(sun)


contacts=[('sudarshan','9176320342'),('Father','9840579546')]

for (name,phone) in contacts:
    print('{} has the phone_number {}'.format(name,phone))
