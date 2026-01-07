from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from qfluentwidgets import *

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
        self.timeLabel = CaptionLabel()
        self.msgTextLabel = CaptionLabel()
        
        self.hMainLayout.addWidget(self.headImgLabel)
        self.hMainLayout.addSpacing(15)
        
        self.vLayout = QVBoxLayout()
        # self.vLayout.addWidget(self.nameLabel)
        # self.vLayout.addWidget(self.msgTextLabel)
        
        self.hNTLayout = QHBoxLayout()
        self.hNTLayout.addWidget(self.nameLabel)
        self.hNTLayout.addStretch()
        self.hNTLayout.addWidget(self.timeLabel)
        self.vLayout.addLayout(self.hNTLayout)
        self.vLayout.addWidget(self.msgTextLabel)
        
        self.hMainLayout.addLayout(self.vLayout)
        self.setFixedHeight(65)
        
        self.unreadLabel = QLabel(self)
        self.unreadLabel.setWordWrap(True)
        self.unreadLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.unreadLabel.setFixedSize(25, 15)
        self.unreadLabel.setObjectName("unreadLabel")
        
        
        # self.setUnReadLabel(100)
        # self.setUnReadLabel(1)
        StyleSheetUtils.setQssByFileName("./_rc/qss/MsgListFriendItem.qss", self)
        
        
        
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
    
    def setTime(self, time: str):
        self.timeLabel.setText(time)
        
    def getTime(self):
        return self.timeLabel.text()
    
    def setUnReadLabel(self, unread: int):
        self.unReadCount = unread
        self.unreadLabel.setText(str(unread))
        if (unread > 99):
            self.unreadLabel.setText("99+")
        
        self.unreadLabel.setVisible(unread > 0)
        
    # resize event: 大小调整时候
    def resizeEvent(self, event: QResizeEvent) -> None:
        self.unreadLabel.move(self.width() - 40, 33)