# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesXsENvG.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1223, 689)
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
        self.gridLayout_17.setContentsMargins(9, 9, 9, 9)
        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1187, 653))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
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
        self.frame_48.setStyleSheet(u"")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_48)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_year = QLabel(self.frame_48)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setMinimumSize(QSize(140, 35))
        self.label_year.setMaximumSize(QSize(140, 35))
        self.label_year.setMouseTracking(False)
        self.label_year.setLayoutDirection(Qt.LeftToRight)
        self.label_year.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_year.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_year.setMargin(0)

        self.gridLayout_7.addWidget(self.label_year, 0, 0, 1, 1)

        self.lineEdit_year = QLineEdit(self.frame_48)
        self.lineEdit_year.setObjectName(u"lineEdit_year")
        self.lineEdit_year.setMinimumSize(QSize(60, 32))
        self.lineEdit_year.setMaximumSize(QSize(112, 16777215))
        self.lineEdit_year.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:100;")
        self.lineEdit_year.setFrame(False)
        self.lineEdit_year.setEchoMode(QLineEdit.Normal)
        self.lineEdit_year.setCursorPosition(4)

        self.gridLayout_7.addWidget(self.lineEdit_year, 0, 1, 1, 1)

        self.QC_Test_RadioButton = QRadioButton(self.frame_48)
        self.QC_Test_RadioButton.setObjectName(u"QC_Test_RadioButton")
        self.QC_Test_RadioButton.setMinimumSize(QSize(140, 32))
        self.QC_Test_RadioButton.setMaximumSize(QSize(140, 35))
        self.QC_Test_RadioButton.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:60px;\n"
"min-width:80;\n"
"max-width:80;")
        self.QC_Test_RadioButton.setChecked(True)

        self.gridLayout_7.addWidget(self.QC_Test_RadioButton, 1, 0, 1, 1)

        self.Costom_Test_RadioButton = QRadioButton(self.frame_48)
        self.Costom_Test_RadioButton.setObjectName(u"Costom_Test_RadioButton")
        self.Costom_Test_RadioButton.setMinimumSize(QSize(0, 32))
        self.Costom_Test_RadioButton.setMaximumSize(QSize(140, 32))
        self.Costom_Test_RadioButton.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:60px;\n"
