# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui_main.qt_core import *

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.core.functions import *

# PY TITLE BUTTON
# ///////////////////////////////////////////////////////////////
class PyDialog(QDialog):

    PyYesSignal=Signal()
    PyNoSignal=Signal()
    PyCancelSignal=Signal()

    warning_2_type="warning_2_type"
    warning_3_type="warning_3_type"
    error_type="error_type"

    def __init__(self,type,text,):
        super().__init__()

        if type==self.warning_2_type:
            self.setWindowTitle("Warning!")
            self.setWindowIcon(QIcon("warning.ico"))
            QBtn = QDialogButtonBox.Yes | QDialogButtonBox.No
        elif type==self.warning_3_type:
            self.setWindowTitle("Warning!")
            self.setWindowIcon(QIcon("warning.ico"))
            QBtn = QDialogButtonBox.Yes | QDialogButtonBox.No | QDialogButtonBox.Cancel
        elif type==self.error_type:
            self.setWindowTitle("Error!")
            self.setWindowIcon(QIcon("error.ico"))
            QBtn = QDialogButtonBox.Ok


        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.clicked.connect(self.dialogCallback)


        self.layout = QVBoxLayout()
        message = QLabel(text)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def exec(self):
        super().exec()
        return self.returnMessage

    def dialogCallback(self,bottum):

        text=bottum.text()
        self.returnMessage=text
        if text =="&Yes":
            self.returnMessage="Yes"
        elif text =="&No":
            self.returnMessage="No"
        elif text =="Cancel":
            self.returnMessage="Cancel"

        super().accept()




class PyMessageDialog(QDialog):

    PyOkSignal=Signal()
    PyCancelSignal=Signal()


    def __init__(self,title,message):
        super().__init__()

        self.setWindowTitle(title)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel


        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.clicked.connect(self.dialogCallback)


        self.layout = QVBoxLayout()
        self.label = QLabel(message)
        self.message = QLineEdit()
        self.message.setValidator(QRegularExpressionValidator("[a-zA-z0-9]+$"))
        self.message.setMaxLength(8)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def exec(self):
        super().exec()
        return self.returnMessage


    #def accept(self):
    #    self.returnMessage=self.message.text()
    #    super().accept()

    #def reject(self):
    #    self.returnMessage="Dialog reject"
    #    super().reject()

    def dialogCallback(self,bottum):

        text=bottum.text()
        self.returnMessage=text
        if text =="OK":
            self.returnMessage=self.message.text()
        elif text =="Cancel":
            self.returnMessage="Dialog reject"

        super().accept()