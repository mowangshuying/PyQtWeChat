from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from qfluentwidgets import *

class CreateGroupListItem(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent = parent)

        self.username = ""
        self.userid = -1

        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setSpacing(0)
        self.hMainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.hMainLayout)
        
        self.headimgLabel = ImageLabel()
        self.headimgLabel.setFixedSize(30, 30)
        self.radiobutton = RadioButton()

        self.infoLabel = BodyLabel()

        self.hMainLayout.addWidget(self.headimgLabel)
        self.hMainLayout.addSpacing(10)
        self.hMainLayout.addWidget(self.infoLabel)
        self.hMainLayout.addStretch()
        self.hMainLayout.addWidget(self.radiobutton)


    def setInfo(self, headimg, username, userid):

        self.username = username
        self.userid = userid

        headimg = headimg.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.headimgLabel.setFixedSize(30, 30)
        self.headimgLabel.setPixmap(headimg)
        self.infoLabel.setText(username + "(" + str(userid) + ")")

    def getUsername(self):
        return self.username
    
    def getUserid(self):
        return self.userid

    def setRadioButonVisiable(self, visiable):
        if visiable:
            self.radiobutton.show()
        else:
            self.radiobutton.hide()
    
    

