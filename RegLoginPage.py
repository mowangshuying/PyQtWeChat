from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from MainPage import MainPage
from StyleSheetUtils import StyleSheetUtils
from NetClientUtils import NetClientUtils
from Msg import *
from Data import *

from NetClientUtils import *

class RegLoginPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__dataMgr = DataMgr()
        
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setSpacing(0)
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.vMainLayout)
        
        self.top = QWidget()
        self.hTopLayout = QHBoxLayout()
        self.hTopLayout.setSpacing(0)
        self.hTopLayout.setContentsMargins(0, 0, 0, 0)
        self.top.setLayout(self.hTopLayout)
        
        self.titleLabel = QLabel()
        self.titleLabel.setObjectName("titleLabel")
        self.minBtn = self.makeBtn("./_rc/img/minBtn.png")
        self.minBtn.setObjectName("minBtn")
        self.closeBtn = self.makeBtn("./_rc/img/closeBtn.png")
        self.closeBtn.setObjectName("closeBtn")
        
        self.hTopLayout.addWidget(self.titleLabel)
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
        
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setFixedSize(256, 36)
        self.passwordEdit.setPlaceholderText("请输入密码")
        self.passwordEdit.setText("")
        
        self.hBtnLayout = QHBoxLayout()
        self.regOrLogin = QCheckBox("注册")
        self.remmberPasswordCheckBox = QCheckBox("记住密码")
        self.hBtnLayout.addWidget(self.regOrLogin)
        self.hBtnLayout.addStretch()
        self.hBtnLayout.addWidget(self.remmberPasswordCheckBox)
        
        self.loginBtn = QPushButton("登录")
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.setFixedSize(256, 36)
        
        self.vBottomLayout.addWidget(self.account)
        self.vBottomLayout.addWidget(self.passwordEdit)
        self.vBottomLayout.addLayout(self.hBtnLayout)
        self.vBottomLayout.addWidget(self.loginBtn)
        # self.vBottomLayout.addSpacing(200)
        
        self.vMainLayout.addWidget(self.top)
        self.vMainLayout.addWidget(self.bottom)
        
        
        self.loginBtn.clicked.connect(self.onBtnClicked)
       
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
        data = {"username": self.account.text(),  "nickname" : self.account.text(), "password": self.passwordEdit.text(), "sex": 0}
        self.__netClientUtils.request(MsgCmd.regUser, data, lambda msg: print(msg))

    def responseRegUser(self, msg):
        pass
        
    def requestLogin(self):
        self.__netClientUtils.request(MsgCmd.login, {"username": self.account.text(), "password": self.passwordEdit.text()}, self.responseLogin)
        
    def responseLogin(self, msg):
        if msg["state"] == MsgState.ok:
            
            self.__dataMgr.setId(msg["data"]["userid"])
            data = Data(msg["data"]["userid"], msg["data"]["username"], "")
            self.__dataMgr.addData(data)
            
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
            
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)
        
        