from PyQt6.QtWidgets import QApplication
from MainPage import MainPage
from PyQt6.QtGui import QIcon
import sys
# from NetClientUtils import NetClientUtils, __getNetClientUtils
from RegLoginPage import RegLoginPage

# res
from _rc.res import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    regLoginPage = RegLoginPage()
    regLoginPage.show()
    
    app.exec()