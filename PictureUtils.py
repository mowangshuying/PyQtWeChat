from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from sigleton import *

class PictureUtils:
    @staticmethod
    def mergePictures(pixmaps):
        # 根据大小确定拼接方式
        pixmapC = len(pixmaps)
        if pixmapC == 0:
            return QPixmap()
        
        if pixmapC == 1:
            return pixmaps[0]
        
        if pixmapC == 2:
            pixmap = QPixmap(90, 90)
            pixmap.fill(Qt.GlobalColor.transparent)
            
            painter = QPainter()
            painter.begin(pixmap)
            
            rect0 = QRect(0, 0, 45, 90)
            pixmaps[0] = pixmaps[0].scaled(rect0.size())
            painter.drawPixmap(rect0, pixmaps[0])
            
            rect1 = QRect(45, 0, 45, 90)
            pixmaps[1] = pixmaps[1].scaled(rect1.size())
            painter.drawPixmap(rect1, pixmaps[1])
            painter.end()            
            return pixmap
        
        if pixmapC == 3:
            pixmap = QPixmap(90, 90)
            pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter()
            painter.begin(pixmap)
            
            rect0 = QRect(0, 0, 30, 90)
            pixmaps[0] = pixmaps[0].scaled(rect0.size())
            painter.drawPixmap(rect0, pixmaps[0])
            
            rect1 = QRect(30, 0, 30, 90)
            pixmaps[1] = pixmaps[1].scaled(rect1.size())
            painter.drawPixmap(rect1, pixmaps[1])
            
            rect2 = QRect(60, 0, 30, 90)
            pixmaps[2] = pixmaps[2].scaled(rect2.size())
            painter.drawPixmap(rect2, pixmaps[2])
            painter.end()
            return pixmap
        
        if pixmapC == 4:
            pixmap = QPixmap(90, 90)
            pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter()
            painter.begin(pixmap)
            
            rect0 = QRect(0, 0, 45, 45)
            pixmaps[0] = pixmaps[0].scaled(rect0.size())
            painter.drawPixmap(rect0, pixmaps[0])
            
            rect1 = QRect(45, 0, 45, 45)
            pixmaps[1] = pixmaps[1].scaled(rect1.size())
            painter.drawPixmap(rect1, pixmaps[1])
            
            rect2 = QRect(0, 45, 45, 45)
            pixmaps[2] = pixmaps[2].scaled(rect2.size())
            painter.drawPixmap(rect2, pixmaps[2])
            
            rect3 = QRect(45, 45, 45, 45)
            pixmaps[3] = pixmaps[3].scaled(rect3.size())
            painter.drawPixmap(rect3, pixmaps[3])
            
            painter.end()
            return pixmap
        
        rects = []
        for j in range(3):
            for i in range(3):
                rects.append(QRect(i * 30, j * 30, 30, 30))
        
        pixmap = QPixmap(90, 90)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter()
        painter.begin(pixmap)    
        for pixmap_ in pixmaps:
            rect = rects.pop()
            pixmap_ = pixmap_.scaled(rect.size())
            painter.drawPixmap(rect, pixmap_)
        painter.end()
        return pixmap         
        
        