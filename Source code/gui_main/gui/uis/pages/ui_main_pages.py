# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesAspUVo.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1234, 836)
        MainPages.setMinimumSize(QSize(0, 0))
        self.gridLayout_8 = QGridLayout(MainPages)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy)
        self.pages.setMinimumSize(QSize(0, 0))
        self.pages.setMaximumSize(QSize(16777215, 16777215))
        self.pages.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"")
        self.gridLayout_17 = QGridLayout(self.page_1)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page_1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(0)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_5 = QLineEdit(self.frame_10)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 32))
        self.lineEdit_5.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_5.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_18.addWidget(self.lineEdit_5, 11, 3, 1, 1)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 15))
        self.label_6.setMaximumSize(QSize(16777215, 15))
        self.label_6.setStyleSheet(u"\n"
"background-color: rgb(65, 72, 88);\n"
"font: 12px bold large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);")

        self.gridLayout_18.addWidget(self.label_6, 1, 1, 1, 11)

        self.radioButton = QRadioButton(self.frame_10)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(0, 35))
        self.radioButton.setMaximumSize(QSize(140, 35))
        self.radioButton.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:60px;\n"
"max-width:80;")

        self.gridLayout_18.addWidget(self.radioButton, 5, 1, 1, 1)

        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(2, 35))
        self.label.setMaximumSize(QSize(2, 35))
        self.label.setStyleSheet(u"background-color: rgb(65, 72, 88);")

        self.gridLayout_18.addWidget(self.label, 5, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_10)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 32))
        self.lineEdit_2.setMaximumSize(QSize(212, 16777215))
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:200;")

        self.gridLayout_18.addWidget(self.lineEdit_2, 5, 4, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_10)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 32))
        self.lineEdit_4.setMaximumSize(QSize(212, 16777215))
        self.lineEdit_4.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:200;")

        self.gridLayout_18.addWidget(self.lineEdit_4, 7, 3, 1, 3)

        self.lineEdit_9 = QLineEdit(self.frame_10)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 32))
        self.lineEdit_9.setMaximumSize(QSize(212, 16777215))
        self.lineEdit_9.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_18.addWidget(self.lineEdit_9, 10, 3, 1, 1)

        self.lineEdit = QLineEdit(self.frame_10)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 32))
        self.lineEdit.setMaximumSize(QSize(112, 16777215))
        self.lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:100;")
        self.lineEdit.setFrame(False)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setCursorPosition(4)

        self.gridLayout_18.addWidget(self.lineEdit, 2, 3, 1, 1)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(140, 35))
        self.label_4.setMaximumSize(QSize(140, 35))
        self.label_4.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_4, 6, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 32))
        self.lineEdit_3.setMaximumSize(QSize(212, 16777215))
        self.lineEdit_3.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:200;")

        self.gridLayout_18.addWidget(self.lineEdit_3, 6, 3, 1, 3)

        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(140, 0))
        self.label_10.setMaximumSize(QSize(140, 16777215))
        self.label_10.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_10, 13, 1, 1, 1)

        self.label_22 = QLabel(self.frame_10)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(140, 35))
        self.label_22.setMaximumSize(QSize(140, 35))
        self.label_22.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_22, 10, 1, 1, 1)

        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(140, 0))
        self.label_9.setMaximumSize(QSize(140, 16777215))
        self.label_9.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_9, 12, 1, 1, 1)

        self.radioButton_2 = QRadioButton(self.frame_10)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(140, 35))
        self.radioButton_2.setMaximumSize(QSize(140, 35))
        self.radioButton_2.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:60px;\n"
"min-width:80;\n"
"max-width:80;")
        self.radioButton_2.setChecked(True)

        self.gridLayout_18.addWidget(self.radioButton_2, 4, 1, 1, 1)

        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(95, 35))
        self.label_3.setMaximumSize(QSize(95, 35))
        self.label_3.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:15px;\n"
