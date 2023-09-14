# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soyabout.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(400, 300)
        About.setMinimumSize(QtCore.QSize(400, 300))
        About.setMaximumSize(QtCore.QSize(400, 300))
        self.pushButton = QtWidgets.QPushButton(About)
        self.pushButton.setGeometry(QtCore.QRect(150, 250, 84, 35))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(About)
        self.frame.setGeometry(QtCore.QRect(10, -10, 401, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 70, 91, 26))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 32, 32))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("recursos/soyicono.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 200, 291, 19))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 150, 301, 18))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 181, 18))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(70, 30, 291, 18))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(About)
        self.pushButton.clicked.connect(About.close)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Acerca de Soy Legión"))
        self.pushButton.setText(_translate("About", "&Meta"))
        self.label.setText(_translate("About", "Soy Legión"))
        self.label_6.setText(_translate("About", "©2020 Pablo Herrera"))
        self.label_5.setText(_translate("About", "Composición: Pablo Herrera"))
        self.label_2.setText(_translate("About", "Ana Carolina"))
        self.label_4.setText(_translate("About", "Programación: Pablo Herrera"))
        self.label_7.setText(_translate("About", "en memoria de Ana Carolina Pujol (1999-2020)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

