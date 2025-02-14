# **Managing Dependencies in Python: pip, Poetry, and Pipenv**

Python provides different tools for **installing, managing, and locking dependencies**.
✅ `pip` is the standard package manager.  
✅ `Poetry` & `Pipenv` provide **better dependency management** and **virtual environments**.

---

# **1. pip (Python Package Manager)**

`pip` is the most commonly used tool for installing and managing Python libraries from **PyPI**.

### **1.1 Installing a Package**

```bash
pip install requests
```

✅ Installs the **latest version** of `requests`.

---

### **1.2 Installing a Specific Version**

```bash
pip install requests==2.28.0
```

✅ Useful when **project dependencies require a specific version**.

---

### **1.3 Uninstalling a Package**

```bash
pip uninstall requests
```

---

### **1.4 Listing Installed Packages**

```bash
pip list
```

---

### **1.5 Checking for Package Updates**

```bash
pip list --outdated
```

---

### **1.6 Saving Installed Packages (`requirements.txt`)**

```bash
pip freeze > requirements.txt
```

✅ Saves **all installed dependencies** into `requirements.txt`.

---

### **1.7 Installing from `requirements.txt`**

```bash
pip install -r requirements.txt
```

✅ Recreates the **exact environment** from the saved dependencies.

---

# **2. Poetry: Modern Dependency Management**

✅ **Handles dependencies, virtual environments, and packaging.**  
✅ **Uses `pyproject.toml` instead of `requirements.txt`.**  
✅ **Faster and more reliable than `pip` and `pipenv`.**

---

### **2.1 Installing Poetry**

```bash
pip install poetry
```

---

### **2.2 Creating a New Project**

```bash
poetry new my_project
cd my_project
```

✅ Creates a **new package structure**.

---

### **2.3 Adding Dependencies**

```bash
poetry add requests
```

✅ **Updates `pyproject.toml` and `poetry.lock`.**

---

### **2.4 Installing Dependencies**

```bash
poetry install
```

✅ Installs dependencies from `pyproject.toml` and `poetry.lock`.

---

### **2.5 Using a Virtual Environment**

```bash
poetry shell
```

✅ Activates Poetry’s **built-in virtual environment**.

---

### **2.6 Locking Dependencies**

```bash
poetry lock
```

✅ Generates `poetry.lock` to **ensure reproducibility**.

---

# **3. Pipenv: Combining pip and venv**

✅ **Replaces `pip` and `venv` with a single tool.**  
✅ **Tracks dependencies using `Pipfile` and `Pipfile.lock`.**

---

### **3.1 Installing Pipenv**

```bash
pip install pipenv
```

---

### **3.2 Creating a Virtual Environment**

```bash
pipenv install
```

✅ Automatically **creates a virtual environment**.

---

### **3.3 Installing Dependencies**

```bash
pipenv install requests
pipenv install pytest --dev  # Dev dependencies
```

✅ Updates `Pipfile` and `Pipfile.lock`.

---

### **3.4 Activating the Environment**

```bash
pipenv shell
```

✅ Starts the Pipenv-managed environment.

---

### **3.5 Reproducing a Locked Environment**

```bash
pipenv install --ignore-pipfile
```

✅ Installs dependencies **only from `Pipfile.lock`**.

---

# **4. Comparison: pip vs Poetry vs Pipenv**

| Feature                          | `pip` + `venv`                  | `poetry`                      | `pipenv`               |
| -------------------------------- | ------------------------------- | ----------------------------- | ---------------------- |
| **Manages dependencies**         | ✅ Yes (with `requirements.txt`) | ✅ Yes (with `pyproject.toml`) | ✅ Yes (with `Pipfile`) |
| **Handles virtual environments** | ❌ No (must use `venv`)          | ✅ Yes (built-in)              | ✅ Yes (built-in)       |
| **Dependency resolution**        | Basic                           | ✅ Best                        | ✅ Good                 |
| **Lock files**                   | `requirements.txt`              | `poetry.lock`                 | `Pipfile.lock`         |
| **Speed**                        | Fast                            | ✅ Faster                     | Slower                 |

---

# **5. When to Use What?**

| **Use Case**                          | **Recommended Tool** |
| ------------------------------------- | -------------------- |
| **Simple projects**                   | `pip` + `venv`       |
| **Modern package management**         | `poetry`             |
| **Replacing `pip` + `venv` with Pipfile** | `pipenv`             |

✅ **Best Practice**: Use `poetry` for new projects and `pip` for quick installs.
