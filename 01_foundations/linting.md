# Python Code Quality: Linting & Formatting

## a) Linting (Code Quality)
**Linting** checks for errors, code smells, and style issues.

| Tool    | Description |
|---------|------------|
| `pylint` | Most configurable and detailed linter. |
| `flake8` | Faster, less strict, widely used in CI/CD. |

### Install & Run Linters
```bash
pip install pylint flake8
pylint script.py
flake8 script.py
```

---

## b) Formatting (Code Style)
**Formatting** automatically corrects code style issues.

| Tool    | Description |
|---------|------------|
| `black` | Opinionated code formatter, widely used in Python projects. |
| `isort` | Sorts and organizes imports in a consistent order. |

### Install & Run Formatters
```bash
pip install black isort
black script.py
isort script.py
```

---

## c) Setting Up in VS Code
To enable automatic formatting and linting in **VS Code**:

1. **Install Extensions**:  
   - Install **Black** and **Pylint** from the VS Code marketplace.

2. **Enable Auto-Formatting**:  
   Open settings and set:
   ```json
   "editor.formatOnSave": true
   ```

3. **Set Default Formatter**:
   ```json
   "python.formatting.provider": "black",
   "editor.defaultFormatter": "ms-python.black-formatter"
   ```

Now, every time you save your Python file, VS Code will format it automatically!
