'''
Polymorphism allows the same method to behave differently based on the object calling it
'''

class Bird:
    def fly(self):
        return "Bird is flying"

class Airplane:
    def fly(self):
        return "Airplane is flying"

def perform_fly(entity):
    print(entity.fly())

bird = Bird()
airplane = Airplane()

perform_fly(bird)  # Output: Bird is flying
perform_fly(airplane)  # Output: Airplane is flying



''' Method Overriding
allows a subclass to provide a specific implementation of a method already defined in its superclass '''

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

my_dog = Dog()
print(my_dog.sound())  # Output: Bark
