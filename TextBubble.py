from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import sys
from BubbleFrame import BubbleFrame
from Def import *

class TextBubble(BubbleFrame):
    def __init__(self, role:ChatRole, text, parent=None):
        super().__init__(role, parent)
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.installEventFilter(self)
        
        font = QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        
        self.setPlainText(text)
        self.setWidget(self.textEdit)
        self.__initStyleSheet()
        
    def setPlainText(self, text):
        self.textEdit.setPlainText(text)
        docMargin = self.textEdit.document().documentMargin()
        marginLeft = self.layout().contentsMargins().left()
        marginRight = self.layout().contentsMargins().right()
        
        fm = QFontMetricsF(self.textEdit.font())
        doc = self.textEdit.document()
        
        maxWidth = 0
        for i in range(doc.blockCount()):
            block = doc.findBlockByNumber(i)
            textWidth = fm.horizontalAdvance(block.text())
            if textWidth > maxWidth:
                maxWidth = textWidth
                
        self.setMaximumWidth(int(maxWidth) + int(docMargin) * 2 + marginLeft + marginRight)
    
    def __initStyleSheet(self):
        self.textEdit.setStyleSheet("QTextEdit{background:transparent;border:none}")
    
    def getTextHeight(self):
        docMargin = self.textEdit.document().documentMargin()
        doc = self.textEdit.document()
        
        textHeight = 0
        for i in range(doc.blockCount()):
            # 获取当前block
            block = doc.findBlockByNumber(i)
            layout = block.layout()
            textRect = layout.boundingRect()
            textHeight += textRect.height()
            
        vMargin = self.layout().contentsMargins().top()
        return (int(textHeight) + int(docMargin) * 2 + vMargin * 2)       
    
    def adjustTextHeight(self):
        self.setFixedHeight(self.getTextHeight())
    
    def eventFilter(self, a0, a1):
        if self.textEdit == a0 and a1.type() == QEvent.Type.Paint:
            self.adjustTextHeight()
            # 
            # listitem = self.property("listitem")
            # height = self.getTextHeight()
            # listitem.setSizeHint(QSize(listitem.sizeHint().width(), height + 20))
            
        return super().eventFilter(a0, a1)
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TextBubble(ChatRole.Self, "今天也是美好的一天要加油哟!")
    w.show()
    
    app.exec()