"max-width:80;\n"
"min-width:80;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_3, 5, 3, 1, 1)

        self.label_yesr = QLabel(self.frame_10)
        self.label_yesr.setObjectName(u"label_yesr")
        self.label_yesr.setMinimumSize(QSize(140, 35))
        self.label_yesr.setMaximumSize(QSize(140, 35))
        self.label_yesr.setMouseTracking(False)
        self.label_yesr.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr.setMargin(0)

        self.gridLayout_18.addWidget(self.label_yesr, 2, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_10)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_6.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_18.addWidget(self.lineEdit_6, 12, 3, 1, 1)

        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(140, 35))
        self.label_8.setMaximumSize(QSize(140, 35))
        self.label_8.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_8, 11, 1, 1, 1)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 15))
        self.label_7.setMaximumSize(QSize(16777215, 15))
        self.label_7.setStyleSheet(u"\n"
"background-color: rgb(65, 72, 88);\n"
"font: 12px bold large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);")

        self.gridLayout_18.addWidget(self.label_7, 8, 1, 1, 11)

        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(140, 35))
        self.label_5.setMaximumSize(QSize(140, 35))
        self.label_5.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_5, 7, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_10)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_7.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_18.addWidget(self.lineEdit_7, 13, 3, 1, 1)

        self.label_24 = QLabel(self.frame_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(140, 35))
        self.label_24.setMaximumSize(QSize(140, 35))
        self.label_24.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_24, 9, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_10)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 32))
        self.lineEdit_10.setMaximumSize(QSize(212, 16777215))
        self.lineEdit_10.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_18.addWidget(self.lineEdit_10, 9, 3, 1, 1)


        self.gridLayout_17.addWidget(self.frame_10, 0, 1, 1, 1, Qt.AlignTop)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridFrame_1 = QFrame(self.page_2)
        self.gridFrame_1.setObjectName(u"gridFrame_1")
        self.gridFrame_1.setMinimumSize(QSize(950, 450))
        self.gridFrame_1.setStyleSheet(u"QFrame{\n"
"background-color: rgb(30, 34, 41);\n"
"border-color:rgb(30, 34, 41);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.gridFrame_1.setFrameShape(QFrame.StyledPanel)
        self.gridFrame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.gridFrame_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(6, 6, 0, 6)
        self.frame = QFrame(self.gridFrame_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 30))
        self.comboBox.setMaximumSize(QSize(100, 30))
        self.comboBox.setStyleSheet(u"")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(950, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignLeft)


        self.gridLayout_4.addWidget(self.gridFrame_1, 2, 0, 1, 1)

        self.gridFrame_3 = QFrame(self.page_2)
        self.gridFrame_3.setObjectName(u"gridFrame_3")
        self.gridFrame_3.setMinimumSize(QSize(250, 0))
        self.gridFrame_3.setMaximumSize(QSize(250, 16777215))
        self.gridFrame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(30, 34, 41);\n"
"border-color:rgb(30, 34, 41);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.gridLayout_7 = QGridLayout(self.gridFrame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.gridFrame_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 120))
        self.frame_3.setMaximumSize(QSize(16777215, 120))
        self.frame_3.setStyleSheet(u"border:none")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_42 = QFrame(self.frame_3)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_42)
        self.gridLayout_28.setObjectName(u"gridLayout_28")

        self.gridLayout_10.addWidget(self.frame_42, 1, 0, 1, 1)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_15)
        self.gridLayout_27.setObjectName(u"gridLayout_27")

        self.gridLayout_10.addWidget(self.frame_15, 0, 0, 1, 1)

        self.label_46 = QLabel(self.frame_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font: 22px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_10.addWidget(self.label_46, 0, 1, 1, 1)

        self.label_47 = QLabel(self.frame_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 22px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_10.addWidget(self.label_47, 1, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.gridFrame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border:none")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_7)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setVerticalSpacing(0)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridFrame = QFrame(self.frame_7)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setMinimumSize(QSize(0, 0))
        self.gridFrame.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.gridFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_AutoMode = QRadioButton(self.gridFrame)
        self.btn_AutoMode.setObjectName(u"btn_AutoMode")
        self.btn_AutoMode.setMinimumSize(QSize(120, 30))
        self.btn_AutoMode.setMaximumSize(QSize(120, 30))
        self.btn_AutoMode.setStyleSheet(u"background-color: rgb(30, 34, 41);\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"min-width:100;\n"
"max-width:100;\n"
"padding-left:20px;")
        self.btn_AutoMode.setCheckable(True)
        self.btn_AutoMode.setChecked(True)

        self.horizontalLayout.addWidget(self.btn_AutoMode)

        self.btn_ManaualMode = QRadioButton(self.gridFrame)
        self.btn_ManaualMode.setObjectName(u"btn_ManaualMode")
        self.btn_ManaualMode.setMinimumSize(QSize(130, 30))
        self.btn_ManaualMode.setMaximumSize(QSize(130, 30))
        self.btn_ManaualMode.setStyleSheet(u"background-color: rgb(30, 34, 41);\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:10px;\n"
"min-width:120;\n"
"max-width:120;")
        self.btn_ManaualMode.setCheckable(True)
        self.btn_ManaualMode.setChecked(False)

        self.horizontalLayout.addWidget(self.btn_ManaualMode)


        self.gridLayout_14.addWidget(self.gridFrame, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.frame_7)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(30, 34, 41);")
        self.page_AutoOperate = QWidget()
        self.page_AutoOperate.setObjectName(u"page_AutoOperate")
        self.gridLayout_15 = QGridLayout(self.page_AutoOperate)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page_AutoOperate)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_8)
        self.gridLayout_16.setSpacing(6)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(10, 10, 10, 10)
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 3))
        self.label_11.setMaximumSize(QSize(16777215, 3))
        self.label_11.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:none;")

        self.gridLayout_16.addWidget(self.label_11, 3, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_8)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 90))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_5)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(10, 10, 10, 10)
        self.radioButton_6 = QRadioButton(self.frame_5)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setMinimumSize(QSize(85, 20))
        self.radioButton_6.setMaximumSize(QSize(85, 20))
        self.radioButton_6.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"min-width:80;\n"
