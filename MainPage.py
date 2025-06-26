# import QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.QtWidgets import QHBoxLayout
from ToolPage import ToolPage
from PyQt5.QtGui import *
from MsgListPage import MsgListPage
from HSplit import HSplit
from SesPage import SesPage

# res
from _rc.res import *

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Main Window")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        # self.setWindowIcon(QIcon("./_rc/img/app.ico"))
        
        
        self.hMainLayout = QHBoxLayout()
        self.hMainLayout.setSpacing(0)
        self.hMainLayout.setContentsMargins(0, 0, 0, 0)
        
        # left;
        self.toolPage = ToolPage(self)
        self.hMainLayout.addWidget(self.toolPage)
        
        # mid;
        self.midPage = MsgListPage()
        self.hMainLayout.addWidget(self.midPage)
        
        # sp
        self.sp = HSplit()
        self.hMainLayout.addWidget(self.sp)
        
        # self.hMainLayout.addStretch(1)
        self.sesPage = SesPage(self)
        # sesPage.maxBtn clicked connect lambda: self.sesPage.showMaximized()

        self.sesPage.getMinBtn().clicked.connect(lambda: self.showMinimized())

        # if max then normal, if normal then max
        self.sesPage.getMaxBtn().clicked.connect(lambda: self.showNormal() if self.isMaximized() else self.showMaximized())
        
        self.sesPage.getCloseBtn().clicked.connect(lambda: self.close())

        self.hMainLayout.addWidget(self.sesPage, 1)
        
        self.setLayout(self.hMainLayout)

        self.resize(800, 600)


        self.pressed = False
        self.pressedPos = None

        self.dragging = False  # 是否正在拖动
        self.resizeEdge = 5    # 边缘可拖动区域的宽度（像素）
        self.dragDirection = None  # 拖动方向，如 Qt.LeftEdge、Qt.RightEdge 等

    # # 支持拖动
    # def mousePressEvent(self, event):
    #     if event.button() != Qt.LeftButton:
    #         return
        
    #     self.pressed = True
    #     self.pressedPos = event.pos()

    # def mouseReleaseEvent(self, event):
    #     self.pressed = False

    # def mouseMoveEvent(self, event):
    #     if self.pressed:
    #         self.move(self.pos() + event.pos() - self.pressedPos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.pos()
            rect = self.rect()
            x = pos.x()
            y = pos.y()

            # 判断是否点击在窗口边缘
            if x < self.resizeEdge:
                if y < self.resizeEdge:
                    self.dragDirection = Qt.TopLeftCorner
                elif y > rect.height() - self.resizeEdge:
                    self.dragDirection = Qt.BottomLeftCorner
                else:
                    self.dragDirection = Qt.LeftEdge
            elif x > rect.width() - self.resizeEdge:
                if y < self.resizeEdge:
                    self.dragDirection = Qt.TopRightCorner
                elif y > rect.height() - self.resizeEdge:
                    self.dragDirection = Qt.BottomRightCorner
                else:
                    self.dragDirection = Qt.RightEdge
            elif y < self.resizeEdge:
                self.dragDirection = Qt.TopEdge
            elif y > rect.height() - self.resizeEdge:
                self.dragDirection = Qt.BottomEdge
            else:
                self.dragDirection = None

            if self.dragDirection is not None:
                self.dragging = True
                self.dragStartPos = pos
                self.originalGeometry = self.geometry()
                event.accept()
            else:
                # super().mousePressEvent(event)
                self.pressed = True
                self.pressedPos = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.dragging:
            dx = event.x() - self.dragStartPos.x()
            dy = event.y() - self.dragStartPos.y()
            new_rect = QRect(self.originalGeometry)

            # 根据拖动方向调整窗口大小
            if self.dragDirection == Qt.LeftEdge:
                new_rect.setLeft(self.originalGeometry.left() + dx)
            elif self.dragDirection == Qt.RightEdge:
                new_rect.setRight(self.originalGeometry.right() + dx)
            elif self.dragDirection == Qt.TopEdge:
                new_rect.setTop(self.originalGeometry.top() + dy)
            elif self.dragDirection == Qt.BottomEdge:
                new_rect.setBottom(self.originalGeometry.bottom() + dy)
            elif self.dragDirection == Qt.TopLeftCorner:
                new_rect.setTop(self.originalGeometry.top() + dy)
                new_rect.setLeft(self.originalGeometry.left() + dx)
            elif self.dragDirection == Qt.TopRightCorner:
                new_rect.setTop(self.originalGeometry.top() + dy)
                new_rect.setRight(self.originalGeometry.right() + dx)
            elif self.dragDirection == Qt.BottomLeftCorner:
                new_rect.setBottom(self.originalGeometry.bottom() + dy)
                new_rect.setLeft(self.originalGeometry.left() + dx)
            elif self.dragDirection == Qt.BottomRightCorner:
                new_rect.setBottom(self.originalGeometry.bottom() + dy)
                new_rect.setRight(self.originalGeometry.right() + dx)

            # dragStartPos更新
            # self.dragStartPos = event.pos()
            self.setGeometry(new_rect)
            event.accept()
        elif self.pressed:
            self.move(self.pos() + event.pos() - self.pressedPos)
        else:
            # 检测是否进入边缘区域，更改光标样式
            pos = event.pos()
            rect = self.rect()
            x = pos.x()
            y = pos.y()

            if x < self.resizeEdge or x > rect.width() - self.resizeEdge or y < self.resizeEdge or y > rect.height() - self.resizeEdge:
                cursor_shape = Qt.ArrowCursor
                if x < self.resizeEdge:
                    if y < self.resizeEdge:
                        cursor_shape = Qt.SizeFDiagCursor
                    elif y > rect.height() - self.resizeEdge:
                        cursor_shape = Qt.SizeBDiagCursor
                    else:
                        cursor_shape = Qt.SizeHorCursor
                elif x > rect.width() - self.resizeEdge:
                    if y < self.resizeEdge:
                        cursor_shape = Qt.SizeBDiagCursor
                    elif y > rect.height() - self.resizeEdge:
                        cursor_shape = Qt.SizeFDiagCursor
                    else:
                        cursor_shape = Qt.SizeHorCursor
                elif y < self.resizeEdge or y > rect.height() - self.resizeEdge:
                    cursor_shape = Qt.SizeVerCursor
                self.setCursor(cursor_shape)
            else:
                self.setCursor(Qt.ArrowCursor)
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.dragDirection = None
            self.pressed = False
            event.accept()
        else:
            super().mouseReleaseEvent(event)
        
        
