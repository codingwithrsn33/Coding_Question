class Student:
    def __init__(self):
        self.__marks = 0
        
    def set_marks(self,marks):
        self.__marks = marks
        
    def get_marks(self):
        return self.__marks
        
c = Student()
c.set_marks(90)
c.get_marks()
        
        
