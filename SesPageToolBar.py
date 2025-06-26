from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from StyleSheetUtils import StyleSheetUtils

class SesPageToolBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.hMainLayout = QHBoxLayout()
        self.setLayout(self.hMainLayout)
        
        self.emojiBtn = self.makeBtn("./_rc/img/emojiBtn.png")
        self.sendFileBtn = self.makeBtn("./_rc/img/sendFileBtn.png")
        self.screenShotBtn = self.makeBtn("./_rc/img/screenShotBtn.png")
        self.voiceTelphoneBtn = self.makeBtn("./_rc/img/voiceTelphoneBtn.png")
        
        self.hMainLayout.addWidget(self.emojiBtn)
        self.hMainLayout.addWidget(self.sendFileBtn)
        self.hMainLayout.addWidget(self.screenShotBtn)
        self.hMainLayout.addStretch(1)
        self.hMainLayout.addWidget(self.voiceTelphoneBtn)
        self.hMainLayout.addSpacing(15)
        
        StyleSheetUtils.setQssByFileName("./_rc/qss/SesPageToolBar.qss", self)
    def makeBtn(self, iconPath,):
        btn = QPushButton()
        btn.setIcon(QIcon(QPixmap(iconPath)))
        btn.setIconSize(QSize(20, 20))
        btn.setFixedSize(30, 30)
        return btn
    
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        
        