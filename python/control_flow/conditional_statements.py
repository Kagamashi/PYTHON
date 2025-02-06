'''
if: Executes a block of code if the condition is True.
elif: Stands for "else if," and it checks another condition if the first one is False.
else: Executes a block of code if all previous conditions are False.
'''

x = 10

if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")

# Output: x is greater than 5 but less than or equal to 15
