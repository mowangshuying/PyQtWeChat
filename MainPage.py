# import QWidget
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
# from PyQt6.QtWidgets import QHBoxLayout
from ToolPage import ToolPage
from PyQt6.QtGui import *
from MsgListPage import MsgListPage
from HSplit import HSplit
from SesPage import SesPage
from NetClientUtils import NetClientUtils
from sigleton import singleton
from StackLayout import StackLayout
from AddFriendsPage import AddFriendsPage

# res
from _rc.res import *

@singleton
class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Main Window")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
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

        self.rightLayout = StackLayout()
        self.__initRightPage()
        self.hMainLayout.addLayout(self.rightLayout, 1)
        
        self.setLayout(self.hMainLayout)

        self.resize(1000, 750)


        self.pressed = False
        self.pressedPos = None

        self.dragging = False  # 是否正在拖动
        self.resizeEdge = 5    # 边缘可拖动区域的宽度（像素）
        self.dragDirection = None  # 拖动方向，如 Qt.LeftEdge、Qt.RightEdge 等
        
        # connect;
        self.midPage.clickedAddBtn.connect(self.onClickedAddBtn)
        self.midPage.clickedCreateBtn.connect(lambda: print("clicked createBtn"))


    def __initRightPage(self):
        # SesPage;
        self.sesPage = SesPage(self)
        self.sesPage.getMinBtn().clicked.connect(lambda: self.showMinimized())
        self.sesPage.getMaxBtn().clicked.connect(lambda: self.showNormal() if self.isMaximized() else self.showMaximized())
        self.sesPage.getCloseBtn().clicked.connect(lambda: self.close())
        self.rightLayout.addWidgetByKey("SesPage", self.sesPage)

        # AddFriendsPage;
        self.addFriendsPage = AddFriendsPage(self)
        self.addFriendsPage.getMinBtn().clicked.connect(lambda: self.showMinimized())
        self.addFriendsPage.getMaxBtn().clicked.connect(lambda: self.showNormal() if self.isMaximized() else self.showMaximized())
        self.addFriendsPage.getCloseBtn().clicked.connect(lambda: self.close())
        # self.addFriendsPage.clickedSearchBtn.connect(lambda: self.onClickedSearchFriendBtn)
        
        
        self.rightLayout.addWidgetByKey("AddFriendsPage", self.addFriendsPage)
        self.rightLayout.setCurrentWidgetByKey("SesPage")

    def onClickedAddBtn(self):
        self.rightLayout.setCurrentWidgetByKey("AddFriendsPage")
        
    # def onClickedSearchFriendBtn(self, text):
    #     # search friend;
    #     print(text)
        

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.pos()
            rect = self.rect()
            x = pos.x()
            y = pos.y()

            # 判断是否点击在窗口边缘
            if x < self.resizeEdge:
                if y < self.resizeEdge:
                    self.dragDirection = Qt.Corner.TopLeftCorner
                elif y > rect.height() - self.resizeEdge:
                    self.dragDirection = Qt.Corner.BottomLeftCorner
                else:
                    self.dragDirection = Qt.Edge.LeftEdge
            elif x > rect.width() - self.resizeEdge:
                if y < self.resizeEdge:
                    self.dragDirection = Qt.Corner.TopRightCorner
                elif y > rect.height() - self.resizeEdge:
                    self.dragDirection = Qt.Corner.BottomRightCorner
                else:
                    self.dragDirection = Qt.Edge.RightEdge
            elif y < self.resizeEdge:
                self.dragDirection = Qt.Edge.TopEdge
            elif y > rect.height() - self.resizeEdge:
                self.dragDirection = Qt.Edge.BottomEdge
            else:
                self.dragDirection = None

            if self.dragDirection is not None:
                self.dragging = True

                # pos globalPos
                self.dragStartPos = event.globalPosition()
                self.originalGeometry = self.geometry()
                # print(f"mousePressEvent Dragging: {self.dragDirection},  Original Geometry: {self.originalGeometry} Evnet Pos: {event.pos()} gloabalPos: {event.globalPosition()}")
                event.accept()
            else:
                # super().mousePressEvent(event)
                self.pressed = True
                self.pressedPos = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.dragging:
            dx = (int)(event.globalPosition().x() - self.dragStartPos.x())
            dy = (int)(event.globalPosition().y() - self.dragStartPos.y())
            new_rect = QRect(self.originalGeometry)

            # 根据拖动方向调整窗口大小
            if self.dragDirection == Qt.Edge.LeftEdge:
                new_rect.setLeft(self.originalGeometry.left() + dx)
            elif self.dragDirection == Qt.Edge.RightEdge:
                new_rect.setRight(self.originalGeometry.right() + dx)
            elif self.dragDirection == Qt.Edge.TopEdge:
                new_rect.setTop(self.originalGeometry.top() + dy)
            elif self.dragDirection == Qt.Edge.BottomEdge:
                new_rect.setBottom(self.originalGeometry.bottom() + dy)
            elif self.dragDirection == Qt.Corner.TopLeftCorner:
                new_rect.setTop(self.originalGeometry.top() + dy)
                new_rect.setLeft(self.originalGeometry.left() + dx)
            elif self.dragDirection == Qt.Corner.TopRightCorner:
                new_rect.setTop(self.originalGeometry.top() + dy)
                new_rect.setRight(self.originalGeometry.right() + dx)
            elif self.dragDirection == Qt.Corner.BottomLeftCorner:
                new_rect.setBottom(self.originalGeometry.bottom() + dy)
                new_rect.setLeft(self.originalGeometry.left() + dx)
            elif self.dragDirection == Qt.Corner.BottomRightCorner:
                new_rect.setBottom(self.originalGeometry.bottom() + dy)
                new_rect.setRight(self.originalGeometry.right() + dx)

            # dragStartPos更新
            # self.dragStartPos = event.pos()
            
            if new_rect.width() < self.minimumWidth() or new_rect.height() < self.minimumHeight():
                event.accept()
                return

            self.setGeometry(new_rect)
            # self.originalGeometry = new_rect
            # self.dragStartPos = event.pos()


            event.accept()
            
            # print(f"mouseMoveEvent Dragging: {self.dragDirection},  Original Geometry: {self.originalGeometry}, New Geometry: {new_rect} Evnet Pos: {event.pos()} dragStartPos: {self.dragStartPos}")

        elif self.pressed:
            self.move(self.pos() + event.pos() - self.pressedPos)
        else:
            # 检测是否进入边缘区域，更改光标样式
            pos = event.pos()
            rect = self.rect()
            x = pos.x()
            y = pos.y()

            if x < self.resizeEdge or x > rect.width() - self.resizeEdge or y < self.resizeEdge or y > rect.height() - self.resizeEdge:
                cursor_shape = Qt.CursorShape.ArrowCursor
                if x < self.resizeEdge:
                    if y < self.resizeEdge:
                        cursor_shape = Qt.CursorShape.SizeFDiagCursor
                    elif y > rect.height() - self.resizeEdge:
                        cursor_shape = Qt.CursorShape.SizeBDiagCursor
                    else:
                        cursor_shape = Qt.CursorShape.SizeHorCursor
                elif x > rect.width() - self.resizeEdge:
                    if y < self.resizeEdge:
                        cursor_shape = Qt.CursorShape.SizeBDiagCursor
                    elif y > rect.height() - self.resizeEdge:
                        cursor_shape = Qt.CursorShape.SizeFDiagCursor
                    else:
                        cursor_shape = Qt.CursorShape.SizeHorCursor
                elif y < self.resizeEdge or y > rect.height() - self.resizeEdge:
                    cursor_shape = Qt.CursorShape.SizeVerCursor
                self.setCursor(cursor_shape)
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
            self.dragDirection = None
            self.pressed = False
            event.accept()
        else:
            super().mouseReleaseEvent(event)
        
        
