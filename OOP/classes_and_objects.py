'''
Class is a blueprint for creating objects (instances).
Object is an instance of a clas and represents a real-world entity.
Classes encapsulate data (attributes) and behavior (methods)

Defining Classes: Use the class keyword to define a class.
Creating Objects: Instantiate a class by calling it like a function.
'''

# Defining a class
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable

# Creating an object (instance)
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)  # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
