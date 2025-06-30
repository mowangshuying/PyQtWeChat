from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from StyleSheetUtils import StyleSheetUtils
from PageTop import PageTop
from SesPageToolBar import SesPageToolBar
# from SesPage import SesPage
# from HSplit import HSplit
from VSplit import VSplit

class SesPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAcceptDrops(True)
        self.setMouseTracking(True)

        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)

        self.pageTop = PageTop(self)
        self.vMainLayout.addWidget(self.pageTop)

        self.sp1 = VSplit(self)

        self.list = QListWidget(self)
        self.list.setAcceptDrops(False)

        self.sp2 = VSplit(self)

        self.sesPageToolBar = SesPageToolBar(self)

        self.edit = QTextEdit(self)
        self.edit.setAcceptDrops(False)
        self.edit.setAcceptRichText(True)

        self.hBottomLayout = QHBoxLayout()
        self.sendBtn = QPushButton("发送[s]")
        self.sendBtn.setFixedSize(70, 30)

        self.hBottomLayout.addStretch(1)
        self.hBottomLayout.addWidget(self.sendBtn)
        self.hBottomLayout.addSpacing(15)
        
        self.vMainLayout.addWidget(self.pageTop)
        self.vMainLayout.addWidget(self.sp1)
        self.vMainLayout.addWidget(self.list, 2)
        self.vMainLayout.addWidget(self.sp2)
        self.vMainLayout.addWidget(self.sesPageToolBar)
        self.vMainLayout.addWidget(self.edit, 1)
        self.vMainLayout.addLayout(self.hBottomLayout)

        StyleSheetUtils.setQssByFileName("./_rc/qss/SesPage.qss", self)

    def getMinBtn(self):
        return self.pageTop.getMinBtn()
    
    def getMaxBtn(self):
        return self.pageTop.getMaxBtn()
    
    def getCloseBtn(self):
        return self.pageTop.getCloseBtn()

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)


        