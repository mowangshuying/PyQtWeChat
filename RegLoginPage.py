from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from MainPage import MainPage
from StyleSheetUtils import StyleSheetUtils
from NetClientUtils import NetClientUtils
from Msg import *

from NetClientUtils import *

class RegLoginPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setSpacing(0)
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.vMainLayout)
        
        self.top = QWidget()
        self.hTopLayout = QHBoxLayout()
        self.hTopLayout.setSpacing(0)
        self.hTopLayout.setContentsMargins(0, 0, 0, 0)
        self.top.setLayout(self.hTopLayout)
        
        self.title = QLabel()
        self.minBtn = self.makeBtn("./_rc/img/minBtn.png")
        self.closeBtn = self.makeBtn("./_rc/img/closeBtn.png")
        
        self.hTopLayout.addWidget(self.title)
        self.hTopLayout.addStretch()
        self.hTopLayout.addWidget(self.minBtn)
        self.hTopLayout.addWidget(self.closeBtn)
        
        
        self.bottom = QWidget()
        self.bottom.setFixedHeight(200)
        self.vBottomLayout =  QVBoxLayout()
        self.bottom.setLayout(self.vBottomLayout)
        
        self.account = QLineEdit()
        self.account.setFixedSize(256, 36)
        self.account.setPlaceholderText("请输入用户名")
        self.account.setText("")
        
        self.password = QLineEdit()
        self.password.setFixedSize(256, 36)
        self.password.setPlaceholderText("请输入密码")
        self.password.setText("")
        
        self.hBtnLayout = QHBoxLayout()
        self.regOrLogin = QCheckBox("注册")
        self.remmberPassword = QCheckBox("记住密码")
        self.hBtnLayout.addWidget(self.regOrLogin)
        self.hBtnLayout.addStretch()
        self.hBtnLayout.addWidget(self.remmberPassword)
        
        self.btn = QPushButton("登录")
        self.btn.setFixedSize(256, 36)
        
        self.vBottomLayout.addWidget(self.account)
        self.vBottomLayout.addWidget(self.password)
        self.vBottomLayout.addLayout(self.hBtnLayout)
        self.vBottomLayout.addWidget(self.btn)
        # self.vBottomLayout.addSpacing(200)
        
        self.vMainLayout.addWidget(self.top)
        self.vMainLayout.addWidget(self.bottom)
        
        
        self.btn.clicked.connect(self.onBtnClicked)
       
        self.__netClientUtils = NetClientUtils()
                
        self.minBtn.clicked.connect(lambda: self.showMinimized())
        self.closeBtn.clicked.connect(lambda: self.close())
        

        self.pressed = False
        self.pressedPos = None
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        StyleSheetUtils.setQssByFileName("./_rc/qss/RegLoginPage.qss", self)
        
    def makeBtn(self, iconPath):
        btn = QPushButton()
        btn.setIcon(QIcon(QPixmap(iconPath)))
        btn.setIconSize(QSize(20, 20))
        btn.setFixedSize(30, 30)
        return btn
    
    def requesRegUser(self):
        data = {"username": self.account.text(),  "nickname" : self.account.text(), "password": self.password.text(), "sex": 0}
        self.__netClientUtils.request(MsgCmd.regUser, data, lambda msg: print(msg))

    def responseRegUser(self, msg):
        pass
        
    def requestLogin(self):
        self.__netClientUtils.request(MsgCmd.login, {"username": self.account.text(), "password": self.password.text()}, self.responseLogin)
        
    def responseLogin(self, msg):
        if msg["state"] == MsgState.ok:
            mainPage = MainPage()
            mainPage.show()
            self.close()
        
    def onBtnClicked(self):
        if self.regOrLogin.isChecked():
            self.requesRegUser()
        else:
            self.requestLogin()
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.pressed = True
            self.pressedPos = event.pos()


    def mouseMoveEvent(self, event):
        if self.pressed:
            self.move(self.pos() + event.pos() - self.pressedPos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.pressed = False
            event.accept()
        else:
            super().mouseReleaseEvent(event)
        
        