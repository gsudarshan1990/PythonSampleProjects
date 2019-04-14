class Stone:
    Number_of_precious_stone=5
    precious_stone=[]

    def enter_precious_stone(self):
        data=input('enter the precious stone')
        self.precious_stone.append(data)

    def display_precious_stone(self):
        print(self.precious_stone)

    def remove_top_precious_stone(self):
        for number in range(self.Number_of_precious_stone,len(self.precious_stone)):
            self.precious_stone.pop(0)

stone1=Stone()
for number in range(1,6):
    stone1.enter_precious_stone()
stone1.display_precious_stone()

stone1.enter_precious_stone()


stone1.remove_top_precious_stone()
print(stone1.precious_stone)
