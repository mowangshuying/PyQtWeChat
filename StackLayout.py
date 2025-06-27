from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class StackLayout(QStackedLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.map = {}
    
    def addWidget(self, key, widget):
        super().addWidget(widget)
        self.map[key] = widget
        
    def removeWidgetByKey(self, key):
        if self.map[key] != None:
            self.removeWidget(self.map[key])
            self.map[key] = None
            
    def setCurrentWidgetByKey(self, key):
        w = self.map[key]
        if w != None:
            self.setCurrentWidget(w)