"max-width:80;")

        self.gridLayout_7.addWidget(self.Costom_Test_RadioButton, 2, 0, 1, 1)

        self.label_60 = QLabel(self.frame_48)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(140, 35))
        self.label_60.setMaximumSize(QSize(140, 35))
        self.label_60.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_60, 3, 0, 1, 1)

        self.lineEdit_testNumber = QLineEdit(self.frame_48)
        self.lineEdit_testNumber.setObjectName(u"lineEdit_testNumber")
        self.lineEdit_testNumber.setMinimumSize(QSize(200, 32))
        self.lineEdit_testNumber.setMaximumSize(QSize(212, 16777215))
        self.lineEdit_testNumber.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:200;")

        self.gridLayout_7.addWidget(self.lineEdit_testNumber, 3, 1, 1, 1)

        self.label_4 = QLabel(self.frame_48)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(140, 35))
        self.label_4.setMaximumSize(QSize(140, 35))
        self.label_4.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_4, 4, 0, 1, 1)

        self.lineEdit_costomer = QLineEdit(self.frame_48)
        self.lineEdit_costomer.setObjectName(u"lineEdit_costomer")
        self.lineEdit_costomer.setMinimumSize(QSize(200, 32))
        self.lineEdit_costomer.setMaximumSize(QSize(212, 16777215))
        self.lineEdit_costomer.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:200;")

        self.gridLayout_7.addWidget(self.lineEdit_costomer, 4, 1, 1, 1)

        self.label_5 = QLabel(self.frame_48)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(140, 35))
        self.label_5.setMaximumSize(QSize(140, 35))
        self.label_5.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_5, 5, 0, 1, 1)

        self.lineEdit_costomerName = QLineEdit(self.frame_48)
        self.lineEdit_costomerName.setObjectName(u"lineEdit_costomerName")
        self.lineEdit_costomerName.setMinimumSize(QSize(200, 32))
        self.lineEdit_costomerName.setMaximumSize(QSize(212, 16777215))
        self.lineEdit_costomerName.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:200;")

        self.gridLayout_7.addWidget(self.lineEdit_costomerName, 5, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_48, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_63 = QFrame(self.frame_42)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(3, 0))
        self.frame_63.setMaximumSize(QSize(3, 16777215))
        self.frame_63.setStyleSheet(u"background-color: rgb(65, 72, 88);")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_64 = QFrame(self.frame_63)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_64, 0, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.frame_63, 0, Qt.AlignLeft)

        self.frame_62 = QFrame(self.frame_42)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setStyleSheet(u"")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_62)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_32 = QLabel(self.frame_62)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(140, 0))
        self.label_32.setMaximumSize(QSize(140, 16777215))
        self.label_32.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_32, 6, 0, 1, 1)

        self.lineEdit_testMeterialName = QLineEdit(self.frame_62)
        self.lineEdit_testMeterialName.setObjectName(u"lineEdit_testMeterialName")
        self.lineEdit_testMeterialName.setMinimumSize(QSize(200, 32))
        self.lineEdit_testMeterialName.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_testMeterialName.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_10.addWidget(self.lineEdit_testMeterialName, 0, 1, 1, 1)

        self.lineEdit_meterialArea = QLabel(self.frame_62)
        self.lineEdit_meterialArea.setObjectName(u"lineEdit_meterialArea")
        self.lineEdit_meterialArea.setMinimumSize(QSize(140, 32))
        self.lineEdit_meterialArea.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_meterialArea.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.lineEdit_meterialArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.lineEdit_meterialArea, 5, 1, 1, 1)

        self.lineEdit_testMeterial = QLineEdit(self.frame_62)
        self.lineEdit_testMeterial.setObjectName(u"lineEdit_testMeterial")
        self.lineEdit_testMeterial.setMinimumSize(QSize(200, 32))
        self.lineEdit_testMeterial.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_testMeterial.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_10.addWidget(self.lineEdit_testMeterial, 1, 1, 1, 1)

        self.label_10 = QLabel(self.frame_62)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(140, 0))
        self.label_10.setMaximumSize(QSize(140, 16777215))
        self.label_10.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_10, 4, 0, 1, 1)

        self.lineEdit_thinkness = QLineEdit(self.frame_62)
        self.lineEdit_thinkness.setObjectName(u"lineEdit_thinkness")
        self.lineEdit_thinkness.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_thinkness.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_10.addWidget(self.lineEdit_thinkness, 4, 1, 1, 1)

        self.label_26 = QLabel(self.frame_62)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(140, 0))
        self.label_26.setMaximumSize(QSize(140, 16777215))
        self.label_26.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_26, 5, 0, 1, 1)

        self.label_8 = QLabel(self.frame_62)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(140, 35))
        self.label_8.setMaximumSize(QSize(140, 35))
        self.label_8.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_8, 2, 0, 1, 1)

        self.lineEdit_MeterialinnerDie = QLineEdit(self.frame_62)
        self.lineEdit_MeterialinnerDie.setObjectName(u"lineEdit_MeterialinnerDie")
        self.lineEdit_MeterialinnerDie.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_MeterialinnerDie.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_10.addWidget(self.lineEdit_MeterialinnerDie, 3, 1, 1, 1)

        self.label_24 = QLabel(self.frame_62)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(140, 35))
        self.label_24.setMaximumSize(QSize(140, 35))
        self.label_24.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_24, 0, 0, 1, 1)

        self.lineEdit_MeterialMainDie = QLineEdit(self.frame_62)
        self.lineEdit_MeterialMainDie.setObjectName(u"lineEdit_MeterialMainDie")
        self.lineEdit_MeterialMainDie.setMinimumSize(QSize(0, 32))
        self.lineEdit_MeterialMainDie.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_MeterialMainDie.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_10.addWidget(self.lineEdit_MeterialMainDie, 2, 1, 1, 1)

        self.label_9 = QLabel(self.frame_62)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(140, 0))
        self.label_9.setMaximumSize(QSize(140, 16777215))
        self.label_9.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_22 = QLabel(self.frame_62)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(140, 35))
        self.label_22.setMaximumSize(QSize(140, 35))
        self.label_22.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_22, 1, 0, 1, 1)

        self.lineEdit_meterialVolume = QLabel(self.frame_62)
        self.lineEdit_meterialVolume.setObjectName(u"lineEdit_meterialVolume")
        self.lineEdit_meterialVolume.setMinimumSize(QSize(140, 32))
        self.lineEdit_meterialVolume.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_meterialVolume.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.lineEdit_meterialVolume.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.lineEdit_meterialVolume, 6, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_62, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_42, 0, Qt.AlignLeft)

        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 6))
        self.label_13.setMaximumSize(QSize(16777215, 6))
        self.label_13.setStyleSheet(u"\n"
"background-color: rgb(65, 72, 88);\n"
"font: 12px bold large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);")

        self.verticalLayout_9.addWidget(self.label_13)

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
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.frame_74 = QFrame(self.frame_72)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(150, 180))
        self.frame_74.setMaximumSize(QSize(150, 180))
        self.frame_74.setStyleSheet(u"background-color: rgb(36, 40, 49);\n"
"border-radius: 5px;")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.gridLayout_60 = QGridLayout(self.frame_74)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_1_D = QLineEdit(self.frame_74)
        self.lineEdit_PID_1_D.setObjectName(u"lineEdit_PID_1_D")
        self.lineEdit_PID_1_D.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_1_D.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_1_D.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_1_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.lineEdit_PID_1_D, 3, 1, 1, 1)

        self.lineEdit_PID_1_I = QLineEdit(self.frame_74)
        self.lineEdit_PID_1_I.setObjectName(u"lineEdit_PID_1_I")
        self.lineEdit_PID_1_I.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_1_I.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_1_I.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_1_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.lineEdit_PID_1_I, 2, 1, 1, 1)

        self.label_109 = QLabel(self.frame_74)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMinimumSize(QSize(0, 32))
        self.label_109.setMaximumSize(QSize(16777215, 32))
        self.label_109.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_109.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.label_109, 0, 0, 1, 2)

        self.label_110 = QLabel(self.frame_74)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(0, 32))
        self.label_110.setMaximumSize(QSize(16777215, 32))
        self.label_110.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_110.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.label_110, 2, 0, 1, 1)

        self.label_111 = QLabel(self.frame_74)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMinimumSize(QSize(0, 32))
        self.label_111.setMaximumSize(QSize(16777215, 32))
        self.label_111.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_111.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.label_111, 1, 0, 1, 1)

        self.label_112 = QLabel(self.frame_74)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(0, 32))
        self.label_112.setMaximumSize(QSize(16777215, 32))
        self.label_112.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_112.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.label_112, 3, 0, 1, 1)

        self.lineEdit_PID_1_P = QLineEdit(self.frame_74)
        self.lineEdit_PID_1_P.setObjectName(u"lineEdit_PID_1_P")
        self.lineEdit_PID_1_P.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_1_P.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_1_P.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_1_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.lineEdit_PID_1_P, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.frame_72)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(150, 180))
        self.frame_75.setMaximumSize(QSize(150, 180))
        self.frame_75.setStyleSheet(u"background-color: rgb(36, 40, 49);\n"
"border-radius: 5px;")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.gridLayout_61 = QGridLayout(self.frame_75)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_2_D = QLineEdit(self.frame_75)
        self.lineEdit_PID_2_D.setObjectName(u"lineEdit_PID_2_D")
        self.lineEdit_PID_2_D.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_2_D.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_2_D.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_2_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.lineEdit_PID_2_D, 3, 1, 1, 1)

        self.lineEdit_PID_2_I = QLineEdit(self.frame_75)
        self.lineEdit_PID_2_I.setObjectName(u"lineEdit_PID_2_I")
        self.lineEdit_PID_2_I.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_2_I.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_2_I.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_2_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.lineEdit_PID_2_I, 2, 1, 1, 1)

        self.label_113 = QLabel(self.frame_75)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(0, 32))
        self.label_113.setMaximumSize(QSize(16777215, 32))
        self.label_113.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_113.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.label_113, 0, 0, 1, 2)

        self.label_114 = QLabel(self.frame_75)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(0, 32))
        self.label_114.setMaximumSize(QSize(16777215, 32))
        self.label_114.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_114.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.label_114, 2, 0, 1, 1)

        self.label_115 = QLabel(self.frame_75)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(0, 32))
        self.label_115.setMaximumSize(QSize(16777215, 32))
        self.label_115.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_115.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.label_115, 1, 0, 1, 1)

        self.label_116 = QLabel(self.frame_75)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(0, 32))
        self.label_116.setMaximumSize(QSize(16777215, 32))
        self.label_116.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_116.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.label_116, 3, 0, 1, 1)

        self.lineEdit_PID_2_P = QLineEdit(self.frame_75)
        self.lineEdit_PID_2_P.setObjectName(u"lineEdit_PID_2_P")
        self.lineEdit_PID_2_P.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_2_P.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_2_P.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_2_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.lineEdit_PID_2_P, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.frame_72)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(150, 180))
        self.frame_76.setMaximumSize(QSize(150, 180))
        self.frame_76.setStyleSheet(u"background-color: rgb(36, 40, 49);\n"
"border-radius: 5px;")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.gridLayout_62 = QGridLayout(self.frame_76)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_3_D = QLineEdit(self.frame_76)
        self.lineEdit_PID_3_D.setObjectName(u"lineEdit_PID_3_D")
        self.lineEdit_PID_3_D.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_3_D.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_3_D.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_3_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_62.addWidget(self.lineEdit_PID_3_D, 3, 1, 1, 1)

        self.lineEdit_PID_3_I = QLineEdit(self.frame_76)
        self.lineEdit_PID_3_I.setObjectName(u"lineEdit_PID_3_I")
        self.lineEdit_PID_3_I.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_3_I.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_3_I.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_3_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_62.addWidget(self.lineEdit_PID_3_I, 2, 1, 1, 1)

        self.label_117 = QLabel(self.frame_76)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(0, 32))
        self.label_117.setMaximumSize(QSize(16777215, 32))
        self.label_117.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_117.setAlignment(Qt.AlignCenter)

        self.gridLayout_62.addWidget(self.label_117, 0, 0, 1, 2)

        self.label_118 = QLabel(self.frame_76)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(0, 32))
        self.label_118.setMaximumSize(QSize(16777215, 32))
        self.label_118.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_118.setAlignment(Qt.AlignCenter)

        self.gridLayout_62.addWidget(self.label_118, 2, 0, 1, 1)

        self.label_119 = QLabel(self.frame_76)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(0, 32))
        self.label_119.setMaximumSize(QSize(16777215, 32))
        self.label_119.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_119.setAlignment(Qt.AlignCenter)

        self.gridLayout_62.addWidget(self.label_119, 1, 0, 1, 1)

        self.label_120 = QLabel(self.frame_76)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(0, 32))
        self.label_120.setMaximumSize(QSize(16777215, 32))
        self.label_120.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_120.setAlignment(Qt.AlignCenter)

        self.gridLayout_62.addWidget(self.label_120, 3, 0, 1, 1)

        self.lineEdit_PID_3_P = QLineEdit(self.frame_76)
        self.lineEdit_PID_3_P.setObjectName(u"lineEdit_PID_3_P")
        self.lineEdit_PID_3_P.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_3_P.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_3_P.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_3_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_62.addWidget(self.lineEdit_PID_3_P, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_76)

        self.frame_73 = QFrame(self.frame_72)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(150, 180))
        self.frame_73.setMaximumSize(QSize(150, 180))
        self.frame_73.setStyleSheet(u"background-color: rgb(36, 40, 49);\n"
"border-radius: 5px;")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.frame_73)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(-1, 9, -1, 9)
        self.lineEdit_PID_4_D = QLineEdit(self.frame_73)
        self.lineEdit_PID_4_D.setObjectName(u"lineEdit_PID_4_D")
        self.lineEdit_PID_4_D.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_4_D.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_4_D.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_4_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.lineEdit_PID_4_D, 3, 1, 1, 1)

        self.lineEdit_PID_4_I = QLineEdit(self.frame_73)
        self.lineEdit_PID_4_I.setObjectName(u"lineEdit_PID_4_I")
        self.lineEdit_PID_4_I.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_4_I.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_4_I.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_4_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.lineEdit_PID_4_I, 2, 1, 1, 1)

        self.label_105 = QLabel(self.frame_73)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMinimumSize(QSize(0, 32))
        self.label_105.setMaximumSize(QSize(16777215, 32))
        self.label_105.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_105.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.label_105, 0, 0, 1, 2)

        self.label_106 = QLabel(self.frame_73)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(0, 32))
        self.label_106.setMaximumSize(QSize(16777215, 32))
        self.label_106.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_106.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.label_106, 2, 0, 1, 1)

        self.label_107 = QLabel(self.frame_73)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(0, 32))
        self.label_107.setMaximumSize(QSize(16777215, 32))
        self.label_107.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_107.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.label_107, 1, 0, 1, 1)

        self.label_108 = QLabel(self.frame_73)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(0, 32))
        self.label_108.setMaximumSize(QSize(16777215, 32))
        self.label_108.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_108.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.label_108, 3, 0, 1, 1)

        self.lineEdit_PID_4_P = QLineEdit(self.frame_73)
        self.lineEdit_PID_4_P.setObjectName(u"lineEdit_PID_4_P")
        self.lineEdit_PID_4_P.setMinimumSize(QSize(0, 32))
        self.lineEdit_PID_4_P.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_PID_4_P.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.lineEdit_PID_4_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.lineEdit_PID_4_P, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_73)


        self.horizontalLayout_11.addWidget(self.frame_72)


        self.verticalLayout_9.addWidget(self.frame_47, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_12.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_17.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridFrame_2 = QFrame(self.page_2)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridFrame_2.setMinimumSize(QSize(0, 0))
        self.gridFrame_2.setMaximumSize(QSize(16777215, 240))
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
        self.label_37 = QLabel(self.frame_30)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_37, 0, 5, 1, 1)

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

        self.label_38 = QLabel(self.frame_30)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_38, 0, 6, 1, 1)

        self.label_30 = QLabel(self.frame_30)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_30, 0, 4, 1, 1)

        self.label_45 = QLabel(self.frame_30)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_45, 0, 0, 1, 1)

        self.label_28 = QLabel(self.frame_30)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_28, 0, 3, 1, 1)

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

        self.label_39 = QLabel(self.frame_30)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 30))
        self.label_39.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_39, 0, 7, 1, 1)

        self.label_17 = QLabel(self.frame_30)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_40 = QLabel(self.frame_30)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.Layout_Status_MSStatus.addWidget(self.label_40, 0, 2, 1, 1)

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
        self.frame_14.setStyleSheet(u"border:none")
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
        self.realtime_Voltage_lineEdit.setMinimumSize(QSize(0, 0))
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
        self.label_31.setStyleSheet(u"font: 18px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
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
        self.label_34.setStyleSheet(u"font: 18px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.label_34, 0, 0, 1, 1)

        self.realtime_Resistor_lineEdit = QLabel(self.frame_21)
        self.realtime_Resistor_lineEdit.setObjectName(u"realtime_Resistor_lineEdit")
        self.realtime_Resistor_lineEdit.setMinimumSize(QSize(0, 0))
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
        self.label_35.setStyleSheet(u"font: 18px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_33.addWidget(self.label_35, 0, 0, 1, 1)

        self.realtime_Current_lineEdit = QLabel(self.frame_67)
        self.realtime_Current_lineEdit.setObjectName(u"realtime_Current_lineEdit")
        self.realtime_Current_lineEdit.setMinimumSize(QSize(0, 0))
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
        self.label_23.setStyleSheet(u"font: 18px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_23, 0, 0, 1, 1)

        self.realtime_Temp_lineEdit = QLabel(self.frame_16)
        self.realtime_Temp_lineEdit.setObjectName(u"realtime_Temp_lineEdit")
        self.realtime_Temp_lineEdit.setMinimumSize(QSize(0, 0))
        self.realtime_Temp_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.realtime_Temp_lineEdit.setStyleSheet(u"font: 30px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"background-color: rgb(16, 18, 22);")
        self.realtime_Temp_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.realtime_Temp_lineEdit, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_16, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_14, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gridFrame_2, 1, 0, 1, 1)

        self.gridFrame_1 = QFrame(self.page_2)
        self.gridFrame_1.setObjectName(u"gridFrame_1")
        self.gridFrame_1.setMinimumSize(QSize(0, 0))
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
        self.frame_65 = QFrame(self.frame)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_44 = QLabel(self.frame_65)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_44)

        self.graphItem_combobox = QComboBox(self.frame_65)
        self.graphItem_combobox.addItem("")
        self.graphItem_combobox.addItem("")
        self.graphItem_combobox.setObjectName(u"graphItem_combobox")
        self.graphItem_combobox.setMinimumSize(QSize(0, 0))
        self.graphItem_combobox.setMaximumSize(QSize(16777215, 16777215))
        self.graphItem_combobox.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"font: 14px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border-color: rgb(22, 25, 30);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"padding-left:5px;")

        self.horizontalLayout_4.addWidget(self.graphItem_combobox)

        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(3, 0))
        self.frame_66.setMaximumSize(QSize(3, 16777215))
        self.frame_66.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:none;")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_66)

        self.timeUnit_Label = QLabel(self.frame_65)
        self.timeUnit_Label.setObjectName(u"timeUnit_Label")
        self.timeUnit_Label.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(202, 206, 216);\n"
"padding-right:5px;")
        self.timeUnit_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.timeUnit_Label)

        self.timeUnit_comboBox = QComboBox(self.frame_65)
        self.timeUnit_comboBox.addItem("")
        self.timeUnit_comboBox.addItem("")
        self.timeUnit_comboBox.addItem("")
        self.timeUnit_comboBox.setObjectName(u"timeUnit_comboBox")
        self.timeUnit_comboBox.setMinimumSize(QSize(0, 0))
        self.timeUnit_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.timeUnit_comboBox.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"font: 14px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border-color: rgb(22, 25, 30);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"padding-left:5px;")

        self.horizontalLayout_4.addWidget(self.timeUnit_comboBox)


        self.gridLayout.addWidget(self.frame_65, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.realtime_grapgLayout = QGridLayout(self.frame_2)
        self.realtime_grapgLayout.setObjectName(u"realtime_grapgLayout")
        self.realtime_grapgLayout.setContentsMargins(-1, -1, 25, -1)

        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gridFrame_1, 2, 0, 1, 1)

        self.frame_31 = QFrame(self.page_2)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(250, 0))
        self.frame_31.setMaximumSize(QSize(250, 16777215))
        self.frame_31.setStyleSheet(u"QFrame{\n"
"background-color: rgb(30, 34, 41);\n"
"border-color:rgb(30, 34, 41);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_31)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.frame_31)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 60))
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setStyleSheet(u"border:none")
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
        self.label_2.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:none;")

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame_18 = QFrame(self.frame_31)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QSize(30, 30))
        self.frame_18.setMaximumSize(QSize(16777215, 50))
        self.frame_18.setStyleSheet(u"border:none")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

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

        self.horizontalLayout.addWidget(self.btn_AutoMode, 0, Qt.AlignBottom)

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

        self.horizontalLayout.addWidget(self.btn_ManaualMode, 0, Qt.AlignBottom)


        self.verticalLayout_8.addWidget(self.gridFrame, 0, Qt.AlignBottom)

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
        self.AutoMode_pattern_comboBox.setMinimumSize(QSize(0, 0))
        self.AutoMode_pattern_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.AutoMode_pattern_comboBox.setBaseSize(QSize(0, 30))
        self.AutoMode_pattern_comboBox.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"font: 14px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;")

        self.verticalLayout_6.addWidget(self.AutoMode_pattern_comboBox, 0, Qt.AlignBottom)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 18px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"border:None")

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignBottom)


        self.gridLayout_16.addWidget(self.frame_6, 0, 0, 1, 1, Qt.AlignBottom)

        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 3))
        self.label_11.setMaximumSize(QSize(16777215, 3))
        self.label_11.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:none;")

        self.gridLayout_16.addWidget(self.label_11, 2, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_8)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 90))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.gasFreeflow_pushButton = QPushButton(self.frame_5)
        self.gasFreeflow_pushButton.setObjectName(u"gasFreeflow_pushButton")
        self.gasFreeflow_pushButton.setMinimumSize(QSize(210, 30))
        self.gasFreeflow_pushButton.setMaximumSize(QSize(210, 30))
        self.gasFreeflow_pushButton.setTabletTracking(False)
        self.gasFreeflow_pushButton.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_5.addWidget(self.gasFreeflow_pushButton, 0, Qt.AlignHCenter)


        self.gridLayout_16.addWidget(self.frame_5, 1, 0, 1, 1, Qt.AlignBottom)

        self.frame_4 = QFrame(self.frame_8)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 10)
        self.autostart_pushButton = QPushButton(self.frame_4)
        self.autostart_pushButton.setObjectName(u"autostart_pushButton")
        self.autostart_pushButton.setMinimumSize(QSize(210, 50))
        self.autostart_pushButton.setMaximumSize(QSize(210, 50))
        self.autostart_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.autostart_pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.autostart_pushButton.setAutoRepeatInterval(100)

        self.verticalLayout_7.addWidget(self.autostart_pushButton)

        self.eMSstop_pushButton = QPushButton(self.frame_4)
        self.eMSstop_pushButton.setObjectName(u"eMSstop_pushButton")
        self.eMSstop_pushButton.setMinimumSize(QSize(210, 90))
        self.eMSstop_pushButton.setMaximumSize(QSize(210, 90))
        self.eMSstop_pushButton.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_7.addWidget(self.eMSstop_pushButton)


        self.gridLayout_16.addWidget(self.frame_4, 3, 0, 1, 1, Qt.AlignBottom)


        self.gridLayout_15.addWidget(self.frame_8, 0, 0, 1, 1, Qt.AlignBottom)

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
        self.gridLayout_19.setContentsMargins(0, 10, 0, 10)
        self.voltageOutput_pushButton = QPushButton(self.frame_9)
        self.voltageOutput_pushButton.setObjectName(u"voltageOutput_pushButton")
        self.voltageOutput_pushButton.setMinimumSize(QSize(210, 50))
        self.voltageOutput_pushButton.setMaximumSize(QSize(210, 50))
        self.voltageOutput_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.voltageOutput_pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.voltageOutput_pushButton.setAutoRepeatInterval(100)

        self.gridLayout_19.addWidget(self.voltageOutput_pushButton, 0, 0, 1, 1, Qt.AlignBottom)

        self.manualMeasurement_pushButton = QPushButton(self.frame_9)
        self.manualMeasurement_pushButton.setObjectName(u"manualMeasurement_pushButton")
        self.manualMeasurement_pushButton.setMinimumSize(QSize(210, 50))
        self.manualMeasurement_pushButton.setMaximumSize(QSize(210, 50))
        self.manualMeasurement_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.manualMeasurement_pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.manualMeasurement_pushButton.setAutoRepeatInterval(100)

        self.gridLayout_19.addWidget(self.manualMeasurement_pushButton, 1, 0, 1, 1, Qt.AlignBottom)

        self.outputStop_pushButton = QPushButton(self.frame_9)
        self.outputStop_pushButton.setObjectName(u"outputStop_pushButton")
        self.outputStop_pushButton.setMinimumSize(QSize(210, 90))
        self.outputStop_pushButton.setMaximumSize(QSize(210, 90))
        self.outputStop_pushButton.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_19.addWidget(self.outputStop_pushButton, 3, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 3))
        self.label_18.setMaximumSize(QSize(16777215, 3))
        self.label_18.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border:none;")

        self.gridLayout_19.addWidget(self.label_18, 2, 0, 1, 1, Qt.AlignBottom)


        self.gridLayout_20.addWidget(self.frame_9, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

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
        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(80, 0))
        self.label_20.setMaximumSize(QSize(80, 16777215))
        self.label_20.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"border:None")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_21 = QLabel(self.frame_12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(80, 0))
        self.label_21.setMaximumSize(QSize(80, 16777215))
        self.label_21.setStyleSheet(u"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"border:None")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_21, 1, 0, 1, 1)

        self.measurement_comboBox = QComboBox(self.frame_12)
        self.measurement_comboBox.addItem("")
        self.measurement_comboBox.addItem("")
        self.measurement_comboBox.setObjectName(u"measurement_comboBox")
        self.measurement_comboBox.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")

        self.gridLayout_21.addWidget(self.measurement_comboBox, 1, 1, 1, 1)

        self.voltage_lineEdit = QLineEdit(self.frame_12)
        self.voltage_lineEdit.setObjectName(u"voltage_lineEdit")
        self.voltage_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.voltage_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px  \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.voltage_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.voltage_lineEdit, 0, 1, 1, 1)


        self.gridLayout_20.addWidget(self.frame_12, 0, 0, 1, 1, Qt.AlignBottom)


        self.gridLayout_2.addWidget(self.frame_11, 0, 0, 1, 1, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.page_ManaulOperate)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_7, 0, Qt.AlignBottom)


        self.gridLayout_4.addWidget(self.frame_31, 1, 1, 2, 1)

        self.pages.addWidget(self.page_2)
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1170, 1410))
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
        self.PatternErrorMessagelabel = QLabel(self.frame_20)
        self.PatternErrorMessagelabel.setObjectName(u"PatternErrorMessagelabel")
        self.PatternErrorMessagelabel.setMinimumSize(QSize(400, 0))
        self.PatternErrorMessagelabel.setMaximumSize(QSize(400, 16777215))
        self.PatternErrorMessagelabel.setStyleSheet(u"font:700 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(221, 0, 0);\n"
"padding-right:10px;")
        self.PatternErrorMessagelabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.PatternErrorMessagelabel, 2, 8, 1, 1, Qt.AlignRight)

        self.label_63 = QLabel(self.frame_20)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(90, 32))
        self.label_63.setMaximumSize(QSize(16777215, 16777215))
        self.label_63.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_6.addWidget(self.label_63, 2, 2, 1, 1)

        self.frame_35 = QFrame(self.frame_20)
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

        self.verticalLayout_10.addWidget(self.frame_43)

        self.scrollArea_3 = QScrollArea(self.frame_35)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setMinimumSize(QSize(0, 200))
        self.scrollArea_3.setSizeIncrement(QSize(0, 0))
        self.scrollArea_3.setStyleSheet(u"\n"
"background-color: rgb(25, 28, 34);\n"
"border:none;")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1112, 200))
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


        self.gridLayout_6.addWidget(self.frame_35, 4, 0, 1, 9)

        self.RT_Label = QLabel(self.frame_20)
        self.RT_Label.setObjectName(u"RT_Label")
        self.RT_Label.setMinimumSize(QSize(90, 0))
        self.RT_Label.setMaximumSize(QSize(90, 16777215))
        self.RT_Label.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.RT_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.RT_Label, 2, 4, 1, 1)

        self.gas_Combobox = QComboBox(self.frame_20)
        self.gas_Combobox.addItem("")
        self.gas_Combobox.addItem("")
        self.gas_Combobox.addItem("")
        self.gas_Combobox.addItem("")
        self.gas_Combobox.setObjectName(u"gas_Combobox")
        self.gas_Combobox.setMinimumSize(QSize(70, 0))
        self.gas_Combobox.setMaximumSize(QSize(70, 16777215))
        self.gas_Combobox.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"font: 14px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border-color: rgb(22, 25, 30);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;")

        self.gridLayout_6.addWidget(self.gas_Combobox, 2, 3, 1, 1)

        self.frame_33 = QFrame(self.frame_20)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(3, 0))
        self.frame_33.setMaximumSize(QSize(3, 16777215))
        self.frame_33.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color:rgb(44, 49, 60);\n"
