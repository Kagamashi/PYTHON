''' Python allows to split code into different files (modules).
These modules can be imported and we can use their functions, classes, variables:
  import module_name: Imports the entire module.
  from module_name import specific_function_or_variable: Imports a specific function, class, or variable from a module.
  import module_name as alias: Imports the module with an alias
'''

# Importing the entire module
import math
print(math.sqrt(16))  # Output: 4.0

# Importing specific functions from a module
from math import sqrt, pi
print(sqrt(25))  # Output: 5.0
print(pi)  # Output: 3.141592653589793

# Importing with an alias
import math as m
print(m.factorial(5))  # Output: 120
