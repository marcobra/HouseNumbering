# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HouseNumbering_update_selected_form.ui'
#
# Created: Sun Apr 19 22:34:32 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_HouseNumbering_update_selected_form(object):
    def setupUi(self, HouseNumbering_update_selected_form):
        HouseNumbering_update_selected_form.setObjectName(_fromUtf8("HouseNumbering_update_selected_form"))
        HouseNumbering_update_selected_form.resize(562, 224)
        self.buttonBox = QtGui.QDialogButtonBox(HouseNumbering_update_selected_form)
        self.buttonBox.setGeometry(QtCore.QRect(295, 155, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.CBfields = QtGui.QComboBox(HouseNumbering_update_selected_form)
        self.CBfields.setGeometry(QtCore.QRect(5, 30, 211, 24))
        self.CBfields.setObjectName(_fromUtf8("CBfields"))
        self.QLEvalore = QtGui.QLineEdit(HouseNumbering_update_selected_form)
        self.QLEvalore.setGeometry(QtCore.QRect(225, 60, 65, 24))
        self.QLEvalore.setObjectName(_fromUtf8("QLEvalore"))
        self.label = QtGui.QLabel(HouseNumbering_update_selected_form)
        self.label.setGeometry(QtCore.QRect(10, 5, 491, 20))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(HouseNumbering_update_selected_form)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 206, 20))
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(HouseNumbering_update_selected_form)
        self.label_3.setGeometry(QtCore.QRect(10, 195, 501, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cBkeepLatestValue = QtGui.QCheckBox(HouseNumbering_update_selected_form)
        self.cBkeepLatestValue.setGeometry(QtCore.QRect(10, 155, 251, 19))
        self.cBkeepLatestValue.setChecked(True)
        self.cBkeepLatestValue.setObjectName(_fromUtf8("cBkeepLatestValue"))
        self.QLEnsteps = QtGui.QLineEdit(HouseNumbering_update_selected_form)
        self.QLEnsteps.setGeometry(QtCore.QRect(330, 60, 45, 24))
        self.QLEnsteps.setAutoFillBackground(True)
        self.QLEnsteps.setMaxLength(4)
        self.QLEnsteps.setObjectName(_fromUtf8("QLEnsteps"))
        self.cBkeepCharFixed = QtGui.QCheckBox(HouseNumbering_update_selected_form)
        self.cBkeepCharFixed.setGeometry(QtCore.QRect(10, 95, 541, 22))
        self.cBkeepCharFixed.setObjectName(_fromUtf8("cBkeepCharFixed"))
        self.label_4 = QtGui.QLabel(HouseNumbering_update_selected_form)
        self.label_4.setGeometry(QtCore.QRect(300, 60, 10, 20))
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(HouseNumbering_update_selected_form)
        self.label_5.setGeometry(QtCore.QRect(385, 60, 140, 20))
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cBsetLabel = QtGui.QCheckBox(HouseNumbering_update_selected_form)
        self.cBsetLabel.setGeometry(QtCore.QRect(10, 125, 426, 22))
        self.cBsetLabel.setObjectName(_fromUtf8("cBsetLabel"))

        self.retranslateUi(HouseNumbering_update_selected_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), HouseNumbering_update_selected_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), HouseNumbering_update_selected_form.reject)
        QtCore.QMetaObject.connectSlotsByName(HouseNumbering_update_selected_form)
        HouseNumbering_update_selected_form.setTabOrder(self.QLEvalore, self.CBfields)
        HouseNumbering_update_selected_form.setTabOrder(self.CBfields, self.cBkeepLatestValue)
        HouseNumbering_update_selected_form.setTabOrder(self.cBkeepLatestValue, self.buttonBox)

    def retranslateUi(self, HouseNumbering_update_selected_form):
        HouseNumbering_update_selected_form.setWindowTitle(_translate("HouseNumbering_update_selected_form", "HouseNumbering", None))
        self.label.setText(_translate("HouseNumbering_update_selected_form", "Set value for the data field:", None))
        self.label_2.setText(_translate("HouseNumbering_update_selected_form", "Start value: (example1 or 1a)", None))
        self.label_3.setText(_translate("HouseNumbering_update_selected_form", "You can also activate this form with F10 funct key - by Marco Braida 2014", None))
        self.cBkeepLatestValue.setText(_translate("HouseNumbering_update_selected_form", "Remember latest inserted  value", None))
        self.cBkeepCharFixed.setText(_translate("HouseNumbering_update_selected_form", "based on start value keep letter part fixed and increase only numeric part", None))
        self.label_4.setText(_translate("HouseNumbering_update_selected_form", "+", None))
        self.label_5.setText(_translate("HouseNumbering_update_selected_form", "numeric step value", None))
        self.cBsetLabel.setText(_translate("HouseNumbering_update_selected_form", "set the working field as active label for current layer", None))