"max-width:80;")

        self.gridLayout_11.addWidget(self.radioButton_6, 1, 0, 1, 1)

        self.radioButton_5 = QRadioButton(self.frame_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setMinimumSize(QSize(85, 20))
        self.radioButton_5.setMaximumSize(QSize(85, 20))
        self.radioButton_5.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"min-width:80;\n"
"max-width:80;")
        self.radioButton_5.setCheckable(True)
        self.radioButton_5.setChecked(True)

        self.gridLayout_11.addWidget(self.radioButton_5, 0, 0, 1, 1)

        self.radioButton_7 = QRadioButton(self.frame_5)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setMinimumSize(QSize(85, 20))
        self.radioButton_7.setMaximumSize(QSize(85, 20))
        self.radioButton_7.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"min-width:80;\n"
"max-width:80;")

        self.gridLayout_11.addWidget(self.radioButton_7, 2, 0, 1, 1, Qt.AlignHCenter)

        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(2, 0))
        self.label_14.setMaximumSize(QSize(2, 16777215))
        self.label_14.setStyleSheet(u"background-color: rgb(44, 49, 60);")

        self.gridLayout_11.addWidget(self.label_14, 0, 1, 3, 1)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(60, 30))
        self.pushButton_2.setMaximumSize(QSize(60, 30))
        self.pushButton_2.setTabletTracking(False)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(44, 36, 0);\n"
"	font: 15px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(255, 65, 182);\n"
"	background-color: rgb(79, 159, 238);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(109, 182, 238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(69, 140, 207);\n"
"}")

        self.gridLayout_11.addWidget(self.pushButton_2, 0, 2, 3, 1)


        self.gridLayout_16.addWidget(self.frame_5, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_8)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(6)
        self.gridLayout_13.setVerticalSpacing(30)
        self.gridLayout_13.setContentsMargins(10, 10, 10, 10)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(210, 50))
        self.pushButton.setMaximumSize(QSize(210, 50))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(44, 36, 0);\n"
"	font: 30px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(79, 159, 238);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(109, 182, 238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(69, 140, 207);\n"
"}")
        self.pushButton.setAutoRepeatInterval(100)

        self.gridLayout_13.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(210, 90))
        self.pushButton_4.setMaximumSize(QSize(210, 90))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(44, 36, 0);\n"
"	font: 30px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(255, 88, 105);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 124, 163);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 37, 95);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 30px;\n"
"}")

        self.gridLayout_13.addWidget(self.pushButton_4, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_4, 4, 0, 1, 1, Qt.AlignBottom)

        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 3))
        self.label_15.setMaximumSize(QSize(16777215, 3))
        self.label_15.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:none;")

        self.gridLayout_16.addWidget(self.label_15, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 120))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(41, 47, 56);\n"
"border-color: rgb(30, 34, 41);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(10, 10, 10, 10)
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setMaximumSize(QSize(16777215, 30))
        self.label_16.setStyleSheet(u"font: 20px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"border:none;\n"
"\n"
"")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_16, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_6)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 0))
        self.comboBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_3.setBaseSize(QSize(0, 30))
        self.comboBox_3.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"font: 14px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 0px;")

        self.gridLayout_12.addWidget(self.comboBox_3, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_6, 0, 0, 1, 1, Qt.AlignVCenter)


        self.gridLayout_15.addWidget(self.frame_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_AutoOperate)
        self.page_ManaulOperate = QWidget()
        self.page_ManaulOperate.setObjectName(u"page_ManaulOperate")
        self.gridLayout_2 = QGridLayout(self.page_ManaulOperate)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_ManaulOperate)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_11)
        self.gridLayout_20.setSpacing(6)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(10, 10, 10, 10)
        self.frame_9 = QFrame(self.frame_11)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setLayoutDirection(Qt.LeftToRight)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_9)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(6)
        self.gridLayout_19.setVerticalSpacing(30)
        self.gridLayout_19.setContentsMargins(10, 10, 10, 10)
        self.pushButton_7 = QPushButton(self.frame_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(210, 50))
        self.pushButton_7.setMaximumSize(QSize(210, 50))
        self.pushButton_7.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	color: rgb(44, 36, 0);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(79, 159, 238);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(109, 182, 238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(69, 140, 207);\n"
"}")
        self.pushButton_7.setAutoRepeatInterval(100)

        self.gridLayout_19.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(210, 50))
        self.pushButton_6.setMaximumSize(QSize(210, 50))
        self.pushButton_6.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(44, 36, 0);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(79, 159, 238);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(109, 182, 238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(69, 140, 207);\n"
"}")
        self.pushButton_6.setAutoRepeatInterval(100)

        self.gridLayout_19.addWidget(self.pushButton_6, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(210, 90))
        self.pushButton_5.setMaximumSize(QSize(210, 90))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(44, 36, 0);\n"
