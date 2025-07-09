# import QWidget
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
# from PyQt6.QtWidgets import QHBoxLayout
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

from qfluentwidgets.components.widgets.frameless_window import FramelessWindow
from qfluentwidgets.components.widgets.button import *
from qfluentwidgets.components.widgets.line_edit import *
from qfluentwidgets.components.widgets.check_box import *
from qframelesswindow import TitleBar
from NetClientUtils import *
from Data import *

# res
from _rc.res import *

@singleton
class MainPage(FramelessWindow):
    def __init__(self):
        super().__init__()
        
        self.__netClientUtils = NetClientUtils()
        self.__users = Users()
        
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
        self.statusLabel = QLabel("status...")
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
        self.rightLayout.setCurrentWidgetByKey("DoApplyFriendsPage")
        
    def __connected(self):
        self.msgListPage.clickedAddBtn.connect(self.onClickedAddBtn)
        self.msgListPage.clickedCreateBtn.connect(lambda: print("clicked createBtn"))
        
        self.contactListPage.clickedAddBtn.connect(self.onClickedAddBtn)
        self.contactListPage.clickedCreateBtn.connect(lambda: print("clicked createBtn"))
        
        self.contactListPage.clickedListItem.connect(self.__onClickedContactListItem)
        
    def setStatusText(self, text):
        self.statusLabel.setText(text)

    def __onClickedContactListItem(self, str):
        
        # 切换到申请
        if str == "新的朋友":
            self.rightLayout.setCurrentWidgetByKey("DoApplyFriendsPage")
            self.doApplyFriendsPage.requestGetApplyList()
            self.titleBar.raise_()
            return

        # 查找会话
        if (not self.rightLayout.hasByKey(str)) and str !="" :
            # 创建一个MsgListPage
            self.sesPage = SesPage(self)
            self.sesPage.setTitle(str)
            self.rightLayout.addWidgetByKey(str, self.sesPage)

        # 直接切换
        self.rightLayout.setCurrentWidgetByKey(str)
        self.titleBar.raise_()
             

        
    def onClickedAddBtn(self):
        self.rightLayout.setCurrentWidgetByKey("AddFriendsPage")
        self.titleBar.raise_()
        
    def __responseSendMsg(self, msg):
        ownerid = msg["data"]["ownerid"]
        sesPage =  self.rightLayout.getByKey(self.__users.getNameById(ownerid))
        if sesPage != None: 
            sesPage.appendChatMsg(msg["data"])
            
