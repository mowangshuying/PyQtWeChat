from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from sigleton import singleton

@singleton
class BusUtils(QObject):
    changeHeadImgSuc = pyqtSignal()
    statusBarTextChanged = pyqtSignal(str)
    agreeAddFriend = pyqtSignal(int)
    refuseAddFriend = pyqtSignal(int)
    swithSesPage = pyqtSignal(str)
    updateSesLastMsg = pyqtSignal(str, str, str, bool) # key msg time