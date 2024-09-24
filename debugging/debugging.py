'''
Inserting print() statements is a simple and effective way to debug the code
We can add print() statements at key points in the code to understand where things might be going wrong
'''

def divide(a, b):
    print(f"Dividing {a} by {b}")  # Debugging info
    return a / b

result = divide(10, 2)
print(f"Result: {result}")

# Debugging output:
# Dividing 10 by 2
# Result: 5.0