"border-width: 1px;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_33, 0, 1, 4, 1)

        self.frame_37 = QFrame(self.frame_20)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(200, 0))
        self.frame_37.setMaximumSize(QSize(200, 16777215))
        self.frame_37.setStyleSheet(u"")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_37)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(9, 0, 9, 0)
        self.frame_41 = QFrame(self.frame_37)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(3, 0))
        self.frame_41.setMaximumSize(QSize(3, 16777215))
        self.frame_41.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color: rgb(44, 49, 60);")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.gridLayout_26.addWidget(self.frame_41, 0, 3, 1, 1)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(40, 0))
        self.frame_38.setMaximumSize(QSize(40, 16777215))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_38)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_38)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.verticalLayout_11.addWidget(self.label_3)


        self.gridLayout_26.addWidget(self.frame_38, 0, 4, 1, 1)

        self.frame_40 = QFrame(self.frame_37)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(40, 0))
        self.frame_40.setMaximumSize(QSize(40, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_40)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_40)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.verticalLayout_13.addWidget(self.label_7)


        self.gridLayout_26.addWidget(self.frame_40, 0, 1, 1, 1)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(40, 0))
        self.frame_39.setMaximumSize(QSize(40, 16777215))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_39)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_39)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.verticalLayout_12.addWidget(self.label_6)


        self.gridLayout_26.addWidget(self.frame_39, 0, 2, 1, 1)


        self.gridLayout_6.addWidget(self.frame_37, 0, 8, 2, 1, Qt.AlignRight)

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
        self.label_65.setStyleSheet(u"font: 20px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.verticalLayout.addWidget(self.label_65)

        self.label_29 = QLabel(self.frame_55)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(140, 0))
        self.label_29.setMaximumSize(QSize(140, 16777215))
        self.label_29.setStyleSheet(u"font: 20px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.verticalLayout.addWidget(self.label_29)


        self.gridLayout_6.addWidget(self.frame_55, 0, 0, 4, 1)

        self.label_27 = QLabel(self.frame_20)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(90, 32))
        self.label_27.setMaximumSize(QSize(90, 16777215))
        self.label_27.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_6.addWidget(self.label_27, 0, 2, 1, 1)

        self.label_25 = QLabel(self.frame_20)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(90, 32))
        self.label_25.setMaximumSize(QSize(16777215, 16777215))
        self.label_25.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_6.addWidget(self.label_25, 1, 2, 1, 1)

        self.RT_combobox = QComboBox(self.frame_20)
        self.RT_combobox.addItem("")
        self.RT_combobox.addItem("")
        self.RT_combobox.addItem("")
        self.RT_combobox.setObjectName(u"RT_combobox")
        self.RT_combobox.setMinimumSize(QSize(70, 0))
        self.RT_combobox.setMaximumSize(QSize(70, 16777215))
        self.RT_combobox.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"font: 14px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border-color: rgb(22, 25, 30);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;")

        self.gridLayout_6.addWidget(self.RT_combobox, 2, 5, 1, 1)

        self.commect_lineEdit = QLineEdit(self.frame_20)
        self.commect_lineEdit.setObjectName(u"commect_lineEdit")
        self.commect_lineEdit.setMinimumSize(QSize(400, 32))
        self.commect_lineEdit.setMaximumSize(QSize(212, 16777215))
        self.commect_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:200;")
        self.commect_lineEdit.setCursorPosition(0)

        self.gridLayout_6.addWidget(self.commect_lineEdit, 1, 3, 1, 4)

        self.patternfile_comboBox = QComboBox(self.frame_20)
        self.patternfile_comboBox.addItem("")
        self.patternfile_comboBox.setObjectName(u"patternfile_comboBox")
        self.patternfile_comboBox.setMinimumSize(QSize(400, 0))
        self.patternfile_comboBox.setMaximumSize(QSize(400, 16777215))
        self.patternfile_comboBox.setMouseTracking(False)
        self.patternfile_comboBox.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"font: 14px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border-color: rgb(22, 25, 30);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;")
        self.patternfile_comboBox.setEditable(False)
        self.patternfile_comboBox.setInsertPolicy(QComboBox.InsertAtTop)

        self.gridLayout_6.addWidget(self.patternfile_comboBox, 0, 3, 1, 4)


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
        self.TestPatternErrorMessagelabel = QLabel(self.frame_34)
        self.TestPatternErrorMessagelabel.setObjectName(u"TestPatternErrorMessagelabel")
        self.TestPatternErrorMessagelabel.setMinimumSize(QSize(200, 0))
        self.TestPatternErrorMessagelabel.setMaximumSize(QSize(400, 16777215))
        self.TestPatternErrorMessagelabel.setStyleSheet(u"font:700 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(221, 0, 0);\n"
"padding-right:10px;")
        self.TestPatternErrorMessagelabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_47.addWidget(self.TestPatternErrorMessagelabel, 5, 4, 1, 1, Qt.AlignRight)

        self.frame_68 = QFrame(self.frame_34)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(3, 0))
        self.frame_68.setMaximumSize(QSize(3, 16777215))
        self.frame_68.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color:rgb(44, 49, 60);\n"
