class GrandFather:
    def House(self):
        print("House is taken by GF")
class Father(GrandFather):  
    def Car(self):
        print("Car is given by Father")
        
class Son(Father):
    def bike(self):
        print("Bike is taken by Son")
        
c= Son()
c.House()
c.Car()
c.bike()
