# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(976, 292)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonShowTables = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonShowTables.setFont(font)
        self.buttonShowTables.setObjectName("buttonShowTables")
        self.gridLayout.addWidget(self.buttonShowTables, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setAutoFillBackground(False)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 3, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonRefresh = QtWidgets.QPushButton(Form)
        self.buttonRefresh.setObjectName("buttonRefresh")
        self.verticalLayout.addWidget(self.buttonRefresh)
        self.buttonInput = QtWidgets.QPushButton(Form)
        self.buttonInput.setObjectName("buttonInput")
        self.verticalLayout.addWidget(self.buttonInput)
        self.buttonEdit = QtWidgets.QPushButton(Form)
        self.buttonEdit.setObjectName("buttonEdit")
        self.verticalLayout.addWidget(self.buttonEdit)
        self.buttonDelete = QtWidgets.QPushButton(Form)
        self.buttonDelete.setObjectName("buttonDelete")
        self.verticalLayout.addWidget(self.buttonDelete)
        self.buttonFilter = QtWidgets.QPushButton(Form)
        self.buttonFilter.setObjectName("buttonFilter")
        self.verticalLayout.addWidget(self.buttonFilter)
        self.gridLayout.addLayout(self.verticalLayout, 0, 3, 2, 1)
        self.listTables = QtWidgets.QListWidget(Form)
        self.listTables.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listTables.setFont(font)
        self.listTables.setObjectName("listTables")
        self.gridLayout.addWidget(self.listTables, 1, 0, 1, 1)
        self.buttonExit = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonExit.setFont(font)
        self.buttonExit.setObjectName("buttonExit")
        self.gridLayout.addWidget(self.buttonExit, 2, 0, 1, 1)
        self.buttonSave = QtWidgets.QPushButton(Form)
        self.buttonSave.setObjectName("buttonSave")
        self.gridLayout.addWidget(self.buttonSave, 2, 3, 1, 1)
        self.Table = QtWidgets.QTableWidget(Form)
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(0)
        self.Table.setRowCount(0)
        self.gridLayout.addWidget(self.Table, 0, 2, 3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "????????"))
        self.buttonShowTables.setText(_translate("Form", "???????????????? ???????????? ?????????????????? ??????????????"))
        self.buttonRefresh.setText(_translate("Form", "?????????????? ??????????????"))
        self.buttonInput.setText(_translate("Form", "????????????"))
        self.buttonEdit.setText(_translate("Form", "????????????????????"))
        self.buttonDelete.setText(_translate("Form", "????????????????"))
        self.buttonFilter.setText(_translate("Form", "????????????"))
        self.buttonExit.setText(_translate("Form", "??????????"))
        self.buttonSave.setText(_translate("Form", "????????????????"))
