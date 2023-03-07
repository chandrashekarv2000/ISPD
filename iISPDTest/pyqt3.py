'''
creating Icons for window
'''
from PyQt6.QtWidgets import QApplication,QWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry()

app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec())