## **6. Requirements Files (`requirements.txt`, `environment.yml`)**
| **File** | **Used By** | **Purpose** |
|---------|------------|------------|
| `requirements.txt` | `pip`, `venv`, `pipenv` | Lists package dependencies |
| `Pipfile` | `pipenv` | Tracks dependencies & Python version |
| `pyproject.toml` | `poetry` | Manages dependencies & build system |
| `environment.yml` | `conda` | Manages Conda environments |

### **Example: `requirements.txt` (for `pip`)**
```txt
requests==2.28.0
numpy>=1.21
```
Install dependencies:
```bash
pip install -r requirements.txt
```

### **Example: `environment.yml` (for `conda`)**
```yaml
name: myenv
dependencies:
  - python=3.9
  - numpy
  - pandas
```
Create environment:
```bash
conda env create -f environment.yml
```
