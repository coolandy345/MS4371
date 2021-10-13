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
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.clicked.connect(self.dialogCallback)


        self.layout = QVBoxLayout()
        message = QLabel(text)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


    def dialogCallback(self,bottum):

        text=bottum.text()
        if text =="&Yes":
            self.PyYesSignal.emit()
        elif text =="&No":
            self.PyNoSignal.emit()
        elif text =="Cancel":
            self.PyCancelSignal.emit()





