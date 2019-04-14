class A:
    def method(self):
        print('This method belongs to Class A')
    pass

class B(A):
    def method(self):
        print('This method belongs to Class B')
    pass

class C(A):
    def method(self):
        print('This method belongs to Class C')
    pass

class D(C,B):
    pass

d=D()
d.method()
