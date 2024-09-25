'''
Python uses indentation (spaces or tabs) to define structure of the code, there are no braces or parentheses to mark blocks.
Indentation must be consistent - can't mix tabs and spaces
By convention 4 spacer per indentation level is recommended
'''

# Correct indentation
if x > 5:
    print("x is greater than 5")
    if y > 3:
        print("y is greater than 3")

# Incorrect indentation (results in an error)
if x > 5:
print("x is greater than 5")  # No indentation here
