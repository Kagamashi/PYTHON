
Installing via Official installer
python.org.

Installing via pyenv (recommended for multiple versions)
curl https://pyenv.run | bash

# add to /.bashrc, /.zshrc
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"

pyenv install 3.10.6  # Install Python 3.10.6
pyenv global 3.10.6   # Set as global version
python --version      # Verify installation




System Install: apt, dnf, brew
- avaialble for all users
- might conflict with OS Python


User install (pyenv, venv, conda)
- isolated doesnt break system Python
- needs manual setup



IDEs:
- VSCode - lightweight, fast, customizable
- PyCharm - best for large projects, full featured IDE
- Jupyer Notebook - data science
- Vim/Neovim
- Sublime Text - fast, extensive via plugins