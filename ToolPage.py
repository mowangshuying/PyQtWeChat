from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPainter
# from PyQt5.QtGui import QStyleOption
# from PyQt5.QtWidgets import QStyle

# import QPainter
# import QStyleOption
# import QStyle
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QStyle, QStyleOption


from _rc.res import *
from StyleSheetUtils import StyleSheetUtils

class ToolPage(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        # self.setObjectName("ToolPage")
        self.setFixedWidth(55)
        self.setMouseTracking(True)
        self.setWindowFlag(Qt.FramelessWindowHint)
        StyleSheetUtils.setQssByFileName("./_rc/qss/ToolPage.qss", self)
        
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)