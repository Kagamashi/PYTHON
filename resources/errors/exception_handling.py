'''
Exception handling is used to manage and respond to runtime errors in Python

try: The code to try (the code that may raise an exception).
except: The block that runs if an exception occurs.
else: The block that runs if no exception occurs.
finally: The block that runs no matter what, useful for cleanup actions like closing files or releasing resources.
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
    print("Execution completed.")  # Runs always, even if there's an exception
