# PyQt
# PyQt is a set of Python bindings for the Qt application framework, used for building cross-platform desktop apps.
from PyQt5.QtWidgets import QApplication, QLabel  # type: ignore
app = QApplication([])
label = QLabel('Hello, PyQt!')
label.show()
app.exec_()
