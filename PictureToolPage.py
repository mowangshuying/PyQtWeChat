from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from VSplit import *
from qfluentwidgets import *

from NetClientUtils import *
from Base64Utils import *
from Data import *

class PictureToolPage(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.picture = None
        self.__netClientUtils = NetClientUtils()
        self.__base64Utils = Base64Utils()
        self.__users = Users()
        
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)
        
        self.vMainLayout.addSpacing(65)
        self.sp = VSplit(self)
        self.vMainLayout.addWidget(self.sp)
        
        self.container = QWidget()
        self.container.setFixedSize(300, 300)
        self.vContainerLayout = QVBoxLayout()
        self.container.setLayout(self.vContainerLayout)
        
        self.picLabel = QLabel()
        self.picLabel.setFixedSize(250, 250)
        # self.vMainLayout.addWidget(self.picLabel, 0, Qt.AlignmentFlag.AlignCenter)
        self.vContainerLayout.addWidget(self.picLabel)
        
        self.hBtnLayout = QHBoxLayout()
        self.uploadBtn = PushButton("上传图片")
        self.cancelBtn = PushButton("取消")
        self.determineBtn = PushButton("确定")
        
        self.hBtnLayout.addWidget(self.uploadBtn)
        self.hBtnLayout.addWidget(self.cancelBtn)
        self.hBtnLayout.addWidget(self.determineBtn)
        # self.vMainLayout.addLayout(self.hBtnLayout)
        self.vContainerLayout.addLayout(self.hBtnLayout)
        
        self.vMainLayout.addWidget(self.container, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.__connected()
        
        
    def __connected(self):
        self.uploadBtn.clicked.connect(self.onClickedUploadBtn)
        self.cancelBtn.clicked.connect(self.onClickedCancelBtn)
        self.determineBtn.clicked.connect(self.onClickedDetermineBtn)
        
    def onClickedUploadBtn(self):
        path = QFileDialog.getOpenFileName(self, "选择图片", "", "*.png *.jpg *.jpeg *.bmp")
        
        picture = QPixmap(path[0])
        picture = picture.scaled(250, 250)
        self.picture = picture
        self.picLabel.setPixmap(picture)
    
    def onClickedCancelBtn(self):
        self.close()
        
    def onClickedDetermineBtn(self):
        if self.picture == None:
            return
        
        base64Str = self.__base64Utils.pixmapToBase64String(self.picture)
        
        data = {"userid" : self.__users.getId(), "headimg" : base64Str}
        self.__netClientUtils.request(MsgCmd.changeHeadImg, data, self.__onResponseChangeHeadImg)
        
    def __onResponseChangeHeadImg(self, msg):
        if msg["state"] == MsgState.ok:
            print("Change head img ok.")
        