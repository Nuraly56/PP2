class Student(Person):

class Person:
    def _init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)

class Student(Person):
    pass

x = Student("Mike")
x.printname()