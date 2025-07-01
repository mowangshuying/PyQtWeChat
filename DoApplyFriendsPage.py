from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from PageTop import *
from VSplit import *
from DoApplyFriendsListItem import *

from Data import *
from Msg import *

class DoApplyFriendsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
    

        self.__netClientUtils = NetClientUtils()
        self.__users = Users()

        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)

        self.pageTop = PageTop(self)
        self.pageTop.setTitle("申请列表")
        self.vMainLayout.addWidget(self.pageTop)

        self.sp = VSplit()
        self.vMainLayout.addWidget(self.sp)

        self.list = QListWidget()
        self.vMainLayout.addWidget(self.list)

    def add(self, headimg, username, msg, state):
        item = DoApplyFriendsListItem()
        item.setHeadImg(headimg)
        item.setName(username)
        item.setMsg(msg)
        item.setState(state)

        listItem = QListWidgetItem(self.list)
        self.list.addItem(listItem)

    def requestGetApplyList(self):
        dataJson = {"ownerid": self.__users.getId()}
        self.__netClientUtils.request(MsgCmd.getApplyFriendList, dataJson, self.responseGetApplyList)

    def responseGetApplyList(self, msg):
        print(msg)
        if msg.cmd != MsgCmd.getApplyFriendList:
            return
        
        for item in msg.data:
            ownerid = item["ownerid"]
            friendid = item["friendid"]
            appplystate = item["appplystate"]
            applymsg = item["applymsg"]
            self.add(friendid, ownerid, applymsg, appplystate)

        
        