from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from StyleSheetUtils import StyleSheetUtils
from ListWidgetEx import ListWidgetEx
from SesPageToolBar import SesPageToolBar
from VSplit import VSplit

from qfluentwidgets import *
from Def import *
from Data import *
from  ChatListItem import ChatListItem
from TextBubble import TextBubble
from Msg import *

class SesPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__user = Users()

        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.sesType = SesType.Friend

        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)


        self.topwidget = QWidget()
        self.topwidget.setContentsMargins(0, 0, 0, 0)
        self.topwidget.setFixedHeight(65)
        self.hTopLayout = QHBoxLayout()
        self.topwidget.setLayout(self.hTopLayout)

        self.titleLabel = CaptionLabel()
        self.titleLabel.setText("消息列表")
        self.hTopLayout.addWidget(self.titleLabel)

        self.sp1 = VSplit(self)

        self.list = ListWidgetEx(self)
        self.list.setAcceptDrops(False)

        self.sp2 = VSplit(self)

        self.sesPageToolBar = SesPageToolBar(self)

        self.edit = QTextEdit(self)
        self.edit.setAcceptDrops(False)
        self.edit.setAcceptRichText(True)

        self.hBottomLayout = QHBoxLayout()
        self.sendBtn = QPushButton("发送[s]")
        self.sendBtn.setFixedSize(70, 30)

        self.hBottomLayout.addStretch(1)
        self.hBottomLayout.addWidget(self.sendBtn)
        self.hBottomLayout.addSpacing(15)
        
        self.vMainLayout.addWidget(self.topwidget)
        self.vMainLayout.addWidget(self.sp1)
        self.vMainLayout.addWidget(self.list, 2)
        self.vMainLayout.addWidget(self.sp2)
        self.vMainLayout.addWidget(self.sesPageToolBar)
        self.vMainLayout.addWidget(self.edit, 1)
        self.vMainLayout.addLayout(self.hBottomLayout)

        self.sendBtn.clicked.connect(self.onClickedSendBtn)
        StyleSheetUtils.setQssByFileName("./_rc/qss/SesPage.qss", self)

    def setTitle(self, str):
        self.titleLabel.setText(str)
        
    def appendChatMsg(self, msg):
        id = msg["id"]
        ownerid = msg["ownerid"]
        friendid = msg["friendid"]
        msgtype = msg["msgtype"]
        text = msg["msgdata"]
        
        if ownerid == self.__user.getId():
            chatItem = ChatListItem(ChatRole.Self)
            chatItem.setUserName(self.__user.getIdByName(self.__user.getId()))
            chatItem.setUserIcon("./_rc/img/head_2.jpg")
            
            textBubble = TextBubble(ChatRole.Self, text)
            chatItem.setBubble(textBubble)
            
            listItem = QListWidgetItem()
            listItem.setSizeHint(chatItem.sizeHint()) 
            self.list.addItem(listItem)   
            self.list.setItemWidget(listItem, chatItem)
            
        if ownerid == self.__user.getId():
            chatItem = ChatListItem(ChatRole.Other)
            chatItem.setUserName(self.__user.getIdByName(friendid))
            chatItem.setUserIcon("./_rc/img/head_2.jpg")
            
            textBubble = TextBubble(ChatRole.Self, text)
            chatItem.setBubble(textBubble)
            
            listItem = QListWidgetItem()
            listItem.setSizeHint(chatItem.sizeHint()) 
            self.list.addItem(listItem)   
            self.list.setItemWidget(listItem, chatItem)
            
    def onClickedSendBtn(self):
        msgText = self.textEdit.toPlainText()
        if msgText == "":
            return
        
        data = {"ownerid":self.__user.getId(), 
                "friendid":self.__user.getIdByName(self.titleLabel.text()),
                "msgtype":MsgType.text,
                "msgdata":msgText
                }
        
        
        
            


        