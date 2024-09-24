'''
is: Returns True if both variables are the same object.
is not: Returns True if both variables are not the same object.
'''

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Output: True (a and b point to the same list object)
print(a is not c)  # Output: True (a and c point to different objects, even though they contain the same values)
