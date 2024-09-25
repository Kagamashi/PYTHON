'''
raise keyword is used to explicitly raise an exception
Can be used to raise built-in or custom exceptions
Trigger an error in specific circumstances
'''

def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    else:
        print("Age is valid.")

try:
    check_age(16)
except ValueError as e:
    print(e)  # Output: Age must be at least 18
