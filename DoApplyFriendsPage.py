from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from PageTop import *
from VSplit import *

class DoApplyFriendsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
    
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)

        self.pageTop = PageTop(self)
        self.pageTop.setTitle("申请列表")
        self.vMainLayout.addWidget(self.pageTop)

        self.sp = VSplit()
        self.vMainLayout.addWidget(self.sp)

        self.list = QListWidget()
        self.vMainLayout.addWidget(self.list)
        
        