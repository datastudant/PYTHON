"""
name = input("enter your name : ")
status = False
x = 0
while name == "" and x <= 2 :
  if x == 2 :
    print("you enter three time  false name,  run program anthor one!")
    status = True
    break
  else:
    status = False
  print(" pleasse enter your corecte name")
  name = input("taype her : ")
  x += 1
  
if status == True:
   pass  # skip code here
elif status == False :
  print("your name has ben uploaded sucsefl")
  """
"""
name = input("Enter your name: ")
attempts = 0
max_attempts = 3

while name == "" and attempts < max_attempts:
    if attempts == max_attempts - 1:
        print("You entered an empty name three times. Please run the program again!")
        break
    else:
        print("Please enter your correct name.")
        name = input("Type here: ")
        attempts += 1

if name != "":
    print("Your name has been uploaded successfully!")"""
"""
def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child2 = "Emil", child1 = "Tobias", child3 = "Linus")
"""
"""class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)"""
"""class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
print(p1)"""
"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"السلام، سميتي {self.name} وعندي {self.age} عام."
person1 = Person("أحمد", 25)
print(person1.name)  # يطبع "أحمد"
print(person1.age)   # يطبع 25"""
print("hello world")





