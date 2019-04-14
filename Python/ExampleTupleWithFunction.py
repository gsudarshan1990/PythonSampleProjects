numbers=[12,3,89,54,8]

def high_and_low(numbers):
    highest=max(numbers)
    lowest=min(numbers)
    return (highest,lowest)



(highest,lowest)=high_and_low(numbers)
print(highest)
print(lowest)
