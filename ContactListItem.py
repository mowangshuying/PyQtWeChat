from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from StyleSheetUtils import StyleSheetUtils
from qfluentwidgets import *

class ContactListItem(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setSpacing(0)
        self.setLayout(self.hMainLayout)
        
        
        self.headImgLabel = ImageLabel()
        self.headImgLabel.setFixedSize(40, 40)
        self.headImgLabel.setImage("./_rc/img/head_2.jpg")
        
        self.nameLabel = StrongBodyLabel()
        self.hMainLayout.addWidget(self.headImgLabel)
        self.hMainLayout.addSpacing(15)
        self.hMainLayout.addWidget(self.nameLabel)
        self.setFixedHeight(65)
        
        # StyleSheetUtils.setQssByFileName("", self)
        
        
    def setHeadImg(self, headimg: QPixmap):
        self.headImgLabel.setPixmap(headimg)
        
    def setName(self, name: str):
        self.nameLabel.setText(name)