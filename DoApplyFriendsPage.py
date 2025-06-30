from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from PageTop import *

class DoApplyFriendsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        
        
        self.pageTop = PageTop(self)
        self.pageTop.setTitle("申请列表")
        
        