class OperatingSystem:
    multitasking = True
    name ='Windows'


class Apple:
    details ='www.apple.com'
    name ='Macintosh'

class MacBook(OperatingSystem,Apple):
    def __init__(self):
        if self.multitasking is True:
            print('This system is a multi tasking system and belongs to {} orgainization'.format(self.details))
            print(self.name)


macbook = MacBook()
