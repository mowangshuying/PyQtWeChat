
from PyQt6.QtWidgets import QListWidget
from StyleSheetUtils import StyleSheetUtils

class ListWidgetEx(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        StyleSheetUtils.setQssByFileName("./_rc/qss/ListWidgetEx.qss", self)