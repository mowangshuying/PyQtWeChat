from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from sigleton import *

@singleton
class Base64Utils(QObject):
    @classmethod
    def pixmapToBase64String(self, pixmap: QPixmap) -> str:
        byteArray = QByteArray()
        buffer = QBuffer(byteArray)
        pixmap.toImage().save(buffer, "PNG")
        
        base64String = byteArray.toBase64().data().decode('utf-8')
        buffer.close()
        return base64String
    
    @classmethod
    def base64StringToPixmap(self, base64String: str) -> QPixmap:
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray.fromBase64(base64String.encode('utf-8')))
        return pixmap