"border-width: 1px;")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)

        self.gridLayout_47.addWidget(self.frame_68, 0, 1, 3, 1)

        self.frame_51 = QFrame(self.frame_34)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 0))
        self.frame_51.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 34, 41);\n"
"	border-color: rgb(44, 49, 60);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_51)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setHorizontalSpacing(6)
        self.gridLayout_42.setContentsMargins(6, 6, 6, 6)
        self.label_58 = QLabel(self.frame_51)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(120, 32))
        self.label_58.setMaximumSize(QSize(120, 16777215))
        self.label_58.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"border:none")
        self.label_58.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_58, 0, 1, 1, 1, Qt.AlignRight)

        self.bg0_SpinBox = QSpinBox(self.frame_51)
        self.bg0_SpinBox.setObjectName(u"bg0_SpinBox")
        sizePolicy.setHeightForWidth(self.bg0_SpinBox.sizePolicy().hasHeightForWidth())
        self.bg0_SpinBox.setSizePolicy(sizePolicy)
        self.bg0_SpinBox.setMinimumSize(QSize(80, 32))
        self.bg0_SpinBox.setMaximumSize(QSize(80, 16777215))
        self.bg0_SpinBox.setMouseTracking(False)
        self.bg0_SpinBox.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.bg0_SpinBox.setFrame(True)
        self.bg0_SpinBox.setAlignment(Qt.AlignCenter)
        self.bg0_SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bg0_SpinBox.setMinimum(0)
        self.bg0_SpinBox.setMaximum(200)
        self.bg0_SpinBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.bg0_SpinBox.setValue(2)

        self.gridLayout_42.addWidget(self.bg0_SpinBox, 0, 6, 1, 1)

        self.label_59 = QLabel(self.frame_51)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(0, 32))
        self.label_59.setMaximumSize(QSize(16777215, 16777215))
        self.label_59.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"border:none")
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_59, 1, 1, 1, 1, Qt.AlignRight)

        self.bg_sampletime_SpinBox = QSpinBox(self.frame_51)
        self.bg_sampletime_SpinBox.setObjectName(u"bg_sampletime_SpinBox")
        sizePolicy.setHeightForWidth(self.bg_sampletime_SpinBox.sizePolicy().hasHeightForWidth())
        self.bg_sampletime_SpinBox.setSizePolicy(sizePolicy)
        self.bg_sampletime_SpinBox.setMinimumSize(QSize(80, 32))
        self.bg_sampletime_SpinBox.setMaximumSize(QSize(80, 16777215))
        self.bg_sampletime_SpinBox.setMouseTracking(False)
        self.bg_sampletime_SpinBox.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.bg_sampletime_SpinBox.setFrame(True)
        self.bg_sampletime_SpinBox.setAlignment(Qt.AlignCenter)
        self.bg_sampletime_SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bg_sampletime_SpinBox.setMinimum(1)
        self.bg_sampletime_SpinBox.setMaximum(10)
        self.bg_sampletime_SpinBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.bg_sampletime_SpinBox.setValue(2)

        self.gridLayout_42.addWidget(self.bg_sampletime_SpinBox, 0, 8, 1, 1)

        self.test_sampletime_SpinBox = QSpinBox(self.frame_51)
        self.test_sampletime_SpinBox.setObjectName(u"test_sampletime_SpinBox")
        sizePolicy.setHeightForWidth(self.test_sampletime_SpinBox.sizePolicy().hasHeightForWidth())
        self.test_sampletime_SpinBox.setSizePolicy(sizePolicy)
        self.test_sampletime_SpinBox.setMinimumSize(QSize(80, 32))
        self.test_sampletime_SpinBox.setMaximumSize(QSize(80, 16777215))
        self.test_sampletime_SpinBox.setMouseTracking(False)
        self.test_sampletime_SpinBox.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.test_sampletime_SpinBox.setFrame(True)
        self.test_sampletime_SpinBox.setAlignment(Qt.AlignCenter)
        self.test_sampletime_SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.test_sampletime_SpinBox.setMinimum(1)
        self.test_sampletime_SpinBox.setMaximum(10)
        self.test_sampletime_SpinBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.test_sampletime_SpinBox.setValue(2)

        self.gridLayout_42.addWidget(self.test_sampletime_SpinBox, 1, 2, 1, 1)

        self.test_time_SpinBox = QSpinBox(self.frame_51)
        self.test_time_SpinBox.setObjectName(u"test_time_SpinBox")
        sizePolicy.setHeightForWidth(self.test_time_SpinBox.sizePolicy().hasHeightForWidth())
        self.test_time_SpinBox.setSizePolicy(sizePolicy)
        self.test_time_SpinBox.setMinimumSize(QSize(80, 32))
        self.test_time_SpinBox.setMaximumSize(QSize(80, 16777215))
        self.test_time_SpinBox.setMouseTracking(False)
        self.test_time_SpinBox.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.test_time_SpinBox.setFrame(True)
        self.test_time_SpinBox.setAlignment(Qt.AlignCenter)
        self.test_time_SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.test_time_SpinBox.setMinimum(1)
        self.test_time_SpinBox.setMaximum(200)
        self.test_time_SpinBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.test_time_SpinBox.setValue(2)

        self.gridLayout_42.addWidget(self.test_time_SpinBox, 0, 2, 1, 1)

        self.label_62 = QLabel(self.frame_51)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(130, 32))
        self.label_62.setMaximumSize(QSize(16777215, 16777215))
        self.label_62.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"border:none")
        self.label_62.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_62, 0, 5, 1, 1, Qt.AlignRight)

        self.label_61 = QLabel(self.frame_51)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(130, 32))
        self.label_61.setMaximumSize(QSize(16777215, 16777215))
        self.label_61.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"border:none")
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_61, 1, 5, 1, 1, Qt.AlignRight)

        self.bg_testtime_SpinBox = QSpinBox(self.frame_51)
        self.bg_testtime_SpinBox.setObjectName(u"bg_testtime_SpinBox")
        sizePolicy.setHeightForWidth(self.bg_testtime_SpinBox.sizePolicy().hasHeightForWidth())
        self.bg_testtime_SpinBox.setSizePolicy(sizePolicy)
        self.bg_testtime_SpinBox.setMinimumSize(QSize(80, 32))
        self.bg_testtime_SpinBox.setMaximumSize(QSize(80, 16777215))
        self.bg_testtime_SpinBox.setMouseTracking(False)
        self.bg_testtime_SpinBox.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.bg_testtime_SpinBox.setFrame(True)
        self.bg_testtime_SpinBox.setAlignment(Qt.AlignCenter)
        self.bg_testtime_SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bg_testtime_SpinBox.setMinimum(0)
        self.bg_testtime_SpinBox.setMaximum(200)
        self.bg_testtime_SpinBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.bg_testtime_SpinBox.setValue(2)

        self.gridLayout_42.addWidget(self.bg_testtime_SpinBox, 1, 6, 1, 1)

        self.label_64 = QLabel(self.frame_51)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 32))
        self.label_64.setMaximumSize(QSize(16777215, 16777215))
        self.label_64.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;\n"
