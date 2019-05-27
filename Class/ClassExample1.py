class FirstClass():
    def __init__(self,param1,param2):
        self.param1=param1
        self.param2=param2
    def print_values(self):
        print(self.param1)
        print(self.param2)

object1=FirstClass('Hello','Sudarshan')
object1.print_values()
print(object1.param1)
