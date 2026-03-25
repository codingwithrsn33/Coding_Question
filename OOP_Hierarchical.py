class Parent:
    def House(self):
        print("I am the BOSS")
        
class Child1(Parent):
    def bike(self):
        print("I am Child1")

class Child2(Parent):
    def cycle(self):
        print("I am child 2")
        
c1=Child1()
c2=Child2()

c1.House()
c1.bike()

c2.House()
c2.cycle()
