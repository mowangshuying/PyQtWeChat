from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

from sigleton import singleton
from VSplit import VSplit
from qfluentwidgets import *
from StyleSheetUtils import StyleSheetUtils

from Data import *
from Base64Utils import Base64Utils

class UserInfoPage(QWidget):
    clickedChangeHeadImgBtn = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__users = Users()
        self.__base64Utils = Base64Utils()
        
        self.vMainLayout = QVBoxLayout()
        self.setLayout(self.vMainLayout)
        
        self.container = QWidget()
        self.container.setObjectName("container")
        self.vMainLayout.addWidget(self.container)
        
        self.setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        # 设置为pop属性
        # self.setWindowFlag(Qt.WindowType.Popup)
        
        self.setFixedSize(280, 190)
        
        self.vContainerLayout = QVBoxLayout()
        self.container.setLayout(self.vContainerLayout)
        self.vContainerLayout.addSpacing(25)
        
        self.hTopLayout = QHBoxLayout()
        self.vInfoLayout = QVBoxLayout()
        
        ft = QFont()
        ft.setPointSize(15)
        
        self.nameLabel = BodyLabel()
        self.userIdLabel = BodyLabel()
        
        self.nameLabel.setText("用户名:" + self.__users.getNameById(self.__users.getId()))
        self.userIdLabel.setText("用户ID:" + str(self.__users.getId()))
        
        self.vInfoLayout.addWidget(self.nameLabel, 0, Qt.AlignmentFlag.AlignLeft)
        self.vInfoLayout.addWidget(self.userIdLabel, 0, Qt.AlignmentFlag.AlignLeft)
        self.vInfoLayout.addStretch()
        
        # self.headLabel = ImageLabel("./_rc/img/head_2.jpg")
        self.headLabel = ImageLabel(self.__base64Utils.base64StringToPixmap(self.__users.getHeadImgById(self.__users.getId())))
        self.headLabel.setFixedSize(60, 60)
        
        self.changeHeadImgBtn = PrimaryPushButton("修改头像")
        self.changeHeadImgBtn.setFixedSize(120, 40)
        
        self.hTopLayout.addWidget(self.headLabel)
        self.hTopLayout.addLayout(self.vInfoLayout)
        self.vContainerLayout.addLayout(self.hTopLayout)
        
        self.vContainerLayout.addSpacing(10)
        self.vSp = VSplit()
        self.vContainerLayout.addWidget(self.vSp)
        
        self.hBtnLayout = QHBoxLayout()
        self.hBtnLayout.addWidget(self.changeHeadImgBtn, Qt.AlignmentFlag.AlignCenter)
        self.vContainerLayout.addSpacing(15)
        self.vContainerLayout.addLayout(self.hBtnLayout)
        self.vContainerLayout.addStretch()
        
        #connect
        self.changeHeadImgBtn.clicked.connect(self.onClickedChangeHeadImgBtn)
        
        StyleSheetUtils.setQssByFileName("./_rc/qss/UserInfoPage.qss", self)
        self.hide()
        
    def onClickedChangeHeadImgBtn(self):
        self.clickedChangeHeadImgBtn.emit()
        