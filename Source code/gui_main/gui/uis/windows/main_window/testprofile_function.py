
from gui_main.gui.widgets.py_table_widget.py_table_widget import PyTableWidget
import math

from . functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui_main.qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui_main.gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# IMPORT ICON
# ///////////////////////////////////////////////////////////////
from gui_main.gui.widgets.py_left_column.py_icon import *

from gui_main.gui.uis.pattern_columns import *

import threading

import sys
import os
import time

from gui_main.qt_core import *

from registor_manager import *

import csv
import datetime


class Testfile_manager(QWidget):
    
    def __init__(
            self,
            parent = None,
            PoolSemaphore = None,
            app_parent = None,
            queuePool={}
    ):
        super().__init__()

        self._parent=parent
        self.PoolSemaphore=PoolSemaphore
        self.queuePool=queuePool

        self._year=""
        self._QC_Test=0
        self._Costom_Test=0
        self._testNumber=""
        self._costomer=""
        self._costomerName=""
        self._testMeterialName=""
        self._testMeterial=""
        self._MeterialMainDie=""
        self._MeterialinnerDie=""
        self._thinkness=""

        self.pid_parameter_list=[]

        self.folder_path=""

        self.memory_reader()
        self.set_parameter()
        self.utility_setup()
        self.utility_update()

        dialog_thread = threading.Thread(target = self.dialog_work,daemon=True)
        dialog_thread.start()

        self.dialog_request=False

        self.timer=QTimer()
        self.timer.timeout.connect(self.ultility_Update_Work)
        self.timer.start(10)

    def ultility_Update_Work(self):

        if self.dialog_request:
            self.dialog_request=False
            if self.dialog_item[0]=="option":
                result=self.lunchOptionDialog(self.dialog_item[1],self.dialog_item[2])
            elif self.dialog_item[0]=="Message":
                result=self.lunchMessageDialog(self.dialog_item[1],self.dialog_item[2])
                
            self.queuePool["dialog resultQueue"].put(result)


    def dialog_work(self):
        while 1:
            self.dialog_item=self.queuePool["dialog comfirmQueue"].get()
            self.dialog_request=True

            
        

    def memory_reader(self):

        self._year=self._parent.MMG.memoryPool["System memory"]["年度"].getValue()
        self._QC_Test=self._parent.MMG.memoryPool["System memory"]["評価試験"].getValue()
        self._Costom_Test=self._parent.MMG.memoryPool["System memory"]["依頼試験"].getValue()
        self._testNumber=self._parent.MMG.memoryPool["System memory"]["依頼測定番号"].getValue()
        self._costomer=self._parent.MMG.memoryPool["System memory"]["依頼元"].getValue()
        self._costomerName=self._parent.MMG.memoryPool["System memory"]["依頼者"].getValue()
        self._testMeterialName=self._parent.MMG.memoryPool["System memory"]["試料名称"].getValue()
        self._testMeterial=self._parent.MMG.memoryPool["System memory"]["材料"].getValue()
        self._MeterialMainDie=self._parent.MMG.memoryPool["System memory"]["主電極径(mm)"].getValue()
        self._MeterialinnerDie=self._parent.MMG.memoryPool["System memory"]["ガード電極の内径(mm)"].getValue()
        self._thinkness=self._parent.MMG.memoryPool["System memory"]["試料の厚さ(mm)"].getValue()

        self.pid_parameter_list=[]
        for pid_number in range(0,10):
            pid=["P","I","D"]
            pid_parameter=[]
            for K in pid:
                pid_parameter.append(self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PID_No_{}_{}".format(pid_number,K)].getValue())
            self.pid_parameter_list.append(pid_parameter)

    def set_memorypool_register(self,pool_name,registor_name,value):
        self.PoolSemaphore.acquire(timeout=10)
        if self._parent.MMG.memoryPool[pool_name][registor_name].getValue()!=value:
            self._parent.MMG.memoryPool[pool_name][registor_name].setValue(value)
            sendItem=MemoryUnit(pool_name,registor_name)
            self.queuePool["memory_UploadToMaster_Queue"].put(sendItem)
        self.PoolSemaphore.release()
        
    def set_parameter(self):
        self._parent.ui.load_pages.QC_Test_RadioButton.setChecked(self._QC_Test)
        self._parent.ui.load_pages.Costom_Test_RadioButton.setChecked(self._Costom_Test)

        self._parent.ui.load_pages.lineEdit_year.setText(str(self._year))
        self._parent.ui.load_pages.lineEdit_testNumber.setText(str(self._testNumber))
        self._parent.ui.load_pages.lineEdit_costomer.setText(str(self._costomer))
        self._parent.ui.load_pages.lineEdit_costomerName.setText(str(self._costomerName))
        self._parent.ui.load_pages.lineEdit_testMeterialName.setText(str(self._testMeterialName))
        self._parent.ui.load_pages.lineEdit_testMeterial.setText(str(self._testMeterial))
        self._parent.ui.load_pages.lineEdit_MeterialMainDie.setText(str(self._MeterialMainDie))
        self._parent.ui.load_pages.lineEdit_MeterialinnerDie.setText(str(self._MeterialinnerDie))
        self._parent.ui.load_pages.lineEdit_thinkness.setText(str(self._thinkness))

        self._parent.ui.load_pages.lineEdit_PID_0_P.setText(str("{:0.01f}".format(0.01*self.pid_parameter_list[0][0])))
        self._parent.ui.load_pages.lineEdit_PID_0_I.setText(str(self.pid_parameter_list[0][1]))
        self._parent.ui.load_pages.lineEdit_PID_0_D.setText(str(self.pid_parameter_list[0][2]))

        self._parent.ui.load_pages.lineEdit_PID_1_P.setText(str("{:0.01f}".format(0.01*self.pid_parameter_list[1][0])))
        self._parent.ui.load_pages.lineEdit_PID_1_I.setText(str(self.pid_parameter_list[1][1]))
        self._parent.ui.load_pages.lineEdit_PID_1_D.setText(str(self.pid_parameter_list[1][2]))

        self._parent.ui.load_pages.lineEdit_PID_2_P.setText(str("{:0.01f}".format(0.01*self.pid_parameter_list[2][0])))
        self._parent.ui.load_pages.lineEdit_PID_2_I.setText(str(self.pid_parameter_list[2][1]))
        self._parent.ui.load_pages.lineEdit_PID_2_D.setText(str(self.pid_parameter_list[2][2]))

        self._parent.ui.load_pages.lineEdit_PID_3_P.setText(str("{:0.01f}".format(0.01*self.pid_parameter_list[3][0])))
        self._parent.ui.load_pages.lineEdit_PID_3_I.setText(str(self.pid_parameter_list[3][1]))
        self._parent.ui.load_pages.lineEdit_PID_3_D.setText(str(self.pid_parameter_list[3][2]))

        self._parent.ui.load_pages.lineEdit_PID_4_P.setText(str("{:0.01f}".format(0.01*self.pid_parameter_list[4][0])))
        self._parent.ui.load_pages.lineEdit_PID_4_I.setText(str(self.pid_parameter_list[4][1]))
        self._parent.ui.load_pages.lineEdit_PID_4_D.setText(str(self.pid_parameter_list[4][2]))

        self._parent.ui.load_pages.lineEdit_PID_5_P.setText(str("{:0.01f}".format(0.01*self.pid_parameter_list[5][0])))
        self._parent.ui.load_pages.lineEdit_PID_5_I.setText(str(self.pid_parameter_list[5][1]))
        self._parent.ui.load_pages.lineEdit_PID_5_D.setText(str(self.pid_parameter_list[5][2]))

        self._parent.ui.load_pages.lineEdit_PID_6_P.setText(str("{:0.01f}".format(0.01*self.pid_parameter_list[6][0])))
        self._parent.ui.load_pages.lineEdit_PID_6_I.setText(str(self.pid_parameter_list[6][1]))
        self._parent.ui.load_pages.lineEdit_PID_6_D.setText(str(self.pid_parameter_list[6][2]))

        self._parent.ui.load_pages.lineEdit_PID_7_P.setText(str("{:0.01f}".format(0.01*self.pid_parameter_list[7][0])))
        self._parent.ui.load_pages.lineEdit_PID_7_I.setText(str(self.pid_parameter_list[7][1]))
        self._parent.ui.load_pages.lineEdit_PID_7_D.setText(str(self.pid_parameter_list[7][2]))

        self._parent.ui.load_pages.lineEdit_PID_8_P.setText(str("{:0.01f}".format(0.01*self.pid_parameter_list[8][0])))
        self._parent.ui.load_pages.lineEdit_PID_8_I.setText(str(self.pid_parameter_list[8][1]))
        self._parent.ui.load_pages.lineEdit_PID_8_D.setText(str(self.pid_parameter_list[8][2]))

        self._parent.ui.load_pages.lineEdit_PID_9_P.setText(str("{:0.01f}".format(0.01*self.pid_parameter_list[9][0])))
        self._parent.ui.load_pages.lineEdit_PID_9_I.setText(str(self.pid_parameter_list[9][1]))
        self._parent.ui.load_pages.lineEdit_PID_9_D.setText(str(self.pid_parameter_list[9][2]))


    def utility_update(self):

        if self._Costom_Test:

            self._parent.ui.load_pages.frame_2.setVisible(True)
            #self._parent.ui.load_pages.lineEdit_costomerName.setVisible(True)
            #self._parent.ui.load_pages.label_4.setVisible(True)
            #self._parent.ui.load_pages.label_5.setVisible(True)



            #self._parent.ui.load_pages.lineEdit_costomer.setEnabled(True)
            #self._parent.ui.load_pages.lineEdit_costomerName.setEnabled(True)
            #self._parent.ui.load_pages.label_4.setEnabled(True)
            #self._parent.ui.load_pages.label_5.setEnabled(True)
        else:
            self._parent.ui.load_pages.frame_2.setVisible(False)
            #self._parent.ui.load_pages.lineEdit_costomer.setVisible(False)
            #self._parent.ui.load_pages.lineEdit_costomerName.setVisible(False)
            #self._parent.ui.load_pages.label_4.setVisible(False)
            #self._parent.ui.load_pages.label_5.setVisible(False)


    def utility_setup(self):
        self._parent.ui.load_pages.QC_Test_RadioButton.clicked.connect(self.button_callback)
        self._parent.ui.load_pages.Costom_Test_RadioButton.clicked.connect(self.button_callback)
         
        self._parent.ui.load_pages.lineEdit_year.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_testNumber.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_costomer.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_costomerName.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_testMeterialName.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_testMeterial.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_MeterialMainDie.textChanged.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_MeterialMainDie.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_MeterialinnerDie.textChanged.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_MeterialinnerDie.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_thinkness.textChanged.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_thinkness.setValidator(QDoubleValidator())

        self._parent.ui.load_pages.lineEdit_PID_0_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_0_P.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.lineEdit_PID_0_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_0_I.setValidator(QIntValidator())
        self._parent.ui.load_pages.lineEdit_PID_0_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_0_D.setValidator(QIntValidator())

        self._parent.ui.load_pages.lineEdit_PID_1_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_1_P.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.lineEdit_PID_1_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_1_I.setValidator(QIntValidator())
        self._parent.ui.load_pages.lineEdit_PID_1_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_1_D.setValidator(QIntValidator())

        self._parent.ui.load_pages.lineEdit_PID_2_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_2_P.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.lineEdit_PID_2_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_2_I.setValidator(QIntValidator())
        self._parent.ui.load_pages.lineEdit_PID_2_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_2_D.setValidator(QIntValidator())

        self._parent.ui.load_pages.lineEdit_PID_3_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_3_P.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.lineEdit_PID_3_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_3_I.setValidator(QIntValidator())
        self._parent.ui.load_pages.lineEdit_PID_3_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_3_D.setValidator(QIntValidator())

        self._parent.ui.load_pages.lineEdit_PID_4_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_4_P.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.lineEdit_PID_4_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_4_I.setValidator(QIntValidator())
        self._parent.ui.load_pages.lineEdit_PID_4_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_4_D.setValidator(QIntValidator())

        self._parent.ui.load_pages.lineEdit_PID_5_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_5_P.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.lineEdit_PID_5_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_5_I.setValidator(QIntValidator())
        self._parent.ui.load_pages.lineEdit_PID_5_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_5_D.setValidator(QIntValidator())

        self._parent.ui.load_pages.lineEdit_PID_6_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_6_P.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.lineEdit_PID_6_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_6_I.setValidator(QIntValidator())
        self._parent.ui.load_pages.lineEdit_PID_6_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_6_D.setValidator(QIntValidator())

        self._parent.ui.load_pages.lineEdit_PID_7_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_7_P.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.lineEdit_PID_7_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_7_I.setValidator(QIntValidator())
        self._parent.ui.load_pages.lineEdit_PID_7_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_7_D.setValidator(QIntValidator())

        self._parent.ui.load_pages.lineEdit_PID_8_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_8_P.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.lineEdit_PID_8_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_8_I.setValidator(QIntValidator())
        self._parent.ui.load_pages.lineEdit_PID_8_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_8_D.setValidator(QIntValidator())

        self._parent.ui.load_pages.lineEdit_PID_9_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_9_P.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.lineEdit_PID_9_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_9_I.setValidator(QIntValidator())
        self._parent.ui.load_pages.lineEdit_PID_9_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_9_D.setValidator(QIntValidator())
        
        self.areaVolumeCal()
        

    def set_content_Editeable(self,enable):

        self._parent.ui.load_pages.QC_Test_RadioButton.setEnabled(enable)
        self._parent.ui.load_pages.Costom_Test_RadioButton.setEnabled(enable)
        
        self._parent.ui.load_pages.lineEdit_year.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_testNumber.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_costomer.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_costomerName.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_testMeterialName.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_testMeterial.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_MeterialMainDie.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_MeterialinnerDie.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_thinkness.setEnabled(enable)

        self._parent.ui.load_pages.lineEdit_PID_0_P.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_0_I.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_0_D.setEnabled(enable)

        self._parent.ui.load_pages.lineEdit_PID_1_P.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_1_I.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_1_D.setEnabled(enable)

        self._parent.ui.load_pages.lineEdit_PID_2_P.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_2_I.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_2_D.setEnabled(enable)

        self._parent.ui.load_pages.lineEdit_PID_3_P.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_3_I.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_3_D.setEnabled(enable)

        self._parent.ui.load_pages.lineEdit_PID_4_P.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_4_I.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_4_D.setEnabled(enable)

        self._parent.ui.load_pages.lineEdit_PID_5_P.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_5_I.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_5_D.setEnabled(enable)

        self._parent.ui.load_pages.lineEdit_PID_6_P.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_6_I.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_6_D.setEnabled(enable)

        self._parent.ui.load_pages.lineEdit_PID_7_P.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_7_I.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_7_D.setEnabled(enable)

        self._parent.ui.load_pages.lineEdit_PID_8_P.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_8_I.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_8_D.setEnabled(enable)

        self._parent.ui.load_pages.lineEdit_PID_9_P.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_9_I.setEnabled(enable)
        self._parent.ui.load_pages.lineEdit_PID_9_D.setEnabled(enable)

    def lunchOptionDialog(self,message,type):

        """
            variable
            PyDialog.error_type
            PyDialog.warning_2_type
            PyDialog.warning_3_type
        """

        diag = PyDialog(type,message)
        return(str(diag.exec()))

    def lunchMessageDialog(self,title,message):
        diag = PyMessageDialog(title,message)
        return(str(diag.exec()))

    def button_callback(self):
        btn=self.sender().objectName()

        if btn=="QC_Test_RadioButton":
            self._QC_Test=1
            self._Costom_Test=0
            self.set_memorypool_register("System memory","評価試験",self._QC_Test)
            self.set_memorypool_register("System memory","依頼試験",self._Costom_Test)
            

        elif btn=="Costom_Test_RadioButton":
            self._QC_Test=0
            self._Costom_Test=1
            self.set_memorypool_register("System memory","評価試験",self._QC_Test)
            self.set_memorypool_register("System memory","依頼試験",self._Costom_Test)

        elif btn=="lineEdit_year":
            self._year=self._parent.ui.load_pages.lineEdit_year.text()
            self.set_memorypool_register("System memory","年度",self._year)

        elif btn=="lineEdit_testNumber":
            self._testNumber=self._parent.ui.load_pages.lineEdit_testNumber.text()
            self.set_memorypool_register("System memory","依頼測定番号",self._testNumber)

        elif btn=="lineEdit_costomer":
            self._costomer=self._parent.ui.load_pages.lineEdit_costomer.text()
            self.set_memorypool_register("System memory","依頼元",self._costomer)

        elif btn=="lineEdit_costomerName":
            self._costomerName=self._parent.ui.load_pages.lineEdit_costomerName.text()
            self.set_memorypool_register("System memory","依頼者",self._costomerName)

        elif btn=="lineEdit_testMeterialName":
            self._testMeterialName=self._parent.ui.load_pages.lineEdit_testMeterialName.text()
            self.set_memorypool_register("System memory","試料名称",self._testMeterialName)

        elif btn=="lineEdit_testMeterial":
            self._testMeterial=self._parent.ui.load_pages.lineEdit_testMeterial.text()
            self.set_memorypool_register("System memory","材料",self._testMeterial)

        elif btn=="lineEdit_MeterialMainDie":
            self._MeterialMainDie=float(self._parent.ui.load_pages.lineEdit_MeterialMainDie.text())
            self.set_memorypool_register("System memory","主電極径(mm)",self._MeterialMainDie)
            self.areaVolumeCal()

        elif btn=="lineEdit_MeterialinnerDie":
            self._MeterialinnerDie=float(self._parent.ui.load_pages.lineEdit_MeterialinnerDie.text())
            self.set_memorypool_register("System memory","ガード電極の内径(mm)",self._MeterialinnerDie)
            self.areaVolumeCal()

        elif btn=="lineEdit_thinkness":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_thinkness.text())
            self.set_memorypool_register("System memory","試料の厚さ(mm)",self._thinkness)
            self.areaVolumeCal()

        elif btn=="lineEdit_PID_0_P":
            if float(self._parent.ui.load_pages.lineEdit_PID_0_P.text())<0.1:
                self._parent.ui.load_pages.lineEdit_PID_0_P.setText(str("{:0.01f}".format(0.1)))
            self.PID_0_P=float(self._parent.ui.load_pages.lineEdit_PID_0_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_0_P",100*self.PID_0_P)

        elif btn=="lineEdit_PID_0_I":
            self.PID_0_I=float(self._parent.ui.load_pages.lineEdit_PID_0_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_0_I",self.PID_0_I)

        elif btn=="lineEdit_PID_0_D":
            self.PID_0_D=float(self._parent.ui.load_pages.lineEdit_PID_0_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_0_D",self.PID_0_D)

        elif btn=="lineEdit_PID_1_P":
            if float(self._parent.ui.load_pages.lineEdit_PID_1_P.text())<0.1:
                self._parent.ui.load_pages.lineEdit_PID_1_P.setText(str("{:0.01f}".format(0.1)))
            self.PID_1_P=float(self._parent.ui.load_pages.lineEdit_PID_1_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_1_P",100*self.PID_1_P)

        elif btn=="lineEdit_PID_1_I":
            self.PID_1_I=float(self._parent.ui.load_pages.lineEdit_PID_1_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_1_I",self.PID_1_I)

        elif btn=="lineEdit_PID_1_D":
            self.PID_1_D=float(self._parent.ui.load_pages.lineEdit_PID_1_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_1_D",self.PID_1_D)

        elif btn=="lineEdit_PID_2_P":
            if float(self._parent.ui.load_pages.lineEdit_PID_2_P.text())<0.1:
                self._parent.ui.load_pages.lineEdit_PID_2_P.setText(str("{:0.01f}".format(0.1)))
            self.PID_2_P=float(self._parent.ui.load_pages.lineEdit_PID_2_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_2_P",100*self.PID_2_P)

        elif btn=="lineEdit_PID_2_I":
            self.PID_2_I=float(self._parent.ui.load_pages.lineEdit_PID_2_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_2_I",self.PID_2_I)

        elif btn=="lineEdit_PID_2_D":
            self.PID_2_D=float(self._parent.ui.load_pages.lineEdit_PID_2_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_2_D",self.PID_2_D)

        elif btn=="lineEdit_PID_3_P":
            if float(self._parent.ui.load_pages.lineEdit_PID_3_P.text())<0.1:
                self._parent.ui.load_pages.lineEdit_PID_3_P.setText(str("{:0.01f}".format(0.1)))
            self.PID_3_P=float(self._parent.ui.load_pages.lineEdit_PID_3_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_3_P",100*self.PID_3_P)

        elif btn=="lineEdit_PID_3_I":
            self.PID_3_I=float(self._parent.ui.load_pages.lineEdit_PID_3_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_3_I",self.PID_3_I)

        elif btn=="lineEdit_PID_3_D":
            self.PID_3_D=float(self._parent.ui.load_pages.lineEdit_PID_3_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_3_D",self.PID_3_D)

        elif btn=="lineEdit_PID_4_P":
            if float(self._parent.ui.load_pages.lineEdit_PID_4_P.text())<0.1:
                self._parent.ui.load_pages.lineEdit_PID_4_P.setText(str("{:0.01f}".format(0.1)))
            self.PID_4_P=float(self._parent.ui.load_pages.lineEdit_PID_4_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_4_P",100*self.PID_4_P)

        elif btn=="lineEdit_PID_4_I":
            self.PID_4_I=float(self._parent.ui.load_pages.lineEdit_PID_4_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_4_I",self.PID_4_I)

        elif btn=="lineEdit_PID_4_D":
            self.PID_4_D=float(self._parent.ui.load_pages.lineEdit_PID_4_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_4_D",self.PID_4_D)

        elif btn=="lineEdit_PID_5_P":   
            if float(self._parent.ui.load_pages.lineEdit_PID_5_P.text())<0.1:
                self._parent.ui.load_pages.lineEdit_PID_5_P.setText(str("{:0.01f}".format(0.1)))
            self.PID_5_P=float(self._parent.ui.load_pages.lineEdit_PID_5_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_5_P",100*self.PID_5_P)

        elif btn=="lineEdit_PID_5_I":
            self.PID_5_I=float(self._parent.ui.load_pages.lineEdit_PID_5_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_5_I",self.PID_5_I)

        elif btn=="lineEdit_PID_5_D":
            self.PID_5_D=float(self._parent.ui.load_pages.lineEdit_PID_5_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_5_D",self.PID_5_D)

        elif btn=="lineEdit_PID_6_P":   
            if float(self._parent.ui.load_pages.lineEdit_PID_6_P.text())<0.1:
                self._parent.ui.load_pages.lineEdit_PID_6_P.setText(str("{:0.01f}".format(0.1)))
            self.PID_6_P=float(self._parent.ui.load_pages.lineEdit_PID_6_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_6_P",100*self.PID_6_P)

        elif btn=="lineEdit_PID_6_I":
            self.PID_6_I=float(self._parent.ui.load_pages.lineEdit_PID_6_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_6_I",self.PID_6_I)

        elif btn=="lineEdit_PID_6_D":
            self.PID_6_D=float(self._parent.ui.load_pages.lineEdit_PID_6_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_6_D",self.PID_6_D)

        elif btn=="lineEdit_PID_7_P":   
            if float(self._parent.ui.load_pages.lineEdit_PID_7_P.text())<0.1:
                self._parent.ui.load_pages.lineEdit_PID_7_P.setText(str("{:0.01f}".format(0.1)))
            self.PID_7_P=float(self._parent.ui.load_pages.lineEdit_PID_7_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_7_P",100*self.PID_7_P)

        elif btn=="lineEdit_PID_7_I":
            self.PID_7_I=float(self._parent.ui.load_pages.lineEdit_PID_7_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_7_I",self.PID_7_I)

        elif btn=="lineEdit_PID_7_D":
            self.PID_7_D=float(self._parent.ui.load_pages.lineEdit_PID_7_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_7_D",self.PID_7_D)

        elif btn=="lineEdit_PID_8_P":   
            if float(self._parent.ui.load_pages.lineEdit_PID_8_P.text())<0.1:
                self._parent.ui.load_pages.lineEdit_PID_8_P.setText(str("{:0.01f}".format(0.1)))
            self.PID_8_P=float(self._parent.ui.load_pages.lineEdit_PID_8_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_8_P",100*self.PID_8_P)

        elif btn=="lineEdit_PID_8_I":
            self.PID_8_I=float(self._parent.ui.load_pages.lineEdit_PID_8_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_8_I",self.PID_8_I)

        elif btn=="lineEdit_PID_8_D":
            self.PID_8_D=float(self._parent.ui.load_pages.lineEdit_PID_8_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_8_D",self.PID_8_D)

        elif btn=="lineEdit_PID_9_P":   
            if float(self._parent.ui.load_pages.lineEdit_PID_9_P.text())<0.1:
                self._parent.ui.load_pages.lineEdit_PID_9_P.setText(str("{:0.01f}".format(0.1)))
            self.PID_9_P=float(self._parent.ui.load_pages.lineEdit_PID_9_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_9_P",100*self.PID_9_P)

        elif btn=="lineEdit_PID_9_I":
            self.PID_9_I=float(self._parent.ui.load_pages.lineEdit_PID_9_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_9_I",self.PID_9_I)

        elif btn=="lineEdit_PID_9_D":
            self.PID_9_D=float(self._parent.ui.load_pages.lineEdit_PID_9_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_9_D",self.PID_9_D)



        self.utility_update()

    def areaVolumeCal(self):

        if self._MeterialMainDie and self._MeterialinnerDie:
            temp=(self._MeterialMainDie+self._MeterialinnerDie)/4
            self.meterial_area=temp*temp*math.pi
            self._parent.ui.load_pages.lineEdit_meterialArea.setText("{:.2e}".format(self.meterial_area))
            if self._thinkness:
                self.meterial_volume=self.meterial_area*self._thinkness
                self._parent.ui.load_pages.lineEdit_meterialVolume.setText("{:.2e}".format(self.meterial_volume))

            else:
                self.meterial_volume=None
                self._parent.ui.load_pages.lineEdit_meterialVolume.setText("")

        else:
            self.meterial_area=None
            self.meterial_volume=None
            self._parent.ui.load_pages.lineEdit_meterialArea.setText("")
            self._parent.ui.load_pages.lineEdit_meterialVolume.setText("")
        
        

    
