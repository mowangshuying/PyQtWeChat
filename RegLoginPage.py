from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from MainPage import MainPage
from StyleSheetUtils import StyleSheetUtils
from NetClientUtils import NetClientUtils
from Msg import *
from Data import *

from NetClientUtils import *
from qfluentwidgets.components.widgets.frameless_window import FramelessWindow
from qfluentwidgets.components.widgets.button import *
from qfluentwidgets.components.widgets.line_edit import *
from qfluentwidgets.components.widgets.check_box import *

class RegLoginPage(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__users = Users()

        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setSpacing(0)
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.vMainLayout)
        
        self.titleBar.maxBtn.hide()
        
        self.bottom = QWidget()
        self.bottom.setFixedHeight(200)
        self.vBottomLayout =  QVBoxLayout()
        self.bottom.setLayout(self.vBottomLayout)
        
        self.accountEdit = LineEdit()
        self.accountEdit.setFixedSize(256, 36)
        self.accountEdit.setPlaceholderText("请输入用户名")
        self.accountEdit.setText("")
        
        self.passwordEdit = LineEdit()
        self.passwordEdit.setFixedSize(256, 36)
        self.passwordEdit.setPlaceholderText("请输入密码")
        self.passwordEdit.setText("")
        
        self.hBtnLayout = QHBoxLayout()
        self.regOrLogin = CheckBox("注册")
        self.remmberPasswordCheckBox = CheckBox("记住密码")
        self.hBtnLayout.addWidget(self.regOrLogin)
        self.hBtnLayout.addStretch()
        self.hBtnLayout.addWidget(self.remmberPasswordCheckBox)
        
        self.loginBtn = PrimaryPushButton("登录")
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.setFixedSize(256, 36)
        
        self.vBottomLayout.addWidget(self.accountEdit)
        self.vBottomLayout.addWidget(self.passwordEdit)
        self.vBottomLayout.addLayout(self.hBtnLayout)
        self.vBottomLayout.addWidget(self.loginBtn)
        self.vMainLayout.addSpacing(36)
        self.vMainLayout.addWidget(self.bottom)
        
        
        self.loginBtn.clicked.connect(self.onBtnClicked)
       
        self.__netClientUtils = NetClientUtils()
        

        # self.pressed = False
        # self.pressedPos = None
        
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(274, 236)
    
    def requesRegUser(self):
        data = {"username": self.accountEdit.text(),  "nickname" : self.accountEdit.text(), "password": self.passwordEdit.text(), "sex": 0}
        self.__netClientUtils.request(MsgCmd.regUser, data, lambda msg: print(msg))

    def responseRegUser(self, msg):
        pass
        
    def requestLogin(self):
        self.__netClientUtils.request(MsgCmd.login, {"username": self.accountEdit.text(), "password": self.passwordEdit.text()}, self.responseLogin)
        
    def responseLogin(self, msg):
        if msg["state"] == MsgState.ok:
            self.__users.setId(msg["data"]["userid"])
            self.__users.addDetail(-1, msg["data"]["userid"], msg["data"]["username"], "", 0, 0, 0)
            self.deleteLater()
            mainPage = MainPage()
            mainPage.show()
            
        
    def onBtnClicked(self):
        if self.regOrLogin.isChecked():
            self.requesRegUser()
        else:
            self.requestLogin()
        
        