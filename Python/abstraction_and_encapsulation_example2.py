class Car:
    def __init__(self,carslist):
        self.availbalecarslist=carslist

    def display_Cars(self):
        for cars in self.availbalecarslist:
            print(cars)

    def total_cost(self,carname,numberofdays):
        cost=1
        if carname == 'HatchBack':
            cost=30*numberofdays
        elif carname == 'Sedan':
            cost=50*numberofdays
        elif carname == 'SUV':
            cost=100*numberofdays
        print('Total cost for the selected car is {0}'.format(cost))


class Customer:
    def request_type_of_car(self):
        print('Enter the name of the car')
        car_name=input()
        return car_name

    def request_number_of_days(self):
        print('Enter the number of the days')
        days=int(input())
        return days


car=Car(['HatchBack','Sedan','SUV'])
customer=Customer()
car.display_Cars()
name_of_the_car=customer.request_type_of_car()
number_of_days=customer.request_number_of_days()
car.total_cost(name_of_the_car,number_of_days)
