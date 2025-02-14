'''
Python scripts should work on Windows, macOS, Linux
'''

import os
from pathlib import Path

# old way
file_path = os.path.join("folder", "file.txt")

# modern, cross-platform way
file_path = Path("folder") / "file.txt"


# cross-platform environment variables
if os.name == "nt":  # Windows
    os.system("cls")
else:  # macOS/Linux
    os.system("clear")


# subprocess for Shell Commands (avoid os.system)
import subprocess

subprocess.run(["ls", "-l"])  # Works on macOS/Linux
subprocess.run(["dir"], shell=True)  # Windows alternative
