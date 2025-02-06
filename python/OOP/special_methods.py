''' Special methods (dunder methods) start and end with double underscores (__) 
These methods enable us to define how objects behave for built-in operations like addition, string representation etc.
  __init__(): Initializes the object (constructor).
  __str__(): Defines the string representation of the object.
  __repr__(): Provides an official string representation of the object.
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title}, {self.author})"

book = Book("1984", "George Orwell")
print(str(book))  # Output: 1984 by George Orwell
print(repr(book))  # Output: Book(1984, George Orwell)
