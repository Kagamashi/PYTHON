'''
raise keyword is used to explicitly raise an exceptipon (custom or built-in)
'''

# raise
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return "Valid age"

try:
    check_age(16)
except ValueError as e:
    print(f"Error: {e}")
