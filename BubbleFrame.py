from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from Def import *

class BubbleFrame(QFrame):
    def __init__(self, role:ChatRole, parent=None):
        super().__init__(parent)
