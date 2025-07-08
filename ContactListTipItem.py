from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from ContactListItem import *
from qfluentwidgets.components.widgets.label import *

class ContactListTipItem(ContactListItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setItemType(ContactListItemType.Tip)
        self.hMainLayout = QHBoxLayout()
        self.label = StrongBodyLabel()
        self.setFixedSize(250, 25)
        
    def setTip(self, str):
        self.label.setText(str)