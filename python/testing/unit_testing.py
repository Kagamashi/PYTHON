'''
Unit testing is a way to test individual units of code (functions,methods) to ensure they work as expected.
  unittest: Built-in Python module for testing.
  pytest: A more advanced and flexible testing framework that provides additional features
'''

''' unittest module is Python built-in testing framework
test cases are written as classes that inherit from unittest.TestCase 
individual tests are defined as methods whose names begin with test_
  setUp(): Optional method that runs before each test.
  tearDown(): Optional method that runs after each test.
  assert methods to check test results
'''
import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

if __name__ == '__main__':
    unittest.main()
# run with: python test_file.py


''' pytest is another popular testing framework that simplifies test writing and offers more functionality compared to unittest
  Functions for test cases are written with the prefix test_.
  You don’t need to create a class, making it more concise.
'''
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_add_negative():
    assert add(-2, -3) == -5
# run with: python test_file.py
