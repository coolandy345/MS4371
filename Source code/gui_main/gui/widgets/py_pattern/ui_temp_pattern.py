# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'temp_patternPgbSsQ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_temp_pattern(object):
    def setupUi(self, temp_pattern):
        if not temp_pattern.objectName():
            temp_pattern.setObjectName(u"temp_pattern")
        temp_pattern.resize(200, 380)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(temp_pattern.sizePolicy().hasHeightForWidth())
        temp_pattern.setSizePolicy(sizePolicy)
        temp_pattern.setMinimumSize(QSize(200, 380))
        temp_pattern.setMaximumSize(QSize(200, 380))
        temp_pattern.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"color: rgb(225, 230, 241);\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"font:12px;\n"
"")
        self.gridLayout_3 = QGridLayout(temp_pattern)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page = QStackedWidget(temp_pattern)
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setEnabled(True)
        self.page1.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.page1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page1)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
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
"	font:12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	color: rgb(225, 230, 241);\n"
"}\n"
"QLabel:disabled {\n"
"	color: rgb(91, 94, 98);\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	font:12px;\n"
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
"}\n"
"\n"
"QComboBox:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	color: rgb(225, 230, 241);\n"
"	border-wi"
                        "dth: 1px;\n"
"}\n"
"QComboBox:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(44, 49, 60);\n"
"	border: none;\n"
"}\n"
"QComboBox:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.page2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 25))
        self.frame_2.setMaximumSize(QSize(16777215, 25))
        self.frame_2.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Step_label = QLabel(self.frame_2)
        self.Step_label.setObjectName(u"Step_label")
        self.Step_label.setMinimumSize(QSize(130, 0))
        self.Step_label.setStyleSheet(u"QLabel:enabled {\n"
"	font:14px;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left:5px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(200, 133, 0);\n"
"	border:none;\n"
"}\n"
"QLabel:disabled {\n"
"	font:17px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left:5px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0, 168, 123);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_2.addWidget(self.Step_label)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.Type_comboBox = QComboBox(self.frame_6)
        self.Type_comboBox.addItem("")
        self.Type_comboBox.addItem("")
        self.Type_comboBox.addItem("")
        self.Type_comboBox.setObjectName(u"Type_comboBox")
        sizePolicy.setHeightForWidth(self.Type_comboBox.sizePolicy().hasHeightForWidth())
        self.Type_comboBox.setSizePolicy(sizePolicy)
        self.Type_comboBox.setMinimumSize(QSize(0, 22))
        self.Type_comboBox.setMaximumSize(QSize(16777215, 22))
        self.Type_comboBox.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}\n"
