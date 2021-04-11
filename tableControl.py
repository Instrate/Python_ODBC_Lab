import sys

import pyodbc

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

import menu
from helper import *
import filterControl
import edit
import delete

class Control(QWidget, menu.Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint)
        self.parent = parent
        self.buttonShowTables.clicked.connect(self.methodShowTables)
        self.buttonRefresh.clicked.connect(self.methodRefresh)
        self.buttonInput.clicked.connect(self.methodInsert)
        self.buttonExit.clicked.connect(self.methodExit)
        self.buttonFilter.clicked.connect(self.methodFilter)
        self.buttonSave.clicked.connect(self.methodSave)
        self.buttonEdit.clicked.connect(self.methodStartEditing)
        self.buttonDelete.clicked.connect(self.methodDelete)

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
        self.Table.setRowCount(0)
        self.Table.setColumnCount(0)
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
        else:
            self.filter = []
            self.lables = lables
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
        self.rows = rows
        if(indicator == True):
            rows += 2
            i = 0
            for temp in types:
                temp = typeToFormat(temp)
                self.Table.setItem(rows - 1,i,QTableWidgetItem(str(temp)))
                i += 1
        self.types = types
        self.Table.resizeColumnsToContents()
         
    def methodInsert(self):
        cur = self.parent.connection.cursor()
        table = self.table
        values = []
        for i in range(len(self.filter)):
            values.append(self.Table.item(self.rows,i).text())
        value = ""
        atr = ""
        for i in range(len(values)):
            if(str(self.types[i]).find('char')!=-1 or str(self.types[i]).find('date')!=-1):
                value +='\"' + values[i] + '\"'
            else:
                value += values[i]
            if(i < len(values)-1):
                value += ','     
        for i in range(len(self.lables)):
            atr +="`"+self.lables[i]+"`"
            if(i < len(self.lables)-1):
                atr += ','  
        request = "INSERT INTO " + table + " (" + atr + ")" + " VALUES ("+value+");"
        cur.execute(request)
        self.methodRefresh()

    def methodStartEditing(self):
        self.editingForm = edit.Edit(self)
        self.editingForm.show()

    def methodDelete(self):
        self.delete = delete.Delete(self)
        self.delete.show()

    def methodFilter(self):
        self.filterForm = filterControl.filterControl(self)
        self.filterForm.show()
        
    def methodSave(self):
        con = self.parent.connection
        con.commit()
        cur = con.cursor()
        request = "ALTER TABLE " + self.table + " AUTO_INCREMENT=1;"
        cur.execute(request)

    def methodExit(self):
        self.close()
        self.parent.connection = 0
        self.parent.menu = 0
        self.parent.show()
        