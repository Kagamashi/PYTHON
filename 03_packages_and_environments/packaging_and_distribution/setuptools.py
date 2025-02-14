'''
setuptools
- works with setuptools, standard Python packaging library
- uses setup.py file to define package metadata
- supports sdist (source distribution) and bdist_wheel (binary wheel)

my_package/
├── my_package/
│   ├── __init__.py
│   ├── module.py
├── setup.py
├── README.md
├── LICENSE
├── requirements.txt

build the package:
  pip install setuptools wheel
  python setup.py sdist bdist_wheel

this generates:
  Source Distribution (sdist) → dist/my_package-0.1.0.tar.gz
  Binary Wheel (bdist_wheel) → dist/my_package-0.1.0-py3-none-any.whl
'''

# setup.py
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),  # Automatically finds subpackages
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Your Name",
    author_email="your@email.com",
    description="A sample Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
