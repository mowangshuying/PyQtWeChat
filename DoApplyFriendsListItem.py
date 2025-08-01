from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from NetClientUtils import NetClientUtils
from Data import *
from Msg import *
from qfluentwidgets import *
from BusUtils import *

class DoApplyFriendsListItem(QFrame):
    
    clickedAgreeBtn = pyqtSignal(int)
    clickedRefuseBtn = pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__netClientUtils = NetClientUtils()
        self.__users = Users()
        self.__friendApplys = FriendApplys()
        self.__busUtils = BusUtils()
        
        self.id = -1

        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setSpacing(0)
        self.hMainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.hMainLayout)

        self.headImgLabel = ImageLabel(QPixmap("./_rc/img/head_2.jpg"))
        self.headImgLabel.setFixedSize(30, 30)

        self.vInfoWidget = QWidget()
        self.vInfoLayout = QVBoxLayout()
        self.vInfoLayout.setContentsMargins(0, 0, 0, 0)
        self.vInfoLayout.setSpacing(0)
        self.vInfoWidget.setLayout(self.vInfoLayout)
        
        self.nameLabel = StrongBodyLabel()
        self.msgLabel = BodyLabel()
        self.nameLabel.setText("username")
        self.msgLabel.setText("msg")

        self.vInfoLayout.addWidget(self.nameLabel)
        self.vInfoLayout.addWidget(self.msgLabel)

        self.stateBtn = PushButton("状态")
        self.agreeBtn = PushButton("同意")
        self.refuseBtn = PushButton("拒绝")

        self.hMainLayout.addWidget(self.headImgLabel)
        self.hMainLayout.addSpacing(15)
        self.hMainLayout.addWidget(self.vInfoWidget, 1)
        self.hMainLayout.addWidget(self.stateBtn)
        self.hMainLayout.addWidget(self.agreeBtn)
        self.hMainLayout.addWidget(self.refuseBtn)
        
        self.setFixedHeight(40)
        
        # connect
        self.agreeBtn.clicked.connect(self.onClickedAgreeBtn)
        self.refuseBtn.clicked.connect(self.onClickedRefuseBtn)

    def setHeadImg(self, headimg):
        headimg = headimg.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.headImgLabel.setPixmap(headimg)

    def setName(self, name):
        self.nameLabel.setText(name)
    
    def setMsg(self, msg):
        self.msgLabel.setText(msg)

    def setState(self, state):
        apply = self.__friendApplys.getApplyById(self.id)
        
        if apply.ownerid == self.__users.getId():
            if state == 0:
                self.stateBtn.show()
                self.stateBtn.setText("等待同意")
                self.agreeBtn.hide()
                self.refuseBtn.hide()
            else:
                self.agreeBtn.hide()
                self.refuseBtn.hide()
                self.stateBtn.show()
                if state == 1:
                    self.stateBtn.setText("已同意")
                    self.__busUtils.agreeAddFriend.emit(apply.friendid)
                elif state == 2:
                    self.stateBtn.setText("已拒绝")
        elif apply.friendid == self.__users.getId():
            if (state == 0):
                self.stateBtn.hide()
                self.agreeBtn.show()
                self.refuseBtn.show()
            else:
                self.agreeBtn.hide()
                self.refuseBtn.hide()
                self.stateBtn.show()
                if state == 1:
                    self.stateBtn.setText("已同意")
                    self.__busUtils.agreeAddFriend.emit(apply.ownerid)
                elif state == 2:
                    self.stateBtn.setText("已拒绝")
        
    def setId(self, id):
        self.id = id
        
    def getId(self):
        return self.id
    def onClickedAgreeBtn(self):
        self.clickedAgreeBtn.emit(self.id)
    
    def onClickedRefuseBtn(self):
        self.clickedRefuseBtn.emit(self.id)