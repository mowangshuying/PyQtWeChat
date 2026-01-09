from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

# from FlowLayout import FlowLayout
from VSplit import VSplit
from FindFriendsListItem import FindFriendsListItem

from StyleSheetUtils import StyleSheetUtils
from NetClientUtils import NetClientUtils
from Msg import MsgCmd, MsgState, MsgType
from Data import *

from qfluentwidgets import *
from FlowLayout import FlowLayout
from Base64Utils import Base64Utils
from ListWidgetEx import ListWidgetEx

class AddFriendsPage(QFrame):
    
    clickedSearchBtn = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
    
        self.__users = Users()
        self.__base64Utils = Base64Utils()
        self.__netClientUtils = NetClientUtils()
        
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)
        
        self.vMainLayout.addSpacing(65)
        self.sp = VSplit()
        self.vMainLayout.addWidget(self.sp)

        self.searchEdit = LineEdit()
        self.searchEdit.setFixedSize(360, 30)
        self.searchEdit.setPlaceholderText("搜索")

        self.searchBtn = PushButton()
        self.searchBtn.setText("搜索")
        self.searchBtn.setFixedSize(80, 30)

        self.hSearchLayout = QHBoxLayout()
        self.hSearchLayout.addSpacing(5)
        self.hSearchLayout.addWidget(self.searchEdit)
        self.hSearchLayout.addSpacing(15)
        self.hSearchLayout.addWidget(self.searchBtn)
        self.hSearchLayout.addStretch(1)
        self.vMainLayout.addSpacing(15)
        self.vMainLayout.addLayout(self.hSearchLayout)


        self.list = ListWidgetEx()
        self.vMainLayout.addWidget(self.list)
        self.searchBtn.clicked.connect(self.onClicedSearchBtn)
        
        StyleSheetUtils.setQssByFileName("./_rc/qss/AddFriendsPage.qss", self)

    def add(self, friend):
        # 遍历list
        for i in range(self.list.count()):
            curWidget = self.list.itemWidget(self.list.item(i))
            if curWidget.getUserName() == friend["username"]:
                return
        
        item = FindFriendsListItem()
        item.setNameAndImg(friend["username"], self.__base64Utils.base64StringToPixmap(friend["headimg"]))
        
        listItem = QListWidgetItem(self.list)
        listItem.setSizeHint(QSize(200, 40))
        self.list.addItem(listItem)
        self.list.setItemWidget(listItem, item)
        
        self.__users.addDetail(friend["id"], friend["userid"], friend["username"], friend["nickname"], 
                    friend["headimg"], friend["sex"], friend["state"], friend["create_date"])

    
    def onClicedSearchBtn(self):
        # get Text from searchEdit
        text = self.searchEdit.text()
        data = {"str":text}
        self.__netClientUtils.request(MsgCmd.findUser, data, self.responseFindUser)
        
    def responseFindUser(self, msg):
        if msg["state"] == MsgState.ok:
            
            # 清空当前的所有元素
            self.vMainLayout.removeWidget(self.list)
            self.list.deleteLater()
            
            self.list = ListWidgetEx()
            self.vMainLayout.addWidget(self.list)
            
            # 返回回来的data是一个数组, 判断是否含有data字段
            if "data" not in msg:
                return
            
            data = msg["data"]
            # 遍历数组添加元素
            for friend in data:
                self.add(friend)