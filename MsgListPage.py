from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QListWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
from VSplit import VSplit
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QStyle, QStyleOption
from StyleSheetUtils import StyleSheetUtils
from SelectPage import SelectPage

class MsgListPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.vMainLayout = QVBoxLayout()
        self.setLayout(self.vMainLayout)
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.vMainLayout.setSpacing(0)
        self.setMouseTracking(True)
        
        self.hTopLayout = QHBoxLayout()
        self.hTopLayout.setContentsMargins(0, 0, 0, 0)
        self.hTopLayout.setSpacing(0)
        
        self.searchEdit = QLineEdit()
        self.addBtn = QPushButton()
        self.searchEdit.setFixedHeight(25)
        self.addBtn.setIconSize(QSize(20, 20))
        self.addBtn.setFixedSize(25, 25)
        self.addBtn.setIcon(QIcon("./_rc/img/add.png"))
        
        self.hTopLayout.addSpacing(10)
        self.hTopLayout.addWidget(self.searchEdit)
        self.hTopLayout.addSpacing(10)
        self.hTopLayout.addWidget(self.addBtn)
        self.hTopLayout.addSpacing(10)
        
        self.vMainLayout.addSpacing(25)
        self.vMainLayout.addLayout(self.hTopLayout)
        self.vMainLayout.addSpacing(15)
        
        self.sp = VSplit()
        self.vMainLayout.addWidget(self.sp)
        
        self.list = QListWidget()
        self.list.setFixedWidth(255)
        self.list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.vMainLayout.addWidget(self.list)
        self.setFixedWidth(255)
        
        
        # 处理事件
        self.addBtn.clicked.connect(self.onAddBtnClicked)
        
        StyleSheetUtils.setQssByFileName("./_rc/qss/MsgListPage.qss", self)
    
    def onAddBtnClicked(self):
        geom = self.addBtn.geometry()
        gp = self.mapToGlobal(geom.topLeft())
        gp.setY(self.addBtn.height() + gp.y())
        
        self.selectPage = SelectPage()
        self.selectPage.move(gp)
        self.selectPage.show()
    
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)
        
        