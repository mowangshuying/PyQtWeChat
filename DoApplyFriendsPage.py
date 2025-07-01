from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from PageTop import *
from VSplit import *
from DoApplyFriendsListItem import *

from Data import *
from Msg import *
from Data import *

class DoApplyFriendsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__friendApplys = FriendApplys()

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

    def add(self, id, headimg, username, msg, state):
        item = DoApplyFriendsListItem()
        item.setHeadImg(QPixmap(""))
        item.setName(username)
        item.setMsg(msg)
        item.setId(id)
        # item.setState(state)

        # print("item sizeHint:" + str(item.sizeHint()))
        listItem = QListWidgetItem(self.list)
        listItem.setSizeHint(QSize(200, 40))
        
        self.list.addItem(listItem)
        self.list.setItemWidget(listItem, item)

    def requestGetApplyList(self):
        dataJson = {"ownerid": self.__users.getId()}
        self.__netClientUtils.request(MsgCmd.getApplyFriendList, dataJson, self.responseGetApplyList)

    def responseGetApplyList(self, msg):
        print(msg)
        # if msg.cmd != MsgCmd.getApplyFriendList:
        #     return
        
        for item in msg["data"]:
            id = item["id"]
            ownerid = item["ownerid"]
            friendid = item["friendid"]
            friendUsername = item["friendUsername"]
            appplystate = item["applystate"]
            applymsg = item["applymsg"]
            
            self.__friendApplys.addDetail(id, ownerid, friendid, appplystate, applymsg)
            self.add(id, "", friendUsername, applymsg, appplystate)

        
        