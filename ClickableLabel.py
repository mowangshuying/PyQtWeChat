from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSignal

class HeadImgLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()