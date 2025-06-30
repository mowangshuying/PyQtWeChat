from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from StyleSheetUtils import StyleSheetUtils

class FriendCard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setContentsMargins(4, 4, 4, 4)
        self.hMainLayout.setSpacing(0)
        self.setLayout(self.hMainLayout)

        self.headImg = QLabel()
        self.headImg.setFixedSize(40, 40)
        self.hMainLayout.addWidget(self.headImg)

        self.vRightLayout = QVBoxLayout()
        self.vRightLayout.setContentsMargins(4, 4, 4, 4)
        self.vRightLayout.setSpacing(0)
        self.uername = QLabel()
        self.btn = QPushButton()
        self.btn.setText("添加")
        # self.btn.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
        self.btn.setFixedSize(40, 20)
        self.vRightLayout.addWidget(self.uername)
        self.vRightLayout.addWidget(self.btn)

        self.hMainLayout.addLayout(self.vRightLayout)

        self.setFixedSize(180, 70)
        StyleSheetUtils.setQssByFileName("./_rc/qss/friendCard.qss", self)

    def setUserName(self, name):
        self.uername.setText(name)

    def setImg(self, img):
        self.headImg.setPixmap(img)

    def setNameAndImg(self, name, img):
        self.setUserName(name)
        self.setImg(img)

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)
