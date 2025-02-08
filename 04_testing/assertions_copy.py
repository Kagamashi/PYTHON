'''
Assertions are used in unit tests to check whether the actual output matches the expected output.
If assertion fails, the test fails.

assertEqual(a, b): Check if a is equal to b.
assertNotEqual(a, b): Check if a is not equal to b.
assertTrue(x): Check if x is True.
assertFalse(x): Check if x is False.
assertIs(a, b): Check if a is b (same object).
assertIsNone(x): Check if x is None.
assertIn(a, b): Check if a is in b (e.g., substring in string, item in list).
'''

import unittest
class TestAssertions(unittest.TestCase):

    def test_assertions(self):
        self.assertEqual(3 + 2, 5)  # Passes
        self.assertNotEqual(3 + 2, 6)  # Passes
        self.assertTrue(3 < 5)  # Passes
        self.assertFalse(3 > 5)  # Passes
        self.assertIsNone(None)  # Passes
        self.assertIn(3, [1, 2, 3, 4])  # Passes

if __name__ == "__main__":
    unittest.main()
