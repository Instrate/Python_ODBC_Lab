import sys

import pyodbc

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

import editing
from helper import *

class Edit(QWidget, editing.Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.ind = False
        self.buttonEdit.clicked.connect(self.methodChange)
        self.buttonApply.clicked.connect(self.methodApply)

    def methodApply(self):
        if(self.ind == True):
            value = self.spinID.value()
            cur = self.parent.parent.connection.cursor()
            table = self.parent.table
            Table = self.table
            request = "SHOW COLUMNS FROM " + table + ";"
            cur.execute(request)
            items = []
            types = []
            for row in cur:
                items.append(row[0])
                types.append(row[1])
            fields = ""
            for i in range(len(items)):
                fields += "`" + items[i] + "`"
                if(i < len(items)-1):
                    fields += ","
            request = "UPDATE " + table + " SET "
            for i in range(len(items)):
                request += "`" + items[i] + "`" # not an items
                request += "="
                buffer = Table.item(0,i).text()
                if(str(types[i]).find('char') != -1 or str(types[i]).find('date') != -1 or str(types[i]).find('enum') != -1):
                    request += "\"" + buffer +"\""
                else:
                    request += buffer
                if(i < len(items)-1):
                    request += ","
            request += " WHERE " + "`" + items[0] + "`" + "=" + str(value) + ";"
            cur.execute(request)
            self.parent.methodRefresh()
    
    def methodChange(self):
        value = self.spinID.value()
        cur = self.parent.parent.connection.cursor()
        table = self.parent.table
        Table = self.table
        request = "SHOW COLUMNS FROM " + table + ";"
        cur.execute(request)
        Table.setRowCount(1)
        rows = 0
        columns = []
        for row in cur:
            rows += 1
            columns.append(row[0])
        Table.setColumnCount(rows)
        Table.setHorizontalHeaderLabels(columns)
        request = "SELECT * FROM " + table + ";"
        cur.execute(request)
        id_list = []
        for row in cur:
            id_list.append(row[0])
        ind = False
        for i in range(len(id_list)):
            if(id_list[i] == value):
                ind = True
                break
        cur.execute(request)
        
        if(ind == True):
            edit = 0
            for row in cur:
                if(row[0] == value):
                    edit = row
                    break
            i = 0
            for row in edit:
                temp = row
                if(type(temp).__name__=='date'):
                    temp = datetimeToStr(temp)
                Table.setItem(0,i,QTableWidgetItem(str(temp)))
                i += 1
            self.ind = True
        else:
            self.ind = False
        Table.resizeColumnsToContents()