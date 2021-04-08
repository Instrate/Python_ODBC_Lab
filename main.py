import sys

import pyodbc

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


# class User(QWidget,):
#     def __init__():
#         super().__init__()
#         self.setupUi(self)


def main():
    # app = QApplication(sys.argv)
    # window = userSpace()
    # window.show()
    # app.exec_()  
    #MySQL ODBC 8.0 Unicode Driver
    #SQL Server
    #ODBC Driver 17 for SQL Server
    con = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};User ID=ODBC;Password=Bigben00;Server=localhost;Port=3306;Database=car_showroom;String Types=Unicode')
    cursor = con.cursor()
    request = 'SELECT * FROM `Склад`'
    cursor.execute(request)

    for row in cursor:
        print(row)



if (__name__=="__main__"):
    main()