"border:none")
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_64, 0, 7, 1, 1, Qt.AlignRight)


        self.gridLayout_47.addWidget(self.frame_51, 5, 0, 1, 4)

        self.label_41 = QLabel(self.frame_34)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(130, 0))
        self.label_41.setMaximumSize(QSize(130, 16777215))
        self.label_41.setStyleSheet(u"font: 20px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_47.addWidget(self.label_41, 0, 0, 3, 1)

        self.label_43 = QLabel(self.frame_34)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(80, 0))
        self.label_43.setMaximumSize(QSize(80, 16777215))
        self.label_43.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_47.addWidget(self.label_43, 0, 2, 1, 1)

        self.test_commect_lineEdit = QLineEdit(self.frame_34)
        self.test_commect_lineEdit.setObjectName(u"test_commect_lineEdit")
        self.test_commect_lineEdit.setMinimumSize(QSize(400, 32))
        self.test_commect_lineEdit.setMaximumSize(QSize(212, 16777215))
        self.test_commect_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;\n"
"max-width:200;")

        self.gridLayout_47.addWidget(self.test_commect_lineEdit, 2, 3, 1, 1)

        self.testfile_comboBox = QComboBox(self.frame_34)
        self.testfile_comboBox.setObjectName(u"testfile_comboBox")
        self.testfile_comboBox.setMinimumSize(QSize(400, 32))
        self.testfile_comboBox.setMaximumSize(QSize(400, 16777215))
        self.testfile_comboBox.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"font: 14px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border-color: rgb(22, 25, 30);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 0px;\n"
"padding-left:5px;")

        self.gridLayout_47.addWidget(self.testfile_comboBox, 0, 3, 1, 1)

        self.frame_44 = QFrame(self.frame_34)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy)
        self.frame_44.setMinimumSize(QSize(0, 0))
        self.frame_44.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 28, 34);\n"
