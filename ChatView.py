from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ChatView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._isAppended = False
        
        self.vMainLayout = QVBoxLayout()
        self.vMainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.vMainLayout)
        
        self.scrollArea = QScrollArea()
        self.setObjectName("scrollArea")
        self.vMainLayout.addWidget(self.scrollArea)
        
        self.widget = QWidget()
        self.widget.setObjectName("widget")
        self.setAutoFillBackground(True)
        
        self.vWidgetLayout = QVBoxLayout()
        self.vWidgetLayout.addWidget(QWidget(), 100000)
        self.widget.setLayout(self.vWidgetLayout)
        self.scrollArea.setWidget(self.widget)
        
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        vScrollBar = self.scrollArea.verticalScrollBar()
        vScrollBar.rangeChanged.connect(self.onVScrollRangeChanged)
        
        self.hScrollAreaLayout = QHBoxLayout()
        self.hScrollAreaLayout.addWidget(vScrollBar, 0, Qt.AlignmentFlag.AlignRight)
        self.hScrollAreaLayout.setSpacing(0)
        self.scrollArea.setLayout(self.hScrollAreaLayout)
        
        vScrollBar.setHidden(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.installEventFilter(self)
        
    def appendChatItem(self, item):
        layout = self.scrollArea.widget().layout()
        layout.addWidget(item)
        
    def removeAllChatItem(self):
        for i in range(self.scrollArea.widget().layout().count() - 1):
            self.scrollArea.widget().layout().itemAt(i).widget().deleteLater()
        
        

    def onVScrollRangeChanged(self, min, max):
        if self._isAppended:
            vScrollBar = self.scrollArea.verticalScrollBar() 
            vScrollBar.setSliderPosition(vScrollBar.maximum())
            
            QTime.singleShot(100, self.onTimer)      
        
    def onTimer(self):
        self._isAppended = False
        
    def eventFilter(self, a0, a1):
        if a1.type() == QEvent.Type.Enter and a0 == self.scrollArea:
            self.scrollArea.verticalScrollBar().setHidden(self.scrollArea.verticalScrollBar().maximum() == 0)
        elif a1.type() == QEvent.Type.Leave and a0 == self.scrollArea: 
            self.scrollArea.verticalScrollBar().setHidden(True)
               
        return super().eventFilter(a0, a1)
    def paintEvent(self, a0):
        opt = QStyleOption()   
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)
        
        