

#Qno  1

class Book:
    Title = "How to do programming"
    Author = "London Jaffery"

    def __init__(self, Title = 'title', Author = 'author'):
     self.Title = Title
     self.Author = Author

    def display_info(self):
     print(f"Title is : {self.Title}")
     print(f"Author is : {self.Author}")

show_book = Book("Sigma Rules", "Chadtag")
show_book . display_info()




# Qno  2

class Circle:
  raduis = 2.0
  
  def __init__(self, raduis = 0.0):
    self.raduis = raduis
  
  def area(self):
    area_of_circle = 3.142 * self.raduis * self.raduis
    print("The area of Circle is :", area_of_circle)
    return area_of_circle

  def circumference(self):
    circumference = 2 * 3.142 * self.raduis
    print("The Circumference of an area is :", circumference)
    return circumference

  def display_info(self):
    area_val = self.area()
    circ_val = self.circumference()
    print(f"The area of circle is {area_val}")
    print(f"The circumference is : {circ_val}")

circle = Circle(5.0)
circle.display_info()



# Qno 3

class Employee:
   name = "Ahsan Raza"
   salary = 200000

   def __init__(self, name="employee", salary=500000):
       self.name = name
       self.salary = salary

   def salary_increase(self, percentage):
       self.salary = self.salary + (self.salary * percentage / 100)
       print("Your salary after increment:", self.salary)
       return self.salary

   def display_info(self):
       print(f"Your new Salary is : {self.salary}")



emp = Employee("Ahsan Raza", 200000)
emp.salary_increase(10)  # Increase by 10%
emp.display_info()


# Qno 4

# Qno 4

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b


# Create object and use it
calc = Calculator()
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))


# Qno 5

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 50:
            print(f"{self.name} has passed with {self.marks} marks.")
        else:
            print(f"{self.name} has failed with {self.marks} marks.")


# Create object and test
student1 = Student("Ahsan Raza", 78)
student2 = Student("Ali", 45)

student1.check_result()
student2.check_result()
