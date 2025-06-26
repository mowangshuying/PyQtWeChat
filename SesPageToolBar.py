from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QSize
from StyleSheetUtils import StyleSheetUtils
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QStyle, QStyleOption

class SesPageToolBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.hMainLayout = QHBoxLayout()
        self.setLayout(self.hMainLayout)
        
        self.emojiBtn = self.makeBtn("./_rc/imgs/emojiBtn.png")
        self.sendFileBtn = self.makeBtn("./_rc/imgs/sendFileBtn.png")
        self.screenShotBtn = self.makeBtn("./_rc/imgs/screenShotBtn.png")
        self.voiceTelphoneBtn = self.makeBtn("./_rc/imgs/voiceTelephoneBtn.png")
        
        self.hMainLayout.addWidget(self.emojiBtn)
        self.hMainLayout.addWidget(self.sendFileBtn)
        self.hMainLayout.addWidget(self.screenShotBtn)
        self.hMainLayout.addStretch(1)
        self.hMainLayout.addWidget(self.voiceTelphoneBtn)
        self.hMainLayout.addSpacing(15)
        
        StyleSheetUtils.setQssByFileName("./_rc/qss/SesPageToolBar.qss", self)
    def makeBtn(self, iconPath,):
        btn = QPushButton()
        btn.setIcon(QPixmap(iconPath))
        btn.setIconSize(QSize(20, 20))
        btn.setFixedSize(30, 30)
        return btn
    
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        
        