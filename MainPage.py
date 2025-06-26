# import QWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout
from ToolPage import ToolPage
from PyQt5.QtGui import QIcon
from MsgListPage import MsgListPage
from HSplit import HSplit
# res
from _rc.res import *

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowIcon(QIcon("./_rc/img/app.ico"))
        
        
        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setSpacing(0)
        self.hMainLayout.setContentsMargins(0, 0, 0, 0)
        
        # left;
        self.toolPage = ToolPage(self)
        self.hMainLayout.addWidget(self.toolPage)
        
        # mid;
        self.midPage = MsgListPage()
        self.hMainLayout.addWidget(self.midPage)
        
        # sp
        self.sp = HSplit()
        self.hMainLayout.addWidget(self.sp)
        
        self.hMainLayout.addStretch(1)
        
        self.setLayout(self.hMainLayout)
        self.resize(800, 600)