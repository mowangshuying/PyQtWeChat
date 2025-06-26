from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class SesPageTop(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        
        self.hBtnLayout = QHBoxLayout()
        self.hBtnLayout.setContentsMargins(0, 0, 0, 0)
        self.hBtnLayout.setSpacing(5)
        # self.hBtnLayout.addStretch(1)
        
        self.minBtn = self.makeBtn("./_rc/imgs/minBtn.png")
        self.maxBtn = self.makeBtn("./_rc/imgs/maxBtn.png")
        self.closeBtn = self.makeBtn("./_rc/imgs/closeBtn.png")
        
        self.hBtnLayout.addSpacing()
        self.hBtnLayout.addWidget(self.minBtn)
        self.hBtnLayout.addWidget(self.maxBtn)
        self.hBtnLayout.addWidget(self.closeBtn)
        
        self.vMainLayout.addLayout(self.hBtnLayout)
        
        self.hTitleLayout = QHBoxLayout()
        self.hTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.hTitleLayout.setSpacing(0)
        self.hTitleLayout.addSpacing(30)
        
        self.titleLable = QLabel()
        self.titleLable.setFixedHeight(40)
        self.titleLable.setAlignment(Qt.AlignLeft)
        
        self.moreBtn = self.makeBtn("./_rc/imgs/moreBtn.png")
        
        self.hTitleLayout.addWidget(self.titleLable)
        
        
                
    def makeBtn(self, iconPath):
        btn = QPushButton()
        btn.setIcon(QIcon(iconPath))
        btn.setIconSize(QSize(20, 20))
        btn.setFixedSize(30, 30)
        return btn