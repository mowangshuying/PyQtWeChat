from PyQt5.QtWidgets import QApplication
from MainPage import MainPage
from PyQt5.QtGui import QIcon
# res
from _rc.res import *

if __name__ == "__main__":
    app = QApplication([])
    
    mainPage = MainPage()
    mainPage.show()
    
    app.exec_()