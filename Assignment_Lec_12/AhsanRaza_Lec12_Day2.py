# Qno 1️1

class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")

    @classmethod
    def show_total_employees(cls):
        print(f"Total Employees Created: {cls.total_employees}")


# Creating objects
emp1 = Employee("Ahsan", 50000)
emp2 = Employee("Raza", 70000)

emp1.display_details()
emp2.display_details()
Employee.show_total_employees()


# QNo 2

class Math:
    @staticmethod
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


# Testing
print(Math.is_prime(7))   # True
print(Math.is_prime(10))  # False


# Qno 3️

class Account:
    def __init__(self, balance):
        self._balance = balance  # private attribute

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative ❌")
        else:
            self._balance = amount
            print(f"Balance updated to: {self._balance}")



acc = Account(1000)
print(acc.balance)
acc.balance = 1500
acc.balance = -500



# Qno 4️⃣

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        print(f"📘 Title: {self.title}")
        print(f"✍️ Author: {self.author}")
        print(f"💰 Price: Rs.{self.price}\n")


# Creating multiple objects
book1 = Book("Python Basics", "Ahsan Raza", 900)
book2 = Book("AI for Beginners", "John Smith", 1200)
book3 = Book("Web Dev Pro", "Raza Khan", 1500)

book1.show_info()
book2.show_info()
book3.show_info()


