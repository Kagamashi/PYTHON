# **Python Virtual Environments & Dependency Management**

Python provides **multiple tools** to manage dependencies and package environments, ensuring **project isolation** and **consistent dependency management**.

---

## **1. Virtual Environment Tools**
| **Tool** | **Best For** | **Manages Virtual Env?** | **Dependency Management?** |
|---------|-------------|----------------|----------------|
| `venv` | Standard, built-in solution | ✅ Yes | ❌ No (Uses `pip` manually) |
| `pipenv` | Replaces `venv` + `requirements.txt` | ✅ Yes | ✅ Yes (Uses `Pipfile`) |
| `poetry` | Modern dependency management | ✅ Yes | ✅ Yes (`pyproject.toml`) |
| `conda` | Data science, system packages | ✅ Yes | ✅ Yes (`environment.yml`) |

---

## **2. Built-in `venv` (Virtual Environments)**
✔ **Creates an isolated Python environment** (no external dependencies).  
✔ **Manages dependencies manually via `pip`**.

### **Creating a Virtual Environment**
```bash
python -m venv myenv
```

### **Activating the Environment**
- **Windows**:
  ```bash
  myenv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source myenv/bin/activate
  ```

### **Installing Dependencies**
```bash
pip install requests
pip freeze > requirements.txt  # Save dependencies
```

### **Deactivating the Virtual Environment**
```bash
deactivate
```

✅ **Best for simple projects**, but dependency management is manual.

---

## **3. `pipenv` (Pip + Virtualenv)**
✔ **Automatically manages a virtual environment**.  
✔ **Tracks dependencies using `Pipfile` instead of `requirements.txt`**.  
✔ **Supports dependency locking (`Pipfile.lock`) for reproducibility**.

### **Installing `pipenv`**
```bash
pip install pipenv
```

### **Creating a Virtual Environment**
```bash
pipenv install
```

### **Installing Packages**
```bash
pipenv install requests
pipenv install pytest --dev  # Dev dependencies
```

### **Activating the Environment**
```bash
pipenv shell
```

✅ **Best for web development** but less popular than `poetry`.

---

## **4. `poetry` (Modern Dependency Management)**
✔ **Manages virtual environments and dependencies**.  
✔ **Uses `pyproject.toml` instead of `requirements.txt`**.  
✔ **Better dependency resolution** than `pip` or `pipenv`.

### **Installing `poetry`**
```bash
pip install poetry
```

### **Creating a New Project**
```bash
poetry new my_project
cd my_project
```

### **Adding Dependencies**
```bash
poetry add requests
poetry add pytest --dev  # Dev dependencies
```

### **Installing Dependencies**
```bash
poetry install
```

✅ **Best for modern Python projects** (faster, more reliable).

---

## **5. `conda` (For Data Science & System Packages)**
✔ **Manages both Python and system dependencies**.  
✔ **Used in `Anaconda` and `Miniconda` distributions**.  
✔ **Tracks dependencies using `environment.yml`**.

### **Installing a Package**
```bash
conda install numpy
```

### **Creating an Environment**
```bash
conda create --name myenv python=3.9
```

### **Activating the Environment**
```bash
conda activate myenv
```

✅ **Best for data science and scientific computing**.
