# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'last.ui'
#
# Created: Thu Apr 20 04:36:16 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog2(object):
    def exitcheck(self):
	sys.exit()
    def setupUi(self, Dialog2,d3):
        Dialog2.setObjectName(_fromUtf8("Dialog2"))
        Dialog2.resize(985, 567)
        self.label = QtGui.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(0, 0, 991, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(Dialog2)
        self.textEdit.setGeometry(QtCore.QRect(0, 40, 971, 421))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(0, 460, 971, 101))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(450, 510, 51, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
	self.pushButton.clicked.connect(self.exitcheck)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.retranslateUi(Dialog2,d3)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2,d3):
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog", None))
        self.label.setText(_translate("Dialog2", "                                                   MAIN CHARACTERS", None))
	self.textEdit.setText(_translate("Dialog2",d3,None))
        self.pushButton.setText(_translate("Dialog2", "Exit", None))
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog2 = QtGui.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())

