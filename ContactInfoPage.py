from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from qfluentwidgets import *
import sys

from VSplit import VSplit

class ContactInfoPage(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        
        self.setLayout(self.vMainLayout)
        
        self.vMainLayout.addSpacing(65)
        
        self.vSp1 = VSplit()
        self.vMainLayout.addWidget(self.vSp1)
        
        self.vMainLayout.addSpacing(60)
        
        
        
        # bottomWidget
        self.bottomWidget = QWidget()
        self.vBottomLayout = QVBoxLayout()
        self.vBottomLayout.setContentsMargins(0, 0, 0, 0)
        self.vBottomLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.vBottomLayout.setSpacing(0)
        self.bottomWidget.setLayout(self.vBottomLayout)
        
        self.vMainLayout.addWidget(self.bottomWidget)
        
        #  wrap widget
        self.wrapWidget = QWidget()
        # self.wrapWidget.setStyleSheet("background-color: pink;")
        self.wrapWidget.setFixedSize(380, 115)
        # self.vMainLayout.addWidget(self.wrapWidget, 1)
        self.vBottomLayout.addWidget(self.wrapWidget)
        
        self.vWrapWidgetLayout = QVBoxLayout()
        self.vWrapWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.vWrapWidgetLayout.setSpacing(0)
        self.wrapWidget.setLayout(self.vWrapWidgetLayout)
        
        self.imageLabel = ImageLabel("./_rc/img/head_2.jpg")
        self.imageLabel.setFixedSize(62, 62)
        
        self.userunameLabel = StrongBodyLabel("****用户名****")
        self.useridLabel = BodyLabel("****用户id****")
        
        self.hLayout1 = QHBoxLayout()
        self.hLayout1.setContentsMargins(0, 0, 0, 0)
        self.hLayout1.setSpacing(0)
        self.hLayout1.addWidget(self.imageLabel)
        
        self.hLayout1.addSpacing(15)
        
        self.vLayout1 = QVBoxLayout()
        self.vLayout1.addWidget(self.userunameLabel)
        self.vLayout1.addSpacing(10)
        self.vLayout1.addWidget(self.useridLabel)
        self.vLayout1.addStretch()
        
        self.hLayout1.addLayout(self.vLayout1)
        
        self.vWrapWidgetLayout.addLayout(self.hLayout1)
        
        self.vSp2 = VSplit()
        self.vWrapWidgetLayout.addWidget(self.vSp2)
        
        self.hLayout2 = QHBoxLayout()
        
        self.sendMsgBtn = TransparentPushButton("发消息")
        self.voiceBtn = TransparentPushButton("语音聊天")
        self.videoBtn = TransparentPushButton("视频聊天")
        
        self.hLayout2.addWidget(self.sendMsgBtn)
        self.hLayout2.addWidget(self.voiceBtn)
        self.hLayout2.addWidget(self.videoBtn)
        
        self.vWrapWidgetLayout.addSpacing(15)
        self.vWrapWidgetLayout.addLayout(self.hLayout2)
        
        
        self.resize(800, 600)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ContactInfoPage()
    widget.show()
    app.exec()