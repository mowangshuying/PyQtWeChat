from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from NetClientUtils import NetClientUtils
from Data import *
from Msg import *

class DoApplyFriendsListItem(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__netClientUtils = NetClientUtils()
        self.__users = Users()
        self.__friendApplys = FriendApplys()
        
        self.id = -1

        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setSpacing(0)
        self.hMainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.hMainLayout)

        self.headImgLabel = QLabel()
        self.headImgLabel.setFixedSize(30, 30)

        self.vInfoLayout = QVBoxLayout()
        self.nameLabel = QLabel()
        self.msgLabel = QLabel()
        self.nameLabel.setText("username")
        self.msgLabel.setText("msg")

        self.vInfoLayout.addWidget(self.nameLabel)
        self.vInfoLayout.addWidget(self.msgLabel)

        self.agreeBtn = QPushButton("同意")
        self.refuseBtn = QPushButton("拒绝")

        self.hMainLayout.addWidget(self.headImgLabel)
        self.hMainLayout.addSpacing(10)
        self.hMainLayout.addLayout(self.vInfoLayout)
        self.hMainLayout.addStretch(1)
        self.hMainLayout.addWidget(self.agreeBtn)
        self.hMainLayout.addWidget(self.refuseBtn)
        
        self.setFixedHeight(40)
        
        # connect
        self.agreeBtn.clicked.connect(self.onClickedAgreeBtn)
        self.refuseBtn.clicked.connect(self.onClickedRefuseBtn)

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
        
    def setId(self, id):
        self.id = id

    def onClickedAgreeBtn(self):
        # 同意好友申请.
        # ownerid = self.__users.getId()
        # friendid = self.__users.getIdByName(self.usernameLabel.text())
        
        apply = self.__friendApplys.getApplyById(self.id)
        ownerid = apply.ownerid
        friendid = apply.friendid
        applystate = 1
        applymsg = apply.applymsg
        data = {"ownerid": ownerid, "friendid": friendid, "applystate": applystate, "applymsg": applymsg}
        self.__netClientUtils.request(MsgCmd.doApplyAddUser, data, self.responseAddUser)
    
    def onClickedRefuseBtn(self):
        # print("onClickedRefuseBtn")
        pass
    
    def responseAddUser(self, msg):
        pass