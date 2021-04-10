import sys

import pyodbc

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

import auth
import tableControl

#==========================
Database = "car_showroom"
Host = "localhost"
Driver = "MySQL ODBC 8.0 Unicode Driver"
Port = 3306
#==========================

class User(QMainWindow, auth.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonLogin.clicked.connect(self.methodSingIn)

    def methodSingIn(self):
        command = "DRIVER={" + Driver + "};"
        command += "UID=" + self.textName.text() + ";"
        command += "Password=" + self.textPWD.text() + ";"
        command += "Server=" + Host + ";"
        command += "Port=" + str(Port) + ";"
        command += "Database=" + Database + ";"
        command += "String Types=Unicode"
        try:
            self.connection = pyodbc.connect(command)
        except RuntimeError:
            self.methodClear()
        except pyodbc.InterfaceError:
            self.methodClear()
        except pyodbc.Error:
            self.methodClear()
        else:
            self.menu = tableControl.Control(self)
            self.menu.show()
            self.close()
        
    def methodClear(self):
        self.textName.setText("")
        self.textPWD.setText("")
   
def main():
    app = QApplication(sys.argv)
    window = User()
    window.show()
    app.exec_()  

if (__name__=="__main__"):
    main()