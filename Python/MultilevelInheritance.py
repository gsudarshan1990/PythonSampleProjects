class GrandFather:
    grand_father_name='vijay raghavan'


class Father(GrandFather):
    father_name='Govindarajan'

class Self(Father):
    def __init__(self):
        self.name = 'Sudarshan'
        print('father name:{0}'.format(self.father_name))
        print('grand father name:{0}'.format(self.grand_father_name))
        print('Self Name:{0}'.format(self.name))

yourself=Self()
