'''
for loop is used to iterate over a sequence (list, tuple, string) or any other literable object
it allows to execute a block of code for each item in the sequence
'''

# Iterate over a list
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)

# Iterate over a string
for char in "Python":
    print(char)

# Output:
# 1
# 2
# 3
# 4
# P
# y
# t
# h
# o
# n

''' break: Terminates the loop and moves the control outside the loop '''
for i in range(10):
    if i == 5:
        break  # Loop stops when i equals 5
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


''' continue: Skips the current iteration and moves to the next iteration '''
for i in range(5):
    if i == 3:
        continue  # Skips the rest of the loop when i equals 3
    print(i)

# Output:
# 0
# 1
# 2
# 4


''' pass: Does nothing; it’s a placeholder for code that will be written later '''
for i in range(5):
    if i == 3:
        pass  # Does nothing here, just a placeholder
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
