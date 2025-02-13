'''
Error types:
- SyntaxError: invalid syntax
- IndentationError: incorrect indentation
- NameError: using variable that hasn't been defined
- TypeError: incorrent operation on incompatible data types
- IndexError: trying to access an index that is out of range
- ValueError: function receives an argument of the correct type but an invalid value
- KeyError: non-existent dictionary key
- AttributeError: undefined attribute of an object
- ImportError: importing a module that doesn't exists

Exception handling is used to manage and respond to runtime errors in Python
    try:       code to try (the code that may raise an exception).
    except:    runs if an exception occurs.
    else:      runs if no exception occurs.
    finally:   runs no matter what, useful for cleanup actions like closing files or releasing resources.
'''

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result is {result}")  # Runs if no exception occurs
finally:
    print("Execution completed.") # Runs always, even if there's an exception
