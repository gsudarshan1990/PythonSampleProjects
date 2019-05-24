total=0
count=0
while True:
    inp=input('Enter the number')
    if inp == 'done':
        break
    num=float(inp)
    total=total+num
    count=count+1
average=total/count
print(average)
