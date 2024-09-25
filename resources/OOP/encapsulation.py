''' Encapsulation restricts direct access to an objects attributes and methods.
Python uses the following conventions:
  Public: Attributes/methods accessible from anywhere.
  Protected: Prefixed with a single underscore _, accessible within the class and subclasses.
  Private: Prefixed with a double underscore __, not accessible outside the class.
'''

class Person:
    def __init__(self, name, age):
        self.name = name  # Public
        self._age = age  # Protected
        self.__salary = 5000  # Private

    def display_info(self):
        return f"Name: {self.name}, Age: {self._age}"

person = Person("Alice", 30)
print(person.name)  # Output: Alice
print(person._age)  # Output: 30
# print(person.__salary)  # Error: AttributeError
