'''
Mocking is a technique used in unit testing to replace parts of our system under test with mock objects.
This is useful when we want to simulate behavior without invoking actual external systems (like databases, APIs)

unittest.mock module provided a way to mock objects '''

''' mocking a function inside a module '''
import unittest
from unittest import TestCase
from unittest.mock import patch

# Function to test
def get_data_from_api():
    return "Original data from API"

class TestMocking(TestCase):

    @patch('__main__.get_data_from_api')  # Mocking the function
    def test_get_data_from_api(self, mock_get):
        mock_get.return_value = "Mocked data from API"  # Simulating API response

        result = get_data_from_api()
        self.assertEqual(result, "Mocked data from API")

if __name__ == "__main__":
    unittest.main()


''' mocking an objects method '''
class Service:
    def fetch_data(self):
        # Simulate a call to an external service
        return "Real data from service"

class TestService(TestCase):

    @patch.object(Service, 'fetch_data')  # Mocking the method in Service
    def test_fetch_data(self, mock_fetch):
        mock_fetch.return_value = "Mocked data"
        service = Service()
        self.assertEqual(service.fetch_data(), "Mocked data")

if __name__ == "__main__":
    unittest.main()
