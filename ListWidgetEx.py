
from PyQt6.QtWidgets import QListWidget
from StyleSheetUtils import StyleSheetUtils
from qfluentwidgets import *

class ListWidgetEx(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        StyleSheetUtils.setQssByFileName("./_rc/qss/ListWidgetEx.qss", self)
        # 设置代理
        self.scrollDelegate = SmoothScrollDelegate(self)