class Employee:
    name='sudarshan'
    designation='Sr. Software engineer'
    Number_of_UserStories_worked=2
    numberOfWorkingHours=40

    def target_achieved(self):
        if self.Number_of_UserStories_worked>1:
            print('Target has been achieved')
        else:
            print('Target has not been achieved')


employee1=Employee()
employee1.target_achieved()
print(employee1.name)

employee2=Employee()
employee2.name='Govindarajan'
print(employee2.name)

employee1.age=28
print(employee1.age)

employee2.age=50
print(employee2.age)

print(employee1.numberOfWorkingHours)
print(employee2.numberOfWorkingHours)

Employee.numberOfWorkingHours=45

print(employee1.numberOfWorkingHours)
print(employee2.numberOfWorkingHours)

employee1.numberOfWorkingHours=40

print(employee1.numberOfWorkingHours)
print(employee2.numberOfWorkingHours)
