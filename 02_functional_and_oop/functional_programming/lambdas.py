''' Lambda function is a small, anonymous function defined using lambda keyword.
It can have any number of rguments but only one expression, which is evaluated and returned.
Lambda functions are often used for short operations where defining a full function might be unnecessary.

lambda arguments: expression
'''

# Lambda function to add two numbers
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8

# Lambda function to square a number
square = lambda x: x ** 2
print(square(4))  # Output: 16


# Lambda functions are often used with functions like: map(), filter(), sorted()
# Using lambda with map to double numbers in a list
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8]