"	font: 30px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(255, 88, 105);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 124, 163);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 37, 95);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 30px;\n"
"}")

        self.gridLayout_19.addWidget(self.pushButton_5, 3, 0, 1, 1)

        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 3))
        self.label_18.setMaximumSize(QSize(16777215, 3))
        self.label_18.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:none;")

        self.gridLayout_19.addWidget(self.label_18, 2, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_9, 2, 0, 1, 1, Qt.AlignBottom)

        self.label_19 = QLabel(self.frame_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 3))
        self.label_19.setMaximumSize(QSize(16777215, 3))
        self.label_19.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:none;")

        self.gridLayout_20.addWidget(self.label_19, 1, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 120))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setStyleSheet(u"background-color: rgb(41, 47, 56);\n"
"border-color: rgb(30, 34, 41);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_12)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_21 = QLabel(self.frame_12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(80, 0))
        self.label_21.setMaximumSize(QSize(80, 16777215))
        self.label_21.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_21, 1, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.frame_12)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_21.addWidget(self.comboBox_5, 1, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_12)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.lineEdit_8, 0, 1, 1, 1)

        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(80, 0))
        self.label_20.setMaximumSize(QSize(80, 16777215))
        self.label_20.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_20, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_12, 0, 0, 1, 1, Qt.AlignVCenter)


        self.gridLayout_2.addWidget(self.frame_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_ManaulOperate)

        self.gridLayout_14.addWidget(self.stackedWidget, 1, 0, 2, 3)


        self.gridLayout_7.addWidget(self.frame_7, 2, 0, 1, 1)

        self.label_2 = QLabel(self.gridFrame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 3))
        self.label_2.setMaximumSize(QSize(16777215, 3))
        self.label_2.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:none;")

        self.gridLayout_7.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gridFrame_3, 0, 3, 3, 1)

        self.gridFrame_2 = QFrame(self.page_2)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridFrame_2.setMinimumSize(QSize(950, 180))
        self.gridFrame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 34, 41);\n"
