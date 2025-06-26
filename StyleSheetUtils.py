from _rc.res import *

class StyleSheetUtils:
    @staticmethod
    def setQssByFileName(fileName, widget):
        # Load the QSS file and apply it to the widget
            with open(fileName, 'r') as file:
                qss = file.read()
                widget.setStyleSheet(qss)