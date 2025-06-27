from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from StyleSheetUtils import StyleSheetUtils

# from MainPage import MainPage
class SelectPage(QWidget):
    
    clickedAddBtn = pyqtSignal()
    clickedCreateBtn = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(5, 5, 5, 5)
        self.vMainLayout.setSpacing(0)
        self.setLayout(self.vMainLayout)
        
        self.addBtn = QPushButton("添加好友/群聊")
        self.createBtn = QPushButton("创建群聊")
        
        self.vMainLayout.addWidget(self.addBtn)
        self.vMainLayout.addWidget(self.createBtn)
         
        self.addBtn.clicked.connect(self.onClickedAddBtn)
        self.createBtn.clicked.connect(self.onClickedCreateBtn)
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Popup)
        StyleSheetUtils.setQssByFileName("./_rc/qss/SelectPage.qss", self)
        
    def onClickedAddBtn(self):
        self.clickedAddBtn.emit()
        self.close()
        
    def onClickedCreateBtn(self):
        self.clickedCreateBtn.emit()
        self.close()
        
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)    