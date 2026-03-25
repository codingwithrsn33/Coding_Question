class Dog:
    def Sound(self):
        print("Bewo ,Bewo")
        
class Cat(Dog):
    def Sound(self):
        print("Meow,Mewo")
        
c= Cat()
c.Sound()
