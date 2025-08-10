from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from qfluentwidgets import *
from VSplit import VSplit
from sigleton import singleton
from ListWidgetEx import ListWidgetEx
from CreateGroupListItem import CreateGroupListItem

from Data import *
from NetClientUtils import *
from Base64Utils import *

@singleton
class CreateGroupPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)

        self.__netClientUtils = NetClientUtils()
        self.__users = Users()
        self.__base64Utils = Base64Utils()

        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)


        # topwidget
        self.topWidget = QWidget()
        self.topWidget.setContentsMargins(0, 0, 0, 0)
        self.topWidget.setFixedHeight(65)
        self.hTopLayout = QHBoxLayout()
        self.topWidget.setLayout(self.hTopLayout)

        self.titleLabel = CaptionLabel()
        self.titleLabel.setText("创建群组")
        self.hTopLayout.addWidget(self.titleLabel)

        self.sp1 = VSplit(self)

        self.bottomWidget = QWidget()
        # self.bottomWidget.setFixedWidth(640)
        self.hBottomLayout = QHBoxLayout()
        self.hBottomLayout.setContentsMargins(35, 35, 35, 35)
        self.hBottomLayout.setSpacing(0)
        self.bottomWidget.setLayout(self.hBottomLayout)


        self.vLeftLayout = QVBoxLayout()
        self.searchEdit = LineEdit()
        self.searchEdit.setFixedHeight(30)
        self.searchEdit.setFixedWidth(240)
        self.searchEdit.setPlaceholderText("输入查找关键字")
        self.rawList = ListWidgetEx()

        self.vLeftLayout.addWidget(self.searchEdit)
        self.vLeftLayout.addSpacing(40)
        self.vLeftLayout.addWidget(self.rawList)
        self.vLeftLayout.addSpacing(35)

        self.groupNameEdit = LineEdit()
        self.groupNameEdit.setFixedHeight(30)
        self.groupNameEdit.setFixedWidth(240)
        self.groupNameEdit.setPlaceholderText("输入群组名称")

        self.hasSelLabel = CaptionLabel()
        self.hasSelLabel.setFixedHeight(30)
        self.hasSelLabel.setFixedWidth(240)
        self.hasSelLabel.setText("已选联系人:0")
        self.destlist = ListWidgetEx()
        # self.groupNameEdit = LineEdit()
        
        self.hButtonLayout = QHBoxLayout()
        self.confirmBtn = PushButton("确定")
        self.confirmBtn.setFixedHeight(30)
        self.hButtonLayout.addStretch()
        self.hButtonLayout.addWidget(self.confirmBtn)

        self.vRightLayout = QVBoxLayout()

        self.vRightLayout.addWidget(self.groupNameEdit)
        self.vRightLayout.addSpacing(5)
        self.vRightLayout.addWidget(self.hasSelLabel)
        self.vRightLayout.addSpacing(5)
        self.vRightLayout.addWidget(self.destlist)
        self.vRightLayout.addSpacing(5)
        self.vRightLayout.addLayout(self.hButtonLayout)

        self.hBottomLayout.addLayout(self.vLeftLayout)
        self.hBottomLayout.addSpacing(15)
        self.hBottomLayout.addLayout(self.vRightLayout)

        self.vMainLayout.addWidget(self.topWidget)
        self.vMainLayout.addWidget(self.sp1)
        self.vMainLayout.addWidget(self.bottomWidget)


    def add(self, userid, username, bRadio):
        item = CreateGroupListItem()

        pixmap = self.__base64Utils.base64StringToPixmap(self.__users.getHeadImgById(userid))
        item.setInfo(pixmap, username, userid)
        item.setRadioButonVisiable(bRadio)

        listitem = QListWidgetItem(self.rawList)
        listitem.setSizeHint(QSize(200, 40))


        if bRadio:
            self.rawList.addItem(listitem)
            self.rawList.setItemWidget(listitem, item)
        else:
            self.destlist.addItem(listitem)
            self.destlist.setItemWidget(listitem, item)

    def has(self, userid, bRadio):

        if bRadio:
            for i in range(self.rawList.count()):
                item = self.list.itemWidget(self.list.item(i))
                if item.getUserid() == userid:
                    return True
                
        else:
            for i in range(self.destlist.count()):
                item = self.list.itemWidget(self.list.item(i))
                if item.getUserid() == userid:
                    return True

        return False 

    def _del(self, userid, bRadio):
        if bRadio:
            for i in range(self.rawList.count()):
                item = self.rawList.itemWidget(self.rawList.item(i))
                if item.getUserid() == userid:
                    self.rawList.takeItem(i)
                    break
        else:
            for i in range(self.destlist.count()):
                item = self.destlist.itemWidget(self.destlist.item(i))
                if item.getUserid() == userid:
                    self.destlist.takeItem(i)
                    break


    def clear(self):
        self.rawList.clear()
        self.destlist.clear()

        self.searchEdit.clear()
        self.groupNameEdit.clear()
        
        # 所有联系人都要显示在rawlist中;
        for user in self.__users.list:
            self.add(user.userid, user.username, True)
