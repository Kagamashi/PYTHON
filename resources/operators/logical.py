'''
and: Returns True if both operands are true.
or: Returns True if at least one operand is true.
not: Returns True if the operand is false (reverses the result).
'''

a = 10
b = 5
c = 15

print(a > b and a < c)  # Output: True (Both conditions are true)
print(a > b or a > c)  # Output: True (One condition is true)
print(not a > b)  # Output: False (a > b is true, but not makes it false)
