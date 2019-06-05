class Sample():

    def __init__(self,value):
        self.value=value

    def add_to_value(self,amount):
        self.value=self.value+amount


sample=Sample(300)
print(sample.value)
sample.add_to_value(800)
print(sample.value)