"	border-color:rgb(30, 34, 41);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.gridLayout_5 = QGridLayout(self.gridFrame_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.gridFrame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"border:none")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.frame_30 = QFrame(self.frame_13)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 0))
        self.frame_30.setMaximumSize(QSize(16777215, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.Layout_Status_MSStatus = QGridLayout(self.frame_30)
        self.Layout_Status_MSStatus.setObjectName(u"Layout_Status_MSStatus")
        self.Layout_Status_MSStatus.setContentsMargins(-1, 0, -1, 0)
        self.label_17 = QLabel(self.frame_30)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_17, 0, 0, 1, 1)

        self.frame_22 = QFrame(self.frame_30)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(90, 0))
        self.frame_22.setMaximumSize(QSize(90, 16777215))
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.Layout_Status_Heating = QGridLayout(self.frame_22)
        self.Layout_Status_Heating.setSpacing(0)
        self.Layout_Status_Heating.setObjectName(u"Layout_Status_Heating")
        self.Layout_Status_Heating.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_22, 1, 1, 1, 1)

        self.frame_18 = QFrame(self.frame_30)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(3, 0))
        self.frame_18.setMaximumSize(QSize(3, 70))
        self.frame_18.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.Layout_Status_MSStatus.addWidget(self.frame_18, 1, 6, 1, 1)

        self.frame_25 = QFrame(self.frame_30)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(90, 0))
        self.frame_25.setMaximumSize(QSize(90, 16777215))
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.Layout_Status_KeepTemp = QGridLayout(self.frame_25)
        self.Layout_Status_KeepTemp.setSpacing(0)
        self.Layout_Status_KeepTemp.setObjectName(u"Layout_Status_KeepTemp")
        self.Layout_Status_KeepTemp.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_25, 1, 2, 1, 1)

        self.frame_28 = QFrame(self.frame_30)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(90, 0))
        self.frame_28.setMaximumSize(QSize(90, 16777215))
        self.frame_28.setStyleSheet(u"")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.Layout_Status_EthernetConnecton = QGridLayout(self.frame_28)
        self.Layout_Status_EthernetConnecton.setSpacing(0)
        self.Layout_Status_EthernetConnecton.setObjectName(u"Layout_Status_EthernetConnecton")
        self.Layout_Status_EthernetConnecton.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_28, 1, 7, 1, 1)

        self.frame_24 = QFrame(self.frame_30)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(90, 0))
        self.frame_24.setMaximumSize(QSize(90, 16777215))
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.Layout_Status_STOP = QGridLayout(self.frame_24)
        self.Layout_Status_STOP.setSpacing(0)
        self.Layout_Status_STOP.setObjectName(u"Layout_Status_STOP")
        self.Layout_Status_STOP.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_24, 1, 0, 1, 1)

        self.frame_26 = QFrame(self.frame_30)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(90, 0))
        self.frame_26.setMaximumSize(QSize(90, 16777215))
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.Layout_Status_Error = QGridLayout(self.frame_26)
        self.Layout_Status_Error.setSpacing(0)
        self.Layout_Status_Error.setObjectName(u"Layout_Status_Error")
        self.Layout_Status_Error.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_26, 1, 5, 1, 1)

        self.frame_23 = QFrame(self.frame_30)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(90, 0))
        self.frame_23.setMaximumSize(QSize(90, 16777215))
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.Layout_Status_TestFinishing = QGridLayout(self.frame_23)
        self.Layout_Status_TestFinishing.setSpacing(0)
        self.Layout_Status_TestFinishing.setObjectName(u"Layout_Status_TestFinishing")
        self.Layout_Status_TestFinishing.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_23, 1, 4, 1, 1)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(90, 0))
        self.frame_31.setMaximumSize(QSize(90, 16777215))
        self.frame_31.setStyleSheet(u"")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.Layout_Status_GPIBConnecton_2 = QGridLayout(self.frame_31)
        self.Layout_Status_GPIBConnecton_2.setSpacing(0)
        self.Layout_Status_GPIBConnecton_2.setObjectName(u"Layout_Status_GPIBConnecton_2")
        self.Layout_Status_GPIBConnecton_2.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_31, 1, 9, 1, 1)

        self.frame_27 = QFrame(self.frame_30)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(90, 0))
        self.frame_27.setMaximumSize(QSize(90, 16777215))
        self.frame_27.setStyleSheet(u"")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.Layout_Status_Testing = QGridLayout(self.frame_27)
        self.Layout_Status_Testing.setSpacing(0)
        self.Layout_Status_Testing.setObjectName(u"Layout_Status_Testing")
        self.Layout_Status_Testing.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_27, 1, 3, 1, 1)

        self.frame_29 = QFrame(self.frame_30)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(90, 0))
        self.frame_29.setMaximumSize(QSize(90, 16777215))
        self.frame_29.setStyleSheet(u"")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.Layout_Status_GPIBConnecton_1 = QGridLayout(self.frame_29)
        self.Layout_Status_GPIBConnecton_1.setSpacing(0)
        self.Layout_Status_GPIBConnecton_1.setObjectName(u"Layout_Status_GPIBConnecton_1")
        self.Layout_Status_GPIBConnecton_1.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_29, 1, 8, 1, 1)

        self.label_28 = QLabel(self.frame_30)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_28, 0, 1, 1, 1)

        self.label_30 = QLabel(self.frame_30)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_30, 0, 2, 1, 1)

        self.label_37 = QLabel(self.frame_30)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_37, 0, 3, 1, 1)

        self.label_38 = QLabel(self.frame_30)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_38, 0, 4, 1, 1)

        self.label_39 = QLabel(self.frame_30)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_39, 0, 5, 1, 1)

        self.label_40 = QLabel(self.frame_30)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_40, 0, 8, 1, 1)

        self.label_44 = QLabel(self.frame_30)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_44, 0, 9, 1, 1)

        self.label_45 = QLabel(self.frame_30)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_45, 0, 7, 1, 1)

        self.frame_27.raise_()
        self.frame_26.raise_()
        self.frame_29.raise_()
        self.frame_28.raise_()
        self.frame_18.raise_()
        self.frame_24.raise_()
        self.frame_22.raise_()
        self.frame_23.raise_()
        self.frame_25.raise_()
        self.frame_31.raise_()
        self.label_28.raise_()
        self.label_30.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.label_40.raise_()
        self.label_44.raise_()
        self.label_45.raise_()
        self.label_17.raise_()

        self.horizontalLayout_2.addWidget(self.frame_30)


        self.gridLayout_5.addWidget(self.frame_13, 0, 0, 1, 1)

        self.frame_14 = QFrame(self.gridFrame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 60))
        self.frame_14.setMaximumSize(QSize(16777215, 60))
        self.frame_14.setStyleSheet(u"border:none")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_14)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_14)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(200, 0))
        self.frame_21.setMaximumSize(QSize(220, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_21)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_35 = QLabel(self.frame_21)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(80, 30))
        self.label_35.setMaximumSize(QSize(60, 16777215))
        self.label_35.setStyleSheet(u"font: 18px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.label_35, 0, 0, 1, 1)

        self.label_36 = QLabel(self.frame_21)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(120, 0))
        self.label_36.setMaximumSize(QSize(120, 16777215))
        self.label_36.setStyleSheet(u"font: 30px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"background-color: rgb(16, 18, 22);")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.label_36, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_21, 0, 2, 1, 1)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(200, 0))
        self.frame_17.setMaximumSize(QSize(220, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_17)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_31 = QLabel(self.frame_17)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(80, 30))
        self.label_31.setMaximumSize(QSize(60, 16777215))
        self.label_31.setStyleSheet(u"font: 18px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_30.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_32 = QLabel(self.frame_17)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(120, 0))
        self.label_32.setMaximumSize(QSize(120, 16777215))
        self.label_32.setStyleSheet(u"font: 30px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"background-color: rgb(16, 18, 22);")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_30.addWidget(self.label_32, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_17, 0, 1, 1, 1)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(200, 0))
        self.frame_16.setMaximumSize(QSize(220, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_16)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(80, 30))
        self.label_23.setMaximumSize(QSize(60, 16777215))
        self.label_23.setStyleSheet(u"font: 18px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_26 = QLabel(self.frame_16)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(120, 0))
        self.label_26.setMaximumSize(QSize(120, 16777215))
        self.label_26.setStyleSheet(u"font: 30px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"background-color: rgb(16, 18, 22);")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_26, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_16, 0, 0, 1, 1)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(200, 0))
        self.frame_19.setMaximumSize(QSize(220, 16777215))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_19)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_33 = QLabel(self.frame_19)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(80, 30))
        self.label_33.setMaximumSize(QSize(60, 16777215))
        self.label_33.setStyleSheet(u"font: 18px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_31.addWidget(self.label_33, 0, 0, 1, 1)

        self.label_34 = QLabel(self.frame_19)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(120, 0))
        self.label_34.setMaximumSize(QSize(120, 16777215))
        self.label_34.setStyleSheet(u"font: 30px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"background-color: rgb(16, 18, 22);")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_31.addWidget(self.label_34, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_19, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.frame_14, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gridFrame_2, 0, 0, 1, 1)

        self.pages.addWidget(self.page_2)
        self.gridFrame_1.raise_()
        self.gridFrame_2.raise_()
        self.gridFrame_3.raise_()
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.scrollArea_2 = QScrollArea(self.page_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"border:none;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1181, 1216))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_20 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 0))
        self.frame_20.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 34, 41);\n"
"	border-color:rgb(30, 34, 41);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_20)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_29 = QLabel(self.frame_20)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(150, 0))
        self.label_29.setMaximumSize(QSize(130, 16777215))
        self.label_29.setStyleSheet(u"font: 20px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_6.addWidget(self.label_29, 0, 0, 2, 1)

        self.label_25 = QLabel(self.frame_20)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(80, 0))
        self.label_25.setMaximumSize(QSize(80, 16777215))
        self.label_25.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_6.addWidget(self.label_25, 1, 2, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_20)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(400, 32))
        self.lineEdit_11.setMaximumSize(QSize(212, 16777215))
        self.lineEdit_11.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:200;")

        self.gridLayout_6.addWidget(self.lineEdit_11, 1, 3, 1, 1)

        self.label_27 = QLabel(self.frame_20)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(80, 0))
        self.label_27.setMaximumSize(QSize(80, 16777215))
        self.label_27.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_6.addWidget(self.label_27, 0, 2, 1, 1)

        self.frame_37 = QFrame(self.frame_20)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(200, 0))
        self.frame_37.setMaximumSize(QSize(16777215, 16777215))
        self.frame_37.setStyleSheet(u"")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_37)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(9, 0, 9, 0)
        self.frame_40 = QFrame(self.frame_37)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(40, 0))
        self.frame_40.setMaximumSize(QSize(40, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_40)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_26.addWidget(self.frame_40, 0, 0, 1, 1)

        self.frame_41 = QFrame(self.frame_37)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(3, 0))
        self.frame_41.setMaximumSize(QSize(3, 16777215))
        self.frame_41.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color: rgb(44, 49, 60);")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.gridLayout_26.addWidget(self.frame_41, 0, 2, 1, 1)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(40, 0))
        self.frame_39.setMaximumSize(QSize(40, 16777215))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_39)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_26.addWidget(self.frame_39, 0, 1, 1, 1)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(40, 0))
        self.frame_38.setMaximumSize(QSize(40, 16777215))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_38)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_26.addWidget(self.frame_38, 0, 3, 1, 1)


        self.gridLayout_6.addWidget(self.frame_37, 0, 4, 2, 1, Qt.AlignRight|Qt.AlignVCenter)

        self.scrollArea_3 = QScrollArea(self.frame_20)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setMinimumSize(QSize(0, 500))
        self.scrollArea_3.setStyleSheet(u"background-color: rgb(30, 34, 41);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1141, 498))
        self.gridLayout_24 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.frame_35 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setMinimumSize(QSize(0, 0))
        self.frame_35.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 28, 34);\n"
