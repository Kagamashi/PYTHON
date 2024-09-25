'''
APIs (Application Programming Interfaces) allow to interact with external services and get or send data.
request library
'''

# GET request
import requests # type: ignore

response = requests.get('https://api.github.com')
print(response.status_code)  # Output: 200 (success)
print(response.json())  # Print the JSON data returned by the API

# POST request
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.json())  # Print the response JSON

# When working with APIs you often get JSON responses which can be parsed using json() method
response = requests.get('https://api.github.com')
data = response.json()
print(data['current_user_url'])  # Example of extracting data
