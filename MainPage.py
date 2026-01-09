from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from ToolPage import ToolPage
from PyQt6.QtGui import *
from MsgListPage import MsgListPage
from ContactListPage import ContactListPage
from HSplit import HSplit
from SesPage import SesPage
from NetClientUtils import NetClientUtils
from sigleton import singleton
from StackLayout import StackLayout
from AddFriendsPage import AddFriendsPage
from DoApplyFriendsPage import DoApplyFriendsPage
from PictureToolPage import PictureToolPage
from ContactInfoPage import ContactInfoPage

from qfluentwidgets.components.widgets.frameless_window import FramelessWindow
from qfluentwidgets.components.widgets.button import *
from qfluentwidgets.components.widgets.line_edit import *
from qfluentwidgets.components.widgets.check_box import *
from qframelesswindow import TitleBar
from NetClientUtils import *
from Data import *
from BusUtils import BusUtils
from Base64Utils import Base64Utils
from CreateGroupPage import CreateGroupPage

# res
from _rc.res import *

@singleton
class MainPage(FramelessWindow):
    def __init__(self):
        super().__init__()
        
        self.__netClientUtils = NetClientUtils()
        self.__users = Users()
        self.__groupInfos = GroupInfos()
        self.__busUtils = BusUtils()
        self.__base64Utils = Base64Utils()
        
        # self.titleBar.raise_()
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)
    
        self.hLayout = QHBoxLayout()
        self.hLayout.setSpacing(0)
        self.hLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.addLayout(self.hLayout)
        
        # left;
        self.toolPage = ToolPage(self)
        self.hLayout.addWidget(self.toolPage)
        
        # mid;
        # self.midPage = MsgListPage()
        # self.hMainLayout.addWidget(self.midPage)
        self.midLayout = StackLayout()
        self.__initMidPage()
        self.hLayout.addLayout(self.midLayout)
        
        # sp
        self.sp = HSplit()
        self.hLayout.addWidget(self.sp)

        self.rightLayout = StackLayout()
        self.__initRightPage()
        self.hLayout.addLayout(self.rightLayout, 1)
        
        # self.setLayout(self.hLayout)

        # status label;
        self.statusLabel = QLabel("")
        self.statusLabel.setFixedHeight(20)
        self.statusLabel.setStyleSheet("background-color: rgb(29,124,202); font-size: 12px; color: white;")
        self.vMainLayout.addWidget(self.statusLabel)
        
        self.resize(1000, 750)

        
        # connect;
        self.__connected()
        
        self.setTitleBar(TitleBar(self))
        self.titleBar.raise_()
        
        # register msg
        self.__netClientUtils.register(MsgType.push, MsgCmd.sendMsg, self.__responseSendMsg)
        self.__request()

    def __initMidPage(self):
        
        # contactListPage;
        self.contactListPage = ContactListPage()
        # self.contactListPage.requestGetFriendList()
        self.midLayout.addWidgetByKey("ContactListPage", self.contactListPage)
        
        # msgListPage
        self.msgListPage = MsgListPage()
        # self.msgListPage.requestSessionList()
        self.midLayout.addWidgetByKey("MsgListPage", self.msgListPage)
    
        
        self.midLayout.setCurrentWidgetByKey("ContactListPage")
        
    def __initRightPage(self):
        # SesPage;
        self.sesPage = SesPage(self)
        self.rightLayout.addWidgetByKey("SesPage", self.sesPage)

        # AddFriendsPage;
        self.addFriendsPage = AddFriendsPage(self)
        self.rightLayout.addWidgetByKey("AddFriendsPage", self.addFriendsPage)        
        
        # DoApplyFriendsPage
        self.doApplyFriendsPage = DoApplyFriendsPage()
        self.rightLayout.addWidgetByKey("DoApplyFriendsPage", self.doApplyFriendsPage)
        
        # PictureToolPage
        self.pictrueToolPage = PictureToolPage()    
        self.rightLayout.addWidgetByKey("PictureToolPage", self.pictrueToolPage)
        
        # ContactInfoPage
        self.contactInfoPage = ContactInfoPage()
        self.rightLayout.addWidgetByKey("ContactInfoPage", self.contactInfoPage)

        # CreateGroupPage
        self.createGroupPage = CreateGroupPage()
        self.rightLayout.addWidgetByKey("CreateGroupPage", self.createGroupPage)
        
    def __connected(self):
        self.toolPage.clickedMsgsBtn.connect(self.__onClickedMsgsBtn)
        self.toolPage.clickedUserBtn.connect(self.__onClickedUserBtn)
        self.toolPage.clickedChangeHeadImgBtn.connect(self.__onClickedChangedHeadImgBtn)
        
        self.msgListPage.clickedAddBtn.connect(self.__onClickedAddBtn)
        self.msgListPage.clickedCreateBtn.connect(self.__onClickedCreateBtn)
        self.msgListPage.clickedListItem.connect(self.__onClickedMsgListItem)
        
        self.contactListPage.clickedAddBtn.connect(self.__onClickedAddBtn)
        self.contactListPage.clickedCreateBtn.connect(self.__onClickedCreateBtn)
        
        self.contactListPage.clickedListItem.connect(self.__onClickedContactListItem)
        
        # bus utils
        self.__busUtils.changeHeadImgSuc.connect(self.__onChangeHeadImgSuc)
        self.__busUtils.statusBarTextChanged.connect(self.__onStatusBarTextChanged)
        self.__busUtils.agreeAddFriend.connect(self.__onAgreeAddFriend)
        self.__busUtils.swithSesPage.connect(self.__onSwithSesPage)
        self.__busUtils.createGroup.connect(self.__onCreateGroup)
        
    
    def __request(self):
        self.requestGetFriendList()
        self.requestGetGroupList()
        self.requestGetSessionList()
    
    # request
    def requestGetFriendList(self):
        dataJson = {"ownerid": self.__users.getId()}
        self.__netClientUtils.request(MsgCmd.getFriendList, dataJson, self.responseGetFriendList)
        
    def requestGetGroupList(self):
        data = {"ownerid": self.__users.getId()}
        self.__netClientUtils.request(MsgCmd.getGroupList, data, self.responseGetGroupList)
        
    # response
    def requestGetSessionList(self):
        data = {"ownerid": self.__users.getId()}
        self.__netClientUtils.request(MsgCmd.getSessionList, data, self.responseGetSessionList)
        
    #response
    def responseGetFriendList(self, msg):
        # 不含数据直接返回.
        if "data" not in msg:
            return
        
        for friend in msg["data"]:
            self.contactListPage.addFriend(friend)
            self.__users.addDetail(friend["id"], friend["userid"], friend["username"], 
                                   friend["nickname"], friend["headimg"], friend["sex"], friend["state"], friend["create_date"])
    
    def responseGetGroupList(self, msg):
        # 不含数据直接返回.
        if "data" not in msg:
            return
        
        for groupInfo in msg["data"]:
            self.contactListPage.addGroup(groupInfo)
            self.__groupInfos.addDetail(groupInfo["id"], groupInfo["groupid"], groupInfo["createid"], 
                                        groupInfo["groupname"], groupInfo["headimg"] ,groupInfo["createtime"], groupInfo["groupsetting"])
    
    
    def responseGetSessionList(self, msg):
        if "data" not in msg:
            return
        
        for ses in msg["data"]:
            userid = ses["id"]
            friendname = self.__users.getNameById(userid)
            headimg = self.__users.getHeadImgById(userid)
            
            # 添加至消息列表中
            self.msgListPage.addMsg(self.__base64Utils.base64StringToPixmap(headimg), friendname, "")
            
            for msg in ses["msgs"]:        
                # 是否是最后一条
                bLastMsg = False
                if msg == ses["msgs"][-1]:
                    bLastMsg = True
                
                self.__addMsgToSes(userid, msg, bLastMsg)
    
        
    def setStatusText(self, text):
        self.statusLabel.setText(text)


    def __makeSesPageByKey(self, key):
        self.sesPage = SesPage(self)
        self.sesPage.setTitle(key)
        self.sesPage.setKey(key)
        self.rightLayout.addWidgetByKey(key, self.sesPage)        
        
    def __addMsgToSes(self, userid, msg, bLastMsg):
        key = self.__users.makeKey(userid, self.__users.getNameById(userid))
        sesPage =  self.rightLayout.getByKey(key)
        if sesPage == None: 
            self.__makeSesPageByKey(key)
            sesPage = self.rightLayout.getByKey(key)
            
        sesPage.appendChatMsg(msg, bLastMsg)
        

    def __onClickedContactListItem(self, str):
        
        # 切换到申请
        if str == "user:0:newfriend":
            self.rightLayout.setCurrentWidgetByKey("DoApplyFriendsPage")
            self.doApplyFriendsPage.requestGetApplyList()
            self.titleBar.raise_()
            return
        
        # 按照":"进行截取
        strs = str.split(":")
        
        
        name = ""
        currentid = -1
        headimg = ""
        
        if strs[0] == "user":
            userid = int(strs[1])
            user = self.__users.getUser(userid)
            name = user.username
            currentid = user.userid
            headimg = self.__base64Utils.base64StringToPixmap(user.headimg)
        
        if strs[0] == "group":
            groupid = int(strs[1])
            groupInfo = self.__groupInfos.getGroupInfo(groupid)
            name = groupInfo.groupname
            currentid = groupInfo.groupid
            headimg = self.__base64Utils.base64StringToPixmap(groupInfo.headimg)
            
        self.contactInfoPage.updateInfo(headimg, name, currentid)
        self.contactInfoPage.setKey(str)
        self.rightLayout.setCurrentWidgetByKey("ContactInfoPage")
        self.titleBar.raise_()
        
    
    def __onClickedMsgListItem(self, key):
        self.midLayout.setCurrentWidgetByKey("MsgListPage")
        self.msgListPage.setCurrentItemByKey(key)
        self.__onSwithSesPage(key)             
        
    def __onClickedAddBtn(self):
        self.rightLayout.setCurrentWidgetByKey("AddFriendsPage")
        self.titleBar.raise_()

    def __onClickedCreateBtn(self):
        self.createGroupPage.clear()
        self.rightLayout.setCurrentWidgetByKey("CreateGroupPage")
        self.titleBar.raise_()
        
    def __onClickedChangedHeadImgBtn(self):
        self.rightLayout.setCurrentWidgetByKey("PictureToolPage")
        self.titleBar.raise_()
        
    def __onClickedMsgsBtn(self):
        self.midLayout.setCurrentWidgetByKey("MsgListPage")
        self.titleBar.raise_()
        
    def __onClickedUserBtn(self):
        self.midLayout.setCurrentWidgetByKey("ContactListPage")
        self.titleBar.raise_()
        
    def __onChangeHeadImgSuc(self):
        self.toolPage.reloadHeadImg()
        
    def __onStatusBarTextChanged(self, text):
        self.statusLabel.setText(text)
        # 操过3秒后清除
        QTimer.singleShot(3000, lambda: self.statusLabel.setText(""))
        
    def __onAgreeAddFriend(self, msg):
        self.requestGetFriendList()
        
    def __responseSendMsg(self, msg):
        ownerid = msg["data"]["ownerid"]
        self.__addMsgToSes(ownerid, msg["data"], True)
    def __onSwithSesPage(self, key):
        
        strs = key.split(":")
        if strs[0] == "user":
            # # 查找会话
            if (not self.rightLayout.hasByKey(key)) and key !="" :
                self.__makeSesPageByKey(key)
            
                strs = key.split(":")
                userid = int(strs[1])
                username = self.__users.getNameById(userid)
                headimg = self.__base64Utils.base64StringToPixmap(self.__users.getHeadImgById(userid))
                msg=""
                
                
                self.msgListPage.addMsg(headimg, username, msg)
                
            # 直接切换到会话
            self.rightLayout.setCurrentWidgetByKey(key)
            # 切换到msgListPage
            self.midLayout.setCurrentWidgetByKey("MsgListPage")
            self.msgListPage.setCurrentItemByKey(key)             
            self.titleBar.raise_()
            
        if strs[0] == "group":
            # # 查找会话
            if (not self.rightLayout.hasByKey(key)) and key !="" :
                self.__makeSesPageByKey(key)
            
                strs = key.split(":")
                groupid = int(strs[1])
                
                groupInfo = self.__groupInfos.getGroupInfo(groupid)
                
                groupname = groupInfo.groupname
                headimg = self.__base64Utils.base64StringToPixmap(groupInfo.headimg)
                msg=""
            
                self.msgListPage.addMsg(headimg, groupname, msg)
                
            # 直接切换到会话
            self.rightLayout.setCurrentWidgetByKey(key)
            # 切换到msgListPage
            self.midLayout.setCurrentWidgetByKey("MsgListPage")
            self.msgListPage.setCurrentItemByKey(key)             
            self.titleBar.raise_()            
        
    def __onCreateGroup(self, groupInfo):
        # 判断__groupInfos中是否已经存在
        if self.__groupInfos.has(groupInfo["id"]):
            return
        
        self.contactListPage.addGroup(self.__base64Utils.base64StringToPixmap(groupInfo["headimg"]), groupInfo["groupname"])
        self.__groupInfos.addDetail(groupInfo["id"], groupInfo["groupid"], groupInfo["createid"], 
                                        groupInfo["groupname"], groupInfo["headimg"] ,groupInfo["createtime"], groupInfo["groupsetting"])      
        
            
