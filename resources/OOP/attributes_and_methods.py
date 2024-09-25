'''
Attributes : variables that hold data about an object
  Instance attributes : belong to individual instances
  Class attributes : shared among all instances of a class

Methods : functions that define behavior for objects of the class '''

class Dog:
    species = "Canine"  # Class attribute
    
    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed  # Instance attribute
    
    def bark(self):  # Instance method
        return f"{self.name} is barking!"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())  # Output: Buddy is barking!
print(Dog.species)  # Output: Canine



''' Instance Variables & Methods 
Instance variables and methods belong to specific objects.
They are defined inside __init__ method or within other methods using self '''

class Car:
    def __init__(self, model, year):
        self.model = model  # Instance variable
        self.year = year  # Instance variable
    
    def display_info(self):  # Instance method
        return f"Car model: {self.model}, Year: {self.year}"

car1 = Car("Toyota", 2021)
print(car1.display_info())  # Output: Car model: Toyota, Year: 2021



''' Class Variables & Methods
Class variables are shared by all instances of a class.
Class methods are bound to class rather than instances.
Class methods are defined using @classmethod decorator '''

class Employee:
    company = "ABC Corp"  # Class variable

    def __init__(self, name, position):
        self.name = name  # Instance variable
        self.position = position  # Instance variable

    @classmethod
    def get_company(cls):  # Class method
        return cls.company

print(Employee.get_company())  # Output: ABC Corp



''' Static Methods
Static Methods do not depends on instance or class-specific data.
They are defined using @staticmethod decorator '''

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(5, 3))  # Output: 8