"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.Type_comboBox)

        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 22))
        self.frame_4.setMaximumSize(QSize(16777215, 22))
        self.frame_4.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Time_label = QLabel(self.frame_4)
        self.Time_label.setObjectName(u"Time_label")
        self.Time_label.setMinimumSize(QSize(0, 0))
        self.Time_label.setMaximumSize(QSize(16777215, 16777215))
        self.Time_label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_3.addWidget(self.Time_label)

        self.time_frame = QFrame(self.frame_4)
        self.time_frame.setObjectName(u"time_frame")
        self.time_frame.setMinimumSize(QSize(80, 0))
        self.time_frame.setMaximumSize(QSize(100, 16777215))
        self.time_frame.setStyleSheet(u"QFrame:enabled {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(0, 0, 0,40);\n"
"	\n"
"	border-width: 1px;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}\n"
"\n"
"QLineEdit:enabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(225, 230, 241);\n"
"	border: none;\n"
"}\n"
"QLineEdit:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(44, 49, 60);\n"
"	border: none;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QLineEdit:read-only {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel:enabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}\n"
"QLabel:disabled {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(44, 49, 60);\n"
"	border: none;\n"
"}\n"
"QLabel:hover {\n"
""
                        "	background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"}")
        self.time_frame.setFrameShape(QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.time_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.Hour_lineEdit = QLineEdit(self.time_frame)
        self.Hour_lineEdit.setObjectName(u"Hour_lineEdit")
        self.Hour_lineEdit.setStyleSheet(u"border:none;\n"
"")
        self.Hour_lineEdit.setAlignment(Qt.AlignCenter)
        self.Hour_lineEdit.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.Hour_lineEdit)

        self.label_4 = QLabel(self.time_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(3, 16777215))
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.Min_lineEdit = QLineEdit(self.time_frame)
        self.Min_lineEdit.setObjectName(u"Min_lineEdit")
        self.Min_lineEdit.setStyleSheet(u"border:none;\n"
"")
        self.Min_lineEdit.setAlignment(Qt.AlignCenter)
        self.Min_lineEdit.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.Min_lineEdit)


        self.horizontalLayout_3.addWidget(self.time_frame)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 22))
        self.frame_8.setMaximumSize(QSize(16777215, 22))
        self.frame_8.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.SV_label = QLabel(self.frame_8)
        self.SV_label.setObjectName(u"SV_label")
        self.SV_label.setMinimumSize(QSize(0, 0))
        self.SV_label.setMaximumSize(QSize(16777215, 16777215))
        self.SV_label.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.SV_label)

        self.SV_lineEdit = QLineEdit(self.frame_8)
        self.SV_lineEdit.setObjectName(u"SV_lineEdit")
        self.SV_lineEdit.setMinimumSize(QSize(75, 0))
        self.SV_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.SV_lineEdit.setStyleSheet(u"")
        self.SV_lineEdit.setAlignment(Qt.AlignCenter)
        self.SV_lineEdit.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.SV_lineEdit)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 22))
        self.frame_5.setMaximumSize(QSize(16777215, 22))
        self.frame_5.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.N2_label = QLabel(self.frame_5)
        self.N2_label.setObjectName(u"N2_label")
        self.N2_label.setMinimumSize(QSize(0, 0))
        self.N2_label.setMaximumSize(QSize(16777215, 16777215))
        self.N2_label.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.N2_label)

        self.N2_lineEdit = QLineEdit(self.frame_5)
        self.N2_lineEdit.setObjectName(u"N2_lineEdit")
        self.N2_lineEdit.setMinimumSize(QSize(75, 0))
        self.N2_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.N2_lineEdit.setStyleSheet(u"")
        self.N2_lineEdit.setAlignment(Qt.AlignCenter)
        self.N2_lineEdit.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.N2_lineEdit)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 22))
        self.frame_7.setMaximumSize(QSize(16777215, 22))
        self.frame_7.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.PID_muffle_label = QLabel(self.frame_7)
        self.PID_muffle_label.setObjectName(u"PID_muffle_label")
        self.PID_muffle_label.setMinimumSize(QSize(0, 0))
        self.PID_muffle_label.setMaximumSize(QSize(16777215, 16777215))
        self.PID_muffle_label.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.PID_muffle_label)

        self.PID_muffle_comboBox = QComboBox(self.frame_7)
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.setObjectName(u"PID_muffle_comboBox")
        sizePolicy.setHeightForWidth(self.PID_muffle_comboBox.sizePolicy().hasHeightForWidth())
        self.PID_muffle_comboBox.setSizePolicy(sizePolicy)
        self.PID_muffle_comboBox.setMinimumSize(QSize(75, 0))
        self.PID_muffle_comboBox.setMaximumSize(QSize(75, 16777215))
        self.PID_muffle_comboBox.setStyleSheet(u"")
        self.PID_muffle_comboBox.setMaxVisibleItems(10)

        self.horizontalLayout_7.addWidget(self.PID_muffle_comboBox)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 22))
        self.frame_12.setMaximumSize(QSize(16777215, 22))
        self.frame_12.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.PID_heater_label = QLabel(self.frame_12)
        self.PID_heater_label.setObjectName(u"PID_heater_label")
        self.PID_heater_label.setMinimumSize(QSize(0, 0))
        self.PID_heater_label.setMaximumSize(QSize(16777215, 16777215))
        self.PID_heater_label.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.PID_heater_label)

        self.PID_heater_comboBox = QComboBox(self.frame_12)
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.setObjectName(u"PID_heater_comboBox")
        sizePolicy.setHeightForWidth(self.PID_heater_comboBox.sizePolicy().hasHeightForWidth())
        self.PID_heater_comboBox.setSizePolicy(sizePolicy)
        self.PID_heater_comboBox.setMinimumSize(QSize(75, 0))
        self.PID_heater_comboBox.setMaximumSize(QSize(75, 16777215))
        self.PID_heater_comboBox.setStyleSheet(u"")
        self.PID_heater_comboBox.setMaxVisibleItems(10)

        self.horizontalLayout_8.addWidget(self.PID_heater_comboBox)


        self.verticalLayout.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 22))
        self.frame_9.setMaximumSize(QSize(16777215, 22))
        self.frame_9.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.KeepTime_label = QLabel(self.frame_9)
        self.KeepTime_label.setObjectName(u"KeepTime_label")
        self.KeepTime_label.setMinimumSize(QSize(0, 0))
        self.KeepTime_label.setMaximumSize(QSize(16777215, 16777215))
        self.KeepTime_label.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.KeepTime_label)

        self.KeepTime_lineEdit = QLineEdit(self.frame_9)
        self.KeepTime_lineEdit.setObjectName(u"KeepTime_lineEdit")
        self.KeepTime_lineEdit.setMinimumSize(QSize(75, 20))
        self.KeepTime_lineEdit.setMaximumSize(QSize(75, 20))
        self.KeepTime_lineEdit.setStyleSheet(u"")
        self.KeepTime_lineEdit.setAlignment(Qt.AlignCenter)
        self.KeepTime_lineEdit.setReadOnly(False)

        self.horizontalLayout_9.addWidget(self.KeepTime_lineEdit)


        self.verticalLayout.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 22))
        self.frame_10.setMaximumSize(QSize(16777215, 22))
        self.frame_10.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Sp_limit_up_label = QLabel(self.frame_10)
        self.Sp_limit_up_label.setObjectName(u"Sp_limit_up_label")
        self.Sp_limit_up_label.setMinimumSize(QSize(0, 0))
        self.Sp_limit_up_label.setMaximumSize(QSize(16777215, 16777215))
        self.Sp_limit_up_label.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.Sp_limit_up_label)

        self.Sp_limit_up_lineEdit = QLineEdit(self.frame_10)
        self.Sp_limit_up_lineEdit.setObjectName(u"Sp_limit_up_lineEdit")
        self.Sp_limit_up_lineEdit.setMinimumSize(QSize(75, 0))
        self.Sp_limit_up_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.Sp_limit_up_lineEdit.setStyleSheet(u"")
        self.Sp_limit_up_lineEdit.setAlignment(Qt.AlignCenter)
        self.Sp_limit_up_lineEdit.setReadOnly(False)

        self.horizontalLayout_10.addWidget(self.Sp_limit_up_lineEdit)


        self.verticalLayout.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 22))
        self.frame_11.setMaximumSize(QSize(16777215, 22))
        self.frame_11.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Sp_limit_down_label = QLabel(self.frame_11)
        self.Sp_limit_down_label.setObjectName(u"Sp_limit_down_label")
        self.Sp_limit_down_label.setMinimumSize(QSize(0, 0))
        self.Sp_limit_down_label.setMaximumSize(QSize(16777215, 16777215))
        self.Sp_limit_down_label.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.Sp_limit_down_label)

        self.Sp_limit_down_lineEdit = QLineEdit(self.frame_11)
        self.Sp_limit_down_lineEdit.setObjectName(u"Sp_limit_down_lineEdit")
        self.Sp_limit_down_lineEdit.setMinimumSize(QSize(75, 0))
        self.Sp_limit_down_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.Sp_limit_down_lineEdit.setStyleSheet(u"")
        self.Sp_limit_down_lineEdit.setAlignment(Qt.AlignCenter)
        self.Sp_limit_down_lineEdit.setReadOnly(False)

        self.horizontalLayout_11.addWidget(self.Sp_limit_down_lineEdit)


        self.verticalLayout.addWidget(self.frame_11)

        self.frame_17 = QFrame(self.frame_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 22))
        self.frame_17.setMaximumSize(QSize(16777215, 22))
        self.frame_17.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Shift_label = QLabel(self.frame_17)
        self.Shift_label.setObjectName(u"Shift_label")
        self.Shift_label.setMinimumSize(QSize(0, 0))
        self.Shift_label.setMaximumSize(QSize(16777215, 16777215))
        self.Shift_label.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.Shift_label)

        self.Shift_lineEdit = QLineEdit(self.frame_17)
        self.Shift_lineEdit.setObjectName(u"Shift_lineEdit")
        self.Shift_lineEdit.setMinimumSize(QSize(75, 0))
        self.Shift_lineEdit.setMaximumSize(QSize(75, 16777215))
        self.Shift_lineEdit.setStyleSheet(u"")
        self.Shift_lineEdit.setAlignment(Qt.AlignCenter)
        self.Shift_lineEdit.setReadOnly(False)

        self.horizontalLayout_12.addWidget(self.Shift_lineEdit)


        self.verticalLayout.addWidget(self.frame_17)

        self.frame_75 = QFrame(self.frame_6)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 22))
        self.frame_75.setMaximumSize(QSize(16777215, 22))
        self.frame_75.setStyleSheet(u"QFrame:hover{\n"
"	border:none;\n"
"}\n"
"QFrame:focus{\n"
"	border:none;\n"
"}")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.TestPattern_label = QLabel(self.frame_75)
        self.TestPattern_label.setObjectName(u"TestPattern_label")
        self.TestPattern_label.setMinimumSize(QSize(0, 15))
        self.TestPattern_label.setMaximumSize(QSize(16777215, 15))
        self.TestPattern_label.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.TestPattern_label)

        self.TestPattern_comboBox = QComboBox(self.frame_75)
        self.TestPattern_comboBox.addItem("")
        self.TestPattern_comboBox.setObjectName(u"TestPattern_comboBox")
        sizePolicy.setHeightForWidth(self.TestPattern_comboBox.sizePolicy().hasHeightForWidth())
        self.TestPattern_comboBox.setSizePolicy(sizePolicy)
        self.TestPattern_comboBox.setMinimumSize(QSize(110, 0))
        self.TestPattern_comboBox.setMaximumSize(QSize(110, 16777215))
        self.TestPattern_comboBox.setStyleSheet(u"")
        self.TestPattern_comboBox.setMaxVisibleItems(5)

        self.horizontalLayout_16.addWidget(self.TestPattern_comboBox)


        self.verticalLayout.addWidget(self.frame_75)

        self.frame_75.raise_()
        self.frame_2.raise_()
        self.Type_comboBox.raise_()
        self.frame_4.raise_()
        self.frame_8.raise_()
        self.frame_5.raise_()
        self.frame_7.raise_()
        self.frame_12.raise_()
        self.frame_10.raise_()
        self.frame_11.raise_()
        self.frame_17.raise_()
        self.frame_9.raise_()

        self.gridLayout_4.addWidget(self.frame_6, 4, 0, 1, 1)

        self.page.addWidget(self.page2)

        self.gridLayout_3.addWidget(self.page, 0, 0, 1, 1)


        self.retranslateUi(temp_pattern)

        self.page.setCurrentIndex(1)
        self.PID_muffle_comboBox.setCurrentIndex(0)
        self.PID_heater_comboBox.setCurrentIndex(0)
        self.TestPattern_comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(temp_pattern)
    # setupUi

    def retranslateUi(self, temp_pattern):
        temp_pattern.setWindowTitle(QCoreApplication.translate("temp_pattern", u"Form", None))
        self.Step_label.setText(QCoreApplication.translate("temp_pattern", u"STEP 1", None))
        self.Type_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"\u6607\u964d\u6e29", None))
        self.Type_comboBox.setItemText(1, QCoreApplication.translate("temp_pattern", u"\u6e2c\u5b9a", None))
        self.Type_comboBox.setItemText(2, QCoreApplication.translate("temp_pattern", u"END", None))

        self.Time_label.setText(QCoreApplication.translate("temp_pattern", u"\u6642\uff1a\u5206", None))
        self.Hour_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"0", None))
        self.label_4.setText(QCoreApplication.translate("temp_pattern", u":", None))
        self.Min_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"0", None))
        self.SV_label.setText(QCoreApplication.translate("temp_pattern", u"\u4e3b\u7089(\u2103)", None))
        self.SV_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"0", None))
        self.N2_label.setText(QCoreApplication.translate("temp_pattern", u"N2 (SLM)", None))
        self.N2_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"0", None))
        self.PID_muffle_label.setText(QCoreApplication.translate("temp_pattern", u"PID(\u30de\u30c3\u30d5\u30eb)", None))
        self.PID_muffle_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 0", None))
        self.PID_muffle_comboBox.setItemText(1, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 1", None))
        self.PID_muffle_comboBox.setItemText(2, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 2", None))
        self.PID_muffle_comboBox.setItemText(3, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 3", None))
        self.PID_muffle_comboBox.setItemText(4, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 4", None))
        self.PID_muffle_comboBox.setItemText(5, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 5", None))
        self.PID_muffle_comboBox.setItemText(6, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 6", None))
        self.PID_muffle_comboBox.setItemText(7, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 7", None))
        self.PID_muffle_comboBox.setItemText(8, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 8", None))
        self.PID_muffle_comboBox.setItemText(9, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 9", None))

        self.PID_heater_label.setText(QCoreApplication.translate("temp_pattern", u"PID(\u30d2\u30fc\u30bf\u30fc)", None))
        self.PID_heater_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 0", None))
        self.PID_heater_comboBox.setItemText(1, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 1", None))
        self.PID_heater_comboBox.setItemText(2, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 2", None))
        self.PID_heater_comboBox.setItemText(3, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 3", None))
        self.PID_heater_comboBox.setItemText(4, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 4", None))
        self.PID_heater_comboBox.setItemText(5, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 5", None))
        self.PID_heater_comboBox.setItemText(6, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 6", None))
        self.PID_heater_comboBox.setItemText(7, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 7", None))
        self.PID_heater_comboBox.setItemText(8, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 8", None))
        self.PID_heater_comboBox.setItemText(9, QCoreApplication.translate("temp_pattern", u"PID\u8a2d\u5b9a 9", None))

        self.KeepTime_label.setText(QCoreApplication.translate("temp_pattern", u"\u30ad\u30fc\u30d7\u6642\u9593(s)", None))
        self.KeepTime_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"0", None))
        self.Sp_limit_up_label.setText(QCoreApplication.translate("temp_pattern", u"\u30b9\u30ec\u30fc\u30d6SP\u4e0a\u9650", None))
        self.Sp_limit_up_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"0", None))
        self.Sp_limit_down_label.setText(QCoreApplication.translate("temp_pattern", u"\u30b9\u30ec\u30fc\u30d6SP\u4e0b\u9650", None))
        self.Sp_limit_down_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"0", None))
        self.Shift_label.setText(QCoreApplication.translate("temp_pattern", u"\u30b7\u30d5\u30c8", None))
        self.Shift_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"0", None))
        self.TestPattern_label.setText(QCoreApplication.translate("temp_pattern", u"\u6e2c\u5b9a\u30d1\u30bf\u30fc\u30f3", None))
        self.TestPattern_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"\u65b0\u3057\u3044\u30a2\u30a4\u30c6\u30e0", None))

    # retranslateUi

