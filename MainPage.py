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

# res
from _rc.res import *

@singleton
class MainPage(FramelessWindow):
    def __init__(self):
        super().__init__()
        # self.titleBar.raise_()
    
        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setSpacing(0)
        self.hMainLayout.setContentsMargins(0, 0, 0, 0)
        
        # left;
        self.toolPage = ToolPage(self)
        self.hMainLayout.addWidget(self.toolPage)
        
        # mid;
        # self.midPage = MsgListPage()
        # self.hMainLayout.addWidget(self.midPage)
        self.midLayout = StackLayout()
        self.__initMidPage()
        self.hMainLayout.addLayout(self.midLayout)
        
        # sp
        self.sp = HSplit()
        self.hMainLayout.addWidget(self.sp)

        self.rightLayout = StackLayout()
        self.__initRightPage()
        self.hMainLayout.addLayout(self.rightLayout, 1)
        
        self.setLayout(self.hMainLayout)

        self.resize(1000, 750)

        
        # connect;
        self.__connected()
        self.setTitleBar(TitleBar(self))
        self.titleBar.raise_()
        

    def __initMidPage(self):
        # msgListPage
        self.msgListPage = MsgListPage()
        self.midLayout.addWidgetByKey("MsgListPage", self.msgListPage)
        
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
        self.toolPage.clickedFriendsBtn.connect(self.onClickedFriendsBtn)
        

    def onClickedAddBtn(self):
        # self.titleBar.raise_()
        self.rightLayout.setCurrentWidgetByKey("AddFriendsPage")
        # self.setTitleBar(TitleBar(self))
        self.titleBar.raise_()
    # 切换到申请列表
    def onClickedFriendsBtn(self):
        self.rightLayout.setCurrentWidgetByKey("DoApplyFriendsPage")
        self.doApplyFriendsPage.requestGetApplyList()
        self.titleBar.raise_() 
