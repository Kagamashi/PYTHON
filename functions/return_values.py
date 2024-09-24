''' Functions can optionally return a value using return statement.
If no return statement is used, the function will return None by default.

def function_name(parameters):
    # Some operations
    return value
'''

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8


# If function doesn't explicitly return a value it returns None by default
def no_return():
    pass

result = no_return()
print(result)  # Output: None
