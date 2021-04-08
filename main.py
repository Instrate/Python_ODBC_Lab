import sys

import pyodbc

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

import auth

class User(QMainWindow,auth.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = User()
    window.show()
    app.exec_()  
    # con = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};User ID=ODBC;Password=Bigben00;Server=localhost;Port=3306;Database=car_showroom;String Types=Unicode')
    # cursor = con.cursor()
    # request = 'SELECT * FROM `Склад`'
    # cursor.execute(request)

    # for row in cursor:
    #     print(row)



if (__name__=="__main__"):
    main()