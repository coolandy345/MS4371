# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pageskTEEKB.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1091, 707)
        MainPages.setMinimumSize(QSize(0, 0))
        MainPages.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"background-color: rgb(44, 49, 60);\n"
"\n"
"border-radius: 5px;\n"
"border-style: solid;")
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
        self.pages.setStyleSheet(u"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border-color: rgb(231, 214, 85);\n"
"	border-width: 5px;\n"
"	border-radius: 5px;\n"
"	border-style: solid;\n"
"	border:none;\n"
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
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.gridLayout_17 = QGridLayout(self.page_1)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(9, 9, 9, 9)
        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1038, 759))
        self.scrollAreaWidgetContents.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_10)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_48 = QFrame(self.frame_42)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 0))
        self.frame_48.setMaximumSize(QSize(16777215, 300))
        self.frame_48.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_48)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(12)
        self.lineEdit_testNumber = QLineEdit(self.frame_48)
        self.lineEdit_testNumber.setObjectName(u"lineEdit_testNumber")
        sizePolicy.setHeightForWidth(self.lineEdit_testNumber.sizePolicy().hasHeightForWidth())
        self.lineEdit_testNumber.setSizePolicy(sizePolicy)
        self.lineEdit_testNumber.setMinimumSize(QSize(200, 30))
        self.lineEdit_testNumber.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_testNumber.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.lineEdit_testNumber, 1, 1, 1, 1)

        self.Costom_Test_RadioButton = QRadioButton(self.frame_48)
        self.Costom_Test_RadioButton.setObjectName(u"Costom_Test_RadioButton")
        sizePolicy.setHeightForWidth(self.Costom_Test_RadioButton.sizePolicy().hasHeightForWidth())
        self.Costom_Test_RadioButton.setSizePolicy(sizePolicy)
        self.Costom_Test_RadioButton.setMinimumSize(QSize(100, 35))
        self.Costom_Test_RadioButton.setMaximumSize(QSize(100, 32))
        self.Costom_Test_RadioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.Costom_Test_RadioButton.setLayoutDirection(Qt.RightToLeft)
        self.Costom_Test_RadioButton.setStyleSheet(u"background-color: rgb(36, 40, 49);")

        self.gridLayout_7.addWidget(self.Costom_Test_RadioButton, 3, 0, 1, 1)

        self.label_60 = QLabel(self.frame_48)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(100, 35))
        self.label_60.setMaximumSize(QSize(100, 35))
        self.label_60.setStyleSheet(u"")
        self.label_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_60, 1, 0, 1, 1)

        self.QC_Test_RadioButton = QRadioButton(self.frame_48)
        self.QC_Test_RadioButton.setObjectName(u"QC_Test_RadioButton")
        sizePolicy.setHeightForWidth(self.QC_Test_RadioButton.sizePolicy().hasHeightForWidth())
        self.QC_Test_RadioButton.setSizePolicy(sizePolicy)
        self.QC_Test_RadioButton.setMinimumSize(QSize(100, 35))
        self.QC_Test_RadioButton.setMaximumSize(QSize(100, 35))
        self.QC_Test_RadioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.QC_Test_RadioButton.setLayoutDirection(Qt.RightToLeft)
        self.QC_Test_RadioButton.setStyleSheet(u"background-color: rgb(36, 40, 49);")
        self.QC_Test_RadioButton.setChecked(False)

        self.gridLayout_7.addWidget(self.QC_Test_RadioButton, 2, 0, 1, 1)

        self.lineEdit_year = QLineEdit(self.frame_48)
        self.lineEdit_year.setObjectName(u"lineEdit_year")
        sizePolicy.setHeightForWidth(self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy)
        self.lineEdit_year.setMinimumSize(QSize(60, 30))
        self.lineEdit_year.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_year.setStyleSheet(u"")
        self.lineEdit_year.setFrame(False)
        self.lineEdit_year.setEchoMode(QLineEdit.Normal)
        self.lineEdit_year.setCursorPosition(4)

        self.gridLayout_7.addWidget(self.lineEdit_year, 0, 1, 1, 1)

        self.label_year = QLabel(self.frame_48)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setMinimumSize(QSize(100, 35))
        self.label_year.setMaximumSize(QSize(100, 35))
        self.label_year.setMouseTracking(True)
        self.label_year.setLayoutDirection(Qt.LeftToRight)
        self.label_year.setStyleSheet(u"")
        self.label_year.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_year.setMargin(0)

        self.gridLayout_7.addWidget(self.label_year, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_48)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(12)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_costomer = QLineEdit(self.frame_2)
        self.lineEdit_costomer.setObjectName(u"lineEdit_costomer")
        sizePolicy.setHeightForWidth(self.lineEdit_costomer.sizePolicy().hasHeightForWidth())
        self.lineEdit_costomer.setSizePolicy(sizePolicy)
        self.lineEdit_costomer.setMinimumSize(QSize(200, 30))
        self.lineEdit_costomer.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_costomer.setStyleSheet(u"")

        self.gridLayout_12.addWidget(self.lineEdit_costomer, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 35))
        self.label_4.setMaximumSize(QSize(100, 35))
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(100, 35))
        self.label_5.setMaximumSize(QSize(100, 35))
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_costomerName = QLineEdit(self.frame_2)
        self.lineEdit_costomerName.setObjectName(u"lineEdit_costomerName")
        sizePolicy.setHeightForWidth(self.lineEdit_costomerName.sizePolicy().hasHeightForWidth())
        self.lineEdit_costomerName.setSizePolicy(sizePolicy)
        self.lineEdit_costomerName.setMinimumSize(QSize(200, 30))
        self.lineEdit_costomerName.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_costomerName.setStyleSheet(u"")

        self.gridLayout_12.addWidget(self.lineEdit_costomerName, 1, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_2, 4, 0, 1, 2, Qt.AlignTop)


        self.horizontalLayout_9.addWidget(self.frame_48, 0, Qt.AlignTop)

        self.frame_63 = QFrame(self.frame_42)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(3, 0))
        self.frame_63.setMaximumSize(QSize(3, 16777215))
        self.frame_63.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.horizontalLayout_9.addWidget(self.frame_63, 0, Qt.AlignLeft)

        self.frame_62 = QFrame(self.frame_42)
        self.frame_62.setObjectName(u"frame_62")
        sizePolicy.setHeightForWidth(self.frame_62.sizePolicy().hasHeightForWidth())
        self.frame_62.setSizePolicy(sizePolicy)
        self.frame_62.setMinimumSize(QSize(0, 0))
        self.frame_62.setMaximumSize(QSize(16777215, 16777215))
        self.frame_62.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_62)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(12)
        self.label_32 = QLabel(self.frame_62)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(140, 35))
        self.label_32.setMaximumSize(QSize(140, 35))
        self.label_32.setStyleSheet(u"")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_32, 6, 0, 1, 1)

        self.lineEdit_testMeterialName = QLineEdit(self.frame_62)
        self.lineEdit_testMeterialName.setObjectName(u"lineEdit_testMeterialName")
        self.lineEdit_testMeterialName.setMinimumSize(QSize(200, 30))
        self.lineEdit_testMeterialName.setMaximumSize(QSize(200, 30))
        self.lineEdit_testMeterialName.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.lineEdit_testMeterialName, 0, 1, 1, 1)

        self.lineEdit_meterialArea = QLabel(self.frame_62)
        self.lineEdit_meterialArea.setObjectName(u"lineEdit_meterialArea")
        self.lineEdit_meterialArea.setMinimumSize(QSize(0, 0))
        self.lineEdit_meterialArea.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_meterialArea.setStyleSheet(u"")
        self.lineEdit_meterialArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.lineEdit_meterialArea, 5, 1, 1, 1)

        self.lineEdit_testMeterial = QLineEdit(self.frame_62)
        self.lineEdit_testMeterial.setObjectName(u"lineEdit_testMeterial")
        self.lineEdit_testMeterial.setMinimumSize(QSize(200, 30))
        self.lineEdit_testMeterial.setMaximumSize(QSize(200, 30))
        self.lineEdit_testMeterial.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.lineEdit_testMeterial, 1, 1, 1, 1)

        self.label_10 = QLabel(self.frame_62)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(140, 35))
        self.label_10.setMaximumSize(QSize(140, 35))
        self.label_10.setStyleSheet(u"")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_10, 4, 0, 1, 1)

        self.lineEdit_thinkness = QLineEdit(self.frame_62)
        self.lineEdit_thinkness.setObjectName(u"lineEdit_thinkness")
        self.lineEdit_thinkness.setMinimumSize(QSize(0, 30))
        self.lineEdit_thinkness.setMaximumSize(QSize(60, 30))
        self.lineEdit_thinkness.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.lineEdit_thinkness, 4, 1, 1, 1)

        self.label_26 = QLabel(self.frame_62)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(140, 35))
        self.label_26.setMaximumSize(QSize(140, 35))
        self.label_26.setStyleSheet(u"")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_26, 5, 0, 1, 1)

        self.label_8 = QLabel(self.frame_62)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(140, 35))
        self.label_8.setMaximumSize(QSize(140, 35))
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_8, 2, 0, 1, 1)

        self.lineEdit_MeterialinnerDie = QLineEdit(self.frame_62)
        self.lineEdit_MeterialinnerDie.setObjectName(u"lineEdit_MeterialinnerDie")
        self.lineEdit_MeterialinnerDie.setMinimumSize(QSize(0, 30))
        self.lineEdit_MeterialinnerDie.setMaximumSize(QSize(60, 30))
        self.lineEdit_MeterialinnerDie.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.lineEdit_MeterialinnerDie, 3, 1, 1, 1)

        self.label_24 = QLabel(self.frame_62)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(140, 35))
        self.label_24.setMaximumSize(QSize(140, 35))
        self.label_24.setStyleSheet(u"")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_24, 0, 0, 1, 1)

        self.lineEdit_MeterialMainDie = QLineEdit(self.frame_62)
        self.lineEdit_MeterialMainDie.setObjectName(u"lineEdit_MeterialMainDie")
        self.lineEdit_MeterialMainDie.setMinimumSize(QSize(0, 30))
        self.lineEdit_MeterialMainDie.setMaximumSize(QSize(60, 30))
        self.lineEdit_MeterialMainDie.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.lineEdit_MeterialMainDie, 2, 1, 1, 1)

        self.label_9 = QLabel(self.frame_62)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(140, 35))
        self.label_9.setMaximumSize(QSize(140, 35))
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_22 = QLabel(self.frame_62)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(140, 35))
        self.label_22.setMaximumSize(QSize(140, 35))
        self.label_22.setStyleSheet(u"")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_22, 1, 0, 1, 1)

        self.lineEdit_meterialVolume = QLabel(self.frame_62)
        self.lineEdit_meterialVolume.setObjectName(u"lineEdit_meterialVolume")
        self.lineEdit_meterialVolume.setMinimumSize(QSize(0, 0))
        self.lineEdit_meterialVolume.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_meterialVolume.setStyleSheet(u"")
        self.lineEdit_meterialVolume.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.lineEdit_meterialVolume, 6, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_62, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_42, 0, Qt.AlignLeft)

        self.frame_64 = QFrame(self.frame_10)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(0, 6))
        self.frame_64.setMaximumSize(QSize(16777215, 6))
        self.frame_64.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_64)

        self.frame_47 = QFrame(self.frame_10)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_72 = QFrame(self.frame_47)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(0, 180))
        self.frame_72.setMaximumSize(QSize(16777215, 180))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_77 = QFrame(self.frame_72)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(150, 180))
        self.frame_77.setMaximumSize(QSize(150, 180))
        self.frame_77.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.gridLayout_63 = QGridLayout(self.frame_77)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.gridLayout_63.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_0_D = QLineEdit(self.frame_77)
        self.lineEdit_PID_0_D.setObjectName(u"lineEdit_PID_0_D")
        self.lineEdit_PID_0_D.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_0_D.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_0_D.setStyleSheet(u"")
        self.lineEdit_PID_0_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_63.addWidget(self.lineEdit_PID_0_D, 3, 1, 1, 1)

        self.lineEdit_PID_0_I = QLineEdit(self.frame_77)
        self.lineEdit_PID_0_I.setObjectName(u"lineEdit_PID_0_I")
        self.lineEdit_PID_0_I.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_0_I.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_0_I.setStyleSheet(u"")
        self.lineEdit_PID_0_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_63.addWidget(self.lineEdit_PID_0_I, 2, 1, 1, 1)

        self.label_121 = QLabel(self.frame_77)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(0, 32))
        self.label_121.setMaximumSize(QSize(16777215, 32))
        self.label_121.setStyleSheet(u"")
        self.label_121.setAlignment(Qt.AlignCenter)

        self.gridLayout_63.addWidget(self.label_121, 0, 0, 1, 2)

        self.label_122 = QLabel(self.frame_77)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(0, 32))
        self.label_122.setMaximumSize(QSize(16777215, 32))
        self.label_122.setStyleSheet(u"")
        self.label_122.setAlignment(Qt.AlignCenter)

        self.gridLayout_63.addWidget(self.label_122, 2, 0, 1, 1)

        self.label_123 = QLabel(self.frame_77)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(0, 32))
        self.label_123.setMaximumSize(QSize(16777215, 32))
        self.label_123.setStyleSheet(u"")
        self.label_123.setAlignment(Qt.AlignCenter)

        self.gridLayout_63.addWidget(self.label_123, 1, 0, 1, 1)

        self.label_124 = QLabel(self.frame_77)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(0, 32))
        self.label_124.setMaximumSize(QSize(16777215, 32))
        self.label_124.setStyleSheet(u"")
        self.label_124.setAlignment(Qt.AlignCenter)

        self.gridLayout_63.addWidget(self.label_124, 3, 0, 1, 1)

        self.lineEdit_PID_0_P = QLineEdit(self.frame_77)
        self.lineEdit_PID_0_P.setObjectName(u"lineEdit_PID_0_P")
        self.lineEdit_PID_0_P.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_0_P.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_0_P.setStyleSheet(u"")
        self.lineEdit_PID_0_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_63.addWidget(self.lineEdit_PID_0_P, 1, 1, 1, 1)

        self.lineEdit_PID_0_I.raise_()
        self.label_121.raise_()
        self.label_122.raise_()
        self.label_123.raise_()
        self.label_124.raise_()
        self.lineEdit_PID_0_P.raise_()
        self.lineEdit_PID_0_D.raise_()

        self.horizontalLayout_10.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.frame_72)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(150, 180))
        self.frame_78.setMaximumSize(QSize(150, 180))
        self.frame_78.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.gridLayout_64 = QGridLayout(self.frame_78)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_1_D = QLineEdit(self.frame_78)
        self.lineEdit_PID_1_D.setObjectName(u"lineEdit_PID_1_D")
        self.lineEdit_PID_1_D.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_1_D.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_1_D.setStyleSheet(u"")
        self.lineEdit_PID_1_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.lineEdit_PID_1_D, 3, 1, 1, 1)

        self.lineEdit_PID_1_I = QLineEdit(self.frame_78)
        self.lineEdit_PID_1_I.setObjectName(u"lineEdit_PID_1_I")
        self.lineEdit_PID_1_I.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_1_I.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_1_I.setStyleSheet(u"")
        self.lineEdit_PID_1_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.lineEdit_PID_1_I, 2, 1, 1, 1)

        self.label_125 = QLabel(self.frame_78)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(0, 32))
        self.label_125.setMaximumSize(QSize(16777215, 32))
        self.label_125.setStyleSheet(u"")
        self.label_125.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.label_125, 0, 0, 1, 2)

        self.label_126 = QLabel(self.frame_78)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(0, 32))
        self.label_126.setMaximumSize(QSize(16777215, 32))
        self.label_126.setStyleSheet(u"")
        self.label_126.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.label_126, 2, 0, 1, 1)

        self.label_127 = QLabel(self.frame_78)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(0, 32))
        self.label_127.setMaximumSize(QSize(16777215, 32))
        self.label_127.setStyleSheet(u"")
        self.label_127.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.label_127, 1, 0, 1, 1)

        self.label_128 = QLabel(self.frame_78)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(0, 32))
        self.label_128.setMaximumSize(QSize(16777215, 32))
        self.label_128.setStyleSheet(u"")
        self.label_128.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.label_128, 3, 0, 1, 1)

        self.lineEdit_PID_1_P = QLineEdit(self.frame_78)
        self.lineEdit_PID_1_P.setObjectName(u"lineEdit_PID_1_P")
        self.lineEdit_PID_1_P.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_1_P.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_1_P.setStyleSheet(u"")
        self.lineEdit_PID_1_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_64.addWidget(self.lineEdit_PID_1_P, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.frame_72)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(150, 180))
        self.frame_79.setMaximumSize(QSize(150, 180))
        self.frame_79.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.gridLayout_66 = QGridLayout(self.frame_79)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_2_D = QLineEdit(self.frame_79)
        self.lineEdit_PID_2_D.setObjectName(u"lineEdit_PID_2_D")
        self.lineEdit_PID_2_D.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_2_D.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_2_D.setStyleSheet(u"")
        self.lineEdit_PID_2_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.lineEdit_PID_2_D, 3, 1, 1, 1)

        self.lineEdit_PID_2_I = QLineEdit(self.frame_79)
        self.lineEdit_PID_2_I.setObjectName(u"lineEdit_PID_2_I")
        self.lineEdit_PID_2_I.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_2_I.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_2_I.setStyleSheet(u"")
        self.lineEdit_PID_2_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.lineEdit_PID_2_I, 2, 1, 1, 1)

        self.label_133 = QLabel(self.frame_79)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMinimumSize(QSize(0, 32))
        self.label_133.setMaximumSize(QSize(16777215, 32))
        self.label_133.setStyleSheet(u"")
        self.label_133.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.label_133, 0, 0, 1, 2)

        self.label_134 = QLabel(self.frame_79)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(0, 32))
        self.label_134.setMaximumSize(QSize(16777215, 32))
        self.label_134.setStyleSheet(u"")
        self.label_134.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.label_134, 2, 0, 1, 1)

        self.label_135 = QLabel(self.frame_79)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMinimumSize(QSize(0, 32))
        self.label_135.setMaximumSize(QSize(16777215, 32))
        self.label_135.setStyleSheet(u"")
        self.label_135.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.label_135, 1, 0, 1, 1)

        self.label_136 = QLabel(self.frame_79)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMinimumSize(QSize(0, 32))
        self.label_136.setMaximumSize(QSize(16777215, 32))
        self.label_136.setStyleSheet(u"")
        self.label_136.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.label_136, 3, 0, 1, 1)

        self.lineEdit_PID_2_P = QLineEdit(self.frame_79)
        self.lineEdit_PID_2_P.setObjectName(u"lineEdit_PID_2_P")
        self.lineEdit_PID_2_P.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_2_P.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_2_P.setStyleSheet(u"")
        self.lineEdit_PID_2_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_66.addWidget(self.lineEdit_PID_2_P, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_79)

        self.frame_80 = QFrame(self.frame_72)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(150, 180))
        self.frame_80.setMaximumSize(QSize(150, 180))
        self.frame_80.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.gridLayout_67 = QGridLayout(self.frame_80)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_3_D = QLineEdit(self.frame_80)
        self.lineEdit_PID_3_D.setObjectName(u"lineEdit_PID_3_D")
        self.lineEdit_PID_3_D.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_3_D.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_3_D.setStyleSheet(u"")
        self.lineEdit_PID_3_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_67.addWidget(self.lineEdit_PID_3_D, 3, 1, 1, 1)

        self.lineEdit_PID_3_I = QLineEdit(self.frame_80)
        self.lineEdit_PID_3_I.setObjectName(u"lineEdit_PID_3_I")
        self.lineEdit_PID_3_I.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_3_I.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_3_I.setStyleSheet(u"")
        self.lineEdit_PID_3_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_67.addWidget(self.lineEdit_PID_3_I, 2, 1, 1, 1)

        self.label_137 = QLabel(self.frame_80)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setMinimumSize(QSize(0, 32))
        self.label_137.setMaximumSize(QSize(16777215, 32))
        self.label_137.setStyleSheet(u"")
        self.label_137.setAlignment(Qt.AlignCenter)

        self.gridLayout_67.addWidget(self.label_137, 0, 0, 1, 2)

        self.label_138 = QLabel(self.frame_80)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMinimumSize(QSize(0, 32))
        self.label_138.setMaximumSize(QSize(16777215, 32))
        self.label_138.setStyleSheet(u"")
        self.label_138.setAlignment(Qt.AlignCenter)

        self.gridLayout_67.addWidget(self.label_138, 2, 0, 1, 1)

        self.label_139 = QLabel(self.frame_80)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMinimumSize(QSize(0, 32))
        self.label_139.setMaximumSize(QSize(16777215, 32))
        self.label_139.setStyleSheet(u"")
        self.label_139.setAlignment(Qt.AlignCenter)

        self.gridLayout_67.addWidget(self.label_139, 1, 0, 1, 1)

        self.label_140 = QLabel(self.frame_80)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(0, 32))
        self.label_140.setMaximumSize(QSize(16777215, 32))
        self.label_140.setStyleSheet(u"")
        self.label_140.setAlignment(Qt.AlignCenter)

        self.gridLayout_67.addWidget(self.label_140, 3, 0, 1, 1)

        self.lineEdit_PID_3_P = QLineEdit(self.frame_80)
        self.lineEdit_PID_3_P.setObjectName(u"lineEdit_PID_3_P")
        self.lineEdit_PID_3_P.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_3_P.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_3_P.setStyleSheet(u"")
        self.lineEdit_PID_3_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_67.addWidget(self.lineEdit_PID_3_P, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_72)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(150, 180))
        self.frame_81.setMaximumSize(QSize(150, 180))
        self.frame_81.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.gridLayout_68 = QGridLayout(self.frame_81)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_4_D = QLineEdit(self.frame_81)
        self.lineEdit_PID_4_D.setObjectName(u"lineEdit_PID_4_D")
        self.lineEdit_PID_4_D.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_4_D.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_4_D.setStyleSheet(u"")
        self.lineEdit_PID_4_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_68.addWidget(self.lineEdit_PID_4_D, 3, 1, 1, 1)

        self.lineEdit_PID_4_I = QLineEdit(self.frame_81)
        self.lineEdit_PID_4_I.setObjectName(u"lineEdit_PID_4_I")
        self.lineEdit_PID_4_I.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_4_I.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_4_I.setStyleSheet(u"")
        self.lineEdit_PID_4_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_68.addWidget(self.lineEdit_PID_4_I, 2, 1, 1, 1)

        self.label_141 = QLabel(self.frame_81)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMinimumSize(QSize(0, 32))
        self.label_141.setMaximumSize(QSize(16777215, 32))
        self.label_141.setStyleSheet(u"")
        self.label_141.setAlignment(Qt.AlignCenter)

        self.gridLayout_68.addWidget(self.label_141, 0, 0, 1, 2)

        self.label_142 = QLabel(self.frame_81)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMinimumSize(QSize(0, 32))
        self.label_142.setMaximumSize(QSize(16777215, 32))
        self.label_142.setStyleSheet(u"")
        self.label_142.setAlignment(Qt.AlignCenter)

        self.gridLayout_68.addWidget(self.label_142, 2, 0, 1, 1)

        self.label_143 = QLabel(self.frame_81)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(0, 32))
        self.label_143.setMaximumSize(QSize(16777215, 32))
        self.label_143.setStyleSheet(u"")
        self.label_143.setAlignment(Qt.AlignCenter)

        self.gridLayout_68.addWidget(self.label_143, 1, 0, 1, 1)

        self.label_144 = QLabel(self.frame_81)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(0, 32))
        self.label_144.setMaximumSize(QSize(16777215, 32))
        self.label_144.setStyleSheet(u"")
        self.label_144.setAlignment(Qt.AlignCenter)

        self.gridLayout_68.addWidget(self.label_144, 3, 0, 1, 1)

        self.lineEdit_PID_4_P = QLineEdit(self.frame_81)
        self.lineEdit_PID_4_P.setObjectName(u"lineEdit_PID_4_P")
        self.lineEdit_PID_4_P.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_4_P.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_4_P.setStyleSheet(u"")
        self.lineEdit_PID_4_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_68.addWidget(self.lineEdit_PID_4_P, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_81)


        self.horizontalLayout_11.addWidget(self.frame_72, 0, Qt.AlignLeft)


        self.verticalLayout_9.addWidget(self.frame_47)

        self.frame_82 = QFrame(self.frame_10)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(0, 180))
        self.frame_83.setMaximumSize(QSize(16777215, 180))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.frame_83)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(150, 180))
        self.frame_84.setMaximumSize(QSize(150, 180))
        self.frame_84.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.gridLayout_65 = QGridLayout(self.frame_84)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_5_D = QLineEdit(self.frame_84)
        self.lineEdit_PID_5_D.setObjectName(u"lineEdit_PID_5_D")
        self.lineEdit_PID_5_D.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_5_D.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_5_D.setStyleSheet(u"")
        self.lineEdit_PID_5_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.lineEdit_PID_5_D, 3, 1, 1, 1)

        self.lineEdit_PID_5_I = QLineEdit(self.frame_84)
        self.lineEdit_PID_5_I.setObjectName(u"lineEdit_PID_5_I")
        self.lineEdit_PID_5_I.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_5_I.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_5_I.setStyleSheet(u"")
        self.lineEdit_PID_5_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.lineEdit_PID_5_I, 2, 1, 1, 1)

        self.label_129 = QLabel(self.frame_84)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(0, 32))
        self.label_129.setMaximumSize(QSize(16777215, 32))
        self.label_129.setStyleSheet(u"")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.label_129, 0, 0, 1, 2)

        self.label_130 = QLabel(self.frame_84)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(0, 32))
        self.label_130.setMaximumSize(QSize(16777215, 32))
        self.label_130.setStyleSheet(u"")
        self.label_130.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.label_130, 2, 0, 1, 1)

        self.label_131 = QLabel(self.frame_84)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMinimumSize(QSize(0, 32))
        self.label_131.setMaximumSize(QSize(16777215, 32))
        self.label_131.setStyleSheet(u"")
        self.label_131.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.label_131, 1, 0, 1, 1)

        self.label_132 = QLabel(self.frame_84)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(0, 32))
        self.label_132.setMaximumSize(QSize(16777215, 32))
        self.label_132.setStyleSheet(u"")
        self.label_132.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.label_132, 3, 0, 1, 1)

        self.lineEdit_PID_5_P = QLineEdit(self.frame_84)
        self.lineEdit_PID_5_P.setObjectName(u"lineEdit_PID_5_P")
        self.lineEdit_PID_5_P.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_5_P.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_5_P.setStyleSheet(u"")
        self.lineEdit_PID_5_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_65.addWidget(self.lineEdit_PID_5_P, 1, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.frame_83)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(150, 180))
        self.frame_85.setMaximumSize(QSize(150, 180))
        self.frame_85.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.gridLayout_69 = QGridLayout(self.frame_85)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.gridLayout_69.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_6_D = QLineEdit(self.frame_85)
        self.lineEdit_PID_6_D.setObjectName(u"lineEdit_PID_6_D")
        self.lineEdit_PID_6_D.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_6_D.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_6_D.setStyleSheet(u"")
        self.lineEdit_PID_6_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_69.addWidget(self.lineEdit_PID_6_D, 3, 1, 1, 1)

        self.lineEdit_PID_6_I = QLineEdit(self.frame_85)
        self.lineEdit_PID_6_I.setObjectName(u"lineEdit_PID_6_I")
        self.lineEdit_PID_6_I.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_6_I.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_6_I.setStyleSheet(u"")
        self.lineEdit_PID_6_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_69.addWidget(self.lineEdit_PID_6_I, 2, 1, 1, 1)

        self.label_145 = QLabel(self.frame_85)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(0, 32))
        self.label_145.setMaximumSize(QSize(16777215, 32))
        self.label_145.setStyleSheet(u"")
        self.label_145.setAlignment(Qt.AlignCenter)

        self.gridLayout_69.addWidget(self.label_145, 0, 0, 1, 2)

        self.label_146 = QLabel(self.frame_85)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(0, 32))
        self.label_146.setMaximumSize(QSize(16777215, 32))
        self.label_146.setStyleSheet(u"")
        self.label_146.setAlignment(Qt.AlignCenter)

        self.gridLayout_69.addWidget(self.label_146, 2, 0, 1, 1)

        self.label_147 = QLabel(self.frame_85)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMinimumSize(QSize(0, 32))
        self.label_147.setMaximumSize(QSize(16777215, 32))
        self.label_147.setStyleSheet(u"")
        self.label_147.setAlignment(Qt.AlignCenter)

        self.gridLayout_69.addWidget(self.label_147, 1, 0, 1, 1)

        self.label_148 = QLabel(self.frame_85)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setMinimumSize(QSize(0, 32))
        self.label_148.setMaximumSize(QSize(16777215, 32))
        self.label_148.setStyleSheet(u"")
        self.label_148.setAlignment(Qt.AlignCenter)

        self.gridLayout_69.addWidget(self.label_148, 3, 0, 1, 1)

        self.lineEdit_PID_6_P = QLineEdit(self.frame_85)
        self.lineEdit_PID_6_P.setObjectName(u"lineEdit_PID_6_P")
        self.lineEdit_PID_6_P.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_6_P.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_6_P.setStyleSheet(u"")
        self.lineEdit_PID_6_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_69.addWidget(self.lineEdit_PID_6_P, 1, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.frame_83)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(150, 180))
        self.frame_86.setMaximumSize(QSize(150, 180))
        self.frame_86.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.gridLayout_70 = QGridLayout(self.frame_86)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.gridLayout_70.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_7_D = QLineEdit(self.frame_86)
        self.lineEdit_PID_7_D.setObjectName(u"lineEdit_PID_7_D")
        self.lineEdit_PID_7_D.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_7_D.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_7_D.setStyleSheet(u"")
        self.lineEdit_PID_7_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_70.addWidget(self.lineEdit_PID_7_D, 3, 1, 1, 1)

        self.lineEdit_PID_7_I = QLineEdit(self.frame_86)
        self.lineEdit_PID_7_I.setObjectName(u"lineEdit_PID_7_I")
        self.lineEdit_PID_7_I.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_7_I.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_7_I.setStyleSheet(u"")
        self.lineEdit_PID_7_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_70.addWidget(self.lineEdit_PID_7_I, 2, 1, 1, 1)

        self.label_149 = QLabel(self.frame_86)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMinimumSize(QSize(0, 32))
        self.label_149.setMaximumSize(QSize(16777215, 32))
        self.label_149.setStyleSheet(u"")
        self.label_149.setAlignment(Qt.AlignCenter)

        self.gridLayout_70.addWidget(self.label_149, 0, 0, 1, 2)

        self.label_150 = QLabel(self.frame_86)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMinimumSize(QSize(0, 32))
        self.label_150.setMaximumSize(QSize(16777215, 32))
        self.label_150.setStyleSheet(u"")
        self.label_150.setAlignment(Qt.AlignCenter)

        self.gridLayout_70.addWidget(self.label_150, 2, 0, 1, 1)

        self.label_151 = QLabel(self.frame_86)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMinimumSize(QSize(0, 32))
        self.label_151.setMaximumSize(QSize(16777215, 32))
        self.label_151.setStyleSheet(u"")
        self.label_151.setAlignment(Qt.AlignCenter)

        self.gridLayout_70.addWidget(self.label_151, 1, 0, 1, 1)

        self.label_152 = QLabel(self.frame_86)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMinimumSize(QSize(0, 32))
        self.label_152.setMaximumSize(QSize(16777215, 32))
        self.label_152.setStyleSheet(u"")
        self.label_152.setAlignment(Qt.AlignCenter)

        self.gridLayout_70.addWidget(self.label_152, 3, 0, 1, 1)

        self.lineEdit_PID_7_P = QLineEdit(self.frame_86)
        self.lineEdit_PID_7_P.setObjectName(u"lineEdit_PID_7_P")
        self.lineEdit_PID_7_P.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_7_P.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_7_P.setStyleSheet(u"")
        self.lineEdit_PID_7_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_70.addWidget(self.lineEdit_PID_7_P, 1, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.frame_83)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(150, 180))
        self.frame_87.setMaximumSize(QSize(150, 180))
        self.frame_87.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.gridLayout_71 = QGridLayout(self.frame_87)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_71.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_8_D = QLineEdit(self.frame_87)
        self.lineEdit_PID_8_D.setObjectName(u"lineEdit_PID_8_D")
        self.lineEdit_PID_8_D.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_8_D.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_8_D.setStyleSheet(u"")
        self.lineEdit_PID_8_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_71.addWidget(self.lineEdit_PID_8_D, 3, 1, 1, 1)

        self.lineEdit_PID_8_I = QLineEdit(self.frame_87)
        self.lineEdit_PID_8_I.setObjectName(u"lineEdit_PID_8_I")
        self.lineEdit_PID_8_I.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_8_I.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_8_I.setStyleSheet(u"")
        self.lineEdit_PID_8_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_71.addWidget(self.lineEdit_PID_8_I, 2, 1, 1, 1)

        self.label_153 = QLabel(self.frame_87)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMinimumSize(QSize(0, 32))
        self.label_153.setMaximumSize(QSize(16777215, 32))
        self.label_153.setStyleSheet(u"")
        self.label_153.setAlignment(Qt.AlignCenter)

        self.gridLayout_71.addWidget(self.label_153, 0, 0, 1, 2)

        self.label_154 = QLabel(self.frame_87)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setMinimumSize(QSize(0, 32))
        self.label_154.setMaximumSize(QSize(16777215, 32))
        self.label_154.setStyleSheet(u"")
        self.label_154.setAlignment(Qt.AlignCenter)

        self.gridLayout_71.addWidget(self.label_154, 2, 0, 1, 1)

        self.label_155 = QLabel(self.frame_87)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMinimumSize(QSize(0, 32))
        self.label_155.setMaximumSize(QSize(16777215, 32))
        self.label_155.setStyleSheet(u"")
        self.label_155.setAlignment(Qt.AlignCenter)

        self.gridLayout_71.addWidget(self.label_155, 1, 0, 1, 1)

        self.label_156 = QLabel(self.frame_87)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setMinimumSize(QSize(0, 32))
        self.label_156.setMaximumSize(QSize(16777215, 32))
        self.label_156.setStyleSheet(u"")
        self.label_156.setAlignment(Qt.AlignCenter)

        self.gridLayout_71.addWidget(self.label_156, 3, 0, 1, 1)

        self.lineEdit_PID_8_P = QLineEdit(self.frame_87)
        self.lineEdit_PID_8_P.setObjectName(u"lineEdit_PID_8_P")
        self.lineEdit_PID_8_P.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_8_P.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_8_P.setStyleSheet(u"")
        self.lineEdit_PID_8_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_71.addWidget(self.lineEdit_PID_8_P, 1, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.frame_83)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(150, 180))
        self.frame_88.setMaximumSize(QSize(150, 180))
        self.frame_88.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 40, 49);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding-left:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.gridLayout_72 = QGridLayout(self.frame_88)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gridLayout_72.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_9_D = QLineEdit(self.frame_88)
        self.lineEdit_PID_9_D.setObjectName(u"lineEdit_PID_9_D")
        self.lineEdit_PID_9_D.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_9_D.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_9_D.setStyleSheet(u"")
        self.lineEdit_PID_9_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_72.addWidget(self.lineEdit_PID_9_D, 3, 1, 1, 1)

        self.lineEdit_PID_9_I = QLineEdit(self.frame_88)
        self.lineEdit_PID_9_I.setObjectName(u"lineEdit_PID_9_I")
        self.lineEdit_PID_9_I.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_9_I.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_9_I.setStyleSheet(u"")
        self.lineEdit_PID_9_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_72.addWidget(self.lineEdit_PID_9_I, 2, 1, 1, 1)

        self.label_157 = QLabel(self.frame_88)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMinimumSize(QSize(0, 32))
        self.label_157.setMaximumSize(QSize(16777215, 32))
        self.label_157.setStyleSheet(u"")
        self.label_157.setAlignment(Qt.AlignCenter)

        self.gridLayout_72.addWidget(self.label_157, 0, 0, 1, 2)

        self.label_158 = QLabel(self.frame_88)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setMinimumSize(QSize(0, 32))
        self.label_158.setMaximumSize(QSize(16777215, 32))
        self.label_158.setStyleSheet(u"")
        self.label_158.setAlignment(Qt.AlignCenter)

        self.gridLayout_72.addWidget(self.label_158, 2, 0, 1, 1)

        self.label_159 = QLabel(self.frame_88)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setMinimumSize(QSize(0, 32))
        self.label_159.setMaximumSize(QSize(16777215, 32))
        self.label_159.setStyleSheet(u"")
        self.label_159.setAlignment(Qt.AlignCenter)

        self.gridLayout_72.addWidget(self.label_159, 1, 0, 1, 1)

        self.label_160 = QLabel(self.frame_88)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMinimumSize(QSize(0, 32))
        self.label_160.setMaximumSize(QSize(16777215, 32))
        self.label_160.setStyleSheet(u"")
        self.label_160.setAlignment(Qt.AlignCenter)

        self.gridLayout_72.addWidget(self.label_160, 3, 0, 1, 1)

        self.lineEdit_PID_9_P = QLineEdit(self.frame_88)
        self.lineEdit_PID_9_P.setObjectName(u"lineEdit_PID_9_P")
        self.lineEdit_PID_9_P.setMinimumSize(QSize(0, 30))
        self.lineEdit_PID_9_P.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_PID_9_P.setStyleSheet(u"")
        self.lineEdit_PID_9_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_72.addWidget(self.lineEdit_PID_9_P, 1, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_88)


        self.horizontalLayout_16.addWidget(self.frame_83, 0, Qt.AlignLeft)


        self.verticalLayout_9.addWidget(self.frame_82)


        self.horizontalLayout_12.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_17.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QFrame{\n"
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
"QCheckBox{\n"
"	color: rgb(225, 230, 241);\n"
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
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QComboBox:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	border-width: 1px;\n"
"}\n"
""
                        "QComboBox:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QComboBox:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridFrame_2 = QFrame(self.page_2)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridFrame_2.setMinimumSize(QSize(0, 240))
        self.gridFrame_2.setMaximumSize(QSize(16777215, 240))
        self.gridFrame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 34, 41);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.gridFrame_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.gridFrame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"")
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
        self.label_17.setStyleSheet(u"")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_40 = QLabel(self.frame_30)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_40, 0, 2, 1, 1)

        self.frame_25 = QFrame(self.frame_30)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(60, 60))
        self.frame_25.setMaximumSize(QSize(60, 60))
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.Layout_Status_KeepTemp = QGridLayout(self.frame_25)
        self.Layout_Status_KeepTemp.setSpacing(0)
        self.Layout_Status_KeepTemp.setObjectName(u"Layout_Status_KeepTemp")
        self.Layout_Status_KeepTemp.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_25, 1, 4, 1, 1)

        self.frame_26 = QFrame(self.frame_30)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(60, 60))
        self.frame_26.setMaximumSize(QSize(60, 60))
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.Layout_Status_Error = QGridLayout(self.frame_26)
        self.Layout_Status_Error.setSpacing(0)
        self.Layout_Status_Error.setObjectName(u"Layout_Status_Error")
        self.Layout_Status_Error.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_26, 1, 7, 1, 1)

        self.frame_27 = QFrame(self.frame_30)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(60, 60))
        self.frame_27.setMaximumSize(QSize(60, 60))
        self.frame_27.setStyleSheet(u"")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.Layout_Status_Testing = QGridLayout(self.frame_27)
        self.Layout_Status_Testing.setSpacing(0)
        self.Layout_Status_Testing.setObjectName(u"Layout_Status_Testing")
        self.Layout_Status_Testing.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_27, 1, 5, 1, 1)

        self.label_37 = QLabel(self.frame_30)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_37, 0, 5, 1, 1)

        self.frame_22 = QFrame(self.frame_30)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(60, 60))
        self.frame_22.setMaximumSize(QSize(60, 60))
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.Layout_Status_Heating = QGridLayout(self.frame_22)
        self.Layout_Status_Heating.setSpacing(0)
        self.Layout_Status_Heating.setObjectName(u"Layout_Status_Heating")
        self.Layout_Status_Heating.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_22, 1, 3, 1, 1)

        self.label_39 = QLabel(self.frame_30)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 30))
        self.label_39.setStyleSheet(u"")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_39, 0, 7, 1, 1)

        self.frame_23 = QFrame(self.frame_30)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(60, 60))
        self.frame_23.setMaximumSize(QSize(60, 60))
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.Layout_Status_TestFinishing = QGridLayout(self.frame_23)
        self.Layout_Status_TestFinishing.setSpacing(0)
        self.Layout_Status_TestFinishing.setObjectName(u"Layout_Status_TestFinishing")
        self.Layout_Status_TestFinishing.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_23, 1, 6, 1, 1)

        self.label_38 = QLabel(self.frame_30)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_38, 0, 6, 1, 1)

        self.label_45 = QLabel(self.frame_30)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_45, 0, 0, 1, 1)

        self.frame_24 = QFrame(self.frame_30)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(60, 60))
        self.frame_24.setMaximumSize(QSize(60, 60))
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.Layout_Status_STOP = QGridLayout(self.frame_24)
        self.Layout_Status_STOP.setSpacing(0)
        self.Layout_Status_STOP.setObjectName(u"Layout_Status_STOP")
        self.Layout_Status_STOP.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_24, 1, 1, 1, 1)

        self.frame_28 = QFrame(self.frame_30)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(60, 60))
        self.frame_28.setMaximumSize(QSize(60, 60))
        self.frame_28.setStyleSheet(u"")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.Layout_Status_RunReady = QGridLayout(self.frame_28)
        self.Layout_Status_RunReady.setSpacing(0)
        self.Layout_Status_RunReady.setObjectName(u"Layout_Status_RunReady")
        self.Layout_Status_RunReady.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_28, 1, 0, 1, 1)

        self.label_30 = QLabel(self.frame_30)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_30, 0, 4, 1, 1)

        self.frame_29 = QFrame(self.frame_30)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(60, 60))
        self.frame_29.setMaximumSize(QSize(60, 60))
        self.frame_29.setStyleSheet(u"")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.Layout_Status_Vacuum = QGridLayout(self.frame_29)
        self.Layout_Status_Vacuum.setSpacing(0)
        self.Layout_Status_Vacuum.setObjectName(u"Layout_Status_Vacuum")
        self.Layout_Status_Vacuum.setContentsMargins(0, 0, 0, 0)

        self.Layout_Status_MSStatus.addWidget(self.frame_29, 1, 2, 1, 1)

        self.label_28 = QLabel(self.frame_30)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_28, 0, 3, 1, 1)

        self.frame_27.raise_()
        self.frame_26.raise_()
        self.frame_24.raise_()
        self.frame_22.raise_()
        self.frame_23.raise_()
        self.frame_25.raise_()
        self.label_28.raise_()
        self.label_30.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.label_17.raise_()
        self.label_45.raise_()
        self.frame_28.raise_()
        self.label_40.raise_()
        self.frame_29.raise_()

        self.horizontalLayout_2.addWidget(self.frame_30)


        self.gridLayout_5.addWidget(self.frame_13, 0, 0, 1, 1)

        self.frame_14 = QFrame(self.gridFrame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 50))
        self.frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.frame_14.setStyleSheet(u"font: 15px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_14)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(200, 0))
        self.frame_17.setMaximumSize(QSize(16777215, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_17)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.realtime_Voltage_lineEdit = QLabel(self.frame_17)
        self.realtime_Voltage_lineEdit.setObjectName(u"realtime_Voltage_lineEdit")
        self.realtime_Voltage_lineEdit.setMinimumSize(QSize(0, 50))
        self.realtime_Voltage_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.realtime_Voltage_lineEdit.setStyleSheet(u"font: 30px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"background-color: rgb(16, 18, 22);")
        self.realtime_Voltage_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_30.addWidget(self.realtime_Voltage_lineEdit, 0, 1, 1, 1)

        self.label_31 = QLabel(self.frame_17)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(80, 30))
        self.label_31.setMaximumSize(QSize(60, 16777215))
        self.label_31.setStyleSheet(u"")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_30.addWidget(self.label_31, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_17, 1, 0, 1, 1)

        self.frame_21 = QFrame(self.frame_14)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(200, 0))
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_21)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_34 = QLabel(self.frame_21)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(80, 30))
        self.label_34.setMaximumSize(QSize(60, 16777215))
        self.label_34.setStyleSheet(u"")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.label_34, 0, 0, 1, 1)

        self.realtime_Resistor_lineEdit = QLabel(self.frame_21)
        self.realtime_Resistor_lineEdit.setObjectName(u"realtime_Resistor_lineEdit")
        self.realtime_Resistor_lineEdit.setMinimumSize(QSize(0, 50))
        self.realtime_Resistor_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.realtime_Resistor_lineEdit.setStyleSheet(u"font: 30px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"background-color: rgb(16, 18, 22);")
        self.realtime_Resistor_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.realtime_Resistor_lineEdit, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_21, 1, 3, 1, 1)

        self.frame_67 = QFrame(self.frame_14)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(200, 0))
        self.frame_67.setMaximumSize(QSize(16777215, 16777215))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_67)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.label_35 = QLabel(self.frame_67)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(80, 30))
        self.label_35.setMaximumSize(QSize(60, 16777215))
        self.label_35.setStyleSheet(u"")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_33.addWidget(self.label_35, 0, 0, 1, 1)

        self.realtime_Current_lineEdit = QLabel(self.frame_67)
        self.realtime_Current_lineEdit.setObjectName(u"realtime_Current_lineEdit")
        self.realtime_Current_lineEdit.setMinimumSize(QSize(0, 50))
        self.realtime_Current_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.realtime_Current_lineEdit.setStyleSheet(u"font: 30px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"background-color: rgb(16, 18, 22);")
        self.realtime_Current_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_33.addWidget(self.realtime_Current_lineEdit, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_67, 1, 2, 1, 1)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(200, 0))
        self.frame_16.setMaximumSize(QSize(16777215, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_16)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(80, 30))
        self.label_23.setMaximumSize(QSize(60, 16777215))
        self.label_23.setStyleSheet(u"")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_23, 0, 0, 1, 1)

        self.realtime_Temp_lineEdit = QLabel(self.frame_16)
        self.realtime_Temp_lineEdit.setObjectName(u"realtime_Temp_lineEdit")
        self.realtime_Temp_lineEdit.setMinimumSize(QSize(0, 50))
        self.realtime_Temp_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.realtime_Temp_lineEdit.setStyleSheet(u"font: 30px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"background-color: rgb(16, 18, 22);")
        self.realtime_Temp_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.realtime_Temp_lineEdit, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_16, 0, 0, 1, 1)

        self.frame_89 = QFrame(self.frame_14)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(200, 0))
        self.frame_89.setMaximumSize(QSize(16777215, 16777215))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_89)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_48 = QLabel(self.frame_89)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(80, 30))
        self.label_48.setMaximumSize(QSize(60, 16777215))
        self.label_48.setStyleSheet(u"")
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_48, 0, 0, 1, 1)

        self.realtime_Pressure_lineEdit = QLabel(self.frame_89)
        self.realtime_Pressure_lineEdit.setObjectName(u"realtime_Pressure_lineEdit")
        self.realtime_Pressure_lineEdit.setMinimumSize(QSize(0, 50))
        self.realtime_Pressure_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.realtime_Pressure_lineEdit.setStyleSheet(u"font: 30px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"background-color: rgb(16, 18, 22);")
        self.realtime_Pressure_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.realtime_Pressure_lineEdit, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_89, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frame_14, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gridFrame_2, 1, 0, 1, 1)

        self.gridFrame_1 = QFrame(self.page_2)
        self.gridFrame_1.setObjectName(u"gridFrame_1")
        self.gridFrame_1.setMinimumSize(QSize(0, 0))
        self.gridFrame_1.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 34, 41);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
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
        self.frame_65 = QFrame(self.frame)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.graphItem_label = QLabel(self.frame_65)
        self.graphItem_label.setObjectName(u"graphItem_label")
        self.graphItem_label.setStyleSheet(u"")
        self.graphItem_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.graphItem_label)

        self.graphItem_combobox = QComboBox(self.frame_65)
        self.graphItem_combobox.addItem("")
        self.graphItem_combobox.addItem("")
        self.graphItem_combobox.setObjectName(u"graphItem_combobox")
        self.graphItem_combobox.setMinimumSize(QSize(100, 25))
        self.graphItem_combobox.setMaximumSize(QSize(16777215, 16777215))
        self.graphItem_combobox.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.graphItem_combobox)

        self.frame_19 = QFrame(self.frame_65)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.frame_19)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(3, 0))
        self.frame_66.setMaximumSize(QSize(3, 16777215))
        self.frame_66.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_66)

        self.timeUnit_Label = QLabel(self.frame_19)
        self.timeUnit_Label.setObjectName(u"timeUnit_Label")
        self.timeUnit_Label.setStyleSheet(u"")
        self.timeUnit_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.timeUnit_Label)

        self.timeUnit_comboBox = QComboBox(self.frame_19)
        self.timeUnit_comboBox.addItem("")
        self.timeUnit_comboBox.addItem("")
        self.timeUnit_comboBox.addItem("")
        self.timeUnit_comboBox.addItem("")
        self.timeUnit_comboBox.addItem("")
        self.timeUnit_comboBox.addItem("")
        self.timeUnit_comboBox.setObjectName(u"timeUnit_comboBox")
        self.timeUnit_comboBox.setMinimumSize(QSize(0, 25))
        self.timeUnit_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.timeUnit_comboBox.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.timeUnit_comboBox)

        self.frame_69 = QFrame(self.frame_19)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(3, 0))
        self.frame_69.setMaximumSize(QSize(3, 16777215))
        self.frame_69.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:none;")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_69)

        self.Resistor_checkBox = QCheckBox(self.frame_19)
        self.Resistor_checkBox.setObjectName(u"Resistor_checkBox")
        self.Resistor_checkBox.setMinimumSize(QSize(0, 25))
        self.Resistor_checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.Resistor_checkBox.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"padding:5px")

        self.horizontalLayout_5.addWidget(self.Resistor_checkBox)

        self.Voltage_checkBox = QCheckBox(self.frame_19)
        self.Voltage_checkBox.setObjectName(u"Voltage_checkBox")
        self.Voltage_checkBox.setMinimumSize(QSize(0, 25))
        self.Voltage_checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.Voltage_checkBox.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"padding:5px")

        self.horizontalLayout_5.addWidget(self.Voltage_checkBox)

        self.Current_checkBox = QCheckBox(self.frame_19)
        self.Current_checkBox.setObjectName(u"Current_checkBox")
        self.Current_checkBox.setMinimumSize(QSize(0, 25))
        self.Current_checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.Current_checkBox.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"padding:5px")

        self.horizontalLayout_5.addWidget(self.Current_checkBox)


        self.horizontalLayout_4.addWidget(self.frame_19)


        self.gridLayout.addWidget(self.frame_65, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.frame_76 = QFrame(self.frame)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 0))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.realtime_grapgLayout = QGridLayout(self.frame_76)
        self.realtime_grapgLayout.setObjectName(u"realtime_grapgLayout")
        self.realtime_grapgLayout.setContentsMargins(-1, -1, 25, -1)

        self.gridLayout.addWidget(self.frame_76, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gridFrame_1, 2, 0, 1, 1)

        self.frame_31 = QFrame(self.page_2)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(250, 0))
        self.frame_31.setMaximumSize(QSize(250, 16777215))
        self.frame_31.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 34, 41);\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_31)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.frame_31)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 60))
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(30, 30))
        self.frame_15.setMaximumSize(QSize(16777215, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.Layout_Status_EthernetConnecton = QGridLayout(self.frame_15)
        self.Layout_Status_EthernetConnecton.setObjectName(u"Layout_Status_EthernetConnecton")
        self.Layout_Status_EthernetConnecton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.frame_15)

        self.frame_45 = QFrame(self.frame_3)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(30, 30))
        self.frame_45.setMaximumSize(QSize(16777215, 16777215))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.Layout_Status_USBConnecton = QGridLayout(self.frame_45)
        self.Layout_Status_USBConnecton.setObjectName(u"Layout_Status_USBConnecton")
        self.Layout_Status_USBConnecton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.frame_45)

        self.frame_60 = QFrame(self.frame_3)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(30, 30))
        self.frame_60.setMaximumSize(QSize(16777215, 16777215))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.Layout_Status_2657A_GPIBConnecton = QGridLayout(self.frame_60)
        self.Layout_Status_2657A_GPIBConnecton.setObjectName(u"Layout_Status_2657A_GPIBConnecton")
        self.Layout_Status_2657A_GPIBConnecton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_3)
        self.frame_61.setObjectName(u"frame_61")
        sizePolicy.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy)
        self.frame_61.setMinimumSize(QSize(30, 30))
        self.frame_61.setMaximumSize(QSize(16777215, 16777215))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.Layout_Status_2635B_GPIBConnecton = QGridLayout(self.frame_61)
        self.Layout_Status_2635B_GPIBConnecton.setObjectName(u"Layout_Status_2635B_GPIBConnecton")
        self.Layout_Status_2635B_GPIBConnecton.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.frame_61)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.label_2 = QLabel(self.frame_31)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 3))
        self.label_2.setMaximumSize(QSize(16777215, 3))
        self.label_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame_18 = QFrame(self.frame_31)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QSize(30, 50))
        self.frame_18.setMaximumSize(QSize(16777215, 50))
        self.frame_18.setStyleSheet(u"border:none")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.remoteConnect_pushButton = QPushButton(self.frame_18)
        self.remoteConnect_pushButton.setObjectName(u"remoteConnect_pushButton")
        self.remoteConnect_pushButton.setMinimumSize(QSize(210, 30))
        self.remoteConnect_pushButton.setMaximumSize(QSize(210, 30))
        self.remoteConnect_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.remoteConnect_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.remoteConnect_pushButton.setStyleSheet(u"QPushButton:enabled {\n"
"	color: rgb(202, 206, 216);\n"
"	font: 15px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(70, 80, 95);\n"
"	background-color: rgba(0, 0, 0,30);\n"
"	font: 15px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(79, 159, 238);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(109, 182, 238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(69, 140, 207);\n"
"}\n"
"\n"
"")
        self.remoteConnect_pushButton.setCheckable(True)
        self.remoteConnect_pushButton.setChecked(False)
        self.remoteConnect_pushButton.setAutoRepeatInterval(100)

        self.horizontalLayout_8.addWidget(self.remoteConnect_pushButton)


        self.verticalLayout_4.addWidget(self.frame_18)

        self.frame_7 = QFrame(self.frame_31)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border:none")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridFrame = QFrame(self.frame_7)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setMinimumSize(QSize(0, 0))
        self.gridFrame.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.gridFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_AutoMode = QRadioButton(self.gridFrame)
        self.btn_AutoMode.setObjectName(u"btn_AutoMode")
        sizePolicy.setHeightForWidth(self.btn_AutoMode.sizePolicy().hasHeightForWidth())
        self.btn_AutoMode.setSizePolicy(sizePolicy)
        self.btn_AutoMode.setMinimumSize(QSize(120, 0))
        self.btn_AutoMode.setMaximumSize(QSize(120, 16777215))
        self.btn_AutoMode.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_AutoMode.setStyleSheet(u"background-color: rgb(30, 34, 41);\n"
"min-width:100;\n"
"max-width:100;\n"
"padding-left:20px;\n"
"")
        self.btn_AutoMode.setCheckable(True)
        self.btn_AutoMode.setChecked(True)

        self.horizontalLayout.addWidget(self.btn_AutoMode)

        self.btn_ManaualMode = QRadioButton(self.gridFrame)
        self.btn_ManaualMode.setObjectName(u"btn_ManaualMode")
        sizePolicy.setHeightForWidth(self.btn_ManaualMode.sizePolicy().hasHeightForWidth())
        self.btn_ManaualMode.setSizePolicy(sizePolicy)
        self.btn_ManaualMode.setMinimumSize(QSize(130, 0))
        self.btn_ManaualMode.setMaximumSize(QSize(130, 16777215))
        self.btn_ManaualMode.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ManaualMode.setStyleSheet(u"background-color: rgb(30, 34, 41);\n"
"min-width:120;\n"
"max-width:120;\n"
"padding-left:10px;\n"
"")
        self.btn_ManaualMode.setCheckable(True)
        self.btn_ManaualMode.setChecked(False)

        self.horizontalLayout.addWidget(self.btn_ManaualMode)


        self.verticalLayout_8.addWidget(self.gridFrame)

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
        self.frame_4 = QFrame(self.frame_8)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gasFreeflow_pushButton = QPushButton(self.frame_4)
        self.gasFreeflow_pushButton.setObjectName(u"gasFreeflow_pushButton")
        sizePolicy.setHeightForWidth(self.gasFreeflow_pushButton.sizePolicy().hasHeightForWidth())
        self.gasFreeflow_pushButton.setSizePolicy(sizePolicy)
        self.gasFreeflow_pushButton.setMinimumSize(QSize(0, 40))
        self.gasFreeflow_pushButton.setMaximumSize(QSize(16777215, 40))
        self.gasFreeflow_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.gasFreeflow_pushButton.setTabletTracking(False)
        self.gasFreeflow_pushButton.setStyleSheet(u"QPushButton:enabled {\n"
"	color: rgb(202, 206, 216);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(70, 80, 95);\n"
"	background-color: rgba(0, 0, 0,30);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(148, 227, 114);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(158, 239, 120);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(125, 189, 95);\n"
"}\n"
"")
        self.gasFreeflow_pushButton.setCheckable(True)

        self.verticalLayout_7.addWidget(self.gasFreeflow_pushButton)

        self.autostart_pushButton = QPushButton(self.frame_4)
        self.autostart_pushButton.setObjectName(u"autostart_pushButton")
        self.autostart_pushButton.setMinimumSize(QSize(210, 50))
        self.autostart_pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.autostart_pushButton.setCursor(QCursor(Qt.BusyCursor))
        self.autostart_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.autostart_pushButton.setStyleSheet(u"QPushButton:enabled {\n"
"	color: rgb(202, 206, 216);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(70, 80, 95);\n"
"	background-color: rgba(0, 0, 0,30);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(79, 159, 238);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(109, 182, 238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(69, 140, 207);\n"
"}")
        self.autostart_pushButton.setCheckable(False)
        self.autostart_pushButton.setChecked(False)
        self.autostart_pushButton.setAutoRepeatInterval(100)

        self.verticalLayout_7.addWidget(self.autostart_pushButton)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 3))
        self.label_11.setMaximumSize(QSize(16777215, 3))
        self.label_11.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")

        self.verticalLayout_7.addWidget(self.label_11)

        self.eMSstop_pushButton = QPushButton(self.frame_4)
        self.eMSstop_pushButton.setObjectName(u"eMSstop_pushButton")
        self.eMSstop_pushButton.setMinimumSize(QSize(210, 90))
        self.eMSstop_pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.eMSstop_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.eMSstop_pushButton.setStyleSheet(u"QPushButton:enabled {\n"
"	color: rgb(202, 206, 216);\n"
"	font: 30px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(70, 80, 95);\n"
"	background-color: rgba(0, 0, 0,30);\n"
"	font: 30px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(255, 88, 105);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(255, 124, 163);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 37, 95);\n"
"}")
        self.eMSstop_pushButton.setCheckable(False)

        self.verticalLayout_7.addWidget(self.eMSstop_pushButton)


        self.gridLayout_16.addWidget(self.frame_4, 2, 0, 1, 1, Qt.AlignBottom)

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
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
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

        self.verticalLayout_6.addWidget(self.label_16, 0, Qt.AlignBottom)

        self.AutoMode_pattern_comboBox = QComboBox(self.frame_6)
        self.AutoMode_pattern_comboBox.addItem("")
        self.AutoMode_pattern_comboBox.addItem("")
        self.AutoMode_pattern_comboBox.setObjectName(u"AutoMode_pattern_comboBox")
        self.AutoMode_pattern_comboBox.setMinimumSize(QSize(0, 30))
        self.AutoMode_pattern_comboBox.setMaximumSize(QSize(16777215, 30))
        self.AutoMode_pattern_comboBox.setBaseSize(QSize(0, 30))
        self.AutoMode_pattern_comboBox.setStyleSheet(u"\n"
"\n"
"QComboBox:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"\n"
"}\n"
"QComboBox:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QComboBox:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}")

        self.verticalLayout_6.addWidget(self.AutoMode_pattern_comboBox, 0, Qt.AlignBottom)

        self.Gas_mode_Label = QLabel(self.frame_6)
        self.Gas_mode_Label.setObjectName(u"Gas_mode_Label")
        self.Gas_mode_Label.setStyleSheet(u"font: 16px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"border:None")

        self.verticalLayout_6.addWidget(self.Gas_mode_Label, 0, Qt.AlignBottom)


        self.gridLayout_16.addWidget(self.frame_6, 0, 0, 1, 1, Qt.AlignBottom)


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
        self.gridLayout_19.setHorizontalSpacing(0)
        self.gridLayout_19.setVerticalSpacing(15)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 3))
        self.label_18.setMaximumSize(QSize(16777215, 3))
        self.label_18.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")

        self.gridLayout_19.addWidget(self.label_18, 4, 0, 1, 1)

        self.outputStop_pushButton = QPushButton(self.frame_9)
        self.outputStop_pushButton.setObjectName(u"outputStop_pushButton")
        self.outputStop_pushButton.setMinimumSize(QSize(210, 90))
        self.outputStop_pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.outputStop_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.outputStop_pushButton.setStyleSheet(u"QPushButton:enabled {\n"
"	color: rgb(202, 206, 216);\n"
"	font: 30px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(70, 80, 95);\n"
"	background-color: rgba(0, 0, 0,30);\n"
"	font: 30px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(255, 88, 105);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(255, 124, 163);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 37, 95);\n"
"}")
        self.outputStop_pushButton.setCheckable(False)
        self.outputStop_pushButton.setChecked(False)

        self.gridLayout_19.addWidget(self.outputStop_pushButton, 5, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_9, 8, 0, 1, 1, Qt.AlignBottom)

        self.manaualMode_comboBox = QComboBox(self.frame_11)
        self.manaualMode_comboBox.addItem("")
        self.manaualMode_comboBox.addItem("")
        self.manaualMode_comboBox.setObjectName(u"manaualMode_comboBox")
        self.manaualMode_comboBox.setStyleSheet(u"QComboBox:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QComboBox:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QComboBox:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}")

        self.gridLayout_20.addWidget(self.manaualMode_comboBox, 1, 0, 1, 1)

        self.stackedWidget_2 = QStackedWidget(self.frame_11)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setMinimumSize(QSize(0, 0))
        self.verticalLayout_17 = QVBoxLayout(self.page)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.page)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QSize(0, 0))
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
        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(70, 0))
        self.label_20.setMaximumSize(QSize(16777215, 16777215))
        self.label_20.setStyleSheet(u"border:None")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_21 = QLabel(self.frame_12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(70, 0))
        self.label_21.setMaximumSize(QSize(16777215, 16777215))
        self.label_21.setStyleSheet(u"border:None")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_21, 1, 0, 1, 1)

        self.measurement_comboBox = QComboBox(self.frame_12)
        self.measurement_comboBox.addItem("")
        self.measurement_comboBox.addItem("")
        self.measurement_comboBox.setObjectName(u"measurement_comboBox")
        sizePolicy.setHeightForWidth(self.measurement_comboBox.sizePolicy().hasHeightForWidth())
        self.measurement_comboBox.setSizePolicy(sizePolicy)
        self.measurement_comboBox.setMaximumSize(QSize(16777215, 30))
        self.measurement_comboBox.setStyleSheet(u"QComboBox:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QComboBox:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QComboBox:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}")

        self.gridLayout_21.addWidget(self.measurement_comboBox, 1, 1, 1, 1)

        self.voltage_lineEdit = QLineEdit(self.frame_12)
        self.voltage_lineEdit.setObjectName(u"voltage_lineEdit")
        sizePolicy.setHeightForWidth(self.voltage_lineEdit.sizePolicy().hasHeightForWidth())
        self.voltage_lineEdit.setSizePolicy(sizePolicy)
        self.voltage_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.voltage_lineEdit.setStyleSheet(u"\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.voltage_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.voltage_lineEdit, 0, 1, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_12, 0, Qt.AlignBottom)

        self.voltageOutput_pushButton = QPushButton(self.page)
        self.voltageOutput_pushButton.setObjectName(u"voltageOutput_pushButton")
        sizePolicy.setHeightForWidth(self.voltageOutput_pushButton.sizePolicy().hasHeightForWidth())
        self.voltageOutput_pushButton.setSizePolicy(sizePolicy)
        self.voltageOutput_pushButton.setMinimumSize(QSize(0, 40))
        self.voltageOutput_pushButton.setMaximumSize(QSize(16777215, 40))
        self.voltageOutput_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.voltageOutput_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.voltageOutput_pushButton.setStyleSheet(u"QPushButton:enabled {\n"
"	color: rgb(202, 206, 216);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(70, 80, 95);\n"
"	background-color: rgba(0, 0, 0,30);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(79, 159, 238);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(109, 182, 238);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(69, 140, 207);\n"
"}")
        self.voltageOutput_pushButton.setCheckable(True)
        self.voltageOutput_pushButton.setChecked(False)
        self.voltageOutput_pushButton.setAutoExclusive(False)
        self.voltageOutput_pushButton.setAutoRepeatInterval(100)

        self.verticalLayout_17.addWidget(self.voltageOutput_pushButton)

        self.manualMeasurement_pushButton = QPushButton(self.page)
        self.manualMeasurement_pushButton.setObjectName(u"manualMeasurement_pushButton")
        sizePolicy.setHeightForWidth(self.manualMeasurement_pushButton.sizePolicy().hasHeightForWidth())
        self.manualMeasurement_pushButton.setSizePolicy(sizePolicy)
        self.manualMeasurement_pushButton.setMinimumSize(QSize(0, 40))
        self.manualMeasurement_pushButton.setMaximumSize(QSize(16777215, 40))
        self.manualMeasurement_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.manualMeasurement_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.manualMeasurement_pushButton.setStyleSheet(u"QPushButton:enabled {\n"
"	color: rgb(202, 206, 216);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(70, 80, 95);\n"
"	background-color: rgba(0, 0, 0,30);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(148, 227, 114);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(132, 200, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(148, 227, 114);\n"
"}")
        self.manualMeasurement_pushButton.setCheckable(True)
        self.manualMeasurement_pushButton.setChecked(False)
        self.manualMeasurement_pushButton.setAutoExclusive(False)
        self.manualMeasurement_pushButton.setAutoRepeatInterval(100)

        self.verticalLayout_17.addWidget(self.manualMeasurement_pushButton)

        self.stackedWidget_2.addWidget(self.page)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_18 = QVBoxLayout(self.page_5)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_75 = QFrame(self.page_5)
        self.frame_75.setObjectName(u"frame_75")
        sizePolicy.setHeightForWidth(self.frame_75.sizePolicy().hasHeightForWidth())
        self.frame_75.setSizePolicy(sizePolicy)
        self.frame_75.setMinimumSize(QSize(0, 0))
        self.frame_75.setMaximumSize(QSize(16777215, 16777215))
        self.frame_75.setStyleSheet(u"background-color: rgb(41, 47, 56);\n"
"border-color: rgb(30, 34, 41);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_75)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.noiseMeasurement_Voltage_lineEdit = QLineEdit(self.frame_75)
        self.noiseMeasurement_Voltage_lineEdit.setObjectName(u"noiseMeasurement_Voltage_lineEdit")
        sizePolicy.setHeightForWidth(self.noiseMeasurement_Voltage_lineEdit.sizePolicy().hasHeightForWidth())
        self.noiseMeasurement_Voltage_lineEdit.setSizePolicy(sizePolicy)
        self.noiseMeasurement_Voltage_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.noiseMeasurement_Voltage_lineEdit.setStyleSheet(u"\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.noiseMeasurement_Voltage_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.noiseMeasurement_Voltage_lineEdit, 0, 1, 1, 1)

        self.label_33 = QLabel(self.frame_75)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(100, 0))
        self.label_33.setMaximumSize(QSize(16777215, 16777215))
        self.label_33.setStyleSheet(u"border:None")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_33, 0, 0, 1, 1)

        self.noiseMeasurement_Current_lineEdit = QLineEdit(self.frame_75)
        self.noiseMeasurement_Current_lineEdit.setObjectName(u"noiseMeasurement_Current_lineEdit")
        sizePolicy.setHeightForWidth(self.noiseMeasurement_Current_lineEdit.sizePolicy().hasHeightForWidth())
        self.noiseMeasurement_Current_lineEdit.setSizePolicy(sizePolicy)
        self.noiseMeasurement_Current_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.noiseMeasurement_Current_lineEdit.setStyleSheet(u"\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.noiseMeasurement_Current_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.noiseMeasurement_Current_lineEdit, 2, 1, 1, 1)

        self.noiseMeasurement_Time_lineEdit = QLineEdit(self.frame_75)
        self.noiseMeasurement_Time_lineEdit.setObjectName(u"noiseMeasurement_Time_lineEdit")
        sizePolicy.setHeightForWidth(self.noiseMeasurement_Time_lineEdit.sizePolicy().hasHeightForWidth())
        self.noiseMeasurement_Time_lineEdit.setSizePolicy(sizePolicy)
        self.noiseMeasurement_Time_lineEdit.setMaximumSize(QSize(16777215, 30))
        self.noiseMeasurement_Time_lineEdit.setStyleSheet(u"\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.noiseMeasurement_Time_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.noiseMeasurement_Time_lineEdit, 1, 1, 1, 1)

        self.label_44 = QLabel(self.frame_75)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(100, 0))
        self.label_44.setMaximumSize(QSize(16777215, 16777215))
        self.label_44.setStyleSheet(u"border:None")
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_44, 2, 0, 1, 1)

        self.label_36 = QLabel(self.frame_75)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(100, 0))
        self.label_36.setMaximumSize(QSize(16777215, 16777215))
        self.label_36.setStyleSheet(u"border:None")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_36, 1, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.frame_75, 0, Qt.AlignBottom)

        self.Noisetest_pushButton = QPushButton(self.page_5)
        self.Noisetest_pushButton.setObjectName(u"Noisetest_pushButton")
        sizePolicy.setHeightForWidth(self.Noisetest_pushButton.sizePolicy().hasHeightForWidth())
        self.Noisetest_pushButton.setSizePolicy(sizePolicy)
        self.Noisetest_pushButton.setMinimumSize(QSize(0, 40))
        self.Noisetest_pushButton.setMaximumSize(QSize(16777215, 40))
        self.Noisetest_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.Noisetest_pushButton.setStyleSheet(u"QPushButton:enabled {\n"
"	color: rgb(202, 206, 216);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(70, 80, 95);\n"
"	background-color: rgba(0, 0, 0,30);\n"
"	font: 28px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}\n"
"QPushButton:checked{\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(148, 227, 114);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(158, 239, 120);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(44, 36, 0);\n"
"	background-color: rgb(125, 189, 95);\n"
"}\n"
"")
        self.Noisetest_pushButton.setCheckable(True)
        self.Noisetest_pushButton.setAutoRepeatInterval(100)

        self.verticalLayout_18.addWidget(self.Noisetest_pushButton)

        self.stackedWidget_2.addWidget(self.page_5)

        self.gridLayout_20.addWidget(self.stackedWidget_2, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_ManaulOperate)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_7, 0, Qt.AlignBottom)


        self.gridLayout_4.addWidget(self.frame_31, 1, 1, 2, 1)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}\n"
