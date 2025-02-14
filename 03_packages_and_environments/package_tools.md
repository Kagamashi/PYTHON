# **Creating Distributable Python Packages**
If you want to share your Python code with others, you need to **package it properly**. Python provides two main ways to package projects:
1. **Using `setuptools` with `setup.py`** (traditional method)
2. **Using `pyproject.toml`** (modern approach)

Once packaged, you can **distribute it as a source distribution (`.tar.gz`)** or **a wheel (`.whl`)** and publish it to **PyPI**.

---

## **1. Packaging with `setuptools` (Using `setup.py`)**
✔ Works with `setuptools`, a standard Python packaging library.  
✔ Uses a **`setup.py`** file to define package metadata.  
✔ Supports **`sdist` (source distribution) and `bdist_wheel` (binary wheel).**

### **Project Structure**
```
my_package/
├── my_package/
│   ├── __init__.py
│   ├── module.py
├── setup.py
├── README.md
├── LICENSE
├── requirements.txt
```

### **Writing `setup.py`**
```python
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
```

### **Building the Package**
```bash
pip install setuptools wheel
python setup.py sdist bdist_wheel
```
This generates:
- **Source Distribution (`sdist`)** → `dist/my_package-0.1.0.tar.gz`
- **Binary Wheel (`bdist_wheel`)** → `dist/my_package-0.1.0-py3-none-any.whl`

✅ **Use wheels (`.whl`) for faster installations.**  
✅ **Use `sdist` when source code needs to be available.**  

---

## **2. Packaging with `pyproject.toml` (Modern Approach)**
✔ **Preferred over `setup.py`** for modern package management.  
✔ Works with `setuptools`, `poetry`, or `flit`.

### **Project Structure**
```
my_package/
├── my_package/
│   ├── __init__.py
│   ├── module.py
├── pyproject.toml
├── README.md
├── LICENSE
```

### **Writing `pyproject.toml`**
```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
description = "A sample Python package"
readme = "README.md"
authors = [{ name = "Your Name", email = "your@email.com" }]
license = { text = "MIT" }
dependencies = ["requests>=2.25.0"]
requires-python = ">=3.6"

[tool.setuptools.packages.find]
where = ["."]
```

### **Building the Package**
```bash
pip install build
python -m build
```
This generates:
- **`dist/my_package-0.1.0.tar.gz`** (source distribution)
- **`dist/my_package-0.1.0-py3-none-any.whl`** (wheel)

✅ **More modern and standardized than `setup.py`.**  
✅ **Works with multiple build backends (`setuptools`, `poetry`, `flit`).**

---

## **3. Wheels (`.whl`) vs Source Distribution (`.tar.gz`)**
| **Format** | **Description** | **Pros** | **Cons** |
|-----------|---------------|---------|--------|
| **Wheel (`.whl`)** | Precompiled binary format | Faster installation | Not editable |
| **Source (`.tar.gz`)** | Full source code package | Editable by users | Slower installation |

**Best Practice**:  
- **Distribute both formats** to ensure compatibility.

---

## **4. Publishing to PyPI (Python Package Index)**
To upload your package to [PyPI](https://pypi.org/), follow these steps.

### **Step 1: Install `twine`**
```bash
pip install twine
```

### **Step 2: Upload to TestPyPI (For Testing)**
Test the upload process **before publishing to PyPI**:
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
- **Visit** [TestPyPI](https://test.pypi.org/) to see your package.

### **Step 3: Upload to PyPI**
```bash
twine upload dist/*
```
You will be prompted for your **PyPI username and password**.

### **Step 4: Install Your Package**
```bash
pip install my_package
```

---

## **5. Summary Table**
| **Method** | **Uses** | **Pros** | **Cons** |
|------------|--------|---------|--------|
| **`setup.py` + `setuptools`** | Traditional packaging | Works with `pip` and `setuptools` | Less modern |
| **`pyproject.toml`** | Modern packaging | Standardized, future-proof | Requires `build` |
| **Wheels (`.whl`)** | Faster installation | No compilation needed | Not editable |
| **Source (`.tar.gz`)** | Editable package | Full source code | Slower installation |

✅ **Use `pyproject.toml` for new projects.**  
✅ **Distribute both `.whl` and `.tar.gz` formats for compatibility.**  
✅ **Test packages on TestPyPI before uploading to PyPI.**

---

## **4. Publishing to PyPI (Python Package Index)**
To upload your package to [PyPI](https://pypi.org/), follow these steps.

### **Step 1: Install `twine`**
```bash
pip install twine
```

### **Step 2: Upload to TestPyPI (For Testing)**
Test the upload process **before publishing to PyPI**:
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
- **Visit** [TestPyPI](https://test.pypi.org/) to see your package.

### **Step 3: Upload to PyPI**
```bash
twine upload dist/*
```
You will be prompted for your **PyPI username and password**.

### **Step 4: Install Your Package**
```bash
pip install my_package
```
