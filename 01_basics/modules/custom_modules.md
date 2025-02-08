'''
We can create our own custom modules by writing Python code in separate files and importing them into other scripts.
A module is simply a .py file
Package is a directory that contains multiple modules typically with __init__.py file.
'''

### ''' CUSTOM MODULE '''
# my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# main.py
import my_module

print(my_module.greet("Alice"))  # Output: Hello, Alice!
print(my_module.add(2, 3))  # Output: 5


### ''' CUSTOM PACKAGE '''
my_package/
├── __init__.py
├── module1.py
└── module2.py

# module1.py
def function1():
    return "Function 1 in module 1"

# module2.py
def function2():
    return "Function 2 in module 2"

# __init__.py
from .module1 import function1
from .module2 import function2

# importing package and using it's functions in main
# main.py
from my_package import function1, function2

print(function1())  # Output: Function 1 in module 1
print(function2())  # Output: Function 2 in module 2
