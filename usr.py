# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usr.ui'
#
# Created: Tue Apr  4 17:19:14 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!
from __future__ import division
from PyQt4 import QtCore, QtGui
from out import Ui_Dialog
import re
import string



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

class Ui_Buk_Summarization(object):
    def showMessageBox(self,title,message):
	msgBox=QtGui.QMessageBox()
	msgBox.setIcon(QtGui.QMessageBox.Warning)
	msgBox.setWindowTitle(title)
	msgBox.setText(message)
	msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
	msgBox.exec_()
    def outshow(self,output,data2):
	out1=output
	d2=data2
	self.outShowWindow=QtGui.QDialog()
	self.ui=Ui_Dialog()
	self.ui.setupUi(self.outShowWindow,out1,data2)
	self.outShowWindow.show()
    def searchcheck(self):
        str1=".txt"
	str2="1.txt"
        buk_name=self.text_label.text()
        buk=buk_name
        buk_name=buk_name.toLower()
	s=str(buk_name)
	s= ''.join(s.split())
       
	f=open("file.txt","r")
        data1=f.read()

	
	
	
	if s in data1:
        	filename="".join((s,str1))
        	f1=open(filename,"r")
      		data1=f1.read()
                data1=str(data1)
		import SummaryTool
 		output=SummaryTool.main(s,data1)
		
		filename2="".join((s,str2))
		f2=open(filename2,"r")
		data2=f2.read()
		
		self.outshow(output,data2)
		
	else:
	 	self.showMessageBox('Warning','Invalid Book Name. Try Another One')
		
		
	
	
    def setupUi(self, Buk_Summarization):
        Buk_Summarization.setObjectName(_fromUtf8("Buk_Summarization"))
        Buk_Summarization.resize(623, 571)
        font = QtGui.QFont()
        font.setUnderline(True)
        Buk_Summarization.setFont(font)
        Buk_Summarization.setAutoFillBackground(False)
        Buk_Summarization.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.label = QtGui.QLabel(Buk_Summarization)
        self.label.setGeometry(QtCore.QRect(0, 90, 651, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Chancery L"))
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(39,237,255);\n"
"color: rgb(0, 0, 0)\n"
""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Buk_Summarization)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 641, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet(_fromUtf8("background-color:rgb(39, 237, 255);\n"
"border-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Buk_Summarization)
        self.label_3.setGeometry(QtCore.QRect(0, 140, 641, 431))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.bookname = QtGui.QLabel(Buk_Summarization)
        self.bookname.setGeometry(QtCore.QRect(40, 210, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Serif"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bookname.setFont(font)
        self.bookname.setAlignment(QtCore.Qt.AlignCenter)
        self.bookname.setObjectName(_fromUtf8("bookname"))
        self.text_label = QtGui.QLineEdit(Buk_Summarization)
        self.text_label.setGeometry(QtCore.QRect(260, 210, 301, 41))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.text_label.setFont(font)
        self.text_label.setObjectName(_fromUtf8("text_label"))
        self.search = QtGui.QPushButton(Buk_Summarization)
        self.search.setGeometry(QtCore.QRect(270, 290, 95, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.search.setFont(font)
        self.search.setObjectName(_fromUtf8("search"))
	self.search.clicked.connect(self.searchcheck)
 
        self.img = QtGui.QLabel(Buk_Summarization)
        self.img.setGeometry(QtCore.QRect(3, 380, 631, 191))
        self.img.setText(_fromUtf8(""))
        self.img.setPixmap(QtGui.QPixmap(_fromUtf8("ssss.jpg")))
        self.img.setObjectName(_fromUtf8("img"))

        self.retranslateUi(Buk_Summarization)
        QtCore.QMetaObject.connectSlotsByName(Buk_Summarization)

    def retranslateUi(self, Buk_Summarization):
        Buk_Summarization.setWindowTitle(_translate("Buk_Summarization", "Dialog", None))
        self.label.setText(_translate("Buk_Summarization", " REVIEW  & ANALYSIS", None))
        self.label_2.setText(_translate("Buk_Summarization", " SUMMARY", None))
        self.bookname.setText(_translate("Buk_Summarization", "Enter The Book Name", None))
        self.search.setText(_translate("Buk_Summarization", "SEARCH", None))





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Buk_Summarization = QtGui.QDialog()
    ui = Ui_Buk_Summarization()
    ui.setupUi(Buk_Summarization)
    Buk_Summarization.show()
    sys.exit(app.exec_())


