import random

values=[1,2,3,4,5]

for i in range(0,5):
    print(random.choice(values))


random.shuffle(values)
print(values)
