from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from StyleSheetUtils import StyleSheetUtils

# from MainPage import MainPage
class SelectPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(5, 5, 5, 5)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)
        
        self.add = QPushButton("添加好友/群聊")
        self.create = QPushButton("创建群聊")
        
        self.vMainLayout.addWidget(self.add)
        self.vMainLayout.addWidget(self.create)
         
        # self.setWindowFlags(Qt.WindowType.Popup)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Popup)
        StyleSheetUtils.setQssByFileName("./_rc/qss/SelectPage.qss", self)
        
    # def event(self, a0):
    #     if a0.type() == QEvent.Type.ActionChanged:
    #         self.close()
    #     return super().event(a0)
    
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)    