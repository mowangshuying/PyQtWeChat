from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from VSplit import VSplit
from StyleSheetUtils import StyleSheetUtils
from NetClientUtils import NetClientUtils
from Msg import *
from Data import *
from ListWidgetEx import ListWidgetEx
from StyleSheetUtils import StyleSheetUtils
from sigleton import *
from ContactListItem import *
from ContactListFriendItem import ContactListFriendItem
from ContactListTipItem import ContactListTipItem
from qfluentwidgets import *
from SyncEvent import *

@singleton
class ContactListPage(QWidget):
    
    clickedAddBtn = pyqtSignal()
    clickedCreateBtn = pyqtSignal()
    clickedListItem = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__netClientUtils = NetClientUtils()
        self.__users = Users()
        self.__syncEvent = SyncEvent()
        
        self.vMainLayout = QVBoxLayout()
        self.setLayout(self.vMainLayout)
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setMouseTracking(True)
        
        self.hTopLayout = QHBoxLayout()
        self.hTopLayout.setContentsMargins(0, 0, 0, 0)
        self.hTopLayout.setSpacing(0)
        
        self.searchEdit = LineEdit()
        self.addBtn = PrimaryToolButton()
        self.searchEdit.setFixedHeight(25)
        self.addBtn.setIconSize(QSize(20, 20))
        self.addBtn.setFixedSize(25, 25)
        self.addBtn.setIcon(FluentIcon.ADD)
        
        self.hTopLayout.addSpacing(10)
        self.hTopLayout.addWidget(self.searchEdit)
        self.hTopLayout.addSpacing(10)
        self.hTopLayout.addWidget(self.addBtn)
        self.hTopLayout.addSpacing(10)
        
        self.vMainLayout.addSpacing(25)
        self.vMainLayout.addLayout(self.hTopLayout)
        self.vMainLayout.addSpacing(15)
        
        self.sp = VSplit()
        self.vMainLayout.addWidget(self.sp)
        
        self.list = ListWidgetEx()
        self.list.setFixedWidth(255)
        self.list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        ## 初始化列表
        self.__initList()
        self.__connected()
        
        self.vMainLayout.addWidget(self.list)
        self.setFixedWidth(255)
        
        
        
        # 处理事件
        self.addBtn.clicked.connect(self.onAddBtnClicked)
    
    def __initList(self):
        self.addNewFriend(QPixmap("./_rc/img/add_friend.png"), "新的朋友")
        self.addTip("联系人")
        self.addTip("群组")
        self.requestGetFriendList()
        
    def __connected(self):
        self.list.itemClicked.connect(self.__onClickedListItem)
        
    def addTip(self, tip):
        item = ContactListTipItem()
        item.setTip(tip)
        
        listItem = QListWidgetItem(self.list)
        listItem.setSizeHint(QSize(200, 30))
        
        self.list.addItem(listItem)
        self.list.setItemWidget(listItem, item)
        # listItem.setFlags(listItem.flags() & (~Qt.ItemFlag.ItemIsSelectable))    
    
    def addNewFriend(self, headimg, username):
        item = ContactListFriendItem()
        item.setHeadImg(headimg)
        item.setName(username)
        
        listItem = QListWidgetItem(self.list)
        listItem.setSizeHint(QSize(200, 65))
        
        self.list.insertItem(0, listItem)
        self.list.setItemWidget(listItem, item)        
    
    def addFriend(self, headimg, username):
        item = ContactListFriendItem()
        item.setHeadImg(headimg)
        item.setName(username)
        
        listItem = QListWidgetItem()
        listItem.setSizeHint(QSize(200, 65))
        
        # self.list.addItem(listItem)
        self.list.insertItem(self.getFriendIndex(), listItem)
        self.list.setItemWidget(listItem, item)
        
        
    def getFriendIndex(self):
        # index = 2
        for i in range(self.list.count()):
            item = self.list.item(i)
            widget = self.list.itemWidget(item)
            if widget == None:
                continue
            
            # widget = self.list.itemWidget(item)
            if widget.getItemType() == ContactListItemType.Friend:
                index = i
        if index < 2:
            index = 2
            
        return index
        
    def onAddBtnClicked(self):
        geom = self.addBtn.geometry()
        gp = self.mapToGlobal(geom.topLeft())
        gp.setY(self.addBtn.height() + gp.y())
        
        menu = RoundMenu(parent=self)
        menu.addAction(Action("添加好友/群聊", triggered=lambda: self.clickedAddBtn.emit()))
        menu.addAction(Action("新建群组", triggered=lambda: self.clickedCreateBtn.emit()))
        menu.exec(gp)
        
    def __onClickedListItem(self, item):
        widget = self.list.itemWidget(item)
        if widget == None:
            return
        
        # 点击tip直接忽略
        if widget.getItemType() == ContactListItemType.Tip:
            return
        
        self.clickedListItem.emit(widget.getName())
        
    def requestGetFriendList(self):
        dataJson = {"ownerid": self.__users.getId()}
        self.__netClientUtils.request(MsgCmd.getFriendList, dataJson, self.responseGetFriendList)
        
    def responseGetFriendList(self, msg):
        # self.list.clear()
        for item in msg["data"]:
            friendname = item["friendusername"]
            self.addFriend(QPixmap("./_rc/img/head_2.jpg"), friendname)
        # pass
        # self.__syncEvent.set()
            