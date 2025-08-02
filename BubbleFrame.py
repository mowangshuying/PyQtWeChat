from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from Def import *

class BubbleFrame(QFrame):
    def __init__(self, role:ChatRole, parent=None):
        super().__init__(parent)
        self.hMainLayout = QHBoxLayout()
        # self.setLayout(self.hMainLayout)
        self.role = role
        self.margin = 3
        self.sanjiaoWidth = 8
        
        if role == ChatRole.Self:
            self.hMainLayout.setContentsMargins(self.margin, self.margin, self.margin + self.sanjiaoWidth, self.margin)
        
        if role == ChatRole.Other:
            self.hMainLayout.setContentsMargins(self.margin + self.sanjiaoWidth, self.margin, self.margin, self.margin)
            
        self.setLayout(self.hMainLayout)
        # self.setStyleSheet("QFrame{background:pink;border:none}")
        
    def setWidget(self, widget):
        if self.hMainLayout.count() > 0:
            return
        
        self.hMainLayout.addWidget(widget)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)
        
        if self.role == ChatRole.Other:
            bkColor = QColor(Qt.GlobalColor.white)
            painter.setBrush(QBrush(bkColor))
            bkRect = QRect(self.sanjiaoWidth, 0, self.width() - self.sanjiaoWidth, self.height())
            painter.drawRoundedRect(bkRect, 5, 5)
            
            points = [
                QPointF(bkRect.x(), 12),
                QPointF(bkRect.x(), 12 + self.sanjiaoWidth),
                QPointF(bkRect.x() - self.sanjiaoWidth, 12 + self.sanjiaoWidth / 2),
            ]
            
            painter.drawPolygon(points)
            
        if self.role == ChatRole.Self:
            bkColor = QColor(158, 234, 106)
            painter.setBrush(QBrush(bkColor))
            bkRect = QRect(0, 0, self.width() - self.sanjiaoWidth, self.height())
            painter.drawRoundedRect(bkRect, 5, 5)
            points = [
                QPointF(bkRect.x() + bkRect.width(), 12),
                QPointF(bkRect.x() + bkRect.width(), 12 + self.sanjiaoWidth),
                QPointF(bkRect.x() + bkRect.width() + self.sanjiaoWidth, 12 + self.sanjiaoWidth / 2),
            ]
            painter.drawPolygon(points)
        return super().paintEvent(event)
        
        
