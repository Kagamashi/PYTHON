'''
os: Provides functions for interacting with the operating system.
sys: Provides access to system-specific parameters and functions.
math: Provides mathematical functions like sqrt(), factorial(), sin(), etc.
random: Provides functions for generating random numbers and choosing random elements.
datetime: Provides functions for working with dates and times.
'''

import os
print(os.getcwd())  # Get current working directory
os.mkdir("new_folder")  # Create a new directory

import sys
print(sys.version)  # Output Python version
sys.exit()  # Exits the program

import math
print(math.sqrt(49))  # Output: 7.0
print(math.pi)  # Output: 3.141592653589793

import random
print(random.randint(1, 10))  # Output: Random number between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Output: Randomly chooses an item from the list

import datetime
now = datetime.datetime.now()
print(now)  # Output: Current date and time
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: Formatted date and time
