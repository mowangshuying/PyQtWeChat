from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from AddFriendsPageTop import AddFriendsPageTop
from FlowLayout import FlowLayout
from VSplit import VSplit
from FriendCard import FriendCard

from StyleSheetUtils import StyleSheetUtils

class AddFriendsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)

        self.addFriendsPageTop = AddFriendsPageTop(self)
        self.addFriendsPageTop.setTitle("搜索好友/添加好友")
        self.vMainLayout.addWidget(self.addFriendsPageTop)

        self.sp = VSplit()
        self.vMainLayout.addWidget(self.sp)

        self.searchEdit = QLineEdit()
        self.searchEdit.setObjectName("searchEdit")
        self.searchEdit.setFixedSize(360, 30)
        self.searchEdit.setPlaceholderText("搜索")

        self.searchBtn = QPushButton()
        self.searchBtn.setObjectName("searchBtn")
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
        self.container.setLayout(self.flowLayout)
        self.vMainLayout.addWidget(self.container)

        StyleSheetUtils.setQssByFileName("./_rc/qss/AddFriendsPage.qss", self)

    def addCard(self, card):
        self.flowLayout.addWidget(card)

    def getMinBtn(self):
        return self.addFriendsPageTop.getMinBtn()
    
    def getMaxBtn(self):
        return self.addFriendsPageTop.getMaxBtn()
    
    def getCloseBtn(self):
        return self.addFriendsPageTop.getCloseBtn()

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)


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