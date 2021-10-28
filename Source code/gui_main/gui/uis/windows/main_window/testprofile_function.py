
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


import numpy as np
import pyqtgraph as pg

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
            app_parent = None,
            queuePool={}
    ):
        super().__init__()

        self._parent=parent
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
        for pid_number in range(0,4):
            pid=["P","I","D"]
            pid_parameter=[]
            for K in pid:
                pid_parameter.append(self._parent.MMG.memoryPool["Modbus Registor Pool - Registor"]["PID_No_{}_{}".format(pid_number,K)].getValue())
            self.pid_parameter_list.append(pid_parameter)

    def set_memorypool_register(self,pool_name,registor_name,value):

        if self._parent.MMG.memoryPool[pool_name][registor_name].getValue()!=value:
            self._parent.MMG.memoryPool[pool_name][registor_name].setValue(value)
            sendItem=MemoryUnit(pool_name,registor_name)
            self.queuePool["memory_UploadToMaster_Queue"].put(sendItem)
        
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

        self._parent.ui.load_pages.lineEdit_PID_1_P.setText(str(self.pid_parameter_list[0][0]))
        self._parent.ui.load_pages.lineEdit_PID_1_I.setText(str(self.pid_parameter_list[0][1]))
        self._parent.ui.load_pages.lineEdit_PID_1_D.setText(str(self.pid_parameter_list[0][2]))

        self._parent.ui.load_pages.lineEdit_PID_2_P.setText(str(self.pid_parameter_list[1][0]))
        self._parent.ui.load_pages.lineEdit_PID_2_I.setText(str(self.pid_parameter_list[1][1]))
        self._parent.ui.load_pages.lineEdit_PID_2_D.setText(str(self.pid_parameter_list[1][2]))

        self._parent.ui.load_pages.lineEdit_PID_3_P.setText(str(self.pid_parameter_list[2][0]))
        self._parent.ui.load_pages.lineEdit_PID_3_I.setText(str(self.pid_parameter_list[2][1]))
        self._parent.ui.load_pages.lineEdit_PID_3_D.setText(str(self.pid_parameter_list[2][2]))

        self._parent.ui.load_pages.lineEdit_PID_4_P.setText(str(self.pid_parameter_list[3][0]))
        self._parent.ui.load_pages.lineEdit_PID_4_I.setText(str(self.pid_parameter_list[3][1]))
        self._parent.ui.load_pages.lineEdit_PID_4_D.setText(str(self.pid_parameter_list[3][2]))

    def utility_setup(self):
        self._parent.ui.load_pages.QC_Test_RadioButton.clicked.connect(self.button_callback)
        self._parent.ui.load_pages.Costom_Test_RadioButton.clicked.connect(self.button_callback)

        self._parent.ui.load_pages.lineEdit_year.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_testNumber.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_costomer.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_costomerName.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_testMeterialName.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_testMeterial.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_MeterialMainDie.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_MeterialMainDie.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_MeterialinnerDie.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_MeterialinnerDie.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_thinkness.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_thinkness.setValidator(QDoubleValidator())

        self._parent.ui.load_pages.lineEdit_PID_1_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_1_P.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_PID_1_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_1_I.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_PID_1_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_1_D.setValidator(QDoubleValidator())

        self._parent.ui.load_pages.lineEdit_PID_2_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_2_P.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_PID_2_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_2_I.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_PID_2_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_2_D.setValidator(QDoubleValidator())

        self._parent.ui.load_pages.lineEdit_PID_3_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_3_P.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_PID_3_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_3_I.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_PID_3_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_3_D.setValidator(QDoubleValidator())

        self._parent.ui.load_pages.lineEdit_PID_4_P.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_4_P.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_PID_4_I.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_4_I.setValidator(QDoubleValidator())
        self._parent.ui.load_pages.lineEdit_PID_4_D.editingFinished.connect(self.button_callback)
        self._parent.ui.load_pages.lineEdit_PID_4_D.setValidator(QDoubleValidator())
        
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
            self.prepare_folder()

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

        elif btn=="lineEdit_PID_1_P":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_1_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_0_P",self._thinkness)

        elif btn=="lineEdit_PID_1_I":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_1_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_0_I",self._thinkness)

        elif btn=="lineEdit_PID_1_D":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_1_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_0_D",self._thinkness)

        elif btn=="lineEdit_PID_2_P":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_2_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_1_P",self._thinkness)

        elif btn=="lineEdit_PID_2_I":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_2_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_1_I",self._thinkness)

        elif btn=="lineEdit_PID_2_D":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_2_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_1_D",self._thinkness)

        elif btn=="lineEdit_PID_3_P":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_3_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_2_P",self._thinkness)

        elif btn=="lineEdit_PID_3_I":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_3_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_2_I",self._thinkness)

        elif btn=="lineEdit_PID_3_D":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_3_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_2_D",self._thinkness)

        elif btn=="lineEdit_PID_4_P":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_4_P.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_3_P",self._thinkness)

        elif btn=="lineEdit_PID_4_I":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_4_I.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_3_I",self._thinkness)

        elif btn=="lineEdit_PID_4_D":
            self._thinkness=float(self._parent.ui.load_pages.lineEdit_PID_4_D.text())
            self.set_memorypool_register("Modbus Registor Pool - Registor","PID_No_3_D",self._thinkness)

    def areaVolumeCal(self):



        if self._MeterialMainDie and self._MeterialinnerDie:
            temp=(self._MeterialMainDie+self._MeterialinnerDie)/4
            self.meterial_area=temp*temp*math.pi

            if self._thinkness:
                self.meterial_volume=self.meterial_area*self._thinkness
            else:
                self.meterial_volume=None

        else:
            self.meterial_area=None
            self.meterial_volume=None


        self._parent.ui.load_pages.lineEdit_meterialArea.setText("{:.2e}".format(self.meterial_area))
        self._parent.ui.load_pages.lineEdit_meterialVolume.setText("{:.2e}".format(self.meterial_volume))

    def prepare_folder(self):

        path = "C:/高温抵抗測定結果"
        directory = "{}".format(str(self._year))
        
        # Create base Directory
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        
        # Create target Year Directory
        try:
            path = os.path.join(path, directory)
            os.mkdir(path)
        except FileExistsError:
            pass
        
        # Create target Directory
        try:
            os.mkdir(os.path.join(path, "評価試験"))
            os.mkdir(os.path.join(path, "依頼測定"))
        except FileExistsError:
            pass
        
        if self._QC_Test:
            
            path=os.path.join(path, "依頼測定")

            timeNow=datetime.datetime.now()
            path = os.path.join(path,"{}_{}_{}_{}_{}_{}_result".format(timeNow.year,timeNow.month,timeNow.date,timeNow.hour,timeNow.minute,timeNow.second))
            os.mkdir(path)

        else:
            
            try:
                path_temp=os.path.join(path, "評価試験/{}".format(self._testNumber))
                os.mkdir(path_temp)

            except FileExistsError:
                
                result=self.lunchOptionDialog("依頼番号 \"{}\" フォルダーが存在しています。上書きますか？".format(self._testNumber),PyDialog.warning_2_type)
                if result=="Yes":
                    
                    path=path_temp
                    os.rmdir(path)
                    os.mkdir(path)

                elif result=="No":
                    NameString_fromDialog=self.lunchMessageDialog("依頼番号編集","新規依頼番号入力 :")
                    path=os.path.join(path, "評価試験/{}".format(NameString_fromDialog))
                    os.mkdir(path)

            

        self.folder_path=path
