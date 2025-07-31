from PyQt6.QtWidgets import QApplication
from MainPage import MainPage
from PyQt6.QtGui import QIcon
import sys
from RegLoginPage import RegLoginPage
from LogUtils import LogUtils

# res
from _rc.res import *

if __name__ == "__main__":

    app = QApplication(sys.argv)
    regLoginPage = RegLoginPage()
    regLoginPage.show()
    
    app.exec()