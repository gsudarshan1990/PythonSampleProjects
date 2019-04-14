class Employee:
    def __init__(self, name):
        self.name= name

    def print_employee_name(self):
        print(self.name)


employee1=Employee('sudarshan')
employee1.print_employee_name()
employee2=Employee('govindarajan')
employee2.print_employee_name()
