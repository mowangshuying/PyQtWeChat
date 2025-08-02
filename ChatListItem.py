from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from Def import *
from qfluentwidgets import *
import sys

class ChatListItem(QWidget):
    def __init__(self, role, parent=None):
        super().__init__(parent)
        
        self.role = role
        self.nameLabel = BodyLabel("just a label")
        self.nameLabel.setObjectName("nameLabel")
        self.nameLabel.setFixedHeight(15)
        
        self.iconLabel = ImageLabel("./_rc/img/head_1.jpg")
        self.iconLabel.setFixedSize(40, 40)
        self.bubble = QWidget()
        self.vGridLayout = QGridLayout()
        self.vGridLayout.setVerticalSpacing(3)
        self.vGridLayout.setHorizontalSpacing(3)
        
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        if self.role == ChatRole.Self:
            self.nameLabel.setContentsMargins(0, 0, 8, 0)
            self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.vGridLayout.addWidget(self.nameLabel, 0, 1, 1, 1)
            self.vGridLayout.addWidget(self.iconLabel, 0, 2, 2, 1, Qt.AlignmentFlag.AlignTop)
            self.vGridLayout.addItem(self.spacer, 1, 0, 1, 1)
            self.vGridLayout.addWidget(self.bubble, 1, 1, 1, 1, Qt.AlignmentFlag.AlignRight)
            self.vGridLayout.setColumnStretch(0, 1)
            self.vGridLayout.setColumnStretch(1, 5)
            
        if self.role == ChatRole.Other:
            self.nameLabel.setContentsMargins(8, 0, 0, 0)
            self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.vGridLayout.addWidget(self.iconLabel, 0, 0, 2, 1, Qt.AlignmentFlag.AlignTop)
            self.vGridLayout.addWidget(self.nameLabel, 0, 1, 1, 1)
            self.vGridLayout.addWidget(self.bubble, 1, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)
            self.vGridLayout.addItem(self.spacer, 2, 2, 1, 1)
            self.vGridLayout.setColumnStretch(1, 5)
            self.vGridLayout.setColumnStretch(2, 1)
            
        self.setLayout(self.vGridLayout)
        
    def setUserName(self, name):
        self.nameLabel.setText(name)
        
    def setUserIcon(self, icon):
        self.iconLabel.setPixmap(icon)
        self.iconLabel.setFixedSize(40, 40)
        
    def setBubble(self, bubble):
        self.vGridLayout.replaceWidget(self.bubble, bubble)
        self.bubble.deleteLater()
        self.bubble = bubble
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ChatListItem(ChatRole.Self)
    w.show()
    app.exec()
        
        