"\n"
"QCheckBox{\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"	font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
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
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QComboBox:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	border-width: 1px;\n"
"}\n"
"QComboBox:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QComboBox:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.scrollArea_2 = QScrollArea(self.page_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1045, 1650))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_20 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.frame_20.setMinimumSize(QSize(0, 0))
        self.frame_20.setMaximumSize(QSize(16777215, 16777215))
        self.frame_20.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 34, 41);\n"
"	border-color:rgb(30, 34, 41);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}\n"
"\n"
"QCheckBox{\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"	font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(91, 94, 98);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
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
"}\n"
"QComboBox:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border"
                        "-width: 1px;\n"
"}\n"
"QComboBox:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(44, 49, 60);\n"
"	border: none;\n"
"}\n"
"QComboBox:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_20)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Temp_Totaltime_Label = QLabel(self.frame_20)
        self.Temp_Totaltime_Label.setObjectName(u"Temp_Totaltime_Label")
        self.Temp_Totaltime_Label.setMinimumSize(QSize(0, 0))
        self.Temp_Totaltime_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Temp_Totaltime_Label.setStyleSheet(u"")
        self.Temp_Totaltime_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.Temp_Totaltime_Label, 2, 7, 1, 1)

        self.label_63 = QLabel(self.frame_20)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(90, 32))
        self.label_63.setMaximumSize(QSize(16777215, 16777215))
        self.label_63.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_63, 2, 2, 1, 1)

        self.label_27 = QLabel(self.frame_20)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(90, 32))
        self.label_27.setMaximumSize(QSize(90, 16777215))
        self.label_27.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_27, 0, 2, 1, 1)

        self.frame_33 = QFrame(self.frame_20)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(3, 0))
        self.frame_33.setMaximumSize(QSize(3, 16777215))
        self.frame_33.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_33, 0, 1, 4, 1)

        self.frame_35 = QFrame(self.frame_20)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setMinimumSize(QSize(0, 0))
        self.frame_35.setStyleSheet(u"background-color: rgb(25, 28, 34);")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_35)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_43 = QFrame(self.frame_35)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 300))
        self.frame_43.setStyleSheet(u"border:None")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_43)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, -1, 18, -1)

        self.verticalLayout_10.addWidget(self.frame_43)

        self.scrollArea_3 = QScrollArea(self.frame_35)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setMinimumSize(QSize(0, 400))
        self.scrollArea_3.setSizeIncrement(QSize(0, 0))
        self.scrollArea_3.setStyleSheet(u"border:none;")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 987, 400))
        self.gridLayout_40 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 0))
        self.frame_32.setMaximumSize(QSize(16777215, 16777215))
        self.frame_32.setStyleSheet(u"")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)

        self.gridLayout_40.addWidget(self.frame_32, 0, 0, 1, 1, Qt.AlignLeft)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_10.addWidget(self.scrollArea_3)


        self.gridLayout_6.addWidget(self.frame_35, 4, 0, 1, 10)

        self.label_25 = QLabel(self.frame_20)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(90, 32))
        self.label_25.setMaximumSize(QSize(16777215, 16777215))
        self.label_25.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_25, 1, 2, 1, 1)

        self.RT_combobox = QComboBox(self.frame_20)
        self.RT_combobox.addItem("")
        self.RT_combobox.addItem("")
        self.RT_combobox.setObjectName(u"RT_combobox")
        self.RT_combobox.setMinimumSize(QSize(70, 35))
        self.RT_combobox.setMaximumSize(QSize(70, 35))
        self.RT_combobox.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.RT_combobox, 2, 5, 1, 1)

        self.patternfile_comboBox = QComboBox(self.frame_20)
        self.patternfile_comboBox.addItem("")
        self.patternfile_comboBox.setObjectName(u"patternfile_comboBox")
        self.patternfile_comboBox.setMinimumSize(QSize(400, 35))
        self.patternfile_comboBox.setMaximumSize(QSize(400, 35))
        self.patternfile_comboBox.setMouseTracking(True)
        self.patternfile_comboBox.setStyleSheet(u"")
        self.patternfile_comboBox.setEditable(False)
        self.patternfile_comboBox.setInsertPolicy(QComboBox.InsertAtTop)

        self.gridLayout_6.addWidget(self.patternfile_comboBox, 0, 3, 1, 5)

        self.RT_Label = QLabel(self.frame_20)
        self.RT_Label.setObjectName(u"RT_Label")
        self.RT_Label.setMinimumSize(QSize(50, 0))
        self.RT_Label.setMaximumSize(QSize(50, 16777215))
        self.RT_Label.setStyleSheet(u"")
        self.RT_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.RT_Label, 2, 4, 1, 1)

        self.frame_37 = QFrame(self.frame_20)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 0))
        self.frame_37.setMaximumSize(QSize(16777215, 16777215))
        self.frame_37.setStyleSheet(u"")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.frame_37)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(50, 0))
        self.frame_40.setMaximumSize(QSize(50, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_40)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_40)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_7)


        self.horizontalLayout_14.addWidget(self.frame_40)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(50, 0))
        self.frame_39.setMaximumSize(QSize(50, 16777215))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_39)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_39)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6)


        self.horizontalLayout_14.addWidget(self.frame_39)

        self.frame_41 = QFrame(self.frame_37)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(3, 0))
        self.frame_41.setMaximumSize(QSize(3, 16777215))
        self.frame_41.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.frame_41)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(50, 0))
        self.frame_38.setMaximumSize(QSize(50, 16777215))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_38)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_38)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_3)


        self.horizontalLayout_14.addWidget(self.frame_38)


        self.gridLayout_6.addWidget(self.frame_37, 0, 9, 2, 1, Qt.AlignRight)

        self.PatternErrorMessagelabel = QLabel(self.frame_20)
        self.PatternErrorMessagelabel.setObjectName(u"PatternErrorMessagelabel")
        self.PatternErrorMessagelabel.setMinimumSize(QSize(0, 0))
        self.PatternErrorMessagelabel.setMaximumSize(QSize(16777215, 16777215))
        self.PatternErrorMessagelabel.setStyleSheet(u"color: rgb(221, 0, 0);")
        self.PatternErrorMessagelabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.PatternErrorMessagelabel, 2, 9, 1, 1)

        self.commect_lineEdit = QLineEdit(self.frame_20)
        self.commect_lineEdit.setObjectName(u"commect_lineEdit")
        self.commect_lineEdit.setMinimumSize(QSize(400, 35))
        self.commect_lineEdit.setMaximumSize(QSize(400, 35))
        self.commect_lineEdit.setStyleSheet(u"")
        self.commect_lineEdit.setCursorPosition(0)

        self.gridLayout_6.addWidget(self.commect_lineEdit, 1, 3, 1, 5)

        self.frame_55 = QFrame(self.frame_20)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(130, 0))
        self.frame_55.setMaximumSize(QSize(130, 16777215))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_55)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.frame_55)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(140, 0))
        self.label_65.setMaximumSize(QSize(140, 16777215))
        self.label_65.setStyleSheet(u"font: 20px;\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.verticalLayout.addWidget(self.label_65)

        self.label_29 = QLabel(self.frame_55)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(140, 0))
        self.label_29.setMaximumSize(QSize(140, 16777215))
        self.label_29.setStyleSheet(u"font: 20px;\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.verticalLayout.addWidget(self.label_29)


        self.gridLayout_6.addWidget(self.frame_55, 0, 0, 4, 1)

        self.gas_Combobox = QComboBox(self.frame_20)
        self.gas_Combobox.addItem("")
        self.gas_Combobox.addItem("")
        self.gas_Combobox.addItem("")
        self.gas_Combobox.setObjectName(u"gas_Combobox")
        self.gas_Combobox.setMinimumSize(QSize(70, 35))
        self.gas_Combobox.setMaximumSize(QSize(70, 35))
        self.gas_Combobox.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.gas_Combobox, 2, 3, 1, 1)

        self.RT_testpattern_combobox = QComboBox(self.frame_20)
        self.RT_testpattern_combobox.addItem("")
        self.RT_testpattern_combobox.addItem("")
        self.RT_testpattern_combobox.setObjectName(u"RT_testpattern_combobox")
        self.RT_testpattern_combobox.setMinimumSize(QSize(120, 35))
        self.RT_testpattern_combobox.setMaximumSize(QSize(120, 35))
        self.RT_testpattern_combobox.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.RT_testpattern_combobox, 2, 6, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_20)

        self.frame_34 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMinimumSize(QSize(0, 0))
        self.frame_34.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 34, 41);\n"
