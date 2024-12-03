# video title : Python Object Oriented Programming
# link : https://youtu.be/A9kSngn7254?si=PU14UeTT8O1ziVQE

#encapsulation in object-oriented programming

#x = 1
#print(type(x))
from datetime import date
class Student :
    no_of_students = 0
    def __init__(self, name,  age=0, courses='none'):
        self.name = name
        self.age = age
        self.courses = courses
        Student.no_of_students += 1
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def describe(self):
        print(f"my name is {self.name} and my age is {self.age} ")
    def is_old(self, num) :
        if self.age <= num :
            print("student is not  old")
        else :
            print("student is old")
    @classmethod
    def initFromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
student_1 = Student("rida",19, ['science'])
student_2 = Student.initFromBirthYear("naima", 2005)
#Student.describe()

#rint(stud#ent_1, student_2)
class Pizza:
    def __ini__(self, ingredients):
        self.ingredients = ingredients
    @classmethod
    def veg(cls):
        return cls(['musharooms', 'olives', 'onions'])
    @classmethod
    def margherita(cls):
        return cls(['mozarella', 'sauce'])
#pizza1 = Pizza(['tomatoes', "olives"])
pizza2 = Pizza.veg()
pizza3 = Pizza.margherita()
print(pizza2,pizza3)