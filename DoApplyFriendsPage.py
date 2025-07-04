from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# from PageTop import *
from VSplit import *
from DoApplyFriendsListItem import *
from ListWidgetEx import *
from Data import *
from Msg import *
from Data import *

from NetClientUtils import *
from Data import *
from Msg import *

from qfluentwidgets import *
from StyleSheetUtils import StyleSheetUtils
@singleton
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

        self.vMainLayout.addSpacing(65)
        self.sp = VSplit()
        self.vMainLayout.addWidget(self.sp)

        self.list = ListWidgetEx()
        self.vMainLayout.addWidget(self.list)
        self.__netClientUtils.register(MsgType.push, MsgCmd.doApplyAddUser, self.onPushDoApplyAddUser)
        # StyleSheetUtils.setQssByFileName("./_rc/qss/DoApplyFriendsPage.qss", self)
        

    def add(self, id, headimg, username, msg, state):
        item = DoApplyFriendsListItem()
        item.setHeadImg(QPixmap(""))
        item.setName(username)
        item.setMsg(msg)
        item.setId(id)
        item.setState(state)
        
        item.clickedAgreeBtn.connect(self.onClickedAgreeBtn)
        item.clickedRefuseBtn.connect(self.onClickedRefuseBtn)
        
        listItem = QListWidgetItem(self.list)
        listItem.setSizeHint(QSize(200, 40))
        
        self.list.addItem(listItem)
        self.list.setItemWidget(listItem, item)
        
    # 根据id从list中查到指定的item
    def setStateById(self, id, state):
        for i in range(self.list.count()):
            item = self.list.item(i)
            widget = self.list.itemWidget(item)
            if widget.getId() == id:
                widget.setState(state) 
        
    def onClickedAgreeBtn(self, id):
        apply = self.__friendApplys.getApplyById(id)
        ownerid = apply.ownerid
        friendid = apply.friendid
        applystate = 1
        applymsg = apply.applymsg
        data = { "id":id, "ownerid": ownerid, "friendid": friendid, "applystate": applystate, "applymsg": applymsg}
        self.__netClientUtils.request(MsgCmd.doApplyAddUser, data, None)
    
    def onClickedRefuseBtn(self, id):
        apply = self.__friendApplys.getApplyById(id)
        ownerid = apply.ownerid
        friendid = apply.friendid
        applystate = 0
        applymsg = apply.applymsg
        data = {"id": id ,"ownerid": ownerid, "friendid": friendid, "applystate": applystate, "applymsg": applymsg}
        self.__netClientUtils.request(MsgCmd.doApplyAddUser, data, None)

    def onPushDoApplyAddUser(self, msg):
        apply = self.__friendApplys.getApplyById(msg["data"]["id"])
        if apply.ownerid == self.__users.getId():
            self.setStateById(msg["data"]["id"], msg["data"]["applystate"])
        elif apply.friendid == self.__users.getId():
            self.setStateById(msg["data"]["id"], msg["data"]["applystate"])

    def requestGetApplyList(self):
        dataJson = {"ownerid": self.__users.getId()}
        self.__netClientUtils.request(MsgCmd.getApplyFriendList, dataJson, self.responseGetApplyList)

    def responseGetApplyList(self, msg):
        self.list.clear()
        for item in msg["data"]:
            id = item["id"]
            ownerid = item["ownerid"]
            friendid = item["friendid"]
            friendUsername = item["friendUsername"]
            appplystate = item["applystate"]
            applymsg = item["applymsg"]
            
            self.__friendApplys.addDetail(id, ownerid, friendid, appplystate, applymsg)
            self.add(id, "", friendUsername, applymsg, appplystate)
        
        