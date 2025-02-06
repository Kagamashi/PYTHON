''' 
Variable scope defines accessibility of a variable in different parts of a program.
  Local variables: Defined inside a function and are only accessible within that function.
  Global variables: Defined outside any function and can be accessed anywhere in the program.
'''

# LOCAL VARIABLES
def greet():
    message = "Hello, World!"  # Local variable
    print(message)

greet()  # Output: Hello, World!
# print(message)  # Error: message is not defined (outside the function)


# GLOBAL VARIABLES
message = "Hello, World!"  # Global variable

def greet():
    print(message)  # Accessing the global variable inside the function

greet()  # Output: Hello, World!
print(message)  # Output: Hello, World!


# Modify GLOBAL variable inside a function using global keyword
x = 10  # Global variable

def modify():
    global x
    x = 20  # Modify the global variable
    print("Inside function:", x)

modify()  # Output: Inside function: 20
print("Outside function:", x)  # Output: Outside function: 20
