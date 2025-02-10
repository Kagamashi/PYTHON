''' 
Functions in Python are defined using def keyword

- functions can return values, if a function doesn't specify return it returns None by default
- functions accept arguments (parameters)
    default: Syntax: def function_name(param=default_value)
    positional: greet(Alice)
    keyword: greet(name = "Alice")
    arbitrary:
        *args if we don't know how many arguments will be passed
        **kwargs if we don't know how many keyword arguments will be passed
- enforce positional arguments by adding ", /" after arguments: def function(x, /)
- enforce keyword-only arguments by adding "*," before arguments: def function(*, x)

built-in functions: https://docs.python.org/3/library/functions.html
'''

def my_function(x):
  return 5 * x

# any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


''' Recursion occurs when a function calls itself in order to solve smaller instances of the same problem.
A recursive function must have a base case to stop the recursion or else it will result in an infinite loop.

def recursive_function(parameters):
    if base_case_condition:
        return base_case_value
    else:
        return recursive_function(modified_parameters)

Common example of recursion is calculating factorial of a number.
n! = n * (n-1) * (n-2) * ... * 1
Base case: When n = 0, the factorial of 0 is 1 '''
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120


''' Fibonacci sequence is a classic recursive problem '''
def fibonacci(n):
    if n <= 1:  # Base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Recursive case

print(fibonacci(6))  # Output: 8
