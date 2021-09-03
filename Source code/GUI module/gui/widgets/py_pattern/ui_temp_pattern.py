# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'temp_patternNwErPR.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_temp_pattern(object):
    def setupUi(self, temp_pattern):
        if not temp_pattern.objectName():
            temp_pattern.setObjectName(u"temp_pattern")
        temp_pattern.resize(195, 265)
        temp_pattern.setMinimumSize(QSize(195, 265))
        temp_pattern.setMaximumSize(QSize(195, 265))
        temp_pattern.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 10px;")
        self.gridLayout_3 = QGridLayout(temp_pattern)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page = QStackedWidget(temp_pattern)
        self.page.setObjectName(u"page")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setEnabled(True)
        self.gridLayout = QGridLayout(self.page1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.page1)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.page.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.gridLayout_4 = QGridLayout(self.page2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_3 = QFrame(self.page2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border:none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.frame_3, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(self.page2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(80, 20))
        self.lineEdit.setMaximumSize(QSize(16777215, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit, 6, 1, 1, 2)

        self.label_7 = QLabel(self.page2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(90, 0))
        self.label_7.setMaximumSize(QSize(90, 16777215))
        self.label_7.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label_7, 7, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(80, 20))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_4.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"\n"
"")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_4, 10, 1, 1, 2)

        self.label_2 = QLabel(self.page2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))
        self.label_2.setMaximumSize(QSize(80, 16777215))
        self.label_2.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label_2, 6, 0, 1, 1)

        self.frame_2 = QFrame(self.page2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 3))
        self.frame_2.setMaximumSize(QSize(16777215, 3))
        self.frame_2.setStyleSheet(u"background-color: rgb(65, 72, 88);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_2, 4, 0, 1, 3)

        self.comboBox_2 = QComboBox(self.page2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(80, 20))
        self.comboBox_2.setMaximumSize(QSize(16777215, 20))
        self.comboBox_2.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")
        self.comboBox_2.setMaxVisibleItems(5)

        self.gridLayout_4.addWidget(self.comboBox_2, 15, 0, 1, 3)

        self.label_6 = QLabel(self.page2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))
        self.label_6.setMaximumSize(QSize(80, 16777215))
        self.label_6.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label_6, 13, 0, 1, 1)

        self.label_3 = QLabel(self.page2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.label_3.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)

        self.frame_5 = QFrame(self.page2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 3))
        self.frame_5.setMaximumSize(QSize(16777215, 3))
        self.frame_5.setStyleSheet(u"background-color: rgb(65, 72, 88);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_5, 9, 0, 1, 3)

        self.comboBox = QComboBox(self.page2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")

        self.gridLayout_4.addWidget(self.comboBox, 2, 0, 1, 3)

        self.label = QLabel(self.page2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"font:17px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"background-color: rgb(53, 59, 72);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)

        self.label_8 = QLabel(self.page2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 5))
        self.label_8.setMaximumSize(QSize(16777215, 5))
        self.label_8.setStyleSheet(u"font:11px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 3)

        self.frame_4 = QFrame(self.page2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(80, 20))
        self.frame_4.setMaximumSize(QSize(16777215, 20))
        self.frame_4.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 0, 0);\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(18, 18))
        self.lineEdit_2.setStyleSheet(u"border:none;\n"
"background-color: rgb(30, 34, 41);")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(3, 18))
        self.label_4.setStyleSheet(u"border:none;\n"
"background-color: rgb(30, 34, 41);")

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(18, 18))
        self.lineEdit_3.setStyleSheet(u"border:none;\n"
"background-color: rgb(30, 34, 41);")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_3)


        self.gridLayout_4.addWidget(self.frame_4, 3, 1, 1, 2)

        self.lineEdit_5 = QLineEdit(self.page2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(80, 20))
        self.lineEdit_5.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_5.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_5, 7, 1, 1, 2)

        self.label_5 = QLabel(self.page2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 0))
        self.label_5.setMaximumSize(QSize(80, 16777215))
        self.label_5.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label_5, 10, 0, 1, 1)

        self.label_9 = QLabel(self.page2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(90, 0))
        self.label_9.setMaximumSize(QSize(90, 16777215))
        self.label_9.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label_9, 8, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.page2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(80, 20))
        self.comboBox_3.setMaximumSize(QSize(16777215, 20))
        self.comboBox_3.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")
        self.comboBox_3.setMaxVisibleItems(5)

        self.gridLayout_4.addWidget(self.comboBox_3, 8, 1, 1, 2)

        self.page.addWidget(self.page2)

        self.gridLayout_3.addWidget(self.page, 0, 0, 1, 1)


        self.retranslateUi(temp_pattern)

        self.page.setCurrentIndex(1)
        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_3.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(temp_pattern)
    # setupUi

    def retranslateUi(self, temp_pattern):
        temp_pattern.setWindowTitle(QCoreApplication.translate("temp_pattern", u"Form", None))
        self.lineEdit.setText(QCoreApplication.translate("temp_pattern", u"450", None))
        self.label_7.setText(QCoreApplication.translate("temp_pattern", u"N2 (SLM)", None))
        self.lineEdit_4.setText(QCoreApplication.translate("temp_pattern", u"30", None))
        self.label_2.setText(QCoreApplication.translate("temp_pattern", u"\u4e3b\u7089(\u2103)", None))
        self.label_6.setText(QCoreApplication.translate("temp_pattern", u"\u6e2c\u5b9a\u30d1\u30bf\u30fc\u30f3", None))
        self.label_3.setText(QCoreApplication.translate("temp_pattern", u"\u6642\uff1a\u5206", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"\u6607\u964d\u6e29", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("temp_pattern", u"\u6e2c\u5b9a", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("temp_pattern", u"END", None))

        self.label.setText(QCoreApplication.translate("temp_pattern", u"STEP 1", None))
        self.label_8.setText("")
        self.lineEdit_2.setText(QCoreApplication.translate("temp_pattern", u"45", None))
        self.label_4.setText(QCoreApplication.translate("temp_pattern", u":", None))
        self.lineEdit_3.setText(QCoreApplication.translate("temp_pattern", u"45", None))
        self.lineEdit_5.setText(QCoreApplication.translate("temp_pattern", u"12", None))
        self.label_5.setText(QCoreApplication.translate("temp_pattern", u"\u30ad\u30fc\u30d7\u6642\u9593(s)", None))
        self.label_9.setText(QCoreApplication.translate("temp_pattern", u"PID", None))
    # retranslateUi

