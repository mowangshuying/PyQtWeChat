from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from MsgListItem import MsgListItem
from StyleSheetUtils import StyleSheetUtils
from qfluentwidgets import *

class MsgListFriendItem(MsgListItem):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setSpacing(0)
        self.setLayout(self.hMainLayout)
        
        self.headImgLabel = ImageLabel()
        self.setHeadImg(QPixmap("./_rc/img/head_2.jpg"))
        
        self.nameLabel = StrongBodyLabel()
        self.msgTextLabel = BodyLabel()
        
        self.hMainLayout.addWidget(self.headImgLabel)
        self.hMainLayout.addSpacing(15)
        
        self.vLayout = QVBoxLayout()
        self.vLayout.addWidget(self.nameLabel)
        self.vLayout.addWidget(self.msgTextLabel)
        
        self.hMainLayout.addLayout(self.vLayout)
        self.setFixedHeight(65)
        
        
    def setHeadImg(self, headimg: QPixmap):
        self.headImgLabel.setPixmap(headimg)
        self.headImgLabel.setScaledSize(QSize(40, 40))
        
    def setName(self, name: str):
        self.nameLabel.setText(name)
        
    def getName(self) -> str:
        return self.nameLabel.text()
    
    
    def getMsgText(self) -> str:
        return self.msgTextLabel.text()
    
    def setMsgText(self, text: str):
        return self.msgTextLabel.setText(text)