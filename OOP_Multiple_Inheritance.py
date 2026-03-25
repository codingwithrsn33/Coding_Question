class Father:
    def Playing_cricket(self):
        print("Father Taught to play cricket")
        
class Mother:
    def Cooking(self):
        print("Mother Taught To Cooked  Delicious Food")

class Son(Father,Mother):
    def Gaming(self):
        print("Child itself Understand how to play game on phone")
        
c = Son()
c.Playing_cricket()
c.Cooking()
c.Gaming()
 
    
