import math
class Circle():
    #class level attribute
    math_pi=math.pi
    normal_pi=3.14

    def __init__(self,radius=1):
        self.radius=radius

    def get_circumference_with_math(self):
        return 2*self.math_pi*self.radius

    def get_normal_circumference(self):
        return 2*self.normal_pi*self.radius

    def get_area_with_math(self):
        return self.math_pi*self.radius**2

    def get_area_with_normal(self):
        return self.normal_pi*self.radius**2

mycircle=Circle(radius=10)
print(mycircle.get_circumference_with_math())
print(mycircle.get_normal_circumference())
print(mycircle.get_area_with_math())
print(mycircle.get_area_with_normal())
