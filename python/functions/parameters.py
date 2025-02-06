''' POSITIONAL parameters : arguments are matched to function parameters by position '''
def greet(name):
    print("Hello,", name)

greet("Alice")  # Output: Hello, Alice


''' DEFAULT parameters : used when we want to provide a default value for a parameter if user doesn't supply one
Syntax: def function_name(param=default_value) '''
def greet(name="Guest"):
    print("Hello,", name)

greet()  # Output: Hello, Guest
greet("Alice")  # Output: Hello, Alice


''' KEYWORD parameters : allow to pass arguments by specifying the parameter names explicitly, regardless of position '''
def describe_person(name, age):
    print(name, "is", age, "years old")

# Using keyword arguments
describe_person(age=30, name="Bob")  # Output: Bob is 30 years old


''' ARBITRARY parameters (Args & Kwargs) : if we don't know how many arguments a function will accept
*args: Collects extra positional arguments as a tuple.
**kwargs: Collects extra keyword arguments as a dictionary. '''
# Using *args to accept arbitrary positional arguments
def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(sum_numbers(1, 2, 3, 4))  # Output: 10

# Using **kwargs to accept arbitrary keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
