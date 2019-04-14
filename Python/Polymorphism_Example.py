class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
print('Number of working hours for the employee is ',end =' ')
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print('Number of working hours for the trainee is', end=' ')
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print('Number of working hours for the trainee is', end=' ')
trainee.displayNumberOfWorkingHours()
