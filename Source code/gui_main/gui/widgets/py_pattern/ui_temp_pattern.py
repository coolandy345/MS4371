# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'temp_patternqvaCvQ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


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
"border-radius: 10px;\n"
"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.gridLayout_3 = QGridLayout(temp_pattern)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page = QStackedWidget(temp_pattern)
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"border-color: rgb(44, 49, 60);\n"
"background-color: rgb(44, 49, 60);\n"
"border-width: 5px;    \n"
"border-style: solid;   \n"
" border-radius: 10px;")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setEnabled(True)
        self.page1.setStyleSheet(u"\n"
"border:none;")
        self.gridLayout = QGridLayout(self.page1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
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
        self.page2.setStyleSheet(u"\n"
"border:none;")
        self.gridLayout_4 = QGridLayout(self.page2)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.PID_muffle_comboBox = QComboBox(self.page2)
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.addItem("")
        self.PID_muffle_comboBox.setObjectName(u"PID_muffle_comboBox")
        sizePolicy.setHeightForWidth(self.PID_muffle_comboBox.sizePolicy().hasHeightForWidth())
        self.PID_muffle_comboBox.setSizePolicy(sizePolicy)
        self.PID_muffle_comboBox.setMinimumSize(QSize(0, 20))
        self.PID_muffle_comboBox.setMaximumSize(QSize(16777215, 20))
        self.PID_muffle_comboBox.setStyleSheet(u"font:12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")
        self.PID_muffle_comboBox.setMaxVisibleItems(5)

        self.gridLayout_4.addWidget(self.PID_muffle_comboBox, 9, 1, 1, 1)

        self.Sp_limit_up_lineEdit = QSpinBox(self.page2)
        self.Sp_limit_up_lineEdit.setObjectName(u"Sp_limit_up_lineEdit")
        sizePolicy.setHeightForWidth(self.Sp_limit_up_lineEdit.sizePolicy().hasHeightForWidth())
        self.Sp_limit_up_lineEdit.setSizePolicy(sizePolicy)
        self.Sp_limit_up_lineEdit.setMinimumSize(QSize(0, 20))
        self.Sp_limit_up_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.Sp_limit_up_lineEdit.setMouseTracking(False)
        self.Sp_limit_up_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.Sp_limit_up_lineEdit.setFrame(True)
        self.Sp_limit_up_lineEdit.setAlignment(Qt.AlignCenter)
        self.Sp_limit_up_lineEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Sp_limit_up_lineEdit.setMaximum(999)
        self.Sp_limit_up_lineEdit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.Sp_limit_up_lineEdit.setValue(23)

        self.gridLayout_4.addWidget(self.Sp_limit_up_lineEdit, 12, 1, 1, 1)

        self.Shift_label = QLabel(self.page2)
        self.Shift_label.setObjectName(u"Shift_label")
        self.Shift_label.setMinimumSize(QSize(0, 15))
        self.Shift_label.setMaximumSize(QSize(16777215, 15))
        self.Shift_label.setStyleSheet(u"\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.Shift_label, 14, 0, 1, 1)

        self.PID_heater_label = QLabel(self.page2)
        self.PID_heater_label.setObjectName(u"PID_heater_label")
        self.PID_heater_label.setMinimumSize(QSize(0, 15))
        self.PID_heater_label.setMaximumSize(QSize(16777215, 15))
        self.PID_heater_label.setStyleSheet(u"\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.PID_heater_label, 10, 0, 1, 1)

        self.KeepTime_label = QLabel(self.page2)
        self.KeepTime_label.setObjectName(u"KeepTime_label")
        self.KeepTime_label.setMinimumSize(QSize(0, 15))
        self.KeepTime_label.setMaximumSize(QSize(16777215, 15))
        self.KeepTime_label.setStyleSheet(u"\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.KeepTime_label, 11, 0, 1, 1)

        self.N2_label = QLabel(self.page2)
        self.N2_label.setObjectName(u"N2_label")
        self.N2_label.setMinimumSize(QSize(0, 15))
        self.N2_label.setMaximumSize(QSize(16777215, 15))
        self.N2_label.setStyleSheet(u"\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.N2_label, 6, 0, 1, 1)

        self.TestPattern_comboBox = QComboBox(self.page2)
        self.TestPattern_comboBox.addItem("")
        self.TestPattern_comboBox.setObjectName(u"TestPattern_comboBox")
        sizePolicy.setHeightForWidth(self.TestPattern_comboBox.sizePolicy().hasHeightForWidth())
        self.TestPattern_comboBox.setSizePolicy(sizePolicy)
        self.TestPattern_comboBox.setMinimumSize(QSize(0, 20))
        self.TestPattern_comboBox.setMaximumSize(QSize(16777215, 20))
        self.TestPattern_comboBox.setStyleSheet(u"font:12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")
        self.TestPattern_comboBox.setMaxVisibleItems(5)

        self.gridLayout_4.addWidget(self.TestPattern_comboBox, 21, 0, 1, 3)

        self.time_frame = QFrame(self.page2)
        self.time_frame.setObjectName(u"time_frame")
        self.time_frame.setMinimumSize(QSize(0, 20))
        self.time_frame.setMaximumSize(QSize(16777215, 20))
        self.time_frame.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 0, 0);\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"")
        self.time_frame.setFrameShape(QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.time_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.Hour_lineEdit = QSpinBox(self.time_frame)
        self.Hour_lineEdit.setObjectName(u"Hour_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Hour_lineEdit.sizePolicy().hasHeightForWidth())
        self.Hour_lineEdit.setSizePolicy(sizePolicy1)
        self.Hour_lineEdit.setMinimumSize(QSize(18, 0))
        self.Hour_lineEdit.setMaximumSize(QSize(18, 16777215))
        self.Hour_lineEdit.setMouseTracking(False)
        self.Hour_lineEdit.setStyleSheet(u"border:none;\n"
"background-color: rgb(30, 34, 41);")
        self.Hour_lineEdit.setFrame(True)
        self.Hour_lineEdit.setAlignment(Qt.AlignCenter)
        self.Hour_lineEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Hour_lineEdit.setMaximum(99)
        self.Hour_lineEdit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.Hour_lineEdit.setValue(23)

        self.horizontalLayout.addWidget(self.Hour_lineEdit)

        self.label_4 = QLabel(self.time_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(3, 16777215))
        self.label_4.setStyleSheet(u"border:none;\n"
"background-color: rgb(30, 34, 41);")

        self.horizontalLayout.addWidget(self.label_4)

        self.Min_lineEdit = QSpinBox(self.time_frame)
        self.Min_lineEdit.setObjectName(u"Min_lineEdit")
        sizePolicy1.setHeightForWidth(self.Min_lineEdit.sizePolicy().hasHeightForWidth())
        self.Min_lineEdit.setSizePolicy(sizePolicy1)
        self.Min_lineEdit.setMinimumSize(QSize(18, 0))
        self.Min_lineEdit.setMaximumSize(QSize(18, 16777215))
        self.Min_lineEdit.setMouseTracking(False)
        self.Min_lineEdit.setStyleSheet(u"border:none;\n"
"background-color: rgb(30, 34, 41);")
        self.Min_lineEdit.setFrame(True)
        self.Min_lineEdit.setAlignment(Qt.AlignCenter)
        self.Min_lineEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Min_lineEdit.setMaximum(59)
        self.Min_lineEdit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.Min_lineEdit.setValue(23)

        self.horizontalLayout.addWidget(self.Min_lineEdit)


        self.gridLayout_4.addWidget(self.time_frame, 2, 1, 1, 1)

        self.Time_label = QLabel(self.page2)
        self.Time_label.setObjectName(u"Time_label")
        self.Time_label.setMinimumSize(QSize(0, 15))
        self.Time_label.setMaximumSize(QSize(16777215, 15))
        self.Time_label.setStyleSheet(u"\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.Time_label, 2, 0, 1, 1)

        self.frame_5 = QFrame(self.page2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 2))
        self.frame_5.setMaximumSize(QSize(16777215, 2))
        self.frame_5.setStyleSheet(u"background-color: rgb(141, 145, 156);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_5, 7, 0, 1, 2)

        self.KeepTime_lineEdit = QSpinBox(self.page2)
        self.KeepTime_lineEdit.setObjectName(u"KeepTime_lineEdit")
        sizePolicy.setHeightForWidth(self.KeepTime_lineEdit.sizePolicy().hasHeightForWidth())
        self.KeepTime_lineEdit.setSizePolicy(sizePolicy)
        self.KeepTime_lineEdit.setMinimumSize(QSize(0, 20))
        self.KeepTime_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.KeepTime_lineEdit.setMouseTracking(False)
        self.KeepTime_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.KeepTime_lineEdit.setFrame(True)
        self.KeepTime_lineEdit.setAlignment(Qt.AlignCenter)
        self.KeepTime_lineEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.KeepTime_lineEdit.setMaximum(999)
        self.KeepTime_lineEdit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.KeepTime_lineEdit.setValue(23)

        self.gridLayout_4.addWidget(self.KeepTime_lineEdit, 11, 1, 1, 1)

        self.Sp_limit_down_lineEdit = QSpinBox(self.page2)
        self.Sp_limit_down_lineEdit.setObjectName(u"Sp_limit_down_lineEdit")
        sizePolicy.setHeightForWidth(self.Sp_limit_down_lineEdit.sizePolicy().hasHeightForWidth())
        self.Sp_limit_down_lineEdit.setSizePolicy(sizePolicy)
        self.Sp_limit_down_lineEdit.setMinimumSize(QSize(0, 20))
        self.Sp_limit_down_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.Sp_limit_down_lineEdit.setMouseTracking(False)
        self.Sp_limit_down_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.Sp_limit_down_lineEdit.setFrame(True)
        self.Sp_limit_down_lineEdit.setAlignment(Qt.AlignCenter)
        self.Sp_limit_down_lineEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Sp_limit_down_lineEdit.setMaximum(999)
        self.Sp_limit_down_lineEdit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.Sp_limit_down_lineEdit.setValue(23)

        self.gridLayout_4.addWidget(self.Sp_limit_down_lineEdit, 13, 1, 1, 1)

        self.PID_muffle_label = QLabel(self.page2)
        self.PID_muffle_label.setObjectName(u"PID_muffle_label")
        self.PID_muffle_label.setMinimumSize(QSize(0, 15))
        self.PID_muffle_label.setMaximumSize(QSize(16777215, 15))
        self.PID_muffle_label.setStyleSheet(u"\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.PID_muffle_label, 9, 0, 1, 1)

        self.Sp_limit_down_label = QLabel(self.page2)
        self.Sp_limit_down_label.setObjectName(u"Sp_limit_down_label")
        self.Sp_limit_down_label.setMinimumSize(QSize(0, 15))
        self.Sp_limit_down_label.setMaximumSize(QSize(16777215, 15))
        self.Sp_limit_down_label.setStyleSheet(u"\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.Sp_limit_down_label, 13, 0, 1, 1)

        self.SV_label = QLabel(self.page2)
        self.SV_label.setObjectName(u"SV_label")
        self.SV_label.setMinimumSize(QSize(0, 15))
        self.SV_label.setMaximumSize(QSize(16777215, 15))
        self.SV_label.setStyleSheet(u"\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.SV_label, 5, 0, 1, 1)

        self.frame_4 = QFrame(self.page2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 2))
        self.frame_4.setMaximumSize(QSize(16777215, 2))
        self.frame_4.setStyleSheet(u"background-color: rgb(141, 145, 156);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_4, 15, 0, 1, 2)

        self.Shift_lineEdit = QSpinBox(self.page2)
        self.Shift_lineEdit.setObjectName(u"Shift_lineEdit")
        sizePolicy.setHeightForWidth(self.Shift_lineEdit.sizePolicy().hasHeightForWidth())
        self.Shift_lineEdit.setSizePolicy(sizePolicy)
        self.Shift_lineEdit.setMinimumSize(QSize(0, 20))
        self.Shift_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.Shift_lineEdit.setMouseTracking(False)
        self.Shift_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.Shift_lineEdit.setFrame(True)
        self.Shift_lineEdit.setAlignment(Qt.AlignCenter)
        self.Shift_lineEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Shift_lineEdit.setMaximum(999)
        self.Shift_lineEdit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.Shift_lineEdit.setValue(23)

        self.gridLayout_4.addWidget(self.Shift_lineEdit, 14, 1, 1, 1)

        self.Sp_limit_up_label = QLabel(self.page2)
        self.Sp_limit_up_label.setObjectName(u"Sp_limit_up_label")
        self.Sp_limit_up_label.setMinimumSize(QSize(0, 15))
        self.Sp_limit_up_label.setMaximumSize(QSize(16777215, 15))
        self.Sp_limit_up_label.setStyleSheet(u"\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.Sp_limit_up_label, 12, 0, 1, 1)

        self.TestPattern_label = QLabel(self.page2)
        self.TestPattern_label.setObjectName(u"TestPattern_label")
        self.TestPattern_label.setMinimumSize(QSize(0, 15))
        self.TestPattern_label.setMaximumSize(QSize(16777215, 15))
        self.TestPattern_label.setStyleSheet(u"\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.TestPattern_label, 19, 0, 1, 2)

        self.PID_heater_comboBox = QComboBox(self.page2)
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.addItem("")
        self.PID_heater_comboBox.setObjectName(u"PID_heater_comboBox")
        sizePolicy.setHeightForWidth(self.PID_heater_comboBox.sizePolicy().hasHeightForWidth())
        self.PID_heater_comboBox.setSizePolicy(sizePolicy)
        self.PID_heater_comboBox.setMinimumSize(QSize(0, 20))
        self.PID_heater_comboBox.setMaximumSize(QSize(16777215, 20))
        self.PID_heater_comboBox.setStyleSheet(u"font:12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")
        self.PID_heater_comboBox.setMaxVisibleItems(5)

        self.gridLayout_4.addWidget(self.PID_heater_comboBox, 10, 1, 1, 1)

        self.Type_comboBox = QComboBox(self.page2)
        self.Type_comboBox.addItem("")
        self.Type_comboBox.addItem("")
        self.Type_comboBox.addItem("")
        self.Type_comboBox.setObjectName(u"Type_comboBox")
        sizePolicy.setHeightForWidth(self.Type_comboBox.sizePolicy().hasHeightForWidth())
        self.Type_comboBox.setSizePolicy(sizePolicy)
        self.Type_comboBox.setMinimumSize(QSize(0, 20))
        self.Type_comboBox.setMaximumSize(QSize(16777215, 20))
        self.Type_comboBox.setStyleSheet(u"font:12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")

        self.gridLayout_4.addWidget(self.Type_comboBox, 1, 0, 1, 2)

        self.frame_2 = QFrame(self.page2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Step_label = QLabel(self.frame_2)
        self.Step_label.setObjectName(u"Step_label")
        self.Step_label.setMinimumSize(QSize(130, 20))
        self.Step_label.setMaximumSize(QSize(16777215, 16777215))
        self.Step_label.setStyleSheet(u"font:17px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(0, 0, 0);\n"
"padding-left:5px;\n"
"border-radius: 5px;\n"
"background-color: rgb(73, 73, 220);\n"
"border:none;")

        self.horizontalLayout_2.addWidget(self.Step_label)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"border:none;\n"
"border-radius: 2px;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 2)

        self.SV_lineEdit = QSpinBox(self.page2)
        self.SV_lineEdit.setObjectName(u"SV_lineEdit")
        sizePolicy.setHeightForWidth(self.SV_lineEdit.sizePolicy().hasHeightForWidth())
        self.SV_lineEdit.setSizePolicy(sizePolicy)
        self.SV_lineEdit.setMinimumSize(QSize(0, 20))
        self.SV_lineEdit.setMaximumSize(QSize(16777215, 20))
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
        self.SV_lineEdit.setMaximum(999)
        self.SV_lineEdit.setStepType(QAbstractSpinBox.DefaultStepType)
        self.SV_lineEdit.setValue(23)

        self.gridLayout_4.addWidget(self.SV_lineEdit, 5, 1, 1, 1)

        self.N2_lineEdit = QLineEdit(self.page2)
        self.N2_lineEdit.setObjectName(u"N2_lineEdit")
        self.N2_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.N2_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.N2_lineEdit, 6, 1, 1, 1)

        self.page.addWidget(self.page2)

        self.gridLayout_3.addWidget(self.page, 0, 0, 1, 1)


        self.retranslateUi(temp_pattern)

        self.page.setCurrentIndex(1)
        self.PID_muffle_comboBox.setCurrentIndex(0)
        self.TestPattern_comboBox.setCurrentIndex(0)
        self.PID_heater_comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(temp_pattern)
    # setupUi

    def retranslateUi(self, temp_pattern):
        temp_pattern.setWindowTitle(QCoreApplication.translate("temp_pattern", u"Form", None))
        self.PID_muffle_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"No.0", None))
        self.PID_muffle_comboBox.setItemText(1, QCoreApplication.translate("temp_pattern", u"No.1", None))
        self.PID_muffle_comboBox.setItemText(2, QCoreApplication.translate("temp_pattern", u"No.2", None))
        self.PID_muffle_comboBox.setItemText(3, QCoreApplication.translate("temp_pattern", u"No.3", None))
        self.PID_muffle_comboBox.setItemText(4, QCoreApplication.translate("temp_pattern", u"No.4", None))

        self.Shift_label.setText(QCoreApplication.translate("temp_pattern", u"\u30b7\u30d5\u30c8", None))
        self.PID_heater_label.setText(QCoreApplication.translate("temp_pattern", u"PID(\u30d2\u30fc\u30bf\u30fc)", None))
        self.KeepTime_label.setText(QCoreApplication.translate("temp_pattern", u"\u30ad\u30fc\u30d7\u6642\u9593(s)", None))
        self.N2_label.setText(QCoreApplication.translate("temp_pattern", u"N2 (SLM)", None))
        self.TestPattern_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"\u65b0\u3057\u3044\u30a2\u30a4\u30c6\u30e0", None))

        self.label_4.setText(QCoreApplication.translate("temp_pattern", u":", None))
        self.Time_label.setText(QCoreApplication.translate("temp_pattern", u"\u6642\uff1a\u5206", None))
        self.PID_muffle_label.setText(QCoreApplication.translate("temp_pattern", u"PID(\u30de\u30c3\u30d5\u30eb)", None))
        self.Sp_limit_down_label.setText(QCoreApplication.translate("temp_pattern", u"\u30b9\u30ec\u30fc\u30d6SP\u4e0b\u9650", None))
        self.SV_label.setText(QCoreApplication.translate("temp_pattern", u"\u4e3b\u7089(\u2103)", None))
        self.Sp_limit_up_label.setText(QCoreApplication.translate("temp_pattern", u"\u30b9\u30ec\u30fc\u30d6SP\u4e0a\u9650", None))
        self.TestPattern_label.setText(QCoreApplication.translate("temp_pattern", u"\u6e2c\u5b9a\u30d1\u30bf\u30fc\u30f3", None))
        self.PID_heater_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"No.0", None))
        self.PID_heater_comboBox.setItemText(1, QCoreApplication.translate("temp_pattern", u"No.1", None))
        self.PID_heater_comboBox.setItemText(2, QCoreApplication.translate("temp_pattern", u"No.2", None))
        self.PID_heater_comboBox.setItemText(3, QCoreApplication.translate("temp_pattern", u"No.3", None))
        self.PID_heater_comboBox.setItemText(4, QCoreApplication.translate("temp_pattern", u"No.4", None))

        self.Type_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"\u6607\u964d\u6e29", None))
        self.Type_comboBox.setItemText(1, QCoreApplication.translate("temp_pattern", u"\u6e2c\u5b9a", None))
        self.Type_comboBox.setItemText(2, QCoreApplication.translate("temp_pattern", u"END", None))

        self.Step_label.setText(QCoreApplication.translate("temp_pattern", u"STEP 1", None))
        self.N2_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"0", None))
    # retranslateUi

