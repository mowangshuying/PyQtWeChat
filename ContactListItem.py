from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from enum import Enum

class ContactListItemType(Enum):
    Tip = 0
    Friend = 1
    Group = 2
    
    

class ContactListItem(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.itemType = ContactListItemType.Friend
        self.key = ""    
    def setItemType(self, itemType: ContactListItemType):
        self.itemType = itemType
        
    def getItemType(self) -> ContactListItemType:
        return self.itemType
    
    def setKey(self, key: str):
        self.key = key
        
    def getKey(self) -> str:
        return self.key
    
    