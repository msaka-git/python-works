# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'currency_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(333, 254)
        Form.setMinimumSize(QtCore.QSize(333, 254))
        Form.setMaximumSize(QtCore.QSize(333, 254))
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        Form.setMouseTracking(False)
        self.horizontalWidget = QtWidgets.QWidget(Form)
        self.horizontalWidget.setGeometry(QtCore.QRect(120, 210, 77, 25))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.horizontalWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 16))
        self.label.setMaximumSize(QtCore.QSize(111, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 133, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 80, 133, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 120, 133, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalWidget = QtWidgets.QWidget(Form)
        self.verticalWidget.setGeometry(QtCore.QRect(19, 19, 291, 131))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.yazi_alani = QtWidgets.QLineEdit(Form)
        self.yazi_alani.setEnabled(False)
        self.yazi_alani.setGeometry(QtCore.QRect(30, 160, 261, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.yazi_alani.setFont(font)
        self.yazi_alani.setMouseTracking(False)
        self.yazi_alani.setAutoFillBackground(False)
        self.yazi_alani.setInputMask("")
        self.yazi_alani.setText("")
        self.yazi_alani.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yazi_alani.setReadOnly(False)
        self.yazi_alani.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.yazi_alani.setObjectName("yazi_alani")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.action)

    def action(self):
        textboxValue = self.lineEdit.text() # line edit is where you enter input
        if textboxValue:
            self.yazi_alani.setText(textboxValue)
        else:
            self.yazi_alani.setText("hesap yok")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Calculate"))
        self.label.setText(_translate("Form", "From Currency: "))
        self.label_2.setText(_translate("Form", "To Currency: "))
        self.label_3.setText(_translate("Form", "Amount: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