"	border-color:rgb(30, 34, 41);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.gridLayout_24.addWidget(self.frame_35, 0, 0, 1, 1)

        self.frame_36 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        self.frame_36.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 28, 34);\n"
"	border-color: rgb(36, 41, 49);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_36)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_32 = QFrame(self.frame_36)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 0))
        self.frame_32.setMaximumSize(QSize(16777215, 16777215))
        self.frame_32.setStyleSheet(u"")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)

        self.gridLayout_22.addWidget(self.frame_32, 0, 0, 1, 1, Qt.AlignLeft)


        self.gridLayout_24.addWidget(self.frame_36, 1, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_6.addWidget(self.scrollArea_3, 2, 0, 1, 5)

        self.frame_33 = QFrame(self.frame_20)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(3, 0))
        self.frame_33.setMaximumSize(QSize(3, 16777215))
        self.frame_33.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color:rgb(44, 49, 60);\n"
"border-width: 1px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_33, 0, 1, 2, 1)

        self.comboBox_6 = QComboBox(self.frame_20)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(200, 32))
        self.comboBox_6.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_6.addWidget(self.comboBox_6, 0, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_20)

        self.frame_34 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 0))
        self.frame_34.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 34, 41);\n"
"	border-color:rgb(30, 34, 41);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.frame_34)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.label_41 = QLabel(self.frame_34)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(150, 0))
        self.label_41.setMaximumSize(QSize(130, 16777215))
        self.label_41.setStyleSheet(u"font: 20px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_47.addWidget(self.label_41, 0, 0, 2, 1)

        self.label_42 = QLabel(self.frame_34)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(80, 0))
        self.label_42.setMaximumSize(QSize(80, 16777215))
        self.label_42.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_47.addWidget(self.label_42, 1, 2, 1, 1)

        self.lineEdit_14 = QLineEdit(self.frame_34)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(400, 32))
        self.lineEdit_14.setMaximumSize(QSize(212, 16777215))
        self.lineEdit_14.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:200;")

        self.gridLayout_47.addWidget(self.lineEdit_14, 1, 3, 1, 1)

        self.label_43 = QLabel(self.frame_34)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(80, 0))
        self.label_43.setMaximumSize(QSize(80, 16777215))
        self.label_43.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_47.addWidget(self.label_43, 0, 2, 1, 1)

        self.frame_60 = QFrame(self.frame_34)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(200, 0))
        self.frame_60.setMaximumSize(QSize(16777215, 16777215))
        self.frame_60.setStyleSheet(u"")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_60)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(9, 0, 9, 0)
        self.frame_61 = QFrame(self.frame_60)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(40, 0))
        self.frame_61.setMaximumSize(QSize(40, 16777215))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_61)
        self.gridLayout_49.setSpacing(0)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_48.addWidget(self.frame_61, 0, 0, 1, 1)

        self.frame_62 = QFrame(self.frame_60)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(3, 0))
        self.frame_62.setMaximumSize(QSize(3, 16777215))
        self.frame_62.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color: rgb(44, 49, 60);")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.gridLayout_48.addWidget(self.frame_62, 0, 2, 1, 1)

        self.frame_63 = QFrame(self.frame_60)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(40, 0))
        self.frame_63.setMaximumSize(QSize(40, 16777215))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.frame_63)
        self.gridLayout_50.setSpacing(0)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_48.addWidget(self.frame_63, 0, 1, 1, 1)

        self.frame_64 = QFrame(self.frame_60)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(40, 0))
        self.frame_64.setMaximumSize(QSize(40, 16777215))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.frame_64)
        self.gridLayout_51.setSpacing(0)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_48.addWidget(self.frame_64, 0, 3, 1, 1)


        self.gridLayout_47.addWidget(self.frame_60, 0, 4, 2, 1, Qt.AlignRight|Qt.AlignVCenter)

        self.scrollArea_6 = QScrollArea(self.frame_34)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMinimumSize(QSize(0, 500))
        self.scrollArea_6.setStyleSheet(u"background-color: rgb(30, 34, 41);")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1141, 498))
        self.gridLayout_52 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.frame_65 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 28, 34);\n"
