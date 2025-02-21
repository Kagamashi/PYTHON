'''
Fetching URLs

downloading web content
'''

from urlib.request import urlopen

urlopen(url)    # open a URL
response.read() # read response data

with urlopen("https://www.example.com") as response:
    print(response.read().decode())
