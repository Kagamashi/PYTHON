'''
Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
It promotes code reuse.
'''

# Single Inheritance : one class inherits from one parent class
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # Dog class inherits from Animal
    def speak(self):
        return "Dog barks"

my_dog = Dog()
print(my_dog.speak())  # Output: Dog barks


# Multiple Inheritance : a class inherits from multiple parent classes
class Animal:
    def eat(self):
        return "Eating..."

class Mammal:
    def walk(self):
        return "Walking..."

class Dog(Animal, Mammal):  # Inherits from both Animal and Mammal
    pass

my_dog = Dog()
print(my_dog.eat())  # Output: Eating...
print(my_dog.walk())  # Output: Walking...
