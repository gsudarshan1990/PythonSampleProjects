class Furniture:
        type_of_furniture ='TeakWood'

class Chair(Furniture):
    def __init__(self):
     self.__number_of_legs= 4

    def change_wood_type(self):
        print('Enter the wood type for changing')
        wood_type = input()
        self.type_of_furniture = wood_type

    def display_description(self):
        print('The default wood type used is ',self.type_of_furniture)
        print('number of legs the chair has',self.__number_of_legs)



furniture = Furniture()
chair=Chair()
chair.display_description()
chair.change_wood_type()
chair.display_description()

