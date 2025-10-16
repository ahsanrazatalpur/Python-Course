
#QNo  1

# Parent class

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 

    def display_info(self):
        print(f"My Motor cycle brand is {self.brand}")
        print(f"My Motor cycle model is {self.model}")

show_vehile_Data = Vehicle("Honda", 2026)
show_vehile_Data.display_info()

# child class

class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
     super().__init__(brand, model)
     self.has_sidecar  =has_sidecar

    def display_info2(self):
       print(f"My motorCyle is {self.brand} and This is {self.model}, and It has {self.has_sidecar}")


motor = Motorcycle("Yamha", 2026, "Sidecar")
motor.display_info2()


    


# Qno 2
# parent 1
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age
# parent 2 
class Employee:
    def __init__(self, id, salary):
       self.id = id
       self.salary = salary
# child
class Developer(Person, Employee):
   def __init__(self, name, age, id, salary, isprogramer):
      self.isprogrammer = isprogramer
      Person.__init__ (self, name, age,)
      Employee.__init__ (self,  id, salary)
      

   def display_info2(self):
      print(f"Employee name is {self.name}")
      print(f"His Age is {self.age}")
      print(f"His id is {self.id}")
      print(f"His Salary is {self.salary}")
      print(f"He is {self.isprogrammer}")
    
show_emp_data = Developer("Ahsan", 20, "idnp09", 2000000, "Programmer")
show_emp_data.display_info2()



# Qno  3
class Animal:
   def __init__(self, animal):
      self.animal = animal

   def eat(self):
      print("Animals eat food to survive 🍃")


class Bird(Animal):
   def eat(self):
      # overriding the eat() method from Animal
      print(f"The {self.animal} eats worms 🪱")

   def fly(self):
      print(f"The {self.animal} can fly high in the sky 🕊️")


# Create object
bird = Bird("Parrot")
bird.eat()
bird.fly()


# QNo  4
class Swimmer:
    def swim(self):
        print("This animal can swim 🏊‍♂️")

class Walker:
    def walk(self):
        print("This animal can walk 🚶‍♂️")

# Amphibian inherits from both Swimmer and Walker
class Amphibian(Swimmer, Walker):
    def habitat(self):
        print("Amphibians can live both in water and on land 🌊🌍")

# Create object
frog = Amphibian()

# Now frog can do both
frog.swim()
frog.walk()
frog.habitat()

# Qno 5
class Person:
    def greet(self):
        print("Hello! I am a person 👋")

class Student(Person):
    def greet(self):
        # Use super() to call the parent's version of greet()
        super().greet()
        # Extend the method (add more functionality)
        print("I am also a student 🎓")

# Create object
s1 = Student()
s1.greet()


# Qno 6


import math

# Base Class
class Shape:
    def area(self):
        pass   # will be defined in subclasses


# Child Class 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Child Class 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Polymorphic function
def print_areas(shapes):
    for shape in shapes:
        print(f"Area: {shape.area():.2f}")


# Create a list of shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(10, 2)
]

# Call the polymorphic function
print_areas(shapes)
