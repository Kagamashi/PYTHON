## **1. Generating Coverage Reports**

✅ **Measure how much of your code is covered by tests.**

### **1.1 Installing Coverage.py**
```bash
pip install coverage
```

### **1.2 Running Tests with Coverage**
```bash
coverage run -m pytest
```

### **1.3 Generating a Coverage Report**
```bash
coverage report -m
```
✅ Shows covered and missed lines in your code.

### **1.4 Generating an HTML Coverage Report**
```bash
coverage html
```
✅ Opens `htmlcov/index.html` to visualize coverage.

---

## **2. Enforcing Coverage Thresholds**

✅ **Ensure that a minimum percentage of code is covered by tests.**

### **2.1 Setting a Minimum Coverage Requirement**
```bash
coverage run -m pytest
coverage report --fail-under=80
```
✅ Fails the test suite if coverage is below 80%.
