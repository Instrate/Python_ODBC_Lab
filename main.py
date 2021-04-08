import sys

import pyodbc

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class User(QWidget,):
    def __init__():
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = userSpace()
    window.show()
    app.exec_()  

if (__name__=="__main__"):
    main()