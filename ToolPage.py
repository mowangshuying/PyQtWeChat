from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


from _rc.res import *
from StyleSheetUtils import StyleSheetUtils

class ToolPage(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.vMainLayout)
        
        self.headBtn = self.makeBtn("./_rc/img/headBtn.png", 40)
        self.userBtn = self.makeBtn("./_rc/img/userBtn.png")
        self.groupBtn = self.makeBtn("./_rc/img/groupBtn.png")
        self.friendsBtn = self.makeBtn("./_rc/img/friendsBtn.png")
        self.msgsBtn = self.makeBtn("./_rc/img/msgsBtn.png")
        
        self.vMainLayout.addSpacing(20)
        self.vMainLayout.addWidget(self.headBtn, 0, Qt.AlignmentFlag.AlignHCenter)
        self.vMainLayout.addWidget(self.userBtn,0, Qt.AlignmentFlag.AlignHCenter)
        self.vMainLayout.addWidget(self.groupBtn, 0, Qt.AlignmentFlag.AlignHCenter)
        self.vMainLayout.addWidget(self.friendsBtn, 0, Qt.AlignmentFlag.AlignHCenter)
        self.vMainLayout.addWidget(self.msgsBtn, 0, Qt.AlignmentFlag.AlignHCenter)
        self.vMainLayout.addStretch()
        
        self.setFixedWidth(55)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        StyleSheetUtils.setQssByFileName("./_rc/qss/ToolPage.qss", self)
        
    def makeBtn(self, iconPath, s = 30): 
        btn = QPushButton()
        btn.setIcon(QIcon(QPixmap(iconPath)))
        btn.setIconSize(QSize(s, s))
        btn.setFixedSize(s, s)
        return btn
        
    
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)