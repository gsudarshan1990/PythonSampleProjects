"""
create a python program that captures and displays a person's to-do list. Continually prompt the user for another item until they enter a blank item.
After all items are entered, display to-do list back to the user
"""

while True:
    print('Enter a task for your to-do list')
    print('If no data is needed to be entered press enter')
    data=input()
    if not data:
        break
    else:
        list.append(data)


print(list)
