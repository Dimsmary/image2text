# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 213)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.btn_open = QtWidgets.QPushButton(MainWindow)
        self.btn_open.setGeometry(QtCore.QRect(290, 20, 93, 28))
        self.btn_open.setObjectName("btn_open")
        self.btn_convert = QtWidgets.QPushButton(MainWindow)
        self.btn_convert.setGeometry(QtCore.QRect(290, 70, 93, 28))
        self.btn_convert.setObjectName("btn_convert")
        self.lab_inp = QtWidgets.QLabel(MainWindow)
        self.lab_inp.setGeometry(QtCore.QRect(20, 20, 72, 15))
        font = QtGui.QFont()
        font.setFamily("3ds")
        self.lab_inp.setFont(font)
        self.lab_inp.setObjectName("lab_inp")
        self.lab_path = QtWidgets.QLabel(MainWindow)
        self.lab_path.setGeometry(QtCore.QRect(20, 50, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lab_path.setFont(font)
        self.lab_path.setAutoFillBackground(False)
        self.lab_path.setMidLineWidth(0)
        self.lab_path.setTextFormat(QtCore.Qt.PlainText)
        self.lab_path.setScaledContents(False)
        self.lab_path.setWordWrap(True)
        self.lab_path.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lab_path.setObjectName("lab_path")
        self.tex_out = QtWidgets.QTextEdit(MainWindow)
        self.tex_out.setGeometry(QtCore.QRect(20, 110, 361, 91))
        self.tex_out.setDocumentTitle("")
        self.tex_out.setPlaceholderText("")
        self.tex_out.setObjectName("tex_out")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ImgConverter"))
        self.btn_open.setText(_translate("MainWindow", "Open"))
        self.btn_convert.setText(_translate("MainWindow", "Convert"))
        self.lab_inp.setText(_translate("MainWindow", "Path:"))
        self.lab_path.setText(_translate("MainWindow", "Null"))

