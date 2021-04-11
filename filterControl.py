import sys

import pyodbc

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

import filter

class filterControl(QWidget, filter.Ui_Filter):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.methodListAttrs()
        self.buttonClean.clicked.connect(self.methodClean)
        self.buttonSubmit.clicked.connect(self.methodSubmit)

    def methodClean(self):
        for i in range(len(self.parent.filter)):
            self.parent.filter[i] = "+"
            self.tableFields.setItem(i,1,QTableWidgetItem("+"))
        self.parent.methodRefresh()

    def methodListAttrs(self):
        cur = self.parent.parent.connection.cursor()
        table = self.parent.table
        request = "SHOW COLUMNS FROM " + table + ";"
        cur.execute(request)
        i = 0
        self.lables = []
        #self.types = []
        for row in cur:
            self.lables.append(row[0])
            #self.types.append(row[1])
        self.tableFields.clear()
        self.tableFields.setColumnCount(2)
        self.tableFields.setHorizontalHeaderLabels(["Імена полів","+/-"])
        self.tableFields.setRowCount(len(self.lables))
        for i in range(len(self.lables)):
            self.tableFields.setItem(i,0,QTableWidgetItem(self.lables[i]))
            self.tableFields.setItem(i,1,QTableWidgetItem("+"))
        self.tableFields.resizeColumnsToContents()

    def methodSubmit(self):
        settings = []
        table = self.tableFields
        for i in range(len(self.lables)):
            ind = table.item(i,1).text()
            if(ind == "+"):
                settings.append(self.lables[i])
                self.parent.filter[i] = "+"
            else:
                self.parent.filter[i] = "-"
        self.lables = settings
        self.parent.methodRefresh()