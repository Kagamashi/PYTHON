# Python Installation & Environment Setup

## Installing Python

### **Official Installer** (Recommended)

Download and install Python from [python.org](https://www.python.org/).

### **Using Pyenv** (Best for Multiple Versions)

```bash
curl https://pyenv.run | bash
```

Add the following to `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
```

Install and set a Python version:

```bash
pyenv install 3.10.6
pyenv global 3.10.6
python --version  # Verify installation
```

### **System Install (apt, dnf, brew)**

- Available for all users.
- Might conflict with OS Python version.

### **User Install (pyenv, venv, conda)**

- Isolated environments that don’t break system Python.
- Requires manual setup.

---

## Best Python IDEs & Editors

| IDE/Editor           | Best For                                     |
| -------------------- | -------------------------------------------- |
| **VS Code**          | Lightweight, fast, highly customizable.      |
| **PyCharm**          | Full-featured IDE, great for large projects. |
| **Jupyter Notebook** | Best for data science & visualization.       |
| **Vim/Neovim**       | For terminal-based editing & power users.    |
| **Sublime Text**     | Fast, extensible with plugins.               |

Choose the one that fits your workflow and coding style!

