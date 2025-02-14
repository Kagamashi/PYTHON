'''
Unit testing is a way to test individual units of code (functions,methods) to ensure they work as expected.

unittest module is Python built-in testing framework
test cases are written as classes that inherit from unittest.TestCase 
individual tests are defined as methods whose names begin with test_
    setUp(): Optional method that runs before each test.
    tearDown(): Optional method that runs after each test.
    assert methods to check test results

run all tests               python -m unittest discover
run specific test file      python -m unittest test_file.py
run specific test case      python -m unittest test_file.TestClass.test_method
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
