class Laptop():
    def __init__(self,brand,processor,user,inches):
        self.brand=brand
        self.processor=processor
        self.user=user
        self.inches=inches

    def __str__(self):
        return f"Laptop {self.brand} with processor {self.processor} is used by {self.user}"

    def __len__(self):
        return self.inches

    def __del__(self):
        print('A laptop object has been deleted')


hp_laptop=Laptop("HP","i5","sudarshan",15)
dell_laptop=Laptop("Dell","i7","sudarshan",17)

print(hp_laptop)
print(dell_laptop)
print(len(hp_laptop))
print(len(dell_laptop))
del hp_laptop
