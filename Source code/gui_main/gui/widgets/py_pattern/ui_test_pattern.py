# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_patternBtERxj.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_test_pattern(object):
    def setupUi(self, test_pattern):
        if not test_pattern.objectName():
            test_pattern.setObjectName(u"test_pattern")
        test_pattern.resize(150, 133)
        test_pattern.setMinimumSize(QSize(150, 0))
        test_pattern.setMaximumSize(QSize(150, 133))
        test_pattern.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 10px;")
        self.gridLayout_3 = QGridLayout(test_pattern)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page = QStackedWidget(test_pattern)
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
        self.label = QLabel(self.page2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"font:17px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(0, 0, 0);\n"
"padding-left:5px;\n"
"\n"
"background-color: rgb(73, 73, 220);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)

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

        self.frame_2 = QFrame(self.page2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 3))
        self.frame_2.setMaximumSize(QSize(16777215, 3))
        self.frame_2.setStyleSheet(u"background-color: rgb(65, 72, 88);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_2, 2, 0, 1, 3)

        self.label_2 = QLabel(self.page2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label_2, 4, 0, 1, 1)

        self.Type_comboBox = QComboBox(self.page2)
        self.Type_comboBox.addItem("")
        self.Type_comboBox.addItem("")
        self.Type_comboBox.addItem("")
        self.Type_comboBox.setObjectName(u"Type_comboBox")
        self.Type_comboBox.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")

        self.gridLayout_4.addWidget(self.Type_comboBox, 1, 0, 1, 3)

        self.SV_lineEdit = QSpinBox(self.page2)
        self.SV_lineEdit.setObjectName(u"SV_lineEdit")
        self.SV_lineEdit.setMinimumSize(QSize(50, 20))
        self.SV_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.SV_lineEdit.setMouseTracking(False)
        self.SV_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.SV_lineEdit.setFrame(True)
        self.SV_lineEdit.setAlignment(Qt.AlignCenter)
        self.SV_lineEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.SV_lineEdit.setMinimum(-2000)
        self.SV_lineEdit.setMaximum(2000)
        self.SV_lineEdit.setSingleStep(1)
        self.SV_lineEdit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.SV_lineEdit.setValue(500)

        self.gridLayout_4.addWidget(self.SV_lineEdit, 4, 1, 1, 2)

        self.page.addWidget(self.page2)

        self.gridLayout_3.addWidget(self.page, 0, 0, 1, 1)


        self.retranslateUi(test_pattern)

        self.page.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(test_pattern)
    # setupUi

    def retranslateUi(self, test_pattern):
        test_pattern.setWindowTitle(QCoreApplication.translate("test_pattern", u"Form", None))
        self.label.setText(QCoreApplication.translate("test_pattern", u"STEP 1", None))
        self.label_2.setText(QCoreApplication.translate("test_pattern", u"\u6e2c\u5b9a\u96fb\u5727 V", None))
        self.Type_comboBox.setItemText(0, QCoreApplication.translate("test_pattern", u"BG", None))
        self.Type_comboBox.setItemText(1, QCoreApplication.translate("test_pattern", u"\u6e2c\u5b9a+BG", None))
        self.Type_comboBox.setItemText(2, QCoreApplication.translate("test_pattern", u"END", None))

    # retranslateUi

