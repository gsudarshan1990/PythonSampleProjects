class Laptop():
    def __init__(self):
        print('I am a laptop')

    def speaker(self):
        print('I am speaker')

class HP(Laptop):
    def __init__(self):
        Laptop.__init__(self)
        print('I belong to brand HP')

    def speaker(self):
        print('I use headphone belong to brand skullcandy')


myhp=HP()
myhp.speaker()
