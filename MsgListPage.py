from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from VSplit import VSplit
from StyleSheetUtils import StyleSheetUtils
# from SelectPage import SelectPage
from qfluentwidgets import *
from ListWidgetEx import ListWidgetEx
from sigleton import singleton
from NetClientUtils import NetClientUtils
from MsgListItem import *
from MsgListFriendItem import *
from Data import *
from Msg import *
from Base64Utils import Base64Utils

@singleton
class MsgListPage(QWidget):
    
    clickedAddBtn = pyqtSignal()
    clickedCreateBtn = pyqtSignal()
    clickedListItem = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__netClientUtils = NetClientUtils()
        self.__users = Users()
        self.__base64Utils = Base64Utils()
        
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
        self.__connected()
    
    
    def __connected(self):
        self.list.itemClicked.connect(self.__onClickedListItem)
    
    def onAddBtnClicked(self):
        geom = self.addBtn.geometry()
        gp = self.mapToGlobal(geom.topLeft())
        gp.setY(self.addBtn.height() + gp.y())
        
        menu = RoundMenu(parent=self)
        menu.addAction(Action("添加好友/群聊", triggered=lambda: self.clickedAddBtn.emit()))
        menu.addAction(Action("新建群组", triggered=lambda: self.clickedCreateBtn.emit()))
        menu.exec(gp)
        
    def addMsg(self, headimg, name, msg):
        for i in range(self.list.count()):
            widget = self.list.itemWidget(self.list.item(i))
            if widget.getItemType() == MsgListItemType.Friend or widget.getItemType() == MsgListItemType.Group:
                if widget.getName() == name:
                    return
        
        names = []
        # 遍历获取所有name
        for i in range(self.list.count()):
            widget = self.list.itemWidget(self.list.item(i))
            names.append(widget.getName())
            
        names.append(name)
        
        names.sort()
        
        index = names.index(name)
            
        item = MsgListFriendItem()
        item.setHeadImg(headimg)
        item.setName(name)
        item.setMsgText(msg)
        item.setItemType(MsgListItemType.Friend)
        
        
        listItem = QListWidgetItem()
        listItem.setSizeHint(QSize(200, 65))
        self.list.insertItem(index, listItem)
        self.list.setItemWidget(listItem, item)
        
        
        
    
    def setCurrentItemByKey(self, key):
        # 遍历查找到name == key的item
        for i in range(self.list.count()):
            listItem = self.list.item(i)
            widget = self.list.itemWidget(listItem)
            if widget.getName() == key:
                self.list.setCurrentItem(listItem)
                return
    
    def __onClickedListItem(self, item):
        widget = self.list.itemWidget(item)
        if widget == None:
            return
        
        self.clickedListItem.emit(widget.getName())
        
        
        
    def requestSessionList(self):
        data = {"ownerid": self.__users.getId()}
        self.__netClientUtils.request(MsgCmd.getSessionList, data, self.__responseGetSessionList)
    
    def __responseGetSessionList(self, msg):
        for item in msg["data"]:
            if item["type"] == MsgListItemType.Friend or item["type"] == MsgListItemType.Group:
                if item["ownerid"] == self.__users.getId():
                    headimg = self.__base64Utils.base64StringToPixmap(item["friend"]["headimg"])
                    username = item["friend"]["username"]
                    msgText = item["msg"]
                    self.addMsg(headimg, username, msgText)
                    continue
                
                if item["friendid"] == self.__users.getId():
                    headimg = self.__base64Utils.base64StringToPixmap(item["owner"]["headimg"])
                    username = item["owner"]["username"]
                    msgText = item["msg"]
                    self.addMsg(headimg, username, msgText)
                    continue
        
        