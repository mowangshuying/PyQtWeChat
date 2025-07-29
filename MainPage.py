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

# res
from _rc.res import *

@singleton
class MainPage(FramelessWindow):
    def __init__(self):
        super().__init__()
        
        self.__netClientUtils = NetClientUtils()
        self.__users = Users()
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

    def __initMidPage(self):
        # msgListPage
        self.msgListPage = MsgListPage()
        self.midLayout.addWidgetByKey("MsgListPage", self.msgListPage)
        
        # contactListPage;
        self.contactListPage = ContactListPage()
        self.contactListPage.requestGetFriendList()
        self.midLayout.addWidgetByKey("ContactListPage", self.contactListPage)
        
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
        
        self.rightLayout.setCurrentWidgetByKey("DoApplyFriendsPage")
        
    def __connected(self):
        self.msgListPage.clickedAddBtn.connect(self.onClickedAddBtn)
        self.msgListPage.clickedCreateBtn.connect(lambda: print("clicked createBtn"))
        
        self.contactListPage.clickedAddBtn.connect(self.onClickedAddBtn)
        self.contactListPage.clickedCreateBtn.connect(lambda: print("clicked createBtn"))
        
        self.contactListPage.clickedListItem.connect(self.__onClickedContactListItem)
        self.toolPage.clickedChangeHeadImgBtn.connect(self.__onClickedChangedHeadImgBtn)
        
        
        # bus utils
        self.__busUtils.changeHeadImgSuc.connect(self.__onChangeHeadImgSuc)
        self.__busUtils.statusBarTextChanged.connect(self.__onStatusBarTextChanged)
        self.__busUtils.agreeAddFriend.connect(self.__onAgreeAddFriend)
        self.__busUtils.swithSesPage.connect(self.__onSwithSesPage)
        
        
    def setStatusText(self, text):
        self.statusLabel.setText(text)


    def __makeSesPageByKey(self, key):
        self.sesPage = SesPage(self)
        self.sesPage.setTitle(key)
        self.rightLayout.addWidgetByKey(key, self.sesPage)        

    def __onClickedContactListItem(self, str):
        
        # 切换到申请
        if str == "新的朋友":
            self.rightLayout.setCurrentWidgetByKey("DoApplyFriendsPage")
            self.doApplyFriendsPage.requestGetApplyList()
            self.titleBar.raise_()
            return

        username = str
        userid = self.__users.getIdByName(username)
        headimg = self.__base64Utils.base64StringToPixmap(self.__users.getHeadImgById(userid))
        
        self.contactInfoPage.updateInfo(headimg, username, userid)
        self.rightLayout.setCurrentWidgetByKey("ContactInfoPage")
        self.titleBar.raise_()

             

        
    def onClickedAddBtn(self):
        self.rightLayout.setCurrentWidgetByKey("AddFriendsPage")
        self.titleBar.raise_()
        
    def __onClickedChangedHeadImgBtn(self):
        self.rightLayout.setCurrentWidgetByKey("PictureToolPage")
        self.titleBar.raise_()
        
    def __onChangeHeadImgSuc(self):
        self.toolPage.reloadHeadImg()
        
    def __onStatusBarTextChanged(self, text):
        self.statusLabel.setText(text)
        # 操过3秒后清除
        QTimer.singleShot(3000, lambda: self.statusLabel.setText(""))
        
    def __onAgreeAddFriend(self, msg):
        self.contactListPage.requestGetFriendList()
        
    def __responseSendMsg(self, msg):
        ownerid = msg["data"]["ownerid"]
        sesPage =  self.rightLayout.getByKey(self.__users.getNameById(ownerid))
        if sesPage == None: 
            self.__makeSesPageByKey(self.__users.getNameById(ownerid))
            sesPage = self.rightLayout.getByKey(self.__users.getNameById(ownerid))
            
        sesPage.appendChatMsg(msg["data"])
        
    
    def __onSwithSesPage(self, key):
        
        # # 查找会话
        if (not self.rightLayout.hasByKey(key)) and key !="" :
            self.__makeSesPageByKey(key)

        # 直接切换
        self.rightLayout.setCurrentWidgetByKey(key)
        self.titleBar.raise_()
            
