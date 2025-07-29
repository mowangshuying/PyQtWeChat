from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from enum import Enum

class MsgListItemType(Enum):
    Friend = 1
    Group = 2
    
class MsgListItem(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.itemType = MsgListItemType.Friend
        
    def setItemType(self, itemType: MsgListItemType):
        self.itemType = itemType
        
    def getItemType(self) -> MsgListItemType:
        return self.itemType
