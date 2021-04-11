import sys

import pyodbc

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

import deleting

class Delete(QWidget, deleting.Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.methodListColumns()
        self.buttonDelete.clicked.connect(self.methodApply)

    def methodListColumns(self):
        cur = self.parent.parent.connection.cursor()
        table = self.parent.table
        request = "SHOW COLUMNS FROM " + table + ";"
        cur.execute(request)
        for row in cur:
            self.comboAttribute.addItem(row[0])

    def methodApply(self):
        cur = self.parent.parent.connection.cursor()
        table = self.parent.table
        request = "SHOW COLUMNS FROM " + table + ";"
        cur.execute(request)
        i = 0
        main_field = ""
        for row in cur:
            if(row[0] == self.comboAttribute.currentText()):
                main_field = row[0]
                break
            i += 1
        main_field = "`" + main_field + "`"
        request = "SELECT * FROM " + table + ";"
        cur.execute(request)
        id_list = []
        j = 0
        for row in cur:
                id_list.append(row[i])
        ind = False
        value = self.lineInput.text()
        for i in range(len(id_list)):
            if(str(id_list[i]) == value):
                ind = True
                break
        if(ind == True):
            request = "DELETE FROM " + table + " WHERE " + main_field + "=" + str(value) + ";"
            cur.execute(request)
            self.parent.methodRefresh()