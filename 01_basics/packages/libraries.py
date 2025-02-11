''' pip tool allows installing external libraries from Python Package Index (PyPi).
These libraries can be used to extend Python functionality

pip install package_name
pip uninstall package_name
'''

# Installing the requests library for HTTP requests
# pip install requests

# Using the requests library
import requests # type: ignore
response = requests.get('https://api.github.com')
print(response.status_code)  # HTTP status code (e.g., 200)
