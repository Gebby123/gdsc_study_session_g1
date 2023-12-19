
#exercise 1
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"
my_dog= dog('Buddy',3)
print(my_dog)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return  self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
my_area= Rectangle(3,4)
my_perimeter= Rectangle(5,6)

area = my_area.get_area()

perimeter = my_perimeter.get_perimeter()
print(area)
print(perimeter)
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# # Creating an instance of the Dog class
# my_dog = Dog()

# # Inheriting and using methods from the parent class
# my_dog.speak()  # Output: Animal speaks

# # Adding specific functionality in the child class
# my_dog.bark()   # Output: Dog barks


#exercise 2
class Shape:
    def __init__(self, color):
        self.color = color

    def getcolor(self):
        return self.color



class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    def area(self):
        return 3.14 * self._radius**2


# Creating objects and printing their color and area
rectangle = Rectangle("Blue", 4, 5)
print("Rectangle color:", rectangle.getcolor())
print("Rectangle area:", rectangle.area())

circle = Circle("Red", 3)
print("Circle color:", circle.getcolor())
print("Circle area:", circle.area())

#exercise 3
# question 1 answer
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)


# Creating a Car object and displaying its information
my_car = Car("Suzuki", "dizzier", 2022)
my_car.display_info()

# question 2 answer
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print("Battery Capacity:", self.battery_capacity)


# Creating an ElectricCar object and displaying its information
my_electric_car = ElectricCar("Tesla", "Model S", 2023, "100 kWh")
my_electric_car.display_info()


#question 3 answer
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal of {amount} successful.")

        else:
            print("Insufficient funds.")

    def display_balance(self):
        print("Balance:", self._balance)


# Creating a BankAccount object and testing its methods
my_account = BankAccount()
my_account.deposit(1000)
my_account.display_balance()
my_account.withdraw(500)
my_account.display_balance()


# question 4 answer
import math

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return (self.base * self.height) / 2


# Creating shape objects and calculating their areas
circle = Circle(5)
print("Circle area:", circle.calculate_area())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.calculate_area())

triangle = Triangle(3, 7)
print("Triangle area:", triangle.calculate_area())

#question 5 answer
import unittest

class BankAccountTests(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount()
        account.deposit(500)
        self.assertEqual(account._balance, 500)

    def test_withdraw_sufficient_funds(self):
        account = BankAccount(1000)
        account.withdraw(500)
        self.assertEqual(account._balance, 500)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount(100)
        account.withdraw(500)
        self.assertEqual(account._balance, 100)

    def test_display_balance(self):
        account = BankAccount(2000)
        self.assertEqual(account.display_balance(), "Balance: 2000")

if __name__ == '__main__':
    unittest.main()