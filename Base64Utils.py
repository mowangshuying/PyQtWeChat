from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from sigleton import *

class Base64Utils(QObject):
    @classmethod
    def pixmapToBase64String(self, pixmap: QPixmap) -> str:
        return pixmap.toImage().toBase64().data().decode()
    
    @classmethod
    def base64StringToPixmap(self, base64String: str) -> QPixmap:
        return QPixmap.fromImage(QImage.fromData(base64String.encode()))