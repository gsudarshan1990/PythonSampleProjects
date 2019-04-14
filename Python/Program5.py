miles=input('how far would you like to travel')
floatvalue=float(miles)
if floatvalue<3.0:
    print('I would suggest you to walk')
elif floatvalue<300.0:
    print('I would suggest you to drive')
else:
    print('I would suggest you to fly')
