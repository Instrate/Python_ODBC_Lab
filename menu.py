# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(348, 369)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.showAvailableTablesButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.showAvailableTablesButton.setFont(font)
        self.showAvailableTablesButton.setObjectName("showAvailableTablesButton")
        self.gridLayout.addWidget(self.showAvailableTablesButton, 0, 0, 1, 1)
        self.tablesListWidget = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tablesListWidget.setFont(font)
        self.tablesListWidget.setObjectName("tablesListWidget")
        self.gridLayout.addWidget(self.tablesListWidget, 1, 0, 1, 1)
        self.editButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.editButton.setFont(font)
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 2, 0, 1, 1)
        self.exitButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.showAvailableTablesButton.setText(_translate("Form", "Показати список доступних таблиць"))
        self.editButton.setText(_translate("Form", "Перейти до редагування"))
        self.exitButton.setText(_translate("Form", "Вийти"))
