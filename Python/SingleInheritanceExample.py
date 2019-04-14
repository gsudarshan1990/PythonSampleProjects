class Apple:
    manufacturer = 'Apple Incorporated'
    contactDetails = 'www.apple.com'

    def display_contact_details(self):
        print('Log on to the website',self.contactDetails)


class Iphone(Apple):
    year=2019

    def print_details(self):
        print('The device was manufactured in the year {0} by the manufacturer {1}'.format(self.year, self.manufacturer))



iphone=Iphone()
iphone.display_contact_details()
iphone.print_details()
