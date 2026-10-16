# Python Abstraction – Practice Tasks 
# 5 beginner-friendly practice tasks covering abstract classes, abstract methods, concrete classes, concrete methods, ABC, and @abstractmethod. 

# basic Syntax

from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def show(self):
        pass

class Child(Parent):
    def show(self):
        print("Method implemented")

obj = Child()
obj.show()



# 1. Bank Payment System 
# Create an abstract class Bank with an abstract method pay(). 
# Create three concrete classes: UPI, CreditCard, and NetBanking. 
# Each class should implement pay() differently. 
# Expected output: 
# Payment using UPI 
# Payment using Credit Card 
# Payment using Net Banking 


from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Bank):
    def pay(self):
        print("Payment using UPI")


class CreditCard(Bank):
    def pay(self):
        print("Payment using Credit Card")


class NetBanking(Bank):
    def pay(self):
        print("Payment using Net Banking")


u = UPI()
c = CreditCard()
n = NetBanking()

u.pay()
c.pay()
n.pay()






# 2. Vehicle System 
# Create an abstract class Vehicle with an abstract method start(). 
# Create Car, Bike, and Bus classes. 
# Each class should provide its own implementation of start(). 
# Also add a concrete method stop() in the Vehicle class. 


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stopped")


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a key")


c = Car()
b = Bike()
bus = Bus()

c.start()
c.stop()

b.start()
b.stop()

bus.start()
bus.stop()







# 3. Employee Salary 
# Create an abstract class Employee with an abstract method calculate_salary(). Create FullTimeEmployee, PartTimeEmployee, and Intern classes. 
# Each class should calculate the salary differently. 
# Also create a concrete method display() that prints the employee name. 


from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def display(self):
        print("Employee Name:", self.name)


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_salary(self):
        return self.hourly_rate * self.hours


class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


e1 = FullTimeEmployee("Rahul", 40000)
e2 = PartTimeEmployee("Priya", 500, 40)
e3 = Intern("Kiran", 10000)

e1.display()
print("Salary:", e1.calculate_salary())

e2.display()
print("Salary:", e2.calculate_salary())

e3.display()
print("Salary:", e3.calculate_salary())



# 4. Shape Area 
# Create an abstract class Shape with an abstract method area(). 
# Create Circle, Rectangle, and Triangle classes. 
# Implement area() differently in each class. 
# Also add a concrete method display() in the Shape class. 


from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def display(self):
        print("Calculating shape area")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(7)
r = Rectangle(10, 5)
t = Triangle(8, 6)

c.display()
print("Circle area:", round(c.area(), 2))

r.display()
print("Rectangle area:", r.area())

t.display()
print("Triangle area:", t.area())



# 5. Online Food Ordering 
# Create an abstract class FoodOrder with an abstract method place_order(). 
# Create PizzaOrder, BurgerOrder, and BiryaniOrder classes. 
# Each class should implement place_order() differently. 
# Also create a concrete method order_status() in the parent class. 
# The concrete method should print: 
# Order is being processed
# Concepts to Practice 
# • abc – Python module used for Abstract Base Classes. 
# • ABC – base class used to create abstract classes. 
# • @abstractmethod – decorator used to declare an abstract method. 
# • Abstract Class – class used as a blueprint/base class. 
# • Abstract Method – method that child classes are required to implement. • Concrete Class – class that implements all required abstract methods and can create objects. • Concrete Method – normal method that already contains implementation.



from abc import ABC, abstractmethod

class FoodOrder(ABC):

    @abstractmethod
    def place_order(self):
        pass

    def order_status(self):
        print("Order is being processed")


class PizzaOrder(FoodOrder):
    def place_order(self):
        print("Pizza order placed")


class BurgerOrder(FoodOrder):
    def place_order(self):
        print("Burger order placed")


class BiryaniOrder(FoodOrder):
    def place_order(self):
        print("Biryani order placed")


p = PizzaOrder()
b = BurgerOrder()
br = BiryaniOrder()

p.place_order()
p.order_status()

b.place_order()
b.order_status()

br.place_order()
br.order_status()
