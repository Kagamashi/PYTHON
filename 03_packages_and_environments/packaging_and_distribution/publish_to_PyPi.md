## **1. Publishing to PyPI (Python Package Index)**
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
