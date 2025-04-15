"""class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def introduce(self):
        print("Hi I'am " + self.firstName + " " + self.lastName)
    
class Student(Person):
    pass

pOne = Person("Jaireell", "Son")
pOne.introduce()

sOne = Student("Kaizer", "Nakamoto")
sOne.introduce()"""

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def introduce(self):
        print("Hi I'am " + self.firstName + " " + self.lastName)

class Student(Person):
    def __init__(self, firstName, lastName, sectionYear):
        super().__init__(firstName, lastName)
        self.section = sectionYear

    def introduce(self):
        print("Hi I'am " + self.firstName + " " + self.lastName + " FROM " + self.section)
        
pOne = Person("Jaireell", "Son")
sOne = Student("Kaizer", "Nakamoto", "BSIT-2A")
pOne.introduce()

sOne.introduce()
