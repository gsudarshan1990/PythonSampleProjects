class Employee:
    def employee_Details(self):
        self.name='sudarshan'
        print('Name= ',self.name)
        age =30
        print('Age= ',age)

    def print_employee_details(self):
        print('Printing from the another function')
        print('Name= ',self.name)
        #print('Age= ',age)

    @staticmethod
    def WelcomeMessage():
         print('Welcome to the new organization')

employee1=Employee()
employee1.employee_Details()
employee1.print_employee_details()
employee1.WelcomeMessage()


