from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from NetClientUtils import NetClientUtils
from Data import *

class DoApplyFriendsListItem(QWidget):
    def __init__(self, parent=None):
        self.__init__(self, parent)

        self.__netClientUtils = NetClientUtils()
        self.__users = Users()

        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setSpacing(0)
        self.hMainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.hMainLayout)

        self.headImgLabel = QLabel()

        self.vInfoLayout = QVBoxLayout()
        self.nameLabel = QLabel()
        self.msgLabel = QLabel()
        self.nameLabel.setText("username")
        self.msgLabel.setText("msg")

        self.vInfoLayout.addWidget(self.nameLabel)
        self.vInfoLayout.addWidget(self.msgLabel)

        self.agreeBtn = QPushButton("同意")
        self.refuseBtn = QPushButton("拒绝")

        self.hMainLayout.addwidget(self.headImgLabel)
        self.hMainLayout.addLayout(self.vInfoLayout)
        self.hMainLayout.addWidget(self.agreeBtn)
        self.hMainLayout.addWidget(self.refuseBtn)

    def setHeadImg(self, headimg):
        self.headImgLabel.setPixmap(headimg)

    def setName(self, name):
        self.nameLabel.setText(name)
    
    def setMsg(self, msg):
        self.msgLabel.setText(msg)

    def setState(self, state):
        if state == 0:
            self.agreeBtn.setText("等待同意")
        elif state == 1:
            self.agreeBtn.setText("已同意")
        elif state == 2:
            self.agreeBtn.setText("已拒绝")
        

    def onClickedAgreeBtn(self):
        pass

    def onClickedRefuseBtn(self):
        print("onClickedRefuseBtn")