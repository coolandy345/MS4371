# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'temp_patternApNJjY.ui'
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
        temp_pattern.resize(200, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(temp_pattern.sizePolicy().hasHeightForWidth())
        temp_pattern.setSizePolicy(sizePolicy)
        temp_pattern.setMinimumSize(QSize(200, 300))
        temp_pattern.setMaximumSize(QSize(195, 318))
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
        self.PID_label = QLabel(self.page2)
        self.PID_label.setObjectName(u"PID_label")
        self.PID_label.setMinimumSize(QSize(90, 0))
        self.PID_label.setMaximumSize(QSize(90, 16777215))
        self.PID_label.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.PID_label, 8, 0, 1, 1)

        self.Time_label = QLabel(self.page2)
        self.Time_label.setObjectName(u"Time_label")
        self.Time_label.setMinimumSize(QSize(80, 0))
        self.Time_label.setMaximumSize(QSize(80, 16777215))
        self.Time_label.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.Time_label, 3, 0, 1, 1)

        self.KeepTime_lineEdit = QLineEdit(self.page2)
        self.KeepTime_lineEdit.setObjectName(u"KeepTime_lineEdit")
        self.KeepTime_lineEdit.setMinimumSize(QSize(80, 20))
        self.KeepTime_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.KeepTime_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"\n"
"")
        self.KeepTime_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.KeepTime_lineEdit, 11, 1, 1, 2)

        self.PID_comboBox = QComboBox(self.page2)
        self.PID_comboBox.addItem("")
        self.PID_comboBox.addItem("")
        self.PID_comboBox.addItem("")
        self.PID_comboBox.addItem("")
        self.PID_comboBox.setObjectName(u"PID_comboBox")
        self.PID_comboBox.setMinimumSize(QSize(80, 20))
        self.PID_comboBox.setMaximumSize(QSize(16777215, 20))
        self.PID_comboBox.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")
        self.PID_comboBox.setMaxVisibleItems(5)

        self.gridLayout_4.addWidget(self.PID_comboBox, 8, 1, 1, 2)

        self.N2_lineEdit = QLineEdit(self.page2)
        self.N2_lineEdit.setObjectName(u"N2_lineEdit")
        self.N2_lineEdit.setMinimumSize(QSize(80, 20))
        self.N2_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.N2_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";")
        self.N2_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.N2_lineEdit, 7, 1, 1, 2)

        self.Temp_lineEdit = QLineEdit(self.page2)
        self.Temp_lineEdit.setObjectName(u"Temp_lineEdit")
        self.Temp_lineEdit.setMinimumSize(QSize(80, 20))
        self.Temp_lineEdit.setMaximumSize(QSize(16777215, 20))
        self.Temp_lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,80);\n"
