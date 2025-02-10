''' Module is simply a .py file '''

import custom_module

print(custom_module.greet("Alice"))
print(custom_module.add(2, 3))


''' Package is a directory that contains multiple modules typically with __init__.py file. '''

# importing package and using it's functions in main
from custom_package import function1, function2

print(function1())
print(function2())
