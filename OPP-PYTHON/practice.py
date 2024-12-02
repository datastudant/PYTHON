# video title : Python Object Oriented Programming
# link : https://youtu.be/A9kSngn7254?si=PU14UeTT8O1ziVQE



#x = 1
#print(type(x))
class Student :
    no_of_students = 0
    def __init__(self, name,  age=0, courses='none'):
        self.__name = name
        self.__age = age
        self.__courses = courses
        Student.no_of_students += 1
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name

    def describe(self):
        print(f"my name is {self.__name} and my age is {self.__age} ")
    def is_old(self, num) :
        if self.__age <= num :
            print("student is not  old")
        else :
            print("student is old")
student_1 = Student("rida",19, ['science'])
student_1.name = "zin abidin"
print(student_1.get_name())