from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from qfluentwidgets import *

from StyleSheetUtils import StyleSheetUtils
from NetClientUtils import NetClientUtils
from Msg import *
from Data import *


class FindFriendsListItem(QFrame):
    def __init__(self, parent=None): 
        super().__init__(parent)

        self.__users = Users()
        self.__netClientUtils = NetClientUtils()
        
        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setContentsMargins(0, 0, 0, 0)
        self.hMainLayout.setSpacing(0)
        self.setLayout(self.hMainLayout)

        self.headImg = ImageLabel()
        self.headImg.setFixedSize(30, 30)
        self.hMainLayout.addWidget(self.headImg)

        self.hMainLayout.addSpacing(10)    
        
        self.usernameLabel = BodyLabel()
        self.usernameLabel.setObjectName("usernameLabel")
        
        self.addFriendbtn = PushButton()
        self.addFriendbtn.setObjectName("addFriendbtn")
        self.addFriendbtn.setText("添加")
        self.addFriendbtn.setFixedHeight(25)
        setFont(self.addFriendbtn, 12)
        
        self.hMainLayout.addWidget(self.usernameLabel)
        self.hMainLayout.addStretch()
        self.hMainLayout.addWidget(self.addFriendbtn)

        self.setFixedHeight(40)
        self.addFriendbtn.clicked.connect(self.onClickedAddFriendbtn)
        StyleSheetUtils.setQssByFileName("./_rc/qss/friendCard.qss", self)

    def setUserName(self, name):
        self.usernameLabel.setText(name)
        
    def getUserName(self):
        return self.usernameLabel.text()

    def setImg(self, img):
        img = img.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.headImg.setPixmap(img)
        # self.headImg.setFixedSize(48, 48)

    def setNameAndImg(self, name, img):
        self.setUserName(name)
        self.setImg(img)
        
    def setFriendId(self, friendid):
        self.friendid = friendid
        
    def getFriendId(self):
        return self.friendid

    def onClickedAddFriendbtn(self):
        ownerid = self.__users.getId()
        friendid = self.__users.getIdByName(self.usernameLabel.text())
        data = {"ownerid":ownerid, "friendid":friendid, "applymsg":"---- 添加好友 ----"}
        self.__netClientUtils.request(MsgCmd.applyAddUser, data, lambda msg: print(msg))
