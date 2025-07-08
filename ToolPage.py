from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


from _rc.res import *
from StyleSheetUtils import StyleSheetUtils

class ToolPage(QWidget):
    
    clickedHeadBtn = pyqtSignal()
    clickedUserBtn = pyqtSignal()
    clickedGroupBtn = pyqtSignal()
    clickedFriendsBtn = pyqtSignal()
    clickedMsgsBtn = pyqtSignal()
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)
        
        self.headBtn = self.makeBtn("./_rc/img/head_1.jpg", 40)
        self.userBtn = self.makeBtn("./_rc/img/contact_list.png")
        self.msgsBtn = self.makeBtn("./_rc/img/chat_icon.png")
        
        # 头像
        self.vMainLayout.addSpacing(20)
        self.vMainLayout.addWidget(self.headBtn, 0, Qt.AlignmentFlag.AlignHCenter)
        self.vMainLayout.addSpacing(30)
        
        # 用户
        self.vMainLayout.addWidget(self.userBtn,0, Qt.AlignmentFlag.AlignHCenter)
        self.vMainLayout.addSpacing(15)
        
        # 消息
        self.vMainLayout.addWidget(self.msgsBtn, 0, Qt.AlignmentFlag.AlignHCenter)
        # self.vMainLayout.addSpacing(10)
        self.vMainLayout.addStretch()
        
        self.setFixedWidth(56)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        
        
        # connect;
        self.headBtn.clicked.connect(self.__onClickedHeadBtn)
        self.userBtn.clicked.connect(self.__onClickedUserBtn)
        # self.groupBtn.clicked.connect(lambda: self.clickedGroupBtn.emit())
        # self.friendsBtn.clicked.connect(lambda: self.clickedFriendsBtn.emit())
        self.msgsBtn.clicked.connect(self.__onClickedMsgsBtn)
        
        StyleSheetUtils.setQssByFileName("./_rc/qss/ToolPage.qss", self)
        
    def makeBtn(self, iconPath, s = 30): 
        btn = QPushButton()
        btn.setIcon(QIcon(QPixmap(iconPath)))
        btn.setIconSize(QSize(s, s))
        btn.setFixedSize(s, s)
        return btn
        
    def __onClickedHeadBtn(self):
        self.clickedHeadBtn.emit()
        
    def __onClickedUserBtn(self):
        self.userBtn.setIcon(QIcon(QPixmap("./_rc/img/contact_list_press.png")))
        self.msgsBtn.setIcon(QIcon(QPixmap("./_rc/img/chat_icon.png")))
        self.clickedUserBtn.emit()
        
    def __onClickedMsgsBtn(self):
        self.userBtn.setIcon(QIcon(QPixmap("./_rc/img/contact_list.png")))
        self.msgsBtn.setIcon(QIcon(QPixmap("./_rc/img/chat_icon_press.png")))
        self.clickedMsgsBtn.emit()
    
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)