"	border-color:rgb(30, 34, 41);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 10px;\n"
"	font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"}")
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
        self.scrollArea_4.setStyleSheet(u"\n"
"background-color: rgb(25, 28, 34);\n"
"border:none;")
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1112, 200))
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


        self.gridLayout_47.addWidget(self.frame_44, 6, 0, 1, 5)

        self.label_42 = QLabel(self.frame_34)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(80, 0))
        self.label_42.setMaximumSize(QSize(80, 16777215))
        self.label_42.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.gridLayout_47.addWidget(self.label_42, 2, 2, 1, 1)

        self.frame_50 = QFrame(self.frame_34)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(200, 50))
        self.frame_50.setMaximumSize(QSize(200, 16777215))
        self.frame_50.setStyleSheet(u"")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_50)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(9, 0, 9, 0)
        self.frame_56 = QFrame(self.frame_50)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(40, 0))
        self.frame_56.setMaximumSize(QSize(40, 16777215))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_56)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_56)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.verticalLayout_15.addWidget(self.label_46)


        self.gridLayout_39.addWidget(self.frame_56, 0, 1, 1, 1)

        self.frame_54 = QFrame(self.frame_50)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(40, 0))
        self.frame_54.setMaximumSize(QSize(40, 16777215))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_54)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_54)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.verticalLayout_14.addWidget(self.label_15)


        self.gridLayout_39.addWidget(self.frame_54, 0, 3, 1, 1)

        self.frame_52 = QFrame(self.frame_50)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(40, 0))
        self.frame_52.setMaximumSize(QSize(40, 16777215))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_52)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_52)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")

        self.verticalLayout_16.addWidget(self.label_47)


        self.gridLayout_39.addWidget(self.frame_52, 0, 0, 1, 1)

        self.frame_53 = QFrame(self.frame_50)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(3, 0))
        self.frame_53.setMaximumSize(QSize(3, 16777215))
        self.frame_53.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color: rgb(44, 49, 60);")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)

        self.gridLayout_39.addWidget(self.frame_53, 0, 2, 1, 1)


        self.gridLayout_47.addWidget(self.frame_50, 0, 4, 3, 1, Qt.AlignRight)

        self.frame_70 = QFrame(self.frame_34)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(0, 3))
        self.frame_70.setMaximumSize(QSize(16777215, 3))
        self.frame_70.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-color:rgb(44, 49, 60);\n"
