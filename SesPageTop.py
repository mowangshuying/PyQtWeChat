from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from StyleSheetUtils import StyleSheetUtils

class SesPageTop(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)
        
        self.hBtnLayout = QHBoxLayout()
        self.hBtnLayout.setContentsMargins(0, 0, 0, 0)
        self.hBtnLayout.setSpacing(0)
        # self.hBtnLayout.addStretch(1)
        
        self.minBtn = self.makeBtn("./_rc/img/minBtn.png")
        self.maxBtn = self.makeBtn("./_rc/img/maxBtn.png")
        self.closeBtn = self.makeBtn("./_rc/img/closeBtn.png")
        
        self.hBtnLayout.addStretch()
        self.hBtnLayout.addWidget(self.minBtn)
        self.hBtnLayout.addWidget(self.maxBtn)
        self.hBtnLayout.addWidget(self.closeBtn)
        
        self.vMainLayout.addLayout(self.hBtnLayout)
        
        self.hTitleLayout = QHBoxLayout()
        self.hTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.hTitleLayout.setSpacing(0)
        self.hTitleLayout.addSpacing(30)
        
        self.titleLable = QLabel()
        self.titleLable.setText("just a title")
        self.titleLable.setFixedHeight(40)
        self.titleLable.setAlignment(Qt.AlignLeft)
        
        self.moreBtn = self.makeBtn("./_rc/img/moreBtn.png")
        
        self.hTitleLayout.addWidget(self.titleLable)
        self.hTitleLayout.addStretch(1)
        self.hTitleLayout.addWidget(self.moreBtn)
        self.hTitleLayout.addSpacing(15)
        self.vMainLayout.addLayout(self.hTitleLayout)

        self.setFixedHeight(65)
        self.setMouseTracking(True)
        StyleSheetUtils.setQssByFileName("./_rc/qss/SesPageTop.qss", self)
        
        
                
    def makeBtn(self, iconPath):
        btn = QPushButton()
        btn.setIcon(QIcon(QPixmap(iconPath)))
        btn.setIconSize(QSize(20, 20))
        btn.setFixedSize(30, 30)
        return btn
    
    def getMinBtn(self):
        return self.minBtn
    
    def getMaxBtn(self):
        return self.maxBtn
    
    def getCloseBtn(self):
        return self.closeBtn
    
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)