"	border-color:rgb(30, 34, 41);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px;\n"
"}\n"
"\n"
"QCheckBox{\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	color: rgb(225, 230, 241);\n"
"	font: 12px;\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(91, 94, 98);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
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
"}\n"
"QComboBox:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	padding:5px;\n"
"	border-width: 1px;\n"
"}\n"
"QComboBox:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
""
                        "	color: rgb(44, 49, 60);\n"
"	border: none;\n"
"}\n"
"QComboBox:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.frame_34)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.TestPatternErrorMessagelabel = QLabel(self.frame_34)
        self.TestPatternErrorMessagelabel.setObjectName(u"TestPatternErrorMessagelabel")
        self.TestPatternErrorMessagelabel.setMinimumSize(QSize(0, 0))
        self.TestPatternErrorMessagelabel.setMaximumSize(QSize(16777215, 16777215))
        self.TestPatternErrorMessagelabel.setStyleSheet(u"color: rgb(221, 0, 0);")
        self.TestPatternErrorMessagelabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_47.addWidget(self.TestPatternErrorMessagelabel, 5, 6, 1, 1, Qt.AlignRight)

        self.frame_71 = QFrame(self.frame_34)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_71)
        self.gridLayout_13.setSpacing(6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(6, 0, 6, 0)
        self.label_43 = QLabel(self.frame_71)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(80, 0))
        self.label_43.setMaximumSize(QSize(80, 16777215))
        self.label_43.setStyleSheet(u"font:13px;\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_13.addWidget(self.label_43, 0, 2, 1, 1)

        self.frame_68 = QFrame(self.frame_71)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(3, 0))
        self.frame_68.setMaximumSize(QSize(3, 16777215))
        self.frame_68.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)

        self.gridLayout_13.addWidget(self.frame_68, 0, 1, 2, 1)

        self.label_42 = QLabel(self.frame_71)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(80, 0))
        self.label_42.setMaximumSize(QSize(80, 16777215))
        self.label_42.setStyleSheet(u"font: 13px;\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_13.addWidget(self.label_42, 1, 2, 1, 1)

        self.test_commect_lineEdit = QLineEdit(self.frame_71)
        self.test_commect_lineEdit.setObjectName(u"test_commect_lineEdit")
        sizePolicy.setHeightForWidth(self.test_commect_lineEdit.sizePolicy().hasHeightForWidth())
        self.test_commect_lineEdit.setSizePolicy(sizePolicy)
        self.test_commect_lineEdit.setMinimumSize(QSize(400, 0))
        self.test_commect_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.test_commect_lineEdit.setStyleSheet(u"")

        self.gridLayout_13.addWidget(self.test_commect_lineEdit, 1, 3, 1, 1)

        self.testfile_comboBox = QComboBox(self.frame_71)
        self.testfile_comboBox.setObjectName(u"testfile_comboBox")
        sizePolicy.setHeightForWidth(self.testfile_comboBox.sizePolicy().hasHeightForWidth())
        self.testfile_comboBox.setSizePolicy(sizePolicy)
        self.testfile_comboBox.setMinimumSize(QSize(400, 0))
        self.testfile_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.testfile_comboBox.setStyleSheet(u"")

        self.gridLayout_13.addWidget(self.testfile_comboBox, 0, 3, 1, 1)

        self.label_41 = QLabel(self.frame_71)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(130, 0))
        self.label_41.setMaximumSize(QSize(130, 16777215))
        self.label_41.setStyleSheet(u"font: 20px;\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_13.addWidget(self.label_41, 0, 0, 2, 1)

        self.Test_Totaltime_Label = QLabel(self.frame_71)
        self.Test_Totaltime_Label.setObjectName(u"Test_Totaltime_Label")
        self.Test_Totaltime_Label.setMinimumSize(QSize(0, 0))
        self.Test_Totaltime_Label.setMaximumSize(QSize(16777215, 16777215))
        self.Test_Totaltime_Label.setStyleSheet(u"")
        self.Test_Totaltime_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.Test_Totaltime_Label, 1, 4, 1, 1)


        self.gridLayout_47.addWidget(self.frame_71, 0, 0, 3, 2, Qt.AlignLeft)

        self.frame_50 = QFrame(self.frame_34)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 0))
        self.frame_50.setMaximumSize(QSize(16777215, 16777215))
        self.frame_50.setStyleSheet(u"")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(9, 0, 9, 0)
        self.frame_52 = QFrame(self.frame_50)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(50, 0))
        self.frame_52.setMaximumSize(QSize(50, 16777215))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_52)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_52)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_47)


        self.horizontalLayout_15.addWidget(self.frame_52)

        self.frame_56 = QFrame(self.frame_50)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(50, 0))
        self.frame_56.setMaximumSize(QSize(50, 16777215))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_56)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_56)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_46)


        self.horizontalLayout_15.addWidget(self.frame_56)

        self.frame_53 = QFrame(self.frame_50)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(3, 0))
        self.frame_53.setMaximumSize(QSize(3, 16777215))
        self.frame_53.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_50)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(50, 0))
        self.frame_54.setMaximumSize(QSize(50, 16777215))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_54)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_54)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_15)


        self.horizontalLayout_15.addWidget(self.frame_54)


        self.gridLayout_47.addWidget(self.frame_50, 0, 6, 3, 1, Qt.AlignRight)

        self.frame_44 = QFrame(self.frame_34)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy)
        self.frame_44.setMinimumSize(QSize(0, 0))
        self.frame_44.setStyleSheet(u"background-color: rgb(25, 28, 34);")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_44)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 300))
        self.frame_46.setStyleSheet(u"border:None")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_46)
        self.gridLayout_11.setObjectName(u"gridLayout_11")

        self.verticalLayout_2.addWidget(self.frame_46)

        self.scrollArea_4 = QScrollArea(self.frame_44)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setMinimumSize(QSize(0, 200))
        self.scrollArea_4.setSizeIncrement(QSize(0, 0))
        self.scrollArea_4.setStyleSheet(u"border:none;")
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 987, 200))
        self.gridLayout_41 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 0))
        self.frame_49.setMaximumSize(QSize(16777215, 16777215))
        self.frame_49.setStyleSheet(u"")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)

        self.gridLayout_41.addWidget(self.frame_49, 0, 0, 1, 1, Qt.AlignLeft)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_2.addWidget(self.scrollArea_4)


        self.gridLayout_47.addWidget(self.frame_44, 6, 0, 1, 7)

        self.frame_70 = QFrame(self.frame_34)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(0, 3))
        self.frame_70.setMaximumSize(QSize(16777215, 3))
        self.frame_70.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)

        self.gridLayout_47.addWidget(self.frame_70, 3, 0, 1, 7)

        self.frame_51 = QFrame(self.frame_34)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy)
        self.frame_51.setMinimumSize(QSize(0, 0))
        self.frame_51.setMaximumSize(QSize(16777215, 16777215))
        self.frame_51.setStyleSheet(u"")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_51)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setHorizontalSpacing(6)
        self.gridLayout_42.setContentsMargins(6, 6, 6, 6)
        self.test_sampletime_LineEdit = QLineEdit(self.frame_51)
        self.test_sampletime_LineEdit.setObjectName(u"test_sampletime_LineEdit")
        sizePolicy.setHeightForWidth(self.test_sampletime_LineEdit.sizePolicy().hasHeightForWidth())
        self.test_sampletime_LineEdit.setSizePolicy(sizePolicy)
        self.test_sampletime_LineEdit.setMinimumSize(QSize(50, 25))
        self.test_sampletime_LineEdit.setMaximumSize(QSize(16777215, 25))
        self.test_sampletime_LineEdit.setStyleSheet(u"")
        self.test_sampletime_LineEdit.setAlignment(Qt.AlignCenter)
        self.test_sampletime_LineEdit.setReadOnly(False)

        self.gridLayout_42.addWidget(self.test_sampletime_LineEdit, 1, 9, 1, 1)

        self.label_61 = QLabel(self.frame_51)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(0, 0))
        self.label_61.setMaximumSize(QSize(16777215, 16777215))
        self.label_61.setStyleSheet(u"")
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_61, 1, 1, 1, 1)

        self.bg_sampletime_LineEdit = QLineEdit(self.frame_51)
        self.bg_sampletime_LineEdit.setObjectName(u"bg_sampletime_LineEdit")
        sizePolicy.setHeightForWidth(self.bg_sampletime_LineEdit.sizePolicy().hasHeightForWidth())
        self.bg_sampletime_LineEdit.setSizePolicy(sizePolicy)
        self.bg_sampletime_LineEdit.setMinimumSize(QSize(50, 25))
        self.bg_sampletime_LineEdit.setMaximumSize(QSize(16777215, 25))
        self.bg_sampletime_LineEdit.setStyleSheet(u"")
        self.bg_sampletime_LineEdit.setAlignment(Qt.AlignCenter)
        self.bg_sampletime_LineEdit.setReadOnly(False)

        self.gridLayout_42.addWidget(self.bg_sampletime_LineEdit, 2, 2, 1, 1)

        self.test_time_LineEdit = QLineEdit(self.frame_51)
        self.test_time_LineEdit.setObjectName(u"test_time_LineEdit")
        sizePolicy.setHeightForWidth(self.test_time_LineEdit.sizePolicy().hasHeightForWidth())
        self.test_time_LineEdit.setSizePolicy(sizePolicy)
        self.test_time_LineEdit.setMinimumSize(QSize(50, 25))
        self.test_time_LineEdit.setMaximumSize(QSize(16777215, 25))
        self.test_time_LineEdit.setStyleSheet(u"")
        self.test_time_LineEdit.setAlignment(Qt.AlignCenter)
        self.test_time_LineEdit.setReadOnly(False)

        self.gridLayout_42.addWidget(self.test_time_LineEdit, 0, 9, 1, 1)

        self.bg_time_LineEdit = QLineEdit(self.frame_51)
        self.bg_time_LineEdit.setObjectName(u"bg_time_LineEdit")
        sizePolicy.setHeightForWidth(self.bg_time_LineEdit.sizePolicy().hasHeightForWidth())
        self.bg_time_LineEdit.setSizePolicy(sizePolicy)
        self.bg_time_LineEdit.setMinimumSize(QSize(50, 25))
        self.bg_time_LineEdit.setMaximumSize(QSize(16777215, 25))
        self.bg_time_LineEdit.setStyleSheet(u"")
        self.bg_time_LineEdit.setAlignment(Qt.AlignCenter)
        self.bg_time_LineEdit.setReadOnly(False)

        self.gridLayout_42.addWidget(self.bg_time_LineEdit, 1, 2, 1, 1)

        self.frame_74 = QFrame(self.frame_51)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(3, 0))
        self.frame_74.setMaximumSize(QSize(3, 16777215))
        self.frame_74.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)

        self.gridLayout_42.addWidget(self.frame_74, 0, 3, 3, 1)

        self.label_59 = QLabel(self.frame_51)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(0, 0))
        self.label_59.setMaximumSize(QSize(16777215, 16777215))
        self.label_59.setStyleSheet(u"")
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_59, 1, 7, 1, 1)

        self.label_58 = QLabel(self.frame_51)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(0, 0))
        self.label_58.setMaximumSize(QSize(16777215, 16777215))
        self.label_58.setStyleSheet(u"")
        self.label_58.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_58, 0, 7, 1, 1)

        self.speed_label = QLabel(self.frame_51)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setMinimumSize(QSize(0, 0))
        self.speed_label.setMaximumSize(QSize(16777215, 16777215))
        self.speed_label.setStyleSheet(u"")
        self.speed_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.speed_label, 0, 12, 1, 1)

        self.label_66 = QLabel(self.frame_51)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(0, 0))
        self.label_66.setMaximumSize(QSize(16777215, 16777215))
        self.label_66.setStyleSheet(u"")
        self.label_66.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_66, 2, 1, 1, 1)

        self.label_62 = QLabel(self.frame_51)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(0, 0))
        self.label_62.setMaximumSize(QSize(16777215, 16777215))
        self.label_62.setStyleSheet(u"")
        self.label_62.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_62, 0, 1, 1, 1)

        self.bg0_time_LineEdit = QLineEdit(self.frame_51)
        self.bg0_time_LineEdit.setObjectName(u"bg0_time_LineEdit")
        sizePolicy.setHeightForWidth(self.bg0_time_LineEdit.sizePolicy().hasHeightForWidth())
        self.bg0_time_LineEdit.setSizePolicy(sizePolicy)
        self.bg0_time_LineEdit.setMinimumSize(QSize(50, 25))
        self.bg0_time_LineEdit.setMaximumSize(QSize(16777215, 25))
        self.bg0_time_LineEdit.setStyleSheet(u"")
        self.bg0_time_LineEdit.setAlignment(Qt.AlignCenter)
        self.bg0_time_LineEdit.setReadOnly(False)

        self.gridLayout_42.addWidget(self.bg0_time_LineEdit, 0, 2, 1, 1)

        self.frame_73 = QFrame(self.frame_51)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(3, 0))
        self.frame_73.setMaximumSize(QSize(3, 16777215))
        self.frame_73.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(141, 145, 156);\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)

        self.gridLayout_42.addWidget(self.frame_73, 0, 10, 3, 1)

        self.speed_comboBox = QComboBox(self.frame_51)
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.setObjectName(u"speed_comboBox")
        sizePolicy.setHeightForWidth(self.speed_comboBox.sizePolicy().hasHeightForWidth())
        self.speed_comboBox.setSizePolicy(sizePolicy)
        self.speed_comboBox.setMinimumSize(QSize(150, 0))
        self.speed_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.speed_comboBox.setStyleSheet(u"")

        self.gridLayout_42.addWidget(self.speed_comboBox, 0, 13, 1, 1)

        self.filter_label = QLabel(self.frame_51)
        self.filter_label.setObjectName(u"filter_label")
        self.filter_label.setMinimumSize(QSize(0, 0))
        self.filter_label.setMaximumSize(QSize(16777215, 16777215))
        self.filter_label.setStyleSheet(u"")
        self.filter_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.filter_label, 1, 12, 1, 1)

        self.filter_comboBox = QComboBox(self.frame_51)
        self.filter_comboBox.addItem("")
        self.filter_comboBox.addItem("")
        self.filter_comboBox.addItem("")
        self.filter_comboBox.addItem("")
        self.filter_comboBox.setObjectName(u"filter_comboBox")
        sizePolicy.setHeightForWidth(self.filter_comboBox.sizePolicy().hasHeightForWidth())
        self.filter_comboBox.setSizePolicy(sizePolicy)
        self.filter_comboBox.setMinimumSize(QSize(150, 0))
        self.filter_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.filter_comboBox.setStyleSheet(u"")

        self.gridLayout_42.addWidget(self.filter_comboBox, 1, 13, 1, 1)

        self.filter_count_label = QLabel(self.frame_51)
        self.filter_count_label.setObjectName(u"filter_count_label")
        self.filter_count_label.setMinimumSize(QSize(0, 0))
        self.filter_count_label.setMaximumSize(QSize(16777215, 16777215))
        self.filter_count_label.setStyleSheet(u"")
        self.filter_count_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.filter_count_label, 2, 12, 1, 1)

        self.filter_count_LineEdit = QLineEdit(self.frame_51)
        self.filter_count_LineEdit.setObjectName(u"filter_count_LineEdit")
        sizePolicy.setHeightForWidth(self.filter_count_LineEdit.sizePolicy().hasHeightForWidth())
        self.filter_count_LineEdit.setSizePolicy(sizePolicy)
        self.filter_count_LineEdit.setMinimumSize(QSize(50, 25))
        self.filter_count_LineEdit.setMaximumSize(QSize(50, 25))
        self.filter_count_LineEdit.setStyleSheet(u"")
        self.filter_count_LineEdit.setAlignment(Qt.AlignCenter)
        self.filter_count_LineEdit.setReadOnly(False)

        self.gridLayout_42.addWidget(self.filter_count_LineEdit, 2, 13, 1, 1)


        self.gridLayout_47.addWidget(self.frame_51, 5, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_34)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.page_3_layout.addWidget(self.scrollArea_2)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setEnabled(True)
        self.page_4.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
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
"	padding-left:5px;\n"
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
        self.gridLayout_24 = QGridLayout(self.page_4)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.frame_36 = QFrame(self.page_4)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_36)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_yesr_7 = QLabel(self.frame_36)
        self.label_yesr_7.setObjectName(u"label_yesr_7")
        self.label_yesr_7.setMinimumSize(QSize(0, 20))
        self.label_yesr_7.setMaximumSize(QSize(16777215, 20))
        self.label_yesr_7.setMouseTracking(True)
        self.label_yesr_7.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_7.setStyleSheet(u"background-color: rgb(65, 72, 88);\n"
"padding:5px\n"
"")
        self.label_yesr_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_7.setMargin(0)

        self.verticalLayout_5.addWidget(self.label_yesr_7)

        self.frame_57 = QFrame(self.frame_36)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_57)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.label_yesr_3 = QLabel(self.frame_57)
        self.label_yesr_3.setObjectName(u"label_yesr_3")
        self.label_yesr_3.setMinimumSize(QSize(150, 35))
        self.label_yesr_3.setMaximumSize(QSize(150, 35))
        self.label_yesr_3.setMouseTracking(True)
        self.label_yesr_3.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_3.setStyleSheet(u"")
        self.label_yesr_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_3.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_3, 0, 4, 1, 1)

        self.label_yesr_2 = QLabel(self.frame_57)
        self.label_yesr_2.setObjectName(u"label_yesr_2")
        self.label_yesr_2.setMinimumSize(QSize(150, 35))
        self.label_yesr_2.setMaximumSize(QSize(150, 35))
        self.label_yesr_2.setMouseTracking(True)
        self.label_yesr_2.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_2.setStyleSheet(u"")
        self.label_yesr_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_2.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_2, 0, 2, 1, 1)

        self.label_yesr_24 = QLabel(self.frame_57)
        self.label_yesr_24.setObjectName(u"label_yesr_24")
        self.label_yesr_24.setMinimumSize(QSize(150, 35))
        self.label_yesr_24.setMaximumSize(QSize(150, 35))
        self.label_yesr_24.setMouseTracking(True)
        self.label_yesr_24.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_24.setStyleSheet(u"")
        self.label_yesr_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_24.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_24, 1, 0, 1, 1)

        self.label_yesr_4 = QLabel(self.frame_57)
        self.label_yesr_4.setObjectName(u"label_yesr_4")
        self.label_yesr_4.setMinimumSize(QSize(150, 35))
        self.label_yesr_4.setMaximumSize(QSize(150, 35))
        self.label_yesr_4.setMouseTracking(True)
        self.label_yesr_4.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_4.setStyleSheet(u"")
        self.label_yesr_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_4.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_4, 1, 2, 1, 1)

        self.label_yesr_26 = QLabel(self.frame_57)
        self.label_yesr_26.setObjectName(u"label_yesr_26")
        self.label_yesr_26.setMinimumSize(QSize(150, 35))
        self.label_yesr_26.setMaximumSize(QSize(150, 35))
        self.label_yesr_26.setMouseTracking(True)
        self.label_yesr_26.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_26.setStyleSheet(u"")
        self.label_yesr_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_26.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_26, 1, 8, 1, 1)

        self.label_yesr_6 = QLabel(self.frame_57)
        self.label_yesr_6.setObjectName(u"label_yesr_6")
        self.label_yesr_6.setMinimumSize(QSize(150, 35))
        self.label_yesr_6.setMaximumSize(QSize(150, 35))
        self.label_yesr_6.setMouseTracking(True)
        self.label_yesr_6.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_6.setStyleSheet(u"")
        self.label_yesr_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_6.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_6, 1, 4, 1, 1)

        self.label_yesr_15 = QLabel(self.frame_57)
        self.label_yesr_15.setObjectName(u"label_yesr_15")
        self.label_yesr_15.setMinimumSize(QSize(150, 35))
        self.label_yesr_15.setMaximumSize(QSize(150, 35))
        self.label_yesr_15.setMouseTracking(True)
        self.label_yesr_15.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_15.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;")
        self.label_yesr_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_15.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_15, 0, 8, 1, 1)

        self.label_yesr_12 = QLabel(self.frame_57)
        self.label_yesr_12.setObjectName(u"label_yesr_12")
        self.label_yesr_12.setMinimumSize(QSize(150, 35))
        self.label_yesr_12.setMaximumSize(QSize(150, 35))
        self.label_yesr_12.setMouseTracking(True)
        self.label_yesr_12.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_12.setStyleSheet(u"")
        self.label_yesr_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_12.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_12, 0, 1, 1, 1)

        self.label_yesr_14 = QLabel(self.frame_57)
        self.label_yesr_14.setObjectName(u"label_yesr_14")
        self.label_yesr_14.setMinimumSize(QSize(150, 35))
        self.label_yesr_14.setMaximumSize(QSize(150, 35))
        self.label_yesr_14.setMouseTracking(True)
        self.label_yesr_14.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_14.setStyleSheet(u"")
        self.label_yesr_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_14.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_14, 1, 7, 1, 1)

        self.label_yesr_13 = QLabel(self.frame_57)
        self.label_yesr_13.setObjectName(u"label_yesr_13")
        self.label_yesr_13.setMinimumSize(QSize(150, 35))
        self.label_yesr_13.setMaximumSize(QSize(150, 35))
        self.label_yesr_13.setMouseTracking(True)
        self.label_yesr_13.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_13.setStyleSheet(u"")
        self.label_yesr_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_13.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_13, 0, 7, 1, 1)

        self.label_yesr_25 = QLabel(self.frame_57)
        self.label_yesr_25.setObjectName(u"label_yesr_25")
        self.label_yesr_25.setMinimumSize(QSize(150, 35))
        self.label_yesr_25.setMaximumSize(QSize(150, 35))
        self.label_yesr_25.setMouseTracking(True)
        self.label_yesr_25.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_25.setStyleSheet(u"")
        self.label_yesr_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_25.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_25, 1, 1, 1, 1)

        self.label_yesr_10 = QLabel(self.frame_57)
        self.label_yesr_10.setObjectName(u"label_yesr_10")
        self.label_yesr_10.setMinimumSize(QSize(150, 35))
        self.label_yesr_10.setMaximumSize(QSize(150, 35))
        self.label_yesr_10.setMouseTracking(True)
        self.label_yesr_10.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_10.setStyleSheet(u"")
        self.label_yesr_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_10.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_10, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_57, 0, Qt.AlignLeft)

        self.label_yesr_8 = QLabel(self.frame_36)
        self.label_yesr_8.setObjectName(u"label_yesr_8")
        self.label_yesr_8.setMinimumSize(QSize(0, 20))
        self.label_yesr_8.setMaximumSize(QSize(16777215, 20))
        self.label_yesr_8.setMouseTracking(True)
        self.label_yesr_8.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_8.setStyleSheet(u"background-color: rgb(65, 72, 88);\n"
"padding:5px\n"
"")
        self.label_yesr_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_8.setMargin(0)

        self.verticalLayout_5.addWidget(self.label_yesr_8)

        self.frame_58 = QFrame(self.frame_36)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_58)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.label_yesr_28 = QLabel(self.frame_58)
        self.label_yesr_28.setObjectName(u"label_yesr_28")
        self.label_yesr_28.setMinimumSize(QSize(150, 35))
        self.label_yesr_28.setMaximumSize(QSize(150, 35))
        self.label_yesr_28.setMouseTracking(True)
        self.label_yesr_28.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_28.setStyleSheet(u"")
        self.label_yesr_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_28.setMargin(0)

        self.gridLayout_48.addWidget(self.label_yesr_28, 1, 1, 1, 1)

        self.label_yesr_27 = QLabel(self.frame_58)
        self.label_yesr_27.setObjectName(u"label_yesr_27")
        self.label_yesr_27.setMinimumSize(QSize(150, 35))
        self.label_yesr_27.setMaximumSize(QSize(150, 35))
        self.label_yesr_27.setMouseTracking(True)
        self.label_yesr_27.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_27.setStyleSheet(u"")
        self.label_yesr_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_27.setMargin(0)

        self.gridLayout_48.addWidget(self.label_yesr_27, 1, 0, 1, 1)

        self.label_yesr_11 = QLabel(self.frame_58)
        self.label_yesr_11.setObjectName(u"label_yesr_11")
        self.label_yesr_11.setMinimumSize(QSize(150, 35))
        self.label_yesr_11.setMaximumSize(QSize(150, 35))
        self.label_yesr_11.setMouseTracking(True)
        self.label_yesr_11.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_11.setStyleSheet(u"")
        self.label_yesr_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_11.setMargin(0)

        self.gridLayout_48.addWidget(self.label_yesr_11, 0, 0, 1, 1)

        self.label_yesr_17 = QLabel(self.frame_58)
        self.label_yesr_17.setObjectName(u"label_yesr_17")
        self.label_yesr_17.setMinimumSize(QSize(150, 35))
        self.label_yesr_17.setMaximumSize(QSize(150, 35))
        self.label_yesr_17.setMouseTracking(True)
        self.label_yesr_17.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_17.setStyleSheet(u"")
        self.label_yesr_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_17.setMargin(0)

        self.gridLayout_48.addWidget(self.label_yesr_17, 0, 2, 1, 1)

        self.label_yesr_16 = QLabel(self.frame_58)
        self.label_yesr_16.setObjectName(u"label_yesr_16")
        self.label_yesr_16.setMinimumSize(QSize(150, 35))
        self.label_yesr_16.setMaximumSize(QSize(150, 35))
        self.label_yesr_16.setMouseTracking(True)
        self.label_yesr_16.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_16.setStyleSheet(u"")
        self.label_yesr_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_16.setMargin(0)

        self.gridLayout_48.addWidget(self.label_yesr_16, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_58)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)

        self.gridLayout_48.addWidget(self.lineEdit, 0, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_58, 0, Qt.AlignLeft)

        self.label_yesr_9 = QLabel(self.frame_36)
        self.label_yesr_9.setObjectName(u"label_yesr_9")
        self.label_yesr_9.setMinimumSize(QSize(0, 20))
        self.label_yesr_9.setMaximumSize(QSize(16777215, 20))
        self.label_yesr_9.setMouseTracking(True)
        self.label_yesr_9.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_9.setStyleSheet(u"background-color: rgb(65, 72, 88);\n"
"padding:5px")
        self.label_yesr_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_9.setMargin(0)

        self.verticalLayout_5.addWidget(self.label_yesr_9)

        self.frame_59 = QFrame(self.frame_36)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_59)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.label_yesr_19 = QLabel(self.frame_59)
        self.label_yesr_19.setObjectName(u"label_yesr_19")
        self.label_yesr_19.setMinimumSize(QSize(150, 35))
        self.label_yesr_19.setMaximumSize(QSize(150, 35))
        self.label_yesr_19.setMouseTracking(True)
        self.label_yesr_19.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_19.setStyleSheet(u"")
        self.label_yesr_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_19.setMargin(0)

        self.gridLayout_49.addWidget(self.label_yesr_19, 0, 1, 1, 1)

        self.label_yesr_30 = QLabel(self.frame_59)
        self.label_yesr_30.setObjectName(u"label_yesr_30")
        self.label_yesr_30.setMinimumSize(QSize(150, 35))
        self.label_yesr_30.setMaximumSize(QSize(150, 35))
        self.label_yesr_30.setMouseTracking(True)
        self.label_yesr_30.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_30.setStyleSheet(u"")
        self.label_yesr_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_30.setMargin(0)

        self.gridLayout_49.addWidget(self.label_yesr_30, 1, 1, 1, 1)

        self.label_yesr_20 = QLabel(self.frame_59)
        self.label_yesr_20.setObjectName(u"label_yesr_20")
        self.label_yesr_20.setMinimumSize(QSize(150, 35))
        self.label_yesr_20.setMaximumSize(QSize(150, 35))
        self.label_yesr_20.setMouseTracking(True)
        self.label_yesr_20.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_20.setStyleSheet(u"")
        self.label_yesr_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_20.setMargin(0)

        self.gridLayout_49.addWidget(self.label_yesr_20, 0, 2, 1, 1)

        self.label_yesr_29 = QLabel(self.frame_59)
        self.label_yesr_29.setObjectName(u"label_yesr_29")
        self.label_yesr_29.setMinimumSize(QSize(150, 35))
        self.label_yesr_29.setMaximumSize(QSize(150, 35))
        self.label_yesr_29.setMouseTracking(True)
        self.label_yesr_29.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_29.setStyleSheet(u"")
        self.label_yesr_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_29.setMargin(0)

        self.gridLayout_49.addWidget(self.label_yesr_29, 1, 0, 1, 1)

        self.label_yesr_22 = QLabel(self.frame_59)
        self.label_yesr_22.setObjectName(u"label_yesr_22")
        self.label_yesr_22.setMinimumSize(QSize(150, 35))
        self.label_yesr_22.setMaximumSize(QSize(150, 35))
        self.label_yesr_22.setMouseTracking(True)
        self.label_yesr_22.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_22.setStyleSheet(u"")
        self.label_yesr_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_22.setMargin(0)

        self.gridLayout_49.addWidget(self.label_yesr_22, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_59)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_49.addWidget(self.lineEdit_2, 0, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_59, 0, Qt.AlignLeft)


        self.gridLayout_24.addWidget(self.frame_36, 0, 0, 1, 1, Qt.AlignTop)

        self.pages.addWidget(self.page_4)

        self.gridLayout_8.addWidget(self.pages, 0, 1, 1, 1)

        QWidget.setTabOrder(self.lineEdit_year, self.lineEdit_testNumber)
        QWidget.setTabOrder(self.lineEdit_testNumber, self.QC_Test_RadioButton)
        QWidget.setTabOrder(self.QC_Test_RadioButton, self.Costom_Test_RadioButton)
        QWidget.setTabOrder(self.Costom_Test_RadioButton, self.lineEdit_costomer)
        QWidget.setTabOrder(self.lineEdit_costomer, self.lineEdit_costomerName)
        QWidget.setTabOrder(self.lineEdit_costomerName, self.lineEdit_testMeterialName)
        QWidget.setTabOrder(self.lineEdit_testMeterialName, self.lineEdit_testMeterial)
        QWidget.setTabOrder(self.lineEdit_testMeterial, self.lineEdit_MeterialMainDie)
        QWidget.setTabOrder(self.lineEdit_MeterialMainDie, self.lineEdit_MeterialinnerDie)
        QWidget.setTabOrder(self.lineEdit_MeterialinnerDie, self.lineEdit_thinkness)
        QWidget.setTabOrder(self.lineEdit_thinkness, self.lineEdit_PID_0_P)
        QWidget.setTabOrder(self.lineEdit_PID_0_P, self.lineEdit_PID_0_I)
        QWidget.setTabOrder(self.lineEdit_PID_0_I, self.lineEdit_PID_0_D)
        QWidget.setTabOrder(self.lineEdit_PID_0_D, self.lineEdit_PID_1_P)
        QWidget.setTabOrder(self.lineEdit_PID_1_P, self.lineEdit_PID_1_I)
        QWidget.setTabOrder(self.lineEdit_PID_1_I, self.lineEdit_PID_1_D)
        QWidget.setTabOrder(self.lineEdit_PID_1_D, self.lineEdit_PID_2_P)
        QWidget.setTabOrder(self.lineEdit_PID_2_P, self.lineEdit_PID_2_I)
        QWidget.setTabOrder(self.lineEdit_PID_2_I, self.lineEdit_PID_2_D)
        QWidget.setTabOrder(self.lineEdit_PID_2_D, self.lineEdit_PID_3_P)
        QWidget.setTabOrder(self.lineEdit_PID_3_P, self.lineEdit_PID_3_I)
        QWidget.setTabOrder(self.lineEdit_PID_3_I, self.lineEdit_PID_3_D)
        QWidget.setTabOrder(self.lineEdit_PID_3_D, self.lineEdit_PID_4_P)
        QWidget.setTabOrder(self.lineEdit_PID_4_P, self.lineEdit_PID_4_I)
        QWidget.setTabOrder(self.lineEdit_PID_4_I, self.lineEdit_PID_4_D)
        QWidget.setTabOrder(self.lineEdit_PID_4_D, self.lineEdit_PID_5_P)
        QWidget.setTabOrder(self.lineEdit_PID_5_P, self.lineEdit_PID_5_I)
        QWidget.setTabOrder(self.lineEdit_PID_5_I, self.lineEdit_PID_5_D)
        QWidget.setTabOrder(self.lineEdit_PID_5_D, self.lineEdit_PID_6_P)
        QWidget.setTabOrder(self.lineEdit_PID_6_P, self.lineEdit_PID_6_I)
        QWidget.setTabOrder(self.lineEdit_PID_6_I, self.lineEdit_PID_6_D)
        QWidget.setTabOrder(self.lineEdit_PID_6_D, self.lineEdit_PID_7_P)
        QWidget.setTabOrder(self.lineEdit_PID_7_P, self.lineEdit_PID_7_I)
        QWidget.setTabOrder(self.lineEdit_PID_7_I, self.lineEdit_PID_7_D)
        QWidget.setTabOrder(self.lineEdit_PID_7_D, self.lineEdit_PID_8_P)
        QWidget.setTabOrder(self.lineEdit_PID_8_P, self.lineEdit_PID_8_I)
        QWidget.setTabOrder(self.lineEdit_PID_8_I, self.lineEdit_PID_8_D)
        QWidget.setTabOrder(self.lineEdit_PID_8_D, self.lineEdit_PID_9_P)
        QWidget.setTabOrder(self.lineEdit_PID_9_P, self.lineEdit_PID_9_I)
        QWidget.setTabOrder(self.lineEdit_PID_9_I, self.lineEdit_PID_9_D)
        QWidget.setTabOrder(self.lineEdit_PID_9_D, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.graphItem_combobox)
        QWidget.setTabOrder(self.graphItem_combobox, self.timeUnit_comboBox)
        QWidget.setTabOrder(self.timeUnit_comboBox, self.Resistor_checkBox)
        QWidget.setTabOrder(self.Resistor_checkBox, self.Voltage_checkBox)
        QWidget.setTabOrder(self.Voltage_checkBox, self.Current_checkBox)
        QWidget.setTabOrder(self.Current_checkBox, self.remoteConnect_pushButton)
        QWidget.setTabOrder(self.remoteConnect_pushButton, self.btn_AutoMode)
        QWidget.setTabOrder(self.btn_AutoMode, self.btn_ManaualMode)
        QWidget.setTabOrder(self.btn_ManaualMode, self.autostart_pushButton)
        QWidget.setTabOrder(self.autostart_pushButton, self.eMSstop_pushButton)
        QWidget.setTabOrder(self.eMSstop_pushButton, self.AutoMode_pattern_comboBox)
        QWidget.setTabOrder(self.AutoMode_pattern_comboBox, self.outputStop_pushButton)
        QWidget.setTabOrder(self.outputStop_pushButton, self.manaualMode_comboBox)
        QWidget.setTabOrder(self.manaualMode_comboBox, self.measurement_comboBox)
        QWidget.setTabOrder(self.measurement_comboBox, self.voltage_lineEdit)
        QWidget.setTabOrder(self.voltage_lineEdit, self.voltageOutput_pushButton)
        QWidget.setTabOrder(self.voltageOutput_pushButton, self.manualMeasurement_pushButton)
        QWidget.setTabOrder(self.manualMeasurement_pushButton, self.noiseMeasurement_Voltage_lineEdit)
        QWidget.setTabOrder(self.noiseMeasurement_Voltage_lineEdit, self.noiseMeasurement_Current_lineEdit)
        QWidget.setTabOrder(self.noiseMeasurement_Current_lineEdit, self.noiseMeasurement_Time_lineEdit)
        QWidget.setTabOrder(self.noiseMeasurement_Time_lineEdit, self.Noisetest_pushButton)
        QWidget.setTabOrder(self.Noisetest_pushButton, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.scrollArea_3)
        QWidget.setTabOrder(self.scrollArea_3, self.RT_combobox)
        QWidget.setTabOrder(self.RT_combobox, self.patternfile_comboBox)
        QWidget.setTabOrder(self.patternfile_comboBox, self.commect_lineEdit)
        QWidget.setTabOrder(self.commect_lineEdit, self.gas_Combobox)
        QWidget.setTabOrder(self.gas_Combobox, self.RT_testpattern_combobox)
        QWidget.setTabOrder(self.RT_testpattern_combobox, self.test_commect_lineEdit)
        QWidget.setTabOrder(self.test_commect_lineEdit, self.testfile_comboBox)
        QWidget.setTabOrder(self.testfile_comboBox, self.scrollArea_4)
        QWidget.setTabOrder(self.scrollArea_4, self.test_sampletime_LineEdit)
        QWidget.setTabOrder(self.test_sampletime_LineEdit, self.bg_sampletime_LineEdit)
        QWidget.setTabOrder(self.bg_sampletime_LineEdit, self.test_time_LineEdit)
        QWidget.setTabOrder(self.test_time_LineEdit, self.bg_time_LineEdit)
        QWidget.setTabOrder(self.bg_time_LineEdit, self.bg0_time_LineEdit)
        QWidget.setTabOrder(self.bg0_time_LineEdit, self.speed_comboBox)
        QWidget.setTabOrder(self.speed_comboBox, self.filter_comboBox)
        QWidget.setTabOrder(self.filter_comboBox, self.filter_count_LineEdit)
        QWidget.setTabOrder(self.filter_count_LineEdit, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.AutoMode_pattern_comboBox.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.lineEdit_testNumber.setText(QCoreApplication.translate("MainPages", u"MS-4371", None))
        self.Costom_Test_RadioButton.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u6e2c\u5b9a", None))
        self.label_60.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u756a\u53f7", None))
        self.QC_Test_RadioButton.setText(QCoreApplication.translate("MainPages", u"\u8a55\u4fa1\u8a66\u9a13", None))
        self.lineEdit_year.setText(QCoreApplication.translate("MainPages", u"2021", None))
        self.label_year.setText(QCoreApplication.translate("MainPages", u"\u5e74\u5ea6", None))
        self.lineEdit_costomer.setText(QCoreApplication.translate("MainPages", u"\u682a\u5f0f\u4f1a\u793e\u30e2\u30c8\u30e4\u30de", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u5143", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u8005", None))
        self.lineEdit_costomerName.setText(QCoreApplication.translate("MainPages", u"\u9ec4", None))
        self.label_32.setText(QCoreApplication.translate("MainPages", u"\u8a66\u6599\u4f53\u7a4d(mm\u00b3)", None))
        self.lineEdit_testMeterialName.setText(QCoreApplication.translate("MainPages", u"material_1", None))
        self.lineEdit_meterialArea.setText(QCoreApplication.translate("MainPages", u"2.5", None))
        self.lineEdit_testMeterial.setText(QCoreApplication.translate("MainPages", u"42", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"\u8a66\u6599\u306e\u539a\u3055(mm)", None))
        self.lineEdit_thinkness.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.label_26.setText(QCoreApplication.translate("MainPages", u"\u8a66\u6599\u8868\u9762\u7a4d(mm\u00b2)", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"\u4e3b\u96fb\u6975\u5f84(mm)", None))
        self.lineEdit_MeterialinnerDie.setText(QCoreApplication.translate("MainPages", u"15", None))
        self.label_24.setText(QCoreApplication.translate("MainPages", u"\u8a66\u6599\u540d\u79f0", None))
        self.lineEdit_MeterialMainDie.setText(QCoreApplication.translate("MainPages", u"42", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"\u30ac\u30fc\u30c9\u96fb\u6975\u306e\u5185\u5f84(mm)", None))
        self.label_22.setText(QCoreApplication.translate("MainPages", u"\u6750\u6599", None))
        self.lineEdit_meterialVolume.setText(QCoreApplication.translate("MainPages", u"4.88", None))
        self.lineEdit_PID_0_D.setText(QCoreApplication.translate("MainPages", u"593", None))
        self.lineEdit_PID_0_I.setText(QCoreApplication.translate("MainPages", u"1000", None))
        self.label_121.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 0", None))
        self.label_122.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_123.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_124.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_0_P.setText(QCoreApplication.translate("MainPages", u"35", None))
        self.lineEdit_PID_1_D.setText(QCoreApplication.translate("MainPages", u"593", None))
        self.lineEdit_PID_1_I.setText(QCoreApplication.translate("MainPages", u"1000", None))
        self.label_125.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 1", None))
        self.label_126.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_127.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_128.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_1_P.setText(QCoreApplication.translate("MainPages", u"35", None))
        self.lineEdit_PID_2_D.setText(QCoreApplication.translate("MainPages", u"593", None))
        self.lineEdit_PID_2_I.setText(QCoreApplication.translate("MainPages", u"1000", None))
        self.label_133.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 2", None))
        self.label_134.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_135.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_136.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_2_P.setText(QCoreApplication.translate("MainPages", u"35", None))
        self.lineEdit_PID_3_D.setText(QCoreApplication.translate("MainPages", u"593", None))
        self.lineEdit_PID_3_I.setText(QCoreApplication.translate("MainPages", u"1000", None))
        self.label_137.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 3", None))
        self.label_138.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_139.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_140.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_3_P.setText(QCoreApplication.translate("MainPages", u"35", None))
        self.lineEdit_PID_4_D.setText(QCoreApplication.translate("MainPages", u"593", None))
        self.lineEdit_PID_4_I.setText(QCoreApplication.translate("MainPages", u"1000", None))
        self.label_141.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 4", None))
        self.label_142.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_143.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_144.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_4_P.setText(QCoreApplication.translate("MainPages", u"35", None))
        self.lineEdit_PID_5_D.setText(QCoreApplication.translate("MainPages", u"593", None))
        self.lineEdit_PID_5_I.setText(QCoreApplication.translate("MainPages", u"1000", None))
        self.label_129.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 5", None))
        self.label_130.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_131.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_132.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_5_P.setText(QCoreApplication.translate("MainPages", u"35", None))
        self.lineEdit_PID_6_D.setText(QCoreApplication.translate("MainPages", u"593", None))
        self.lineEdit_PID_6_I.setText(QCoreApplication.translate("MainPages", u"1000", None))
        self.label_145.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 6", None))
        self.label_146.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_147.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_148.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_6_P.setText(QCoreApplication.translate("MainPages", u"35", None))
        self.lineEdit_PID_7_D.setText(QCoreApplication.translate("MainPages", u"593", None))
        self.lineEdit_PID_7_I.setText(QCoreApplication.translate("MainPages", u"1000", None))
        self.label_149.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 7", None))
        self.label_150.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_151.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_152.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_7_P.setText(QCoreApplication.translate("MainPages", u"35", None))
        self.lineEdit_PID_8_D.setText(QCoreApplication.translate("MainPages", u"593", None))
        self.lineEdit_PID_8_I.setText(QCoreApplication.translate("MainPages", u"1000", None))
        self.label_153.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 8", None))
        self.label_154.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_155.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_156.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_8_P.setText(QCoreApplication.translate("MainPages", u"35", None))
        self.lineEdit_PID_9_D.setText(QCoreApplication.translate("MainPages", u"593", None))
        self.lineEdit_PID_9_I.setText(QCoreApplication.translate("MainPages", u"1000", None))
        self.label_157.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 9", None))
        self.label_158.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_159.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_160.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_9_P.setText(QCoreApplication.translate("MainPages", u"35", None))
        self.label_17.setText(QCoreApplication.translate("MainPages", u"\u505c\u6b62\u4e2d", None))
        self.label_40.setText(QCoreApplication.translate("MainPages", u"\u771f\u7a7a\u7f6e\u63db\u4e2d", None))
        self.label_37.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u4e2d", None))
        self.label_39.setText(QCoreApplication.translate("MainPages", u"\u8b66\u5831", None))
        self.label_38.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u7d42\u4e86", None))
        self.label_45.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u53ef", None))
        self.label_30.setText(QCoreApplication.translate("MainPages", u"\u6e29\u5ea6\u30ad\u30fc\u30d7\u4e2d", None))
        self.label_28.setText(QCoreApplication.translate("MainPages", u"\u6607\u6e29\u4e2d", None))
        self.realtime_Voltage_lineEdit.setText("")
        self.label_31.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u96fb\u5727", None))
        self.label_34.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u62b5\u6297", None))
        self.realtime_Resistor_lineEdit.setText("")
        self.label_35.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u96fb\u6d41", None))
        self.realtime_Current_lineEdit.setText("")
        self.label_23.setText(QCoreApplication.translate("MainPages", u"\u7089\u5185\u6e29\u5ea6", None))
        self.realtime_Temp_lineEdit.setText("")
        self.label_48.setText(QCoreApplication.translate("MainPages", u"\u7089\u5185\u5727\u529b", None))
        self.realtime_Pressure_lineEdit.setText("")
        self.graphItem_label.setText(QCoreApplication.translate("MainPages", u"\u8868\u793a\u9805\u76ee", None))
        self.graphItem_combobox.setItemText(0, QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u6570\u5024", None))
        self.graphItem_combobox.setItemText(1, QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u30d1\u30bf\u30fc\u30f3", None))

        self.timeUnit_Label.setText(QCoreApplication.translate("MainPages", u"\u6642\u9593\u5358\u4f4d", None))
        self.timeUnit_comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1s/div", None))
        self.timeUnit_comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"10s/div", None))
        self.timeUnit_comboBox.setItemText(2, QCoreApplication.translate("MainPages", u"30s/div", None))
        self.timeUnit_comboBox.setItemText(3, QCoreApplication.translate("MainPages", u"1min/div", None))
        self.timeUnit_comboBox.setItemText(4, QCoreApplication.translate("MainPages", u"10min/div", None))
        self.timeUnit_comboBox.setItemText(5, QCoreApplication.translate("MainPages", u"1h/div", None))

        self.Resistor_checkBox.setText(QCoreApplication.translate("MainPages", u"\u62b5\u6297\u5024", None))
        self.Voltage_checkBox.setText(QCoreApplication.translate("MainPages", u"\u96fb\u5727", None))
        self.Current_checkBox.setText(QCoreApplication.translate("MainPages", u"\u96fb\u6d41", None))
        self.label_2.setText("")
        self.remoteConnect_pushButton.setText(QCoreApplication.translate("MainPages", u"\u30ea\u30e2\u30fc\u30c8\u63a5\u7d9a", None))
        self.btn_AutoMode.setText(QCoreApplication.translate("MainPages", u"\u81ea\u52d5\u30e2\u30fc\u30c9", None))
        self.btn_ManaualMode.setText(QCoreApplication.translate("MainPages", u"\u624b\u52d5\u6e2c\u5b9a\u30e2\u30fc\u30c9", None))
        self.gasFreeflow_pushButton.setText(QCoreApplication.translate("MainPages", u"\u5927\u6c17\u5727", None))
        self.autostart_pushButton.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u958b\u59cb", None))
        self.label_11.setText("")
        self.eMSstop_pushButton.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u505c\u6b62", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u30d1\u30bf\u30fc\u30f3\u540d", None))
        self.AutoMode_pattern_comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"pattern1", None))
        self.AutoMode_pattern_comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"pattern2", None))

        self.Gas_mode_Label.setText(QCoreApplication.translate("MainPages", u"\u96f0\u56f2\u6c17\u30e2\u30fc\u30c9\uff1a\u5927\u6c17", None))
        self.label_18.setText("")
        self.outputStop_pushButton.setText(QCoreApplication.translate("MainPages", u"\u51fa\u529b\u505c\u6b62", None))
        self.manaualMode_comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"\u4e00\u822c\u6e2c\u5b9a", None))
        self.manaualMode_comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"\u30ce\u30a4\u30ba\u6e2c\u5b9a", None))

        self.label_20.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u96fb\u5727(V)", None))
        self.label_21.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u30e2\u30fc\u30c9", None))
        self.measurement_comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"\u9023\u7d9a\u4e8c\u56de\u6e2c\u5b9a", None))
        self.measurement_comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"\u4e00\u56de\u6e2c\u5b9a", None))

        self.voltage_lineEdit.setText(QCoreApplication.translate("MainPages", u"2000", None))
        self.voltageOutput_pushButton.setText(QCoreApplication.translate("MainPages", u"\u96fb\u5727\u5370\u52a0", None))
        self.manualMeasurement_pushButton.setText(QCoreApplication.translate("MainPages", u"\u30de\u30cb\u30e5\u30a2\u30eb\u6e2c\u5b9a", None))
        self.noiseMeasurement_Voltage_lineEdit.setText(QCoreApplication.translate("MainPages", u"100", None))
        self.label_33.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u96fb\u5727(V)", None))
        self.noiseMeasurement_Current_lineEdit.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.noiseMeasurement_Time_lineEdit.setText(QCoreApplication.translate("MainPages", u"10", None))
        self.label_44.setText(QCoreApplication.translate("MainPages", u"\u5408\u683c\u5224\u5b9a\u57fa\u6e96(pA)", None))
        self.label_36.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u6642\u9593(min)", None))
        self.Noisetest_pushButton.setText(QCoreApplication.translate("MainPages", u"\u30ce\u30a4\u30ba\u6e2c\u5b9a", None))
        self.Temp_Totaltime_Label.setText(QCoreApplication.translate("MainPages", u"\u5408\u8a08\u6642\u9593: 0 \u6642\u9593 0 \u5206", None))
        self.label_63.setText(QCoreApplication.translate("MainPages", u"\u96f0\u56f2\u6c17", None))
        self.label_27.setText(QCoreApplication.translate("MainPages", u"\u30d1\u30bf\u30fc\u30f3\u540d", None))
        self.label_25.setText(QCoreApplication.translate("MainPages", u"\u8a3b\u8a18", None))
        self.RT_combobox.setItemText(0, QCoreApplication.translate("MainPages", u"\u306a\u3044", None))
        self.RT_combobox.setItemText(1, QCoreApplication.translate("MainPages", u"\u6709\u308a", None))

        self.patternfile_comboBox.setItemText(0, "")

        self.RT_Label.setText(QCoreApplication.translate("MainPages", u"RT\u6e2c\u5b9a", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"\u4fdd\u5b58", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"\u8ffd\u52a0", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"\u524a\u9664", None))
        self.PatternErrorMessagelabel.setText(QCoreApplication.translate("MainPages", u"\u7121\u52b9\u5165\u529b:", None))
        self.commect_lineEdit.setInputMask("")
        self.commect_lineEdit.setText("")
        self.label_65.setText(QCoreApplication.translate("MainPages", u"\u6607\u964d\u6e29", None))
        self.label_29.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u30d1\u30bf\u30fc\u30f3", None))
        self.gas_Combobox.setItemText(0, QCoreApplication.translate("MainPages", u"\u5927\u6c17", None))
        self.gas_Combobox.setItemText(1, QCoreApplication.translate("MainPages", u"\u771f\u7a7a", None))
        self.gas_Combobox.setItemText(2, QCoreApplication.translate("MainPages", u"N2\u7f6e\u63db", None))

        self.RT_testpattern_combobox.setItemText(0, QCoreApplication.translate("MainPages", u"\u306a\u3044", None))
        self.RT_testpattern_combobox.setItemText(1, QCoreApplication.translate("MainPages", u"\u6709\u308a", None))

        self.TestPatternErrorMessagelabel.setText(QCoreApplication.translate("MainPages", u"\u7121\u52b9\u5165\u529b:", None))
        self.label_43.setText(QCoreApplication.translate("MainPages", u"\u30d1\u30bf\u30fc\u30f3\u540d", None))
        self.label_42.setText(QCoreApplication.translate("MainPages", u"\u8a3b\u8a18", None))
        self.test_commect_lineEdit.setInputMask("")
        self.label_41.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u30d1\u30bf\u30fc\u30f3", None))
        self.Test_Totaltime_Label.setText(QCoreApplication.translate("MainPages", u"\u5408\u8a08\u6642\u9593: 0 \u6642\u9593 0 \u5206", None))
        self.label_47.setText(QCoreApplication.translate("MainPages", u"\u4fdd\u5b58", None))
        self.label_46.setText(QCoreApplication.translate("MainPages", u"\u8ffd\u52a0", None))
        self.label_15.setText(QCoreApplication.translate("MainPages", u"\u524a\u9664", None))
        self.test_sampletime_LineEdit.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.label_61.setText(QCoreApplication.translate("MainPages", u"BG \u6e2c\u5b9a\u6642\u9593(min)", None))
        self.bg_sampletime_LineEdit.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.test_time_LineEdit.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.bg_time_LineEdit.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.label_59.setText(QCoreApplication.translate("MainPages", u"\u4e3b\u6e2c\u5b9a\u30b5\u30f3\u30d7\u30ea\u30f3\u30b0\u5468\u671f(s)", None))
        self.label_58.setText(QCoreApplication.translate("MainPages", u"\u4e3b\u6e2c\u5b9a\u6642\u9593(min)", None))
        self.speed_label.setText(QCoreApplication.translate("MainPages", u"Speed", None))
        self.label_66.setText(QCoreApplication.translate("MainPages", u"BG \u6e2c\u5b9a\u30b5\u30f3\u30d7\u30ea\u30f3\u30b0\u5468\u671f(s)", None))
        self.label_62.setText(QCoreApplication.translate("MainPages", u"BG0 \u6e2c\u5b9a\u6642\u9593(min)", None))
        self.bg0_time_LineEdit.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.speed_comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"Normal (1PLC)", None))
        self.speed_comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"Hi Accuracy (10PLC)", None))

        self.filter_label.setText(QCoreApplication.translate("MainPages", u"Filter", None))
        self.filter_comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"\u306a\u3057", None))
        self.filter_comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"\u5e73\u5747(repeating)", None))
        self.filter_comboBox.setItemText(2, QCoreApplication.translate("MainPages", u"\u79fb\u52d5\u5e73\u5747(moving)", None))
        self.filter_comboBox.setItemText(3, QCoreApplication.translate("MainPages", u"\u4e2d\u592e\u5024(Median)", None))

        self.filter_count_label.setText(QCoreApplication.translate("MainPages", u"Filter count", None))
        self.filter_count_LineEdit.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.label_yesr_7.setText(QCoreApplication.translate("MainPages", u"Ethernet \u30a4\u30f3\u30bf\u30fc\u30d5\u30a7\u30fc\u30b9 : Modbus TCP \u30b5\u30fc\u30d0\u30fc", None))
        self.label_yesr_3.setText(QCoreApplication.translate("MainPages", u"192.168.0.105:502", None))
        self.label_yesr_2.setText(QCoreApplication.translate("MainPages", u"IPv4 \u30a2\u30c9\u30ec\u30b9:", None))
        self.label_yesr_24.setText(QCoreApplication.translate("MainPages", u"\u671f\u9593:", None))
        self.label_yesr_4.setText(QCoreApplication.translate("MainPages", u"\u30dd\u30fc\u30c8:", None))
        self.label_yesr_26.setText(QCoreApplication.translate("MainPages", u"192.168.0.25", None))
        self.label_yesr_6.setText(QCoreApplication.translate("MainPages", u"502", None))
        self.label_yesr_15.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.label_yesr_12.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u4e2d", None))
        self.label_yesr_14.setText(QCoreApplication.translate("MainPages", u"\u30af\u30e9\u30a4\u30a2\u30f3\u30c8 IP:", None))
        self.label_yesr_13.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u30af\u30e9\u30a4\u30a2\u30f3\u30c8\u6570:", None))
        self.label_yesr_25.setText(QCoreApplication.translate("MainPages", u"15:41:10", None))
        self.label_yesr_10.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u72b6\u614b:", None))
        self.label_yesr_8.setText(QCoreApplication.translate("MainPages", u"GPIB \u30a4\u30f3\u30bf\u30fc\u30d5\u30a7\u30fc\u30b9 : 2657A  \u30cf\u30a4\u30d1\u30ef\u30fc\u30b7\u30b9\u30c6\u30e0\u30bd\u30fc\u30b9\u30e1\u30fc\u30c0", None))
        self.label_yesr_28.setText(QCoreApplication.translate("MainPages", u"15:41:10", None))
        self.label_yesr_27.setText(QCoreApplication.translate("MainPages", u"\u671f\u9593:", None))
        self.label_yesr_11.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u72b6\u614b:", None))
        self.label_yesr_17.setText(QCoreApplication.translate("MainPages", u"\u30a2\u30c9\u30ec\u30b9: ", None))
        self.label_yesr_16.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u4e2d", None))
        self.lineEdit.setText(QCoreApplication.translate("MainPages", u"24", None))
        self.label_yesr_9.setText(QCoreApplication.translate("MainPages", u"GPIB \u30a4\u30f3\u30bf\u30fc\u30d5\u30a7\u30fc\u30b9 : 2635B  \u30b7\u30b9\u30c6\u30e0\u30fb\u30bd\u30fc\u30b9\u30e1\u30fc\u30bf", None))
        self.label_yesr_19.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u4e2d", None))
        self.label_yesr_30.setText(QCoreApplication.translate("MainPages", u"15:41:10", None))
        self.label_yesr_20.setText(QCoreApplication.translate("MainPages", u"\u30a2\u30c9\u30ec\u30b9: ", None))
        self.label_yesr_29.setText(QCoreApplication.translate("MainPages", u"\u671f\u9593:", None))
        self.label_yesr_22.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u72b6\u614b:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainPages", u"26", None))
    # retranslateUi

