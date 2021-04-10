import sys

import pyodbc

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

import menu
from helper import *

class Control(QWidget, menu.Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint)
        self.parent = parent
        self.buttonShowTables.clicked.connect(self.methodShowTables)
        self.buttonRefresh.clicked.connect(self.methodRefresh)
        self.buttonExit.clicked.connect(self.methodExit)
        

    def methodShowTables(self):
        cur = self.parent.connection.cursor()
        request = "SHOW TABLES;"
        cur.execute(request)
        self.listTables.clear()
        for row in cur:
            self.listTables.addItem(row[0])
        if(hasattr(self,"filter") == True):
            delattr(self, "filter")

    def methodRefresh(self):
        cur = self.parent.connection.cursor()
        self.table = self.listTables.currentItem().text()
        table = self.table
        self.buttonInput.setEnabled(True)
        
        request = "SHOW COLUMNS FROM " + table + ";"
        cur.execute(request)

        # list columns from table with filter
        i = 0
        lables = []
        types = []
        for row in cur:
            lables.append(row[0])
            types.append(row[1])
        if(hasattr(self, "filter") == True):
            newLables = []
            i = 0
            for label in lables:
                if(self.filter[i] == "+"):
                    newLables.append(label)
                    i += 1
            lables = newLables
            newLables = 0
        else:
            self.filter = []
            for i in range(len(lables)):
                self.filter.append("+")

        # fill headers
        self.Table.setColumnCount(len(lables))
        for i in range(len(lables)):
            self.Table.setHorizontalHeaderItem(i,QTableWidgetItem(lables[i]))
        
        # forming next request
        columns = ""
        for i in range(len(lables)):
            columns += "`" + lables[i] + "`"
            if(i < len(lables) - 1):
                columns += ","         

        request = "SELECT " + columns + " FROM " + table + ";"
        cur.execute(request)

        # displaying table recordings
        rows = 0
        self.Table.setRowCount(rows)
        for row in cur:
            rows += 1
            indicator = True
            for f in self.filter:
                if(f == "-"):
                    indicator = False
            if(indicator == True):
                self.Table.setRowCount(rows + 2)
            else:
                self.Table.setRowCount(rows)
                self.buttonInput.setEnabled(False)
            for j in range(len(lables)):
                temp = row[j]
                if(type(temp).__name__=='date'):
                    temp = datetimeToStr(temp)
                self.Table.setItem(rows - 1,j,QTableWidgetItem(str(temp)))
        if(indicator == True):
            rows += 2
            i = 0
            for temp in types:
                temp = typeToFormat(temp)
                self.Table.setItem(rows - 1,i,QTableWidgetItem(str(temp)))
                i += 1
        self.Table.resizeColumnsToContents()
         

    def methodInsert(self):
        cur = self.parent.connection.cursor()
        table = self.table
        request = 0

    def methodFilter(self):
        x = 0

    def methodExit(self):
        self.close()
        self.parent.connection = 0
        self.parent.menu = 0
        self.parent.show()
        