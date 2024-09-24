# Tkinter
# Tkinter is a built-in Python library for creating graphical user interfaces (GUIs).
import tkinter as tk  # type: ignore
root = tk.Tk()
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
root.mainloop()
