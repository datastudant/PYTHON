#@staticmethod
#@classmethod
#polymorphism in object-oriented programming
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return f"name is {self.name} and age is {self.age} "
class Man(Person) :
    gender = 'Male'
    nb_of_men = 0

    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice
        Man.nb_of_men += 1
    def display(self):
        string = super().display()
        return string + f"and voice is {self.voice} and gender is {self.gender}"
man = Man("Rida", 30, "hard")
#print(man.display())
#print(Man.nb_of_men)
class Woman(Person) :
    gender = 'Famale'
    nb_of_woman = 0

    def __init__(self, name, age, hair):
        super().__init__(name, age)
        self.hair = hair
        Woman.nb_of_woman += 1
    def display(self):
        string = super().display()
        return string + f"and voice is {self.hair} and gender is {self.gender}"
woman = Woman("Najiya", 20, "black")
print(woman.display())
print(Woman.nb_of_woman)