"color: rgb(225, 230, 241);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"font: 12px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"")
        self.Temp_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.Temp_lineEdit, 6, 1, 1, 2)

        self.TestPattern_comboBox = QComboBox(self.page2)
        self.TestPattern_comboBox.setObjectName(u"TestPattern_comboBox")
        self.TestPattern_comboBox.setMinimumSize(QSize(80, 20))
        self.TestPattern_comboBox.setMaximumSize(QSize(16777215, 20))
        self.TestPattern_comboBox.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")
        self.TestPattern_comboBox.setMaxVisibleItems(5)

        self.gridLayout_4.addWidget(self.TestPattern_comboBox, 16, 0, 1, 3)

        self.TestPattern_label = QLabel(self.page2)
        self.TestPattern_label.setObjectName(u"TestPattern_label")
        self.TestPattern_label.setMinimumSize(QSize(80, 0))
        self.TestPattern_label.setMaximumSize(QSize(80, 16777215))
        self.TestPattern_label.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.TestPattern_label, 14, 0, 1, 1)

        self.frame_2 = QFrame(self.page2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 3))
        self.frame_2.setMaximumSize(QSize(16777215, 3))
        self.frame_2.setStyleSheet(u"background-color: rgb(65, 72, 88);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_2, 4, 0, 1, 3)

        self.time_frame = QFrame(self.page2)
        self.time_frame.setObjectName(u"time_frame")
        self.time_frame.setMinimumSize(QSize(80, 20))
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
        self.Hour_lineEdit = QLineEdit(self.time_frame)
        self.Hour_lineEdit.setObjectName(u"Hour_lineEdit")
        self.Hour_lineEdit.setMaximumSize(QSize(18, 18))
        self.Hour_lineEdit.setStyleSheet(u"border:none;\n"
"background-color: rgb(30, 34, 41);")
        self.Hour_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Hour_lineEdit)

        self.label_4 = QLabel(self.time_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(3, 18))
        self.label_4.setStyleSheet(u"border:none;\n"
"background-color: rgb(30, 34, 41);")

        self.horizontalLayout.addWidget(self.label_4)

        self.Min_lineEdit = QLineEdit(self.time_frame)
        self.Min_lineEdit.setObjectName(u"Min_lineEdit")
        self.Min_lineEdit.setMaximumSize(QSize(18, 18))
        self.Min_lineEdit.setStyleSheet(u"border:none;\n"
"background-color: rgb(30, 34, 41);")
        self.Min_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Min_lineEdit)


        self.gridLayout_4.addWidget(self.time_frame, 3, 1, 1, 2)

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

        self.gridLayout_4.addWidget(self.Type_comboBox, 2, 0, 1, 3)

        self.Temp_label = QLabel(self.page2)
        self.Temp_label.setObjectName(u"Temp_label")
        self.Temp_label.setMinimumSize(QSize(80, 0))
        self.Temp_label.setMaximumSize(QSize(80, 16777215))
        self.Temp_label.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.Temp_label, 6, 0, 1, 1)

        self.label_8 = QLabel(self.page2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 5))
        self.label_8.setMaximumSize(QSize(16777215, 5))
        self.label_8.setStyleSheet(u"font:11px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 3)

        self.Step_label = QLabel(self.page2)
        self.Step_label.setObjectName(u"Step_label")
        self.Step_label.setMinimumSize(QSize(0, 25))
        self.Step_label.setMaximumSize(QSize(16777215, 30))
        self.Step_label.setStyleSheet(u"font:17px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(0, 0, 0);\n"
"padding-left:5px;\n"
"\n"
"background-color: rgb(73, 73, 220);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.Step_label, 0, 0, 1, 2)

        self.frame_5 = QFrame(self.page2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 3))
        self.frame_5.setMaximumSize(QSize(16777215, 3))
        self.frame_5.setStyleSheet(u"background-color: rgb(65, 72, 88);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_5, 10, 0, 1, 3)

        self.N2_label = QLabel(self.page2)
        self.N2_label.setObjectName(u"N2_label")
        self.N2_label.setMinimumSize(QSize(90, 0))
        self.N2_label.setMaximumSize(QSize(90, 16777215))
        self.N2_label.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.N2_label, 7, 0, 1, 1)

        self.KeepTime_label = QLabel(self.page2)
        self.KeepTime_label.setObjectName(u"KeepTime_label")
        self.KeepTime_label.setMinimumSize(QSize(80, 0))
        self.KeepTime_label.setMaximumSize(QSize(80, 16777215))
        self.KeepTime_label.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.KeepTime_label, 11, 0, 1, 1)

        self.cascade_label = QLabel(self.page2)
        self.cascade_label.setObjectName(u"cascade_label")
        self.cascade_label.setMinimumSize(QSize(90, 0))
        self.cascade_label.setMaximumSize(QSize(90, 16777215))
        self.cascade_label.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"border:none;")

        self.gridLayout_4.addWidget(self.cascade_label, 9, 0, 1, 1)

        self.cascade_comboBox = QComboBox(self.page2)
        self.cascade_comboBox.addItem("")
        self.cascade_comboBox.addItem("")
        self.cascade_comboBox.setObjectName(u"cascade_comboBox")
        self.cascade_comboBox.setMinimumSize(QSize(80, 20))
        self.cascade_comboBox.setMaximumSize(QSize(16777215, 20))
        self.cascade_comboBox.setStyleSheet(u"font:13px \"\u6e38\u30b4\u30b7\u30c3\u30af\";\n"
"color: rgb(225, 230, 241);\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 4px;")
        self.cascade_comboBox.setMaxVisibleItems(5)

        self.gridLayout_4.addWidget(self.cascade_comboBox, 9, 1, 1, 2, Qt.AlignHCenter)

        self.page.addWidget(self.page2)

        self.gridLayout_3.addWidget(self.page, 0, 0, 1, 1)


        self.retranslateUi(temp_pattern)

        self.page.setCurrentIndex(1)
        self.PID_comboBox.setCurrentIndex(0)
        self.TestPattern_comboBox.setCurrentIndex(-1)
        self.cascade_comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(temp_pattern)
    # setupUi

    def retranslateUi(self, temp_pattern):
        temp_pattern.setWindowTitle(QCoreApplication.translate("temp_pattern", u"Form", None))
        self.PID_label.setText(QCoreApplication.translate("temp_pattern", u"PID", None))
        self.Time_label.setText(QCoreApplication.translate("temp_pattern", u"\u6642\uff1a\u5206", None))
        self.KeepTime_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"30", None))
        self.PID_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"No.1", None))
        self.PID_comboBox.setItemText(1, QCoreApplication.translate("temp_pattern", u"No.2", None))
        self.PID_comboBox.setItemText(2, QCoreApplication.translate("temp_pattern", u"No.3", None))
        self.PID_comboBox.setItemText(3, QCoreApplication.translate("temp_pattern", u"No.4", None))

        self.N2_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"12", None))
        self.Temp_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"450", None))
        self.TestPattern_label.setText(QCoreApplication.translate("temp_pattern", u"\u6e2c\u5b9a\u30d1\u30bf\u30fc\u30f3", None))
        self.Hour_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"45", None))
        self.label_4.setText(QCoreApplication.translate("temp_pattern", u":", None))
        self.Min_lineEdit.setText(QCoreApplication.translate("temp_pattern", u"45", None))
        self.Type_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"\u6607\u964d\u6e29", None))
        self.Type_comboBox.setItemText(1, QCoreApplication.translate("temp_pattern", u"\u6e2c\u5b9a", None))
        self.Type_comboBox.setItemText(2, QCoreApplication.translate("temp_pattern", u"END", None))

        self.Temp_label.setText(QCoreApplication.translate("temp_pattern", u"\u4e3b\u7089(\u2103)", None))
        self.label_8.setText("")
        self.Step_label.setText(QCoreApplication.translate("temp_pattern", u"STEP 1", None))
        self.N2_label.setText(QCoreApplication.translate("temp_pattern", u"N2 (SLM)", None))
        self.KeepTime_label.setText(QCoreApplication.translate("temp_pattern", u"\u30ad\u30fc\u30d7\u6642\u9593(s)", None))
        self.cascade_label.setText(QCoreApplication.translate("temp_pattern", u"\u30ab\u30b9\u30b1\u30fc\u30c9\u5236\u5fa1", None))
        self.cascade_comboBox.setItemText(0, QCoreApplication.translate("temp_pattern", u"NO", None))
        self.cascade_comboBox.setItemText(1, QCoreApplication.translate("temp_pattern", u"YES", None))

    # retranslateUi

