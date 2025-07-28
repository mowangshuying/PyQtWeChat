from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from sigleton import singleton

@singleton
class BusUtils(QObject):
    changeHeadImgSuc = pyqtSignal()
    statusBarTextChanged = pyqtSignal(str)