"	border-color:rgb(30, 34, 41);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)

        self.gridLayout_52.addWidget(self.frame_65, 0, 0, 1, 1)

        self.frame_66 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 28, 34);\n"
"	border-color: rgb(36, 41, 49);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.gridLayout_53 = QGridLayout(self.frame_66)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.frame_67 = QFrame(self.frame_66)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(0, 270))
        self.frame_67.setMaximumSize(QSize(16777215, 16777215))
        self.frame_67.setStyleSheet(u"")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)

        self.gridLayout_53.addWidget(self.frame_67, 0, 0, 1, 1, Qt.AlignLeft)


        self.gridLayout_52.addWidget(self.frame_66, 1, 0, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_47.addWidget(self.scrollArea_6, 2, 0, 1, 5)

        self.frame_68 = QFrame(self.frame_34)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(3, 0))
        self.frame_68.setMaximumSize(QSize(3, 16777215))
        self.frame_68.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color:rgb(44, 49, 60);\n"
"border-width: 1px;")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)

        self.gridLayout_47.addWidget(self.frame_68, 0, 1, 2, 1)

        self.comboBox_9 = QComboBox(self.frame_34)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMinimumSize(QSize(200, 32))
        self.comboBox_9.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_47.addWidget(self.comboBox_9, 0, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_34)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.page_3_layout.addWidget(self.scrollArea_2)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setEnabled(True)
        self.page_4.setStyleSheet(u"")
        self.pages.addWidget(self.page_4)

        self.gridLayout_8.addWidget(self.pages, 0, 1, 1, 1)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(1)
        self.comboBox_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainPages", u"42", None))
        self.label_6.setText("")
        self.radioButton.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u6e2c\u5b9a", None))
        self.label.setText("")
        self.lineEdit_2.setText(QCoreApplication.translate("MainPages", u"MS-4371", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainPages", u"\u9ec4", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainPages", u"42", None))
        self.lineEdit.setText(QCoreApplication.translate("MainPages", u"2021", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u5143", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainPages", u"\u682a\u5f0f\u4f1a\u793e\u30e2\u30c8\u30e4\u30de", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"\u8a66\u6599\u306e\u539a\u3055(mm)", None))
        self.label_22.setText(QCoreApplication.translate("MainPages", u"\u6750\u6599", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"\u30ac\u30fc\u30c9\u96fb\u6975\u306e\u5185\u5f84(mm)", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainPages", u"\u8a55\u4fa1\u8a66\u9a13", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u6e2c\u5b9a\u756a\u53f7", None))
        self.label_yesr.setText(QCoreApplication.translate("MainPages", u"\u5e74\u5ea6", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainPages", u"15", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"\u4e3b\u96fb\u6975\u5f84(mm)", None))
        self.label_7.setText("")
        self.label_5.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u8005", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.label_24.setText(QCoreApplication.translate("MainPages", u"\u8a66\u6599\u540d\u79f0", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainPages", u"material_1", None))
        self.label_46.setText(QCoreApplication.translate("MainPages", u"\u96fb\u6c17\u7089\u63a5\u7d9a", None))
        self.label_47.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u5668\u63a5\u7d9a", None))
        self.btn_AutoMode.setText(QCoreApplication.translate("MainPages", u"\u81ea\u52d5\u30e2\u30fc\u30c9", None))
        self.btn_ManaualMode.setText(QCoreApplication.translate("MainPages", u"\u624b\u52d5\u30e2\u30fc\u30c9", None))
        self.label_11.setText("")
        self.radioButton_6.setText(QCoreApplication.translate("MainPages", u"\u771f\u7a7a", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainPages", u"\u5927\u6c17", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainPages", u"N2\u7f6e\u63db", None))
        self.label_14.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainPages", u"\u5927\u6c17\u5727", None))
        self.pushButton.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u958b\u59cb", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u505c\u6b62", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainPages", u"\u30c6\u30b9\u30c8\u30d1\u30bf\u30fc\u30f3\u540d", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainPages", u"pattern1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainPages", u"pattern2", None))

        self.pushButton_7.setText(QCoreApplication.translate("MainPages", u"\u96fb\u5727\u5370\u52a0", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainPages", u"\u30de\u30cb\u30e5\u30a2\u30eb\u6e2c\u5b9a", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainPages", u"\u51fa\u529b\u505c\u6b62", None))
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_21.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u30e2\u30fc\u30c9", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainPages", u"\u9023\u7d9a\u4e8c\u56de\u6e2c\u5b9a", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainPages", u"\u4e00\u56de\u6e2c\u5b9a", None))

        self.lineEdit_8.setText(QCoreApplication.translate("MainPages", u"350", None))
        self.label_20.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u96fb\u5727(V)", None))
        self.label_2.setText("")
        self.label_17.setText(QCoreApplication.translate("MainPages", u"\u505c\u6b62\u4e2d", None))
        self.label_28.setText(QCoreApplication.translate("MainPages", u"\u6607\u6e29\u4e2d", None))
        self.label_30.setText(QCoreApplication.translate("MainPages", u"\u6e29\u5ea6\u30ad\u30fc\u30d7\u4e2d", None))
        self.label_37.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u4e2d", None))
        self.label_38.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u7d42\u4e86(\u964d\u6e29\u4e2d)", None))
        self.label_39.setText(QCoreApplication.translate("MainPages", u"\u8b66\u5831\u767a\u751f\u4e2d", None))
        self.label_40.setText(QCoreApplication.translate("MainPages", u"2657A\u63a5\u7d9a", None))
        self.label_44.setText(QCoreApplication.translate("MainPages", u"2635B\u63a5\u7d9a", None))
        self.label_45.setText(QCoreApplication.translate("MainPages", u"\u96fb\u6c17\u7089\u63a5\u7d9a", None))
        self.label_35.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u96fb\u6d41", None))
        self.label_36.setText(QCoreApplication.translate("MainPages", u"100uA", None))
        self.label_31.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u96fb\u5727", None))
        self.label_32.setText(QCoreApplication.translate("MainPages", u"450V", None))
        self.label_23.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u6e29\u5ea6", None))
        self.label_26.setText(QCoreApplication.translate("MainPages", u"1200\u2103", None))
        self.label_33.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u62b5\u6297", None))
        self.label_34.setText(QCoreApplication.translate("MainPages", u"10\u03a9", None))
        self.label_29.setText(QCoreApplication.translate("MainPages", u"\u30c6\u30b9\u30c8\u30d1\u30bf\u30fc\u30f3", None))
        self.label_25.setText(QCoreApplication.translate("MainPages", u"\u8a3b\u8a18", None))
        self.label_27.setText(QCoreApplication.translate("MainPages", u"\u30d1\u30bf\u30fc\u30f3\u540d", None))
        self.label_41.setText(QCoreApplication.translate("MainPages", u"\u30c6\u30b9\u30c8\u30d1\u30bf\u30fc\u30f3", None))
        self.label_42.setText(QCoreApplication.translate("MainPages", u"\u8a3b\u8a18", None))
        self.label_43.setText(QCoreApplication.translate("MainPages", u"\u30d1\u30bf\u30fc\u30f3\u540d", None))
    # retranslateUi

