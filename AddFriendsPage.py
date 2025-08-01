from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

# from FlowLayout import FlowLayout
from VSplit import VSplit
from FriendCard import FriendCard

from StyleSheetUtils import StyleSheetUtils
from NetClientUtils import NetClientUtils
from Msg import MsgCmd, MsgState, MsgType
from Data import *

from qfluentwidgets import *
from FlowLayout import FlowLayout
from Base64Utils import Base64Utils

class AddFriendsPage(QWidget):
    
    clickedSearchBtn = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
    
        self.__users = Users()
        self.__base64Utils = Base64Utils()
        
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)
        
        self.vMainLayout.addSpacing(65)
        self.sp = VSplit()
        self.vMainLayout.addWidget(self.sp)

        self.searchEdit = LineEdit()
        # self.searchEdit.setObjectName("searchEdit")
        self.searchEdit.setFixedSize(360, 30)
        self.searchEdit.setPlaceholderText("搜索")

        self.searchBtn = PushButton()
        # self.searchBtn.setObjectName("searchBtn")
        self.searchBtn.setText("搜索")
        self.searchBtn.setFixedSize(80, 30)

        self.hSearchLayout = QHBoxLayout()
        self.hSearchLayout.addSpacing(30)
        self.hSearchLayout.addWidget(self.searchEdit)
        self.hSearchLayout.addSpacing(15)
        self.hSearchLayout.addWidget(self.searchBtn)
        self.hSearchLayout.addStretch(1)
        self.vMainLayout.addSpacing(30)
        self.vMainLayout.addLayout(self.hSearchLayout)


        self.container = QWidget()
        self.flowLayout = FlowLayout(self.container)
        self.flowLayout.setContentsMargins(30, 20, 30, 20)
        self.container.setLayout(self.flowLayout)
        self.vMainLayout.addWidget(self.container)

        self.__netClientUtils = NetClientUtils()
        
        self.searchBtn.clicked.connect(self.onClicedSearchBtn)
        # StyleSheetUtils.setQssByFileName("./_rc/qss/AddFriendsPage.qss", self)

    def addCard(self, item):

        # 遍历flowLayout
        for i in range(self.flowLayout.count()):
            curWidget = self.flowLayout.itemAt(i)
            if curWidget.widget().getUserName() == item["username"]:
                return
            
        card = FriendCard()        
        card.setUserName(item["username"])
        card.setImg(self.__base64Utils.base64StringToPixmap(item["headimg"]))
        
                    
        self.flowLayout.addWidget(card)
        self.__users.addDetail(-1, item["userid"], item["username"], "", item["headimg"], 0, 0, 0)
    
    def onClicedSearchBtn(self):
        # get Text from searchEdit
        text = self.searchEdit.text()
        data = {"str":text}
        self.__netClientUtils.request(MsgCmd.findUser, data, self.responseFindUser)
        
    def responseFindUser(self, msg):
        if msg["state"] == MsgState.ok:
            
            # 清空当前的所有元素
            self.vMainLayout.removeWidget(self.container)
            self.container.deleteLater()
            
            self.container = QWidget()
            self.flowLayout = FlowLayout(self.container)
            self.flowLayout.setContentsMargins(30, 20, 30, 20)
            self.container.setLayout(self.flowLayout)
            self.vMainLayout.addWidget(self.container)
            
            
            # 返回回来的data是一个数组
            # 判断是否含有data字段
            if "data" not in msg:
                return
            
            data = msg["data"]
            # 遍历数组添加元素
            for item in data:
                self.addCard(item)


if __name__ == "__main__":
    app = QApplication([])
    w = AddFriendsPage()
    w.resize(1200, 800)

    # add freiend card;
    for i in range(10):
        card = FriendCard()
        card.setNameAndImg("user" + str(i), QPixmap("./_rc/img/headImg.png"))
        w.addCard(card)

    w.show()
    app.exec()