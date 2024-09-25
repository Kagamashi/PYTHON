''' Assertions are used to verify that a condition is true during code execution
If the condition is false, AssertionError is raised
This is useful for debugging and ensuring certain conditions are met during development

Syntax: assert condition, "Error message"
'''

x = 10
assert x > 5, "x must be greater than 5"
assert x < 5, "x must be less than 5"  # This will raise an AssertionError

# Output: AssertionError: x must be less than 5
