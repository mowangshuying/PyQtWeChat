from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from StyleSheetUtils import StyleSheetUtils
from NetClientUtils import NetClientUtils
from Msg import *
from Data import *

class FriendCard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__users = Users()
        self.__netClientUtils = NetClientUtils()
        
        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setContentsMargins(4, 4, 4, 4)
        self.hMainLayout.setSpacing(0)
        self.setLayout(self.hMainLayout)

        self.headImg = QLabel()
        self.headImg.setFixedSize(48, 48)
        self.hMainLayout.addWidget(self.headImg)

        self.hMainLayout.addSpacing(10)    

        self.vRightLayout = QVBoxLayout()
        self.vRightLayout.setContentsMargins(4, 4, 4, 4)
        self.vRightLayout.setSpacing(0)
        
        self.usernameLabel = QLabel()
        self.usernameLabel.setObjectName("usernameLabel")
        
        self.addFriendbtn = QPushButton()
        self.addFriendbtn.setObjectName("addFriendbtn")
        self.addFriendbtn.setText("添加")
        
        self.addFriendbtn.setFixedSize(40, 20)
        self.vRightLayout.addWidget(self.usernameLabel)
        self.vRightLayout.addWidget(self.addFriendbtn)

        self.hMainLayout.addLayout(self.vRightLayout)
        self.hMainLayout.addStretch()

        self.setFixedSize(180, 70)
        
        self.addFriendbtn.clicked.connect(self.onClickedAddFriendbtn)
        StyleSheetUtils.setQssByFileName("./_rc/qss/friendCard.qss", self)

    def setUserName(self, name):
        self.usernameLabel.setText(name)

    def setImg(self, img):
        self.headImg.setPixmap(img)

    def setNameAndImg(self, name, img):
        self.setUserName(name)
        self.setImg(img)
        
    def setFriendId(self, friendid):
        self.friendid = friendid

    def onClickedAddFriendbtn(self):
        ownerid = self.__users.getId()
        friendid = self.__users.getIdByName(self.usernameLabel.text())
        data = {"ownerid":ownerid, "friendid":friendid, "applymsg":"---- 添加好友 ----"}
        self.__netClientUtils.request(MsgCmd.applyAddUser, data, lambda msg: print(msg))
        
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)
