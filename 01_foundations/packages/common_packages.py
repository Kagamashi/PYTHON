## requests (HTTP requests handling)
# simplifies working with APIs and web scraping
import requests  # type: ignore

response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200
print(response.json())  # Parse JSON response



## pathlib (file and directory handling)
# provides an object-oriented approach to file paths
from pathlib import Path

file_path = Path("example.txt")

if file_path.exists():
    print("File exists!")
else:
    file_path.write_text("Hello, World!")  # Create and write text



## asyncio (asynchronous programming)
# handles non-blocking I/O, concurrent tasks, and coroutines
import asyncio

async def hello():
    await asyncio.sleep(1)
    print("Hello, Async World!")

asyncio.run(hello())  # Run the async function



## dataclasses (lightweight classes for data)
# reduces boilerplate code by automatically generating __init__, __repr__
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 30)
print(p)  # Output: Person(name='Alice', age=30)



## python-dotenv (manage environment variables)
# loads environment variables from a .env file
from dotenv import load_dotenv  # type: ignore
import os

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("API_KEY")
print(api_key)



## numpy (numerical computing)
# optimized for scientific computing, linear algebra, and statistics
import numpy as np  # type: ignore

arr = np.array([1, 2, 3, 4])
print(arr * 2)  # Output: [2 4 6 8]



## pandas (data manipulation & analysis)
# provides DataFrames and Series for structured data analysis
import pandas as pd  # type: ignore

df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [30, 25]})
print(df)
