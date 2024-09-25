''' Decorators are a way to modify the behavior of functions or classes.
They are high-order functions that take another function or class as input, extend or modify its behavior and return the modified function or class.
  Function Decorators: Used to modify functions.
  Class Decorators: Used to modify classes
'''

''' Function decorator applied using @decorator_name syntax '''
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Before the function call
# Hello!
# After the function call


''' Classs Decorator '''
def class_decorator(cls):
    cls.decorated = True
    return cls

@class_decorator
class MyClass:
    pass

print(MyClass.decorated)  # Output: True
