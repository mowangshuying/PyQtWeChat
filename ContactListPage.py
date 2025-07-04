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
from ContactListItem import ContactListItem
from qfluentwidgets import *

@singleton
class ContactListPage(QWidget):
    
    clickedAddBtn = pyqtSignal()
    clickedCreateBtn = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__netClientUtils = NetClientUtils()
        self.__users = Users()
        
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
        self.vMainLayout.addWidget(self.list)
        self.setFixedWidth(255)
        
        
        
        # 处理事件
        self.addBtn.clicked.connect(self.onAddBtnClicked)
    
    def add(self, headimg, username):
        item = ContactListItem()
        item.setHeadImg(headimg)
        item.setName(username)
        
        listItem = QListWidgetItem(self.list)
        listItem.setSizeHint(QSize(200, 65))
        self.list.addItem(listItem)
        self.list.setItemWidget(listItem, item)
        
    def onAddBtnClicked(self):
        geom = self.addBtn.geometry()
        gp = self.mapToGlobal(geom.topLeft())
        gp.setY(self.addBtn.height() + gp.y())
        
        menu = RoundMenu(parent=self)
        menu.addAction(Action("添加好友/群聊", triggered=lambda: self.clickedAddBtn.emit()))
        menu.addAction(Action("新建群组", triggered=lambda: self.clickedCreateBtn.emit()))
        menu.exec(gp)
        
    def requestGetFriendList(self):
        dataJson = {"ownerid": self.__users.getId()}
        self.__netClientUtils.request(MsgCmd.getFriendList, dataJson, self.responseGetFriendList)
        
    def responseGetFriendList(self, msg):
        self.list.clear()
        for item in msg["data"]:
            friendname = item["friendusername"]
            self.add(QPixmap(), friendname)
            