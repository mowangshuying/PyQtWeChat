from PyQt5.QtWidgets import QWidget
from StyleSheetUtils import StyleSheetUtils
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QStyle, QStyleOption

class HSplit(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(1)
        StyleSheetUtils.setQssByFileName('./_rc/qss/HSplit.qss', self)
        
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)