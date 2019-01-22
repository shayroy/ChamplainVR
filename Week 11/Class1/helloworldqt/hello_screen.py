# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello_screen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelloWorldDialog(object):
    def setupUi(self, HelloWorldDialog):
        HelloWorldDialog.setObjectName("HelloWorldDialog")
        HelloWorldDialog.resize(400, 300)
        self.label = QtWidgets.QLabel(HelloWorldDialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 91, 16))
        self.label.setObjectName("label")
        self.edit_inputname = QtWidgets.QLineEdit(HelloWorldDialog)
        self.edit_inputname.setGeometry(QtCore.QRect(30, 50, 113, 20))
        self.edit_inputname.setObjectName("edit_inputname")
        self.btn_ok = QtWidgets.QPushButton(HelloWorldDialog)
        self.btn_ok.setGeometry(QtCore.QRect(170, 70, 41, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.label_result = QtWidgets.QLabel(HelloWorldDialog)
        self.label_result.setGeometry(QtCore.QRect(40, 130, 47, 13))
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")

        self.retranslateUi(HelloWorldDialog)
        QtCore.QMetaObject.connectSlotsByName(HelloWorldDialog)

        self.btn_ok.clicked.connect(self.button_pressed)  # We added this.

    def retranslateUi(self, HelloWorldDialog):
        _translate = QtCore.QCoreApplication.translate
        HelloWorldDialog.setWindowTitle(_translate("HelloWorldDialog", "Dialog"))
        self.label.setText(_translate("HelloWorldDialog", "Enter your name:"))
        self.btn_ok.setText(_translate("HelloWorldDialog", "OK"))

    def button_pressed(self): # We added this.

        self.label_result.setText("Hello " + self.edit_inputname.text()) # We added this.

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelloWorldDialog = QtWidgets.QDialog()
    ui = Ui_HelloWorldDialog()
    ui.setupUi(HelloWorldDialog)
    HelloWorldDialog.show()
    sys.exit(app.exec_())