"border-width: 1px;")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)

        self.gridLayout_47.addWidget(self.frame_70, 3, 0, 1, 5)


        self.verticalLayout_3.addWidget(self.frame_34)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.page_3_layout.addWidget(self.scrollArea_2)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setEnabled(True)
        self.page_4.setStyleSheet(u"")
        self.gridLayout_24 = QGridLayout(self.page_4)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.frame_36 = QFrame(self.page_4)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_36)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(6)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
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
        self.label_yesr_3.setMouseTracking(False)
        self.label_yesr_3.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_3.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"")
        self.label_yesr_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_3.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_3, 0, 4, 1, 1)

        self.label_yesr_2 = QLabel(self.frame_57)
        self.label_yesr_2.setObjectName(u"label_yesr_2")
        self.label_yesr_2.setMinimumSize(QSize(150, 35))
        self.label_yesr_2.setMaximumSize(QSize(150, 35))
        self.label_yesr_2.setMouseTracking(False)
        self.label_yesr_2.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_2.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_2.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_2, 0, 2, 1, 1)

        self.label_yesr_24 = QLabel(self.frame_57)
        self.label_yesr_24.setObjectName(u"label_yesr_24")
        self.label_yesr_24.setMinimumSize(QSize(150, 35))
        self.label_yesr_24.setMaximumSize(QSize(150, 35))
        self.label_yesr_24.setMouseTracking(False)
        self.label_yesr_24.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_24.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_24.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_24, 1, 0, 1, 1)

        self.label_yesr_4 = QLabel(self.frame_57)
        self.label_yesr_4.setObjectName(u"label_yesr_4")
        self.label_yesr_4.setMinimumSize(QSize(150, 35))
        self.label_yesr_4.setMaximumSize(QSize(150, 35))
        self.label_yesr_4.setMouseTracking(False)
        self.label_yesr_4.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_4.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_4.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_4, 1, 2, 1, 1)

        self.label_yesr_26 = QLabel(self.frame_57)
        self.label_yesr_26.setObjectName(u"label_yesr_26")
        self.label_yesr_26.setMinimumSize(QSize(150, 35))
        self.label_yesr_26.setMaximumSize(QSize(150, 35))
        self.label_yesr_26.setMouseTracking(False)
        self.label_yesr_26.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_26.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;")
        self.label_yesr_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_26.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_26, 1, 8, 1, 1)

        self.label_yesr_6 = QLabel(self.frame_57)
        self.label_yesr_6.setObjectName(u"label_yesr_6")
        self.label_yesr_6.setMinimumSize(QSize(150, 35))
        self.label_yesr_6.setMaximumSize(QSize(150, 35))
        self.label_yesr_6.setMouseTracking(False)
        self.label_yesr_6.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_6.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;")
        self.label_yesr_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_6.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_6, 1, 4, 1, 1)

        self.label_yesr_15 = QLabel(self.frame_57)
        self.label_yesr_15.setObjectName(u"label_yesr_15")
        self.label_yesr_15.setMinimumSize(QSize(150, 35))
        self.label_yesr_15.setMaximumSize(QSize(150, 35))
        self.label_yesr_15.setMouseTracking(False)
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
        self.label_yesr_12.setMouseTracking(False)
        self.label_yesr_12.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_12.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;")
        self.label_yesr_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_12.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_12, 0, 1, 1, 1)

        self.label_yesr_14 = QLabel(self.frame_57)
        self.label_yesr_14.setObjectName(u"label_yesr_14")
        self.label_yesr_14.setMinimumSize(QSize(150, 35))
        self.label_yesr_14.setMaximumSize(QSize(150, 35))
        self.label_yesr_14.setMouseTracking(False)
        self.label_yesr_14.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_14.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_14.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_14, 1, 7, 1, 1)

        self.label_yesr_13 = QLabel(self.frame_57)
        self.label_yesr_13.setObjectName(u"label_yesr_13")
        self.label_yesr_13.setMinimumSize(QSize(150, 35))
        self.label_yesr_13.setMaximumSize(QSize(150, 35))
        self.label_yesr_13.setMouseTracking(False)
        self.label_yesr_13.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_13.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_13.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_13, 0, 7, 1, 1)

        self.label_yesr_25 = QLabel(self.frame_57)
        self.label_yesr_25.setObjectName(u"label_yesr_25")
        self.label_yesr_25.setMinimumSize(QSize(150, 35))
        self.label_yesr_25.setMaximumSize(QSize(150, 35))
        self.label_yesr_25.setMouseTracking(False)
        self.label_yesr_25.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_25.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;")
        self.label_yesr_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_25.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_25, 1, 1, 1, 1)

        self.label_yesr_10 = QLabel(self.frame_57)
        self.label_yesr_10.setObjectName(u"label_yesr_10")
        self.label_yesr_10.setMinimumSize(QSize(150, 35))
        self.label_yesr_10.setMaximumSize(QSize(150, 35))
        self.label_yesr_10.setMouseTracking(False)
        self.label_yesr_10.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_10.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_10.setMargin(0)

        self.gridLayout_46.addWidget(self.label_yesr_10, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.frame_57, 2, 1, 1, 1, Qt.AlignLeft)

        self.label_yesr_7 = QLabel(self.frame_36)
        self.label_yesr_7.setObjectName(u"label_yesr_7")
        self.label_yesr_7.setMinimumSize(QSize(0, 20))
        self.label_yesr_7.setMaximumSize(QSize(16777215, 20))
        self.label_yesr_7.setMouseTracking(False)
        self.label_yesr_7.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_7.setStyleSheet(u"background-color: rgb(65, 72, 88);\n"
"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:10px;\n"
"border-radius: 5px;")
        self.label_yesr_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_7.setMargin(0)

        self.gridLayout_22.addWidget(self.label_yesr_7, 1, 1, 1, 9)

        self.label_yesr_8 = QLabel(self.frame_36)
        self.label_yesr_8.setObjectName(u"label_yesr_8")
        self.label_yesr_8.setMinimumSize(QSize(0, 20))
        self.label_yesr_8.setMaximumSize(QSize(16777215, 20))
        self.label_yesr_8.setMouseTracking(False)
        self.label_yesr_8.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_8.setStyleSheet(u"background-color: rgb(65, 72, 88);\n"
"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:10px;\n"
"border-radius: 5px;")
        self.label_yesr_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_8.setMargin(0)

        self.gridLayout_22.addWidget(self.label_yesr_8, 3, 1, 1, 9)

        self.frame_58 = QFrame(self.frame_36)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_58)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.label_yesr_16 = QLabel(self.frame_58)
        self.label_yesr_16.setObjectName(u"label_yesr_16")
        self.label_yesr_16.setMinimumSize(QSize(150, 35))
        self.label_yesr_16.setMaximumSize(QSize(150, 35))
        self.label_yesr_16.setMouseTracking(False)
        self.label_yesr_16.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_16.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;")
        self.label_yesr_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_16.setMargin(0)

        self.gridLayout_48.addWidget(self.label_yesr_16, 0, 1, 1, 1)

        self.label_yesr_17 = QLabel(self.frame_58)
        self.label_yesr_17.setObjectName(u"label_yesr_17")
        self.label_yesr_17.setMinimumSize(QSize(150, 35))
        self.label_yesr_17.setMaximumSize(QSize(150, 35))
        self.label_yesr_17.setMouseTracking(False)
        self.label_yesr_17.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_17.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_17.setMargin(0)

        self.gridLayout_48.addWidget(self.label_yesr_17, 0, 2, 1, 1)

        self.label_yesr_27 = QLabel(self.frame_58)
        self.label_yesr_27.setObjectName(u"label_yesr_27")
        self.label_yesr_27.setMinimumSize(QSize(150, 35))
        self.label_yesr_27.setMaximumSize(QSize(150, 35))
        self.label_yesr_27.setMouseTracking(False)
        self.label_yesr_27.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_27.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_27.setMargin(0)

        self.gridLayout_48.addWidget(self.label_yesr_27, 1, 0, 1, 1)

        self.label_yesr_11 = QLabel(self.frame_58)
        self.label_yesr_11.setObjectName(u"label_yesr_11")
        self.label_yesr_11.setMinimumSize(QSize(150, 35))
        self.label_yesr_11.setMaximumSize(QSize(150, 35))
        self.label_yesr_11.setMouseTracking(False)
        self.label_yesr_11.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_11.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_11.setMargin(0)

        self.gridLayout_48.addWidget(self.label_yesr_11, 0, 0, 1, 1)

        self.label_yesr_28 = QLabel(self.frame_58)
        self.label_yesr_28.setObjectName(u"label_yesr_28")
        self.label_yesr_28.setMinimumSize(QSize(150, 35))
        self.label_yesr_28.setMaximumSize(QSize(150, 35))
        self.label_yesr_28.setMouseTracking(False)
        self.label_yesr_28.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_28.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;")
        self.label_yesr_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_28.setMargin(0)

        self.gridLayout_48.addWidget(self.label_yesr_28, 1, 1, 1, 1)

        self.spinBox = QSpinBox(self.frame_58)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(60, 32))
        self.spinBox.setMaximumSize(QSize(60, 16777215))
        self.spinBox.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox.setMaximum(30)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(26)

        self.gridLayout_48.addWidget(self.spinBox, 0, 3, 1, 1)


        self.gridLayout_22.addWidget(self.frame_58, 4, 1, 1, 1, Qt.AlignLeft)

        self.frame_59 = QFrame(self.frame_36)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_59)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.label_yesr_30 = QLabel(self.frame_59)
        self.label_yesr_30.setObjectName(u"label_yesr_30")
        self.label_yesr_30.setMinimumSize(QSize(150, 35))
        self.label_yesr_30.setMaximumSize(QSize(150, 35))
        self.label_yesr_30.setMouseTracking(False)
        self.label_yesr_30.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_30.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;")
        self.label_yesr_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_30.setMargin(0)

        self.gridLayout_49.addWidget(self.label_yesr_30, 1, 1, 1, 1)

        self.label_yesr_29 = QLabel(self.frame_59)
        self.label_yesr_29.setObjectName(u"label_yesr_29")
        self.label_yesr_29.setMinimumSize(QSize(150, 35))
        self.label_yesr_29.setMaximumSize(QSize(150, 35))
        self.label_yesr_29.setMouseTracking(False)
        self.label_yesr_29.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_29.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_29.setMargin(0)

        self.gridLayout_49.addWidget(self.label_yesr_29, 1, 0, 1, 1)

        self.label_yesr_22 = QLabel(self.frame_59)
        self.label_yesr_22.setObjectName(u"label_yesr_22")
        self.label_yesr_22.setMinimumSize(QSize(150, 35))
        self.label_yesr_22.setMaximumSize(QSize(150, 35))
        self.label_yesr_22.setMouseTracking(False)
        self.label_yesr_22.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_22.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_22.setMargin(0)

        self.gridLayout_49.addWidget(self.label_yesr_22, 0, 0, 1, 1)

        self.label_yesr_19 = QLabel(self.frame_59)
        self.label_yesr_19.setObjectName(u"label_yesr_19")
        self.label_yesr_19.setMinimumSize(QSize(150, 35))
        self.label_yesr_19.setMaximumSize(QSize(150, 35))
        self.label_yesr_19.setMouseTracking(False)
        self.label_yesr_19.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_19.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;")
        self.label_yesr_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_19.setMargin(0)

        self.gridLayout_49.addWidget(self.label_yesr_19, 0, 1, 1, 1)

        self.label_yesr_20 = QLabel(self.frame_59)
        self.label_yesr_20.setObjectName(u"label_yesr_20")
        self.label_yesr_20.setMinimumSize(QSize(150, 35))
        self.label_yesr_20.setMaximumSize(QSize(150, 35))
        self.label_yesr_20.setMouseTracking(False)
        self.label_yesr_20.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_20.setStyleSheet(u"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-right:5px;")
        self.label_yesr_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_yesr_20.setMargin(0)

        self.gridLayout_49.addWidget(self.label_yesr_20, 0, 2, 1, 1)

        self.spinBox_2 = QSpinBox(self.frame_59)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(60, 32))
        self.spinBox_2.setMaximumSize(QSize(60, 16777215))
        self.spinBox_2.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"min-height:30;")
        self.spinBox_2.setAlignment(Qt.AlignCenter)
        self.spinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_2.setMaximum(30)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_2.setValue(26)

        self.gridLayout_49.addWidget(self.spinBox_2, 0, 3, 1, 1)


        self.gridLayout_22.addWidget(self.frame_59, 6, 1, 1, 1, Qt.AlignLeft)

        self.label_yesr_9 = QLabel(self.frame_36)
        self.label_yesr_9.setObjectName(u"label_yesr_9")
        self.label_yesr_9.setMinimumSize(QSize(0, 20))
        self.label_yesr_9.setMaximumSize(QSize(16777215, 20))
        self.label_yesr_9.setMouseTracking(False)
        self.label_yesr_9.setLayoutDirection(Qt.LeftToRight)
        self.label_yesr_9.setStyleSheet(u"background-color: rgb(65, 72, 88);\n"
"font: 12px bold italic large \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:10px;\n"
"border-radius: 5px;")
        self.label_yesr_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_yesr_9.setMargin(0)

        self.gridLayout_22.addWidget(self.label_yesr_9, 5, 1, 1, 9)


        self.gridLayout_24.addWidget(self.frame_36, 0, 0, 1, 1, Qt.AlignTop)

        self.pages.addWidget(self.page_4)

        self.gridLayout_8.addWidget(self.pages, 0, 1, 1, 1)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.AutoMode_pattern_comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_year.setText(QCoreApplication.translate("MainPages", u"\u5e74\u5ea6", None))
        self.lineEdit_year.setText(QCoreApplication.translate("MainPages", u"2021", None))
        self.QC_Test_RadioButton.setText(QCoreApplication.translate("MainPages", u"\u8a55\u4fa1\u8a66\u9a13", None))
        self.Costom_Test_RadioButton.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u6e2c\u5b9a", None))
        self.label_60.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u6e2c\u5b9a\u756a\u53f7", None))
        self.lineEdit_testNumber.setText(QCoreApplication.translate("MainPages", u"MS-4371", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u5143", None))
        self.lineEdit_costomer.setText(QCoreApplication.translate("MainPages", u"\u682a\u5f0f\u4f1a\u793e\u30e2\u30c8\u30e4\u30de", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"\u4f9d\u983c\u8005", None))
        self.lineEdit_costomerName.setText(QCoreApplication.translate("MainPages", u"\u9ec4", None))
        self.label_32.setText(QCoreApplication.translate("MainPages", u"\u8a66\u6599\u4f53\u7a4d(mm\u00b3)", None))
        self.lineEdit_testMeterialName.setText(QCoreApplication.translate("MainPages", u"material_1", None))
        self.lineEdit_meterialArea.setText(QCoreApplication.translate("MainPages", u"\u8a66\u6599\u306e\u539a\u3055(mm)", None))
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
        self.lineEdit_meterialVolume.setText(QCoreApplication.translate("MainPages", u"\u8a66\u6599\u306e\u539a\u3055(mm)", None))
        self.label_13.setText("")
        self.lineEdit_PID_1_D.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.lineEdit_PID_1_I.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.label_109.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 1", None))
        self.label_110.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_111.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_112.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_1_P.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.lineEdit_PID_2_D.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.lineEdit_PID_2_I.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.label_113.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 2", None))
        self.label_114.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_115.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_116.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_2_P.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.lineEdit_PID_3_D.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.lineEdit_PID_3_I.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.label_117.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 3", None))
        self.label_118.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_119.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_120.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_3_P.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.lineEdit_PID_4_D.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.lineEdit_PID_4_I.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.label_105.setText(QCoreApplication.translate("MainPages", u"PID\u8a2d\u5b9a 4", None))
        self.label_106.setText(QCoreApplication.translate("MainPages", u"I", None))
        self.label_107.setText(QCoreApplication.translate("MainPages", u"P", None))
        self.label_108.setText(QCoreApplication.translate("MainPages", u"D", None))
        self.lineEdit_PID_4_P.setText(QCoreApplication.translate("MainPages", u"1.5", None))
        self.label_37.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u4e2d", None))
        self.label_38.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u7d42\u4e86", None))
        self.label_30.setText(QCoreApplication.translate("MainPages", u"\u6e29\u5ea6\u30ad\u30fc\u30d7\u4e2d", None))
        self.label_45.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u53ef", None))
        self.label_28.setText(QCoreApplication.translate("MainPages", u"\u6607\u6e29\u4e2d", None))
        self.label_39.setText(QCoreApplication.translate("MainPages", u"\u8b66\u5831", None))
        self.label_17.setText(QCoreApplication.translate("MainPages", u"\u505c\u6b62\u4e2d", None))
        self.label_40.setText(QCoreApplication.translate("MainPages", u"\u771f\u7a7a\u7f6e\u63db\u4e2d", None))
        self.realtime_Voltage_lineEdit.setText(QCoreApplication.translate("MainPages", u"450V", None))
        self.label_31.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u96fb\u5727", None))
        self.label_34.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u62b5\u6297", None))
        self.realtime_Resistor_lineEdit.setText(QCoreApplication.translate("MainPages", u"10\u03a9", None))
        self.label_35.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u96fb\u6d41", None))
        self.realtime_Current_lineEdit.setText(QCoreApplication.translate("MainPages", u"100uA", None))
        self.label_23.setText(QCoreApplication.translate("MainPages", u"\u7089\u5185\u6e29\u5ea6", None))
        self.realtime_Temp_lineEdit.setText(QCoreApplication.translate("MainPages", u"12.200 \u2103", None))
        self.label_44.setText(QCoreApplication.translate("MainPages", u"\u8868\u793a\u9805\u76ee", None))
        self.graphItem_combobox.setItemText(0, QCoreApplication.translate("MainPages", u"\u62b5\u6297\u5024", None))
        self.graphItem_combobox.setItemText(1, QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u30d1\u30bf\u30fc\u30f3", None))

        self.timeUnit_Label.setText(QCoreApplication.translate("MainPages", u"\u6642\u9593\u5358\u4f4d", None))
        self.timeUnit_comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"1s/div", None))
        self.timeUnit_comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"1min/div", None))
        self.timeUnit_comboBox.setItemText(2, QCoreApplication.translate("MainPages", u"1h/div", None))

        self.label_2.setText("")
        self.btn_AutoMode.setText(QCoreApplication.translate("MainPages", u"\u81ea\u52d5\u30e2\u30fc\u30c9", None))
        self.btn_ManaualMode.setText(QCoreApplication.translate("MainPages", u"\u624b\u52d5\u30e2\u30fc\u30c9", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u30d1\u30bf\u30fc\u30f3\u540d", None))
        self.AutoMode_pattern_comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"pattern1", None))
        self.AutoMode_pattern_comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"pattern2", None))

        self.label.setText(QCoreApplication.translate("MainPages", u"\u96f0\u56f2\u6c17\u30e2\u30fc\u30c9\uff1a\u5927\u6c17", None))
        self.label_11.setText("")
        self.gasFreeflow_pushButton.setText(QCoreApplication.translate("MainPages", u"\u5927\u6c17\u5727", None))
        self.autostart_pushButton.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u958b\u59cb", None))
        self.eMSstop_pushButton.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u505c\u6b62", None))
        self.voltageOutput_pushButton.setText(QCoreApplication.translate("MainPages", u"\u96fb\u5727\u5370\u52a0", None))
        self.manualMeasurement_pushButton.setText(QCoreApplication.translate("MainPages", u"\u30de\u30cb\u30e5\u30a2\u30eb\u6e2c\u5b9a", None))
        self.outputStop_pushButton.setText(QCoreApplication.translate("MainPages", u"\u51fa\u529b\u505c\u6b62", None))
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u96fb\u5727(V)", None))
        self.label_21.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u30e2\u30fc\u30c9", None))
        self.measurement_comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"\u9023\u7d9a\u4e8c\u56de\u6e2c\u5b9a", None))
        self.measurement_comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"\u4e00\u56de\u6e2c\u5b9a", None))

        self.voltage_lineEdit.setText(QCoreApplication.translate("MainPages", u"2000", None))
        self.PatternErrorMessagelabel.setText(QCoreApplication.translate("MainPages", u"\u7121\u52b9\u5165\u529b:", None))
        self.label_63.setText(QCoreApplication.translate("MainPages", u"\u96f0\u56f2\u6c17", None))
        self.RT_Label.setText(QCoreApplication.translate("MainPages", u"RT\u6e2c\u5b9a", None))
        self.gas_Combobox.setItemText(0, "")
        self.gas_Combobox.setItemText(1, QCoreApplication.translate("MainPages", u"\u5927\u6c17", None))
        self.gas_Combobox.setItemText(2, QCoreApplication.translate("MainPages", u"\u771f\u7a7a", None))
        self.gas_Combobox.setItemText(3, QCoreApplication.translate("MainPages", u"N2\u7f6e\u63db", None))

        self.label_3.setText(QCoreApplication.translate("MainPages", u"\u524a\u9664", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"\u4fdd\u5b58", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"\u8ffd\u52a0", None))
        self.label_65.setText(QCoreApplication.translate("MainPages", u"\u6607\u964d\u6e29", None))
        self.label_29.setText(QCoreApplication.translate("MainPages", u"\u904b\u8ee2\u30d1\u30bf\u30fc\u30f3", None))
        self.label_27.setText(QCoreApplication.translate("MainPages", u"\u30d1\u30bf\u30fc\u30f3\u540d", None))
        self.label_25.setText(QCoreApplication.translate("MainPages", u"\u8a3b\u8a18", None))
        self.RT_combobox.setItemText(0, "")
        self.RT_combobox.setItemText(1, QCoreApplication.translate("MainPages", u"\u6709\u308a", None))
        self.RT_combobox.setItemText(2, QCoreApplication.translate("MainPages", u"\u306a\u3044", None))

        self.commect_lineEdit.setInputMask("")
        self.commect_lineEdit.setText("")
        self.patternfile_comboBox.setItemText(0, "")

        self.TestPatternErrorMessagelabel.setText(QCoreApplication.translate("MainPages", u"\u7121\u52b9\u5165\u529b:", None))
        self.label_58.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u6642\u9593(min)", None))
        self.label_59.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u30b5\u30f3\u30d7\u30ea\u30f3\u30b0\u5468\u671f(s)", None))
        self.label_62.setText(QCoreApplication.translate("MainPages", u"BG0 \u6e2c\u5b9a\u6642\u9593(min)", None))
        self.label_61.setText(QCoreApplication.translate("MainPages", u"BG \u6e2c\u5b9a\u6642\u9593(min)", None))
        self.label_64.setText(QCoreApplication.translate("MainPages", u"BG \u6e2c\u5b9a\u30b5\u30f3\u30d7\u30ea\u30f3\u30b0\u5468\u671f(s)", None))
        self.label_41.setText(QCoreApplication.translate("MainPages", u"\u6e2c\u5b9a\u30d1\u30bf\u30fc\u30f3", None))
        self.label_43.setText(QCoreApplication.translate("MainPages", u"\u30d1\u30bf\u30fc\u30f3\u540d", None))
        self.test_commect_lineEdit.setInputMask("")
        self.label_42.setText(QCoreApplication.translate("MainPages", u"\u8a3b\u8a18", None))
        self.label_46.setText(QCoreApplication.translate("MainPages", u"\u8ffd\u52a0", None))
        self.label_15.setText(QCoreApplication.translate("MainPages", u"\u524a\u9664", None))
        self.label_47.setText(QCoreApplication.translate("MainPages", u"\u4fdd\u5b58", None))
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
        self.label_yesr_7.setText(QCoreApplication.translate("MainPages", u"Ethernet \u30a4\u30f3\u30bf\u30fc\u30d5\u30a7\u30fc\u30b9 : Modbus TCP \u30b5\u30fc\u30d0\u30fc", None))
        self.label_yesr_8.setText(QCoreApplication.translate("MainPages", u"GPIB \u30a4\u30f3\u30bf\u30fc\u30d5\u30a7\u30fc\u30b9 : 2657A  \u30cf\u30a4\u30d1\u30ef\u30fc\u30b7\u30b9\u30c6\u30e0\u30bd\u30fc\u30b9\u30e1\u30fc\u30c0", None))
        self.label_yesr_16.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u4e2d", None))
        self.label_yesr_17.setText(QCoreApplication.translate("MainPages", u"\u30a2\u30c9\u30ec\u30b9: ", None))
        self.label_yesr_27.setText(QCoreApplication.translate("MainPages", u"\u671f\u9593:", None))
        self.label_yesr_11.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u72b6\u614b:", None))
        self.label_yesr_28.setText(QCoreApplication.translate("MainPages", u"15:41:10", None))
        self.label_yesr_30.setText(QCoreApplication.translate("MainPages", u"15:41:10", None))
        self.label_yesr_29.setText(QCoreApplication.translate("MainPages", u"\u671f\u9593:", None))
        self.label_yesr_22.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u72b6\u614b:", None))
        self.label_yesr_19.setText(QCoreApplication.translate("MainPages", u"\u63a5\u7d9a\u4e2d", None))
        self.label_yesr_20.setText(QCoreApplication.translate("MainPages", u"\u30a2\u30c9\u30ec\u30b9: ", None))
        self.label_yesr_9.setText(QCoreApplication.translate("MainPages", u"GPIB \u30a4\u30f3\u30bf\u30fc\u30d5\u30a7\u30fc\u30b9 : 2635B  \u30b7\u30b9\u30c6\u30e0\u30fb\u30bd\u30fc\u30b9\u30e1\u30fc\u30bf", None))
    # retranslateUi

