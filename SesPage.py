from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from StyleSheetUtils import StyleSheetUtils
from SesPageTop import SesPageTop
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

        self.sesPageTop = SesPageTop(self)
        self.vMainLayout.addWidget(self.sesPageTop)

        self.sp1 = VSplit(self)

        self.list = QListWidget(self)
        self.list.setAcceptDrops(False)

        self.sp2 = VSplit(self)

        self.sesPageToolBar = SesPageToolBar(self)

        self.edit = QTextEdit(self)
        self.edit.setAcceptDrops(False)
        self.edit.setAcceptRichText(True)

        self.vMainLayout.addWidget(self.sesPageTop)
        self.vMainLayout.addWidget(self.sp1)
        self.vMainLayout.addWidget(self.list, 2)
        self.vMainLayout.addWidget(self.sp2)
        self.vMainLayout.addWidget(self.sesPageToolBar)
        self.vMainLayout.addWidget(self.edit, 1)

        self.hBottomLayout = QHBoxLayout()
        self.sendBtn = QPushButton("发送[s]")
        self.sendBtn.setFixedSize(70, 30)

        self.hBottomLayout.addStretch(1)
        self.hBottomLayout.addWidget(self.sendBtn)
        self.hBottomLayout.addSpacing(15)

        StyleSheetUtils.setQssByFileName("./_rc/qss/SesPage.qss", self)

    def getMinBtn(self):
        return self.sesPageTop.getMinBtn()
    
    def getMaxBtn(self):
        return self.sesPageTop.getMaxBtn()
    
    def getCloseBtn(self):
        return self.sesPageTop.getCloseBtn()

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)


        