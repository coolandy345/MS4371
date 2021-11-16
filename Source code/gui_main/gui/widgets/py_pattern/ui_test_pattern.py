# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_patterncKqaSz.ui'
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
        test_pattern.resize(140, 133)
        test_pattern.setMinimumSize(QSize(140, 133))
        test_pattern.setMaximumSize(QSize(140, 133))
        test_pattern.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"color: rgb(225, 230, 241);\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"font:12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"")
        self.gridLayout_3 = QGridLayout(test_pattern)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page = QStackedWidget(test_pattern)
        self.page.setObjectName(u"page")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setEnabled(True)
        self.page1.setStyleSheet(u"border:none;")
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
        self.page2.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border-color: rgb(231, 214, 85);\n"
"	border-width: 5px;\n"
"	border-radius: 5px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:focus{\n"
"	border-color: rgb(231, 214, 85);\n"
"	border-width: 5px;\n"
"	border-radius: 5px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(91, 94, 98);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(44, 49, 60);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.page2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 30))
        self.frame_6.setMaximumSize(QSize(16777215, 30))
        self.frame_6.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Step_label = QLabel(self.frame_6)
        self.Step_label.setObjectName(u"Step_label")
        self.Step_label.setMinimumSize(QSize(80, 20))
        self.Step_label.setMaximumSize(QSize(80, 30))
        self.Step_label.setStyleSheet(u"QLabel:enabled {\n"
"	font:17px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left:5px;\n"
"	background-color: rgb(126, 229, 214);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_2.addWidget(self.Step_label)

        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setStyleSheet(u"border:none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 2))
        self.frame_2.setMaximumSize(QSize(16777215, 2))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Valtage_label = QLabel(self.frame_5)
        self.Valtage_label.setObjectName(u"Valtage_label")
        self.Valtage_label.setMaximumSize(QSize(16777215, 16777215))
        self.Valtage_label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.Valtage_label)

        self.Valtage_lineEdit = QLineEdit(self.frame_5)
        self.Valtage_lineEdit.setObjectName(u"Valtage_lineEdit")
        self.Valtage_lineEdit.setMinimumSize(QSize(50, 20))
        self.Valtage_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.Valtage_lineEdit.setStyleSheet(u"")
        self.Valtage_lineEdit.setAlignment(Qt.AlignCenter)
        self.Valtage_lineEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.Valtage_lineEdit)


        self.verticalLayout.addWidget(self.frame_5)


        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)

        self.page.addWidget(self.page2)

        self.gridLayout_3.addWidget(self.page, 0, 0, 1, 1)


        self.retranslateUi(test_pattern)

        self.page.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(test_pattern)
    # setupUi

    def retranslateUi(self, test_pattern):
        test_pattern.setWindowTitle(QCoreApplication.translate("test_pattern", u"Form", None))
        self.Step_label.setText(QCoreApplication.translate("test_pattern", u"STEP 1", None))
        self.Valtage_label.setText(QCoreApplication.translate("test_pattern", u"\u6e2c\u5b9a\u96fb\u5727 V", None))
        self.Valtage_lineEdit.setText(QCoreApplication.translate("test_pattern", u"0", None))
    # retranslateUi

