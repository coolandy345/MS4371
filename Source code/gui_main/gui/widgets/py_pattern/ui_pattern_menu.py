# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pattern_menuFofenw.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_pattern_menu(object):
    def setupUi(self, pattern_menu):
        if not pattern_menu.objectName():
            pattern_menu.setObjectName(u"pattern_menu")
        pattern_menu.resize(100, 230)
        pattern_menu.setMinimumSize(QSize(100, 230))
        pattern_menu.setMaximumSize(QSize(100, 230))
        pattern_menu.setStyleSheet(u"background-color: rgb(40, 44, 54);")
        self.verticalLayout = QVBoxLayout(pattern_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(pattern_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QPushButton:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"	font: 12px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	border:none;\n"
"	Text-align:left;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(99, 99, 99);\n"
"	border:none;\n"
"	Text-align:left;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(29, 33, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(69, 140, 207);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 5, 5, 5)
        self.pattern_menu_leftinsertblank_pushButton = QPushButton(self.frame_4)
        self.pattern_menu_leftinsertblank_pushButton.setObjectName(u"pattern_menu_leftinsertblank_pushButton")
        self.pattern_menu_leftinsertblank_pushButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pattern_menu_leftinsertblank_pushButton, 8, 0, 1, 1)

        self.pattern_menu_leftinsert_pushButton = QPushButton(self.frame_4)
        self.pattern_menu_leftinsert_pushButton.setObjectName(u"pattern_menu_leftinsert_pushButton")
        self.pattern_menu_leftinsert_pushButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pattern_menu_leftinsert_pushButton, 5, 0, 1, 1)

        self.pattern_menu_copy_pushButton = QPushButton(self.frame_4)
        self.pattern_menu_copy_pushButton.setObjectName(u"pattern_menu_copy_pushButton")
        self.pattern_menu_copy_pushButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pattern_menu_copy_pushButton, 1, 0, 1, 1)

        self.pattern_menu_rightinsertblank_pushButton = QPushButton(self.frame_4)
        self.pattern_menu_rightinsertblank_pushButton.setObjectName(u"pattern_menu_rightinsertblank_pushButton")
        self.pattern_menu_rightinsertblank_pushButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pattern_menu_rightinsertblank_pushButton, 7, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 2))
        self.frame_8.setMaximumSize(QSize(16777215, 2))
        self.frame_8.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_8, 3, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 2))
        self.frame_7.setMaximumSize(QSize(16777215, 2))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_7, 9, 0, 1, 1)

        self.pattern_menu_rightinsert_pushButton = QPushButton(self.frame_4)
        self.pattern_menu_rightinsert_pushButton.setObjectName(u"pattern_menu_rightinsert_pushButton")
        self.pattern_menu_rightinsert_pushButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pattern_menu_rightinsert_pushButton, 4, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 2))
        self.frame_6.setMaximumSize(QSize(16777215, 2))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_6, 6, 0, 1, 1)

        self.pattern_menu_paste_pushButton = QPushButton(self.frame_4)
        self.pattern_menu_paste_pushButton.setObjectName(u"pattern_menu_paste_pushButton")
        self.pattern_menu_paste_pushButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pattern_menu_paste_pushButton, 2, 0, 1, 1)

        self.pattern_menu_delete_pushButton = QPushButton(self.frame_4)
        self.pattern_menu_delete_pushButton.setObjectName(u"pattern_menu_delete_pushButton")
        self.pattern_menu_delete_pushButton.setStyleSheet(u"QPushButton:enabled {\n"
"	color: rgb(255, 88, 105);\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(99, 99, 99);\n"
"}")

        self.gridLayout_2.addWidget(self.pattern_menu_delete_pushButton, 10, 0, 1, 1)

        self.pattern_menu_cut_pushButton = QPushButton(self.frame_4)
        self.pattern_menu_cut_pushButton.setObjectName(u"pattern_menu_cut_pushButton")
        self.pattern_menu_cut_pushButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pattern_menu_cut_pushButton, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(pattern_menu)

        QMetaObject.connectSlotsByName(pattern_menu)
    # setupUi

    def retranslateUi(self, pattern_menu):
        pattern_menu.setWindowTitle(QCoreApplication.translate("pattern_menu", u"Form", None))
        self.pattern_menu_leftinsertblank_pushButton.setText(QCoreApplication.translate("pattern_menu", u"\u5de6\u306b\u65b0\u898f\u633f\u5165", None))
        self.pattern_menu_leftinsert_pushButton.setText(QCoreApplication.translate("pattern_menu", u"\u5de6\u306b\u633f\u5165", None))
        self.pattern_menu_copy_pushButton.setText(QCoreApplication.translate("pattern_menu", u"\u30b3\u30d4\u30fc", None))
        self.pattern_menu_rightinsertblank_pushButton.setText(QCoreApplication.translate("pattern_menu", u"\u53f3\u306b\u65b0\u898f\u633f\u5165", None))
        self.pattern_menu_rightinsert_pushButton.setText(QCoreApplication.translate("pattern_menu", u"\u53f3\u306b\u633f\u5165", None))
        self.pattern_menu_paste_pushButton.setText(QCoreApplication.translate("pattern_menu", u"\u8cbc\u308a\u4ed8\u3051", None))
        self.pattern_menu_delete_pushButton.setText(QCoreApplication.translate("pattern_menu", u"\u524a\u9664", None))
        self.pattern_menu_cut_pushButton.setText(QCoreApplication.translate("pattern_menu", u"\u5207\u308a\u53d6\u308a", None))
    # retranslateUi

