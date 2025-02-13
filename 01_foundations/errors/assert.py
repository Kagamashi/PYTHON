'''
assert checks if a condition is True, otherwise it raises an AssertionError
'''

# assert
x = -5
assert x > 0, "x must be positive!"  # AssertionError


# Custom exceptions can be defined by inheriting from Exception
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"Caught error: {e}")
