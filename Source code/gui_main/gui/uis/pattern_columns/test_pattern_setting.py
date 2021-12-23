from gui_main.qt_core import *
from gui_main.gui.uis.windows.main_window import *
from gui_main.gui.uis.pattern_columns.pattern_function import testUnit,testlist
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *
from gui_main.gui.core.json_settings import Settings
from gui_main.gui.core.json_themes import Themes
from PyQt5.QtCore import QTimer
import threading

#from modbus_TcpServer import ModbusRegistorClass
import modbus_TcpServer
import time
import sys

import copy

from registor_manager import *

import numpy as np
import pyqtgraph as pg

class updata_step_widge_Thread(QRunnable):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        self.parent.updata_step_widge_work()

class update_graph_Thread(QRunnable):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        self.parent.update_graph_work()

class patternFile_Save_Thread(QRunnable):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        self.parent.patternFile_Save_work()


class TestPatternWidget(QWidget):
    
    def __init__(
            self,
            parent = None,
            app_parent = None,
            PoolSemaphore = None,
            queuePool={}
    ):
        super().__init__()

        
        self._parent=parent
        self.PoolSemaphore=PoolSemaphore
        self.Step_number=0
        self.queuePool=queuePool
        self.step_widges_list=[]
        self.patternFiles=[]
        self.availlible_patternFile_count=0
        self.focus_patternFile_number=0
        self.focus_step_number=0
        self.cache_step=testUnit()
        self.cache_steplist=testlist()
        self.paste_ready=False
        self.content_Change=False
        self.activeStep_noFull=False
        self.update_Request=False
        self.IconButtonUpdate=False
        self.delete_IconButtonActiveState=True
        self.add_IconButtonActiveState=False
        self.save_IconButtonActiveState=False

        self.utility_setup()
        self.setup_TempPattern()
        self.setup_TempGraph()
        self.memory_reader()
        self.patternFile_Load()
        self.update_Request=True

        self.timer=QTimer()
        self.timer.timeout.connect(self.ultility_Update_Work)
        self.timer.start(10)

        #ultility_Update_Thread = threading.Thread(target = self.ultility_Update_Work,daemon=True)
        #ultility_Update_Thread.start()

        self.test=0
        self.test1=0

    def setup_TempPattern(self):
        self.step_widges_list=[None]
        for _step in range(1,21):
            test_step = PyTestStep(
                active=False,
                step=_step,
                parent = self._parent,
                )
            self.step_widges_list.append(test_step)
            self.step_widges_list[_step].setVisible (False)
            self._parent.ui.load_pages.horizontalLayout_6.addWidget(self.step_widges_list[_step])
            self._parent.ui.load_pages.scrollArea_4.setMinimumSize(QSize(0, 160))
        
    def setup_TempGraph(self):
        self.graph =pg.PlotWidget(background=None,title="測定パターン")
        
        self.graph.setLabel(axis='left', text='電圧', units='V')

        self.graph.setLimits(xMin=0,xMax=17.9)
        self.Xaxis = self.graph.getAxis('bottom')
        self.Xaxis.setStyle(autoReduceTextSpace=False)
        self.Xaxis.setTickSpacing(1,1)
        self.Xaxis.setTextPen(pg.mkPen((25,28,34)))
        self.graph.setAxisItems({'bottom':self.Xaxis})
        
        self.Yaxis = self.graph.getAxis('left')
        self.Yaxis.enableAutoSIPrefix(False)

        self.graph.showGrid(x=True, y=True)
        self.graph.setMouseEnabled(x=True, y=False)
        self.graph.setLimits(minXRange=9,maxXRange=20)
        #self.graph.setMinimumSize(QSize(1100, 300))
        
        self.curve=self.graph.plot(
                                   pen=pg.mkPen('w',width=5), 
                                   symbolBrush=(0,0,0),
                                   symbolPen='w', 
                                   symbol='o', 
                                   symbolSize=5, 
                                   name="測定パターン")
        
        self._parent.ui.load_pages.gridLayout_11.addWidget(self.graph, Qt.AlignCenter, Qt.AlignCenter)
        
        

        self.GraphRegionList=[]
        #self.GraphRegionList.append(None)
        self.GraphStepLabelList=[]
        #self.GraphStepLabelList.append(None)

        for _step in range(0,10):

            region = PyGraphRegionItem(
                    parent  =self,
                    app_parent = self._parent,
                    brush = QBrush(QColor(0, 0, 0, 0)),
                    hoverBrush=QBrush(QColor(0, 10, 10, 100)),
                    pen=pg.mkPen(50,50,50),
                    step=_step,
                    movable=False
                    )
            if _step ==0:
                region.setRegion([0,1])
            elif _step ==9:
                region.setRegion([17,19])
            else:
                region.setRegion([(_step*2)-1, (_step*2)+1])
            self.GraphRegionList.append(region)

            self.graph.plotItem.addItem(self.GraphRegionList[_step], ignoreBounds=True)
            
            #text="STEP %d" %_step
            #print(text)
            if _step ==0:
                label=pg.TextItem(text="BG")
                label.setPos(0.1, 20)

            elif _step ==9:

                label=pg.TextItem(text="")
                label.setPos(17.1, 20)

            else:
                label=pg.TextItem(text="STEP {}".format(_step))
                label.setPos((_step*2)-1, 20)
            
            self.GraphStepLabelList.append(label)
            self.graph.plotItem.addItem(self.GraphStepLabelList[_step], ignoreBounds=True)
            
    def new_TestPattern(self):
        self.cache_steplist.setStep(self.cache_steplist.step_number+1,testUnit())
        self.cache_steplist.step_number+=1

        self.update_Request=True
        


    def memory_reader(self):
        _20_pattern_lists=[None]

        #Try to get number of PTN list
        self.availlible_patternFile_count=self._parent.MMG.memoryPool["Measurement Pattern"]["有効PTN総数"].getValue()
        self.focus_patternFile_number=self._parent.MMG.memoryPool["Measurement Pattern"]["フォーカスPTN番号"].getValue()
        #Auto load last pattern
        if self.focus_patternFile_number==0:
            if self.availlible_patternFile_count:
                self.focus_patternFile_number=self.availlible_patternFile_count
        else:
            if self.focus_patternFile_number>self.availlible_patternFile_count:
                self.focus_patternFile_number=self.availlible_patternFile_count
        

        self.patternFile_nameList=[]

        
        for file_number in range(1,21):
            pattern=testlist(
                name            =str(self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_名称".format(file_number)].value),
                step_number     =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_実行STEP数".format(file_number)].getValue(),
                active          =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_パターン有効".format(file_number)].getValue(),
                comment         =str(self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_註記".format(file_number)].value),
                test_time       =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_測定時間".format(file_number)].getValue(),
                test_sampletime =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_測定sampletime".format(file_number)].getValue(),
                BG0_test_time   =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_BG0測定時間".format(file_number)].getValue(),
                BG_test_time    =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_BG測定時間".format(file_number)].getValue(),
                BG_sampletime   =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_BG測定sampletime".format(file_number)].getValue(),
                speed   =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_speed".format(file_number)].getValue(),
                filter_type    =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_filter_type".format(file_number)].getValue(),
                filter_count   =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_filter_count".format(file_number)].getValue()
                )

            if pattern.active:
                self.patternFile_nameList.append(pattern.name)
            
            units=[None]

            for step_number in range(1,9):

                unit=testUnit(
                    voltage     =self._parent.MMG.memoryPool["Measurement Pattern"]["PTNData_{}_STEP_{}_電圧".format(file_number,step_number)].getValue(),
                    )
                units.append(unit)
            
            pattern.units=units
            _20_pattern_lists.append(pattern)
        self.patternFiles=_20_pattern_lists

    def memory_writer(self):

        for file_number in range(1,21):

            self.set_memorypool_register("Measurement Pattern","PTNData_{}_名称".format(file_number),self.patternFiles[file_number].name)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_註記".format(file_number),self.patternFiles[file_number].comment)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_パターン有効".format(file_number),self.patternFiles[file_number].active)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_実行STEP数".format(file_number),self.patternFiles[file_number].step_number)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_測定時間".format(file_number),self.patternFiles[file_number].test_time)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_測定sampletime".format(file_number),self.patternFiles[file_number].test_sampletime)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_BG0測定時間".format(file_number),self.patternFiles[file_number].BG0_test_time)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_BG測定時間".format(file_number),self.patternFiles[file_number].BG_test_time)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_BG測定sampletime".format(file_number),self.patternFiles[file_number].BG_sampletime)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_speed".format(file_number),self.patternFiles[file_number].speed)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_filter_type".format(file_number),self.patternFiles[file_number].filter_type)
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_filter_count".format(file_number),self.patternFiles[file_number].filter_count)

            for step_number in range(1,9):
                step_unit=self.patternFiles[file_number].getStep(step_number)
                self.set_memorypool_register("Measurement Pattern","PTNData_{}_STEP_{}_電圧".format(file_number,step_number),step_unit.voltage)
                
    def utility_update(self):
        #Check if we can still create new pattern list
        if self.patternFiles[20].active:
            self.add_IconButtonActiveState=False
            self.IconButtonUpdate=True
        else:
            self.add_IconButtonActiveState=True
            self.IconButtonUpdate=True


        #Scan Avilible pattern import to patternfile_comboBox

        #self._parent.ui.load_pages.Test_Totalcount_Label.setText("計測回数：{} 回".format(hour,min))

        self.cache_steplist.total_time=self.cache_steplist.BG0_test_time+self.cache_steplist.step_number*self.cache_steplist.test_time+self.cache_steplist.step_number*self.cache_steplist.BG_test_time
        
        self._parent.ui.load_pages.Test_Totaltime_Label.setText("合計時間：{:.2f} 分".format(self.cache_steplist.total_time))

        self._parent.ui.load_pages.testfile_comboBox.blockSignals(True)
        self._parent.ui.load_pages.testfile_comboBox.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.testfile_comboBox.clear()
        self._parent.ui.load_pages.testfile_comboBox.addItems(self.patternFile_nameList)
        self._parent.ui.load_pages.testfile_comboBox.setCurrentIndex(self.focus_patternFile_number-1)
        self._parent.ui.load_pages.testfile_comboBox.blockSignals(False)

        
        self._parent.ui.load_pages.test_commect_lineEdit.blockSignals(True)
        self._parent.ui.load_pages.test_commect_lineEdit.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.test_commect_lineEdit.setText(str(self.cache_steplist.comment))
        self._parent.ui.load_pages.test_commect_lineEdit.blockSignals(False)

        self._parent.ui.load_pages.test_time_LineEdit.blockSignals(True)
        self._parent.ui.load_pages.test_time_LineEdit.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.test_time_LineEdit.setText(str(self.cache_steplist.test_time))
        self._parent.ui.load_pages.test_time_LineEdit.blockSignals(False)



        self._parent.ui.load_pages.test_sampletime_LineEdit.blockSignals(True)
        self._parent.ui.load_pages.test_sampletime_LineEdit.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.test_sampletime_LineEdit.setText(str(self.cache_steplist.test_sampletime))
        self._parent.ui.load_pages.test_sampletime_LineEdit.blockSignals(False)

        
        self._parent.ui.load_pages.bg0_time_LineEdit.blockSignals(True)
        self._parent.ui.load_pages.bg0_time_LineEdit.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.bg0_time_LineEdit.setText(str(self.cache_steplist.BG0_test_time))
        self._parent.ui.load_pages.bg0_time_LineEdit.blockSignals(False)


        self._parent.ui.load_pages.bg_time_LineEdit.blockSignals(True)
        self._parent.ui.load_pages.bg_time_LineEdit.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.bg_time_LineEdit.setText(str(self.cache_steplist.BG_test_time))
        self._parent.ui.load_pages.bg_time_LineEdit.blockSignals(False)


        self._parent.ui.load_pages.bg_sampletime_LineEdit.blockSignals(True)
        self._parent.ui.load_pages.bg_sampletime_LineEdit.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.bg_sampletime_LineEdit.setText(str(self.cache_steplist.BG_sampletime))
        self._parent.ui.load_pages.bg_sampletime_LineEdit.blockSignals(False)


        self._parent.ui.load_pages.speed_comboBox.blockSignals(True)
        self._parent.ui.load_pages.speed_comboBox.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.speed_comboBox.setCurrentIndex(self.cache_steplist.speed)
        self._parent.ui.load_pages.speed_comboBox.blockSignals(False)

        self._parent.ui.load_pages.filter_comboBox.blockSignals(True)
        self._parent.ui.load_pages.filter_comboBox.setEnabled(self.editorEnable)
        self._parent.ui.load_pages.filter_comboBox.setCurrentIndex(self.cache_steplist.filter_type)
        self._parent.ui.load_pages.filter_comboBox.blockSignals(False)

        if self.cache_steplist.filter_type:
            self._parent.ui.load_pages.filter_count_LineEdit.setVisible(True)
            self._parent.ui.load_pages.filter_count_label.setVisible(True)
            self._parent.ui.load_pages.filter_count_LineEdit.blockSignals(True)
            self._parent.ui.load_pages.filter_count_LineEdit.setEnabled(self.editorEnable)
            self._parent.ui.load_pages.filter_count_LineEdit.setText(str(self.cache_steplist.filter_count))
            self._parent.ui.load_pages.filter_count_LineEdit.blockSignals(False)
        else:
            self._parent.ui.load_pages.filter_count_LineEdit.setVisible(False)
            self._parent.ui.load_pages.filter_count_label.setVisible(False)
            self._parent.ui.load_pages.filter_count_LineEdit.blockSignals(True)
            self._parent.ui.load_pages.filter_count_LineEdit.setEnabled(self.editorEnable)
            self._parent.ui.load_pages.filter_count_LineEdit.setText(str(0))
            self._parent.ui.load_pages.filter_count_LineEdit.blockSignals(False)


        self.save_IconButtonActiveState=self.content_Change
        self.delete_IconButtonActiveState=self.editorEnable

        self.IconButtonUpdate=True
        
        errormessage=self.cache_steplist.checkRule()
        
        self._parent.ui.load_pages.TestPatternErrorMessagelabel.setText(errormessage)


    def utility_setup(self):
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        self.settings = Settings().items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        self.themes = Themes().items

        #self.delete_IconButton = PyIconButton(
        #        icon_path = Functions.set_svg_icon("fi-rr-trash.svg"),
        #        parent = self._parent,
        #        app_parent = self._app_parent,
        #        btn_id = "削除",
        #        tooltip_text = "削除",
        #        width = 30,
        #        height = 30,
        #        radius = 10,
        #        dark_one = self.themes["app_color"]["dark_one"],
        #        icon_color = self.themes["app_color"]["critical_icon"]["icon_color"],
        #        icon_color_hover = self.themes["app_color"]["critical_icon"]["icon_hover"],
        #        icon_color_pressed = self.themes["app_color"]["critical_icon"]["icon_pressed"],
        #        icon_color_deactive = self.themes["app_color"]["critical_icon"]["icon_deactive"],
        #        bg_color = self.themes["app_color"]["critical_icon"]["icon_bg"],
        #        bg_color_hover = self.themes["app_color"]["critical_icon"]["icon_bg_hover"],
        #        bg_color_pressed = self.themes["app_color"]["critical_icon"]["icon_bg_pressed"],
        #    )
        self.delete_IconButton = PyIconButton_simple(
                icon = "fi-rr-trash.svg",
                icon_active = "fi-rr-trash.svg",
                icon_hover = "fi-rr-trash.svg",
                icon_deactive = "fi-rr-trash-deactive.svg",
                btn_id = "削除",
                tooltip_text = "削除",
                width = 30,
                height = 30,
                bg_color = self.themes["app_color"]["regular_icon"]["icon_bg"],
                bg_color_hover = self.themes["app_color"]["regular_icon"]["icon_bg_hover"],
                bg_color_pressed = self.themes["app_color"]["regular_icon"]["icon_bg_pressed"],

            )
        self._parent.ui.load_pages.verticalLayout_14.addWidget(self.delete_IconButton, Qt.AlignCenter, Qt.AlignCenter)
        self.delete_IconButton.clicked.connect(self.ui_click_callback)

        #self.add_IconButton = PyIconButton(
        #        icon_path = Functions.set_svg_icon("fi-rr-file-add.svg"),
        #        parent = self._parent,
        #        app_parent = self._app_parent,
        #        btn_id = "追加",
        #        tooltip_text = "追加",
        #        width = 30,
        #        height = 30,
        #        radius = 10,
        #        dark_one = self.themes["app_color"]["dark_one"],
        #        icon_color = self.themes["app_color"]["regular_icon"]["icon_color"],
        #        icon_color_hover = self.themes["app_color"]["regular_icon"]["icon_hover"],
        #        icon_color_pressed = self.themes["app_color"]["regular_icon"]["icon_pressed"],
        #        icon_color_deactive = self.themes["app_color"]["regular_icon"]["icon_deactive"],
        #        bg_color = self.themes["app_color"]["regular_icon"]["icon_bg"],
        #        bg_color_hover = self.themes["app_color"]["regular_icon"]["icon_bg_hover"],
        #        bg_color_pressed = self.themes["app_color"]["regular_icon"]["icon_bg_pressed"],
        #    )
        self.add_IconButton = PyIconButton_simple(
                icon = "fi-rr-file-add.svg",
                icon_active = "fi-rr-file-add.svg",
                icon_hover = "fi-rr-file-add.svg",
                icon_deactive = "fi-rr-file-add-deactive.svg",
                btn_id = "追加",
                tooltip_text = "追加",
                width = 30,
                height = 30,
                bg_color = self.themes["app_color"]["regular_icon"]["icon_bg"],
                bg_color_hover = self.themes["app_color"]["regular_icon"]["icon_bg_hover"],
                bg_color_pressed = self.themes["app_color"]["regular_icon"]["icon_bg_pressed"],

            )
        self._parent.ui.load_pages.verticalLayout_15.addWidget(self.add_IconButton, Qt.AlignCenter, Qt.AlignCenter)
        self.add_IconButton.clicked.connect(self.ui_click_callback)

        #self.save_IconButton = PyIconButton(
        #        icon_path = Functions.set_svg_icon("fi-rr-edit.svg"),
        #        parent = self._parent,
        #        app_parent = self._app_parent,
        #        btn_id = "保存",
        #        tooltip_text = "保存",
        #        width = 30,
        #        height = 30,
        #        radius = 10,
        #        dark_one = self.themes["app_color"]["dark_one"],
        #        icon_color = self.themes["app_color"]["regular_icon"]["icon_color"],
        #        icon_color_hover = self.themes["app_color"]["regular_icon"]["icon_hover"],
        #        icon_color_pressed = self.themes["app_color"]["regular_icon"]["icon_pressed"],
        #        icon_color_deactive = self.themes["app_color"]["regular_icon"]["icon_deactive"],
        #        bg_color = self.themes["app_color"]["regular_icon"]["icon_bg"],
        #        bg_color_hover = self.themes["app_color"]["regular_icon"]["icon_bg_hover"],
        #        bg_color_pressed = self.themes["app_color"]["regular_icon"]["icon_bg_pressed"],
        #    )

        self.save_IconButton = PyIconButton_simple(
                icon = "fi-rr-edit.svg",
                icon_active = "fi-rr-edit.svg",
                icon_hover = "fi-rr-edit.svg",
                icon_deactive = "fi-rr-edit-deactive.svg",
                btn_id = "保存",
                tooltip_text = "編集",
                width = 30,
                height = 30,
                bg_color = self.themes["app_color"]["regular_icon"]["icon_bg"],
                bg_color_hover = self.themes["app_color"]["regular_icon"]["icon_bg_hover"],
                bg_color_pressed = self.themes["app_color"]["regular_icon"]["icon_bg_pressed"],

            )


        self._parent.ui.load_pages.verticalLayout_16.addWidget(self.save_IconButton, Qt.AlignCenter, Qt.AlignCenter)
        self.save_IconButton.clicked.connect(self.ui_click_callback)

        self._parent.ui.load_pages.testfile_comboBox.currentIndexChanged.connect(self.ui_click_callback)
        self._parent.ui.load_pages.test_commect_lineEdit.textChanged.connect(self.ui_click_callback)
        
        self._parent.ui.load_pages.test_time_LineEdit.editingFinished.connect(self.ui_click_callback)
        self._parent.ui.load_pages.test_time_LineEdit.setValidator(QDoubleValidator(decimals=3))
        self._parent.ui.load_pages.test_sampletime_LineEdit.editingFinished.connect(self.ui_click_callback)
        self._parent.ui.load_pages.test_sampletime_LineEdit.setValidator(QDoubleValidator(decimals=2))
        self._parent.ui.load_pages.bg0_time_LineEdit.editingFinished.connect(self.ui_click_callback)
        self._parent.ui.load_pages.bg0_time_LineEdit.setValidator(QDoubleValidator(decimals=3))
        self._parent.ui.load_pages.bg_time_LineEdit.editingFinished.connect(self.ui_click_callback)
        self._parent.ui.load_pages.bg_time_LineEdit.setValidator(QDoubleValidator(decimals=3))
        self._parent.ui.load_pages.bg_sampletime_LineEdit.editingFinished.connect(self.ui_click_callback)
        self._parent.ui.load_pages.bg_sampletime_LineEdit.setValidator(QDoubleValidator(decimals=2))

        self._parent.ui.load_pages.speed_comboBox.currentIndexChanged.connect(self.ui_click_callback)
        self._parent.ui.load_pages.filter_comboBox.currentIndexChanged.connect(self.ui_click_callback)
        self._parent.ui.load_pages.filter_count_LineEdit.setValidator(QIntValidator())
        self._parent.ui.load_pages.filter_count_LineEdit.editingFinished.connect(self.ui_click_callback)
        

    # update step widge
    # /////////////////////////////
    def updata_step_widge(self):
        self.updata_step_widge_Worker=updata_step_widge_Thread(self)
        QThreadPool.globalInstance().start(self.updata_step_widge_Worker)

    def updata_step_widge_work(self):
        #adjust the Visible of each step
        for _step in range(1,9):

            if _step<=self.cache_steplist.step_number :
                self.step_widges_list[_step].setVisible (True)
                self.step_widges_list[_step].pattern.page.setCurrentIndex(True)
            else:
                if _step==self.cache_steplist.step_number+1 and self.editorEnable:
                    self.step_widges_list[_step].setVisible (True)
                    self.step_widges_list[_step].pattern.page.setCurrentIndex(False)
                else:
                    self.step_widges_list[_step].setVisible (False)
                    self.step_widges_list[_step].pattern.page.setCurrentIndex(False)

            #Check if we can still add step unit
            if self.cache_steplist.step_number<8:
                self.activeStep_noFull=True
            else:
                self.activeStep_noFull=False

            unit=testUnit()
            unit=self.cache_steplist.getStep(_step)

            self.step_widges_list[_step].pattern.Valtage_lineEdit.setText(str(unit.voltage))

    # update graph
    # /////////////////////////////
    def update_graph(self):
        self.update_graph_Worker=update_graph_Thread(self)
        QThreadPool.globalInstance().start(self.update_graph_Worker)

    def update_graph_work(self):
        data_array=[{"x":0,"y":0}]
        SV_array=[0]

        has_bg0=False

        if self.cache_steplist.BG0_test_time >0:
            data_array.append({"x":1,"y":0})
            self.GraphStepLabelList[0].show()
            has_bg0=True
        else:
            data_array=[{"x":1,"y":0}]
            self.GraphStepLabelList[0].hide()
            has_bg0=False
        
        for _step in range(1,9):
            if _step<=self.cache_steplist.step_number:
                #load Graph data
                
                unit=self.cache_steplist.getStep(_step)

                xy_dot={}
                xy_dot["x"]=_step*2-1
                xy_dot["y"]=unit.voltage
                data_array.append(xy_dot)

                xy_dot={}
                xy_dot["x"]=_step*2
                xy_dot["y"]=unit.voltage
                data_array.append(xy_dot)

                xy_dot={}
                xy_dot["x"]=_step*2
                xy_dot["y"]=0
                data_array.append(xy_dot)

                xy_dot={}
                xy_dot["x"]=_step*2+1
                xy_dot["y"]=0
                data_array.append(xy_dot)


                SV_array.append(unit.voltage)
                #load Region
                self.GraphRegionList[_step].show()
                #load Label
                self.GraphStepLabelList[_step].show()
            else:
                #load Region
                self.GraphRegionList[_step].hide()
                #load Label
                self.GraphStepLabelList[_step].hide()


        self.curve.setData(data_array)
        maxpos=max(SV_array)
        minpos=min(SV_array)
        if(maxpos<1):
            self.graph.setYRange(0, 10)
            for _step in range(0,10):
                if _step ==0:
                    self.GraphStepLabelList[0].setPos(0.1,10)
                else:
                    self.GraphStepLabelList[_step].setPos(((2*_step)-1)+0.1,10)
        else:
            max_limit=0
            min_limit=0

            if minpos<0:
                max_limit=1.2*(maxpos-minpos)+minpos
                min_limit=1.1*minpos

            else:
                max_limit=1.2*maxpos
                min_limit=0

            self.graph.setYRange(min_limit,max_limit)

            for _step in range(0,10):
                if _step ==0:
                    self.GraphStepLabelList[0].setPos(0.1,max_limit)
                else:
                    self.GraphStepLabelList[_step].setPos((2*_step-1)+0.1,max_limit)

        if has_bg0:
            self.graph.setLimits(xMin=0,xMax=17.9)
        else:
            self.graph.setLimits(xMin=0.1,xMax=17.9)

        
    
    def lunchOptionDialog(self,message,type):

        '''
        PyDialog.error_type
        PyDialog.warning_2_type
        PyDialog.warning_3_type
        '''

        diag = PyDialog(type,message)
        return(str(diag.exec()))

    def lunchMessageDialog(self,title,message):
        diag = PyMessageDialog(title,message)
        return(str(diag.exec()))

    def maxmin(self,max,min,data):
        if data>=max:
            return max,True
        elif data<=min:
            return min,True
        else:
            return data,False
    
    def ui_click_callback(self):

        btn_name=self.sender().objectName()

        if btn_name=="削除":
            self.patternFile_Delete()
        elif btn_name=="保存":
            self.patternFile_Save()
        elif btn_name=="追加":
            self.patternFile_New()

        elif btn_name=="testfile_comboBox":

            if self.content_Change:
                result=self.lunchOptionDialog("変更内容は未保存です。内容を保存しますか",PyDialog.warning_3_type)

                if result=="Yes":
                    #User is want to save file
                    self.patternFile_Save_work()
                
                elif result=="No":
                    #User is do not want to save file
                    pass

                elif result=="Cancel":
                    #User is not want Delete file
                    self._parent.ui.load_pages.testfile_comboBox.blockSignals(True)
                    self._parent.ui.load_pages.testfile_comboBox.setCurrentIndex(self.focus_patternFile_number-1)
                    self._parent.ui.load_pages.testfile_comboBox.blockSignals(False)
                    return


            self.focus_patternFile_number=self._parent.ui.load_pages.testfile_comboBox.currentIndex()+1
            self.patternFile_Load()

        elif btn_name=="test_commect_lineEdit":
            self.cache_steplist.set_Comment(self._parent.ui.load_pages.test_commect_lineEdit.text())
            self.update_Request=True

        elif btn_name=="test_time_LineEdit":
            data=float(self._parent.ui.load_pages.test_time_LineEdit.text())
            data,err=self.maxmin(999,0,data)
            if err:
                self._parent.ui.load_pages.test_time_LineEdit.setText(str(data))

            self.cache_steplist.set_Test_time(data)
            self.update_Request=True


        elif btn_name=="test_sampletime_LineEdit":
            data=float(self._parent.ui.load_pages.test_sampletime_LineEdit.text())
            data,err=self.maxmin(999,0.01,data)
            if err:
                self._parent.ui.load_pages.test_sampletime_LineEdit.setText(str(data))

            self.cache_steplist.set_Test_sampletime(data)
            self.update_Request=True


        elif btn_name=="bg0_time_LineEdit":
            data=float(self._parent.ui.load_pages.bg0_time_LineEdit.text())
            data,err=self.maxmin(999,0,data)
            if err:
                self._parent.ui.load_pages.bg0_time_LineEdit.setText(str(data))

            self.cache_steplist.set_BG0_test_time(data)
            self.update_Request=True



        elif btn_name=="bg_time_LineEdit":
            data=float(self._parent.ui.load_pages.bg_time_LineEdit.text())
            data,err=self.maxmin(999,0,data)
            if err:
                self._parent.ui.load_pages.bg_time_LineEdit.setText(str(data))

            self.cache_steplist.set_BG_test_time(data)
            self.update_Request=True


        elif btn_name=="bg_sampletime_LineEdit":
            data=float(self._parent.ui.load_pages.bg_sampletime_LineEdit.text())
            data,err=self.maxmin(999,0.01,data)
            if err:
                self._parent.ui.load_pages.bg_sampletime_LineEdit.setText(str(data))

            self.cache_steplist.set_BG_sampletime(data)
            self.update_Request=True

        elif btn_name=="filter_comboBox":
            self.cache_steplist.filter_type=self._parent.ui.load_pages.filter_comboBox.currentIndex()
            self.update_Request=True

        elif btn_name=="speed_comboBox":
            self.cache_steplist.speed=self._parent.ui.load_pages.speed_comboBox.currentIndex()
            self.update_Request=True

        elif btn_name=="filter_count_LineEdit":

            data=float(self._parent.ui.load_pages.filter_count_LineEdit.text())
            data,err=self.maxmin(100,1,data)
            if err:
                self._parent.ui.load_pages.filter_count_LineEdit.setText(str(data))

            self.cache_steplist.filter_count=data

            self.update_Request=True


    def patternFile_Load(self):

        
        self.set_memorypool_register("Measurement Pattern","フォーカスPTN番号",self.focus_patternFile_number)
        self.memory_reader()

        #Reset paste function
        self.paste_ready=False

        if(self.focus_patternFile_number>=1 and self.focus_patternFile_number<=20):
            self.cache_steplist=copy.deepcopy(self.patternFiles[self.focus_patternFile_number])
            self.editorEnable=True
        else:
            self.editorEnable=False

        self.update_Request=True

        try:
            self._parent.tempPattern.update_testPattern_Combobox()
        except:
            pass

    def patternFile_Delete(self):


        result=self.lunchOptionDialog("測定パターン \"{}\" 削除しますか？".format(self.patternFile_nameList[self.focus_patternFile_number-1]),PyDialog.warning_2_type)

        if result=="No":
            return
                
        self.availlible_patternFile_count-=1
        self.set_memorypool_register("Measurement Pattern","有効PTN総数",self.availlible_patternFile_count)

        self.patternFiles.append(testlist())
        self.patternFiles.pop(self.focus_patternFile_number)

        if self.focus_patternFile_number>self.availlible_patternFile_count:
            self.focus_patternFile_number=self.availlible_patternFile_count

        if self.focus_patternFile_number:
            self.cache_steplist=self.patternFiles[self.focus_patternFile_number]
        else:
            self.cache_steplist=testlist()
            
        self.memory_writer()
        self.patternFile_Load()

    def patternFile_Save(self):
        self.patternFile_Save_Worker=patternFile_Save_Thread(self)
        QThreadPool.globalInstance().start(self.patternFile_Save_Worker)

    def patternFile_Save_work(self):

        #Refresh patternFiles
        self.patternFiles[self.focus_patternFile_number]=copy.deepcopy(self.cache_steplist)
        
        list=self.cache_steplist

        self.set_memorypool_register("Measurement Pattern","PTNData_{}_名称".format(self.focus_patternFile_number),list.name)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_註記".format(self.focus_patternFile_number),list.comment)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_パターン有効".format(self.focus_patternFile_number),list.active)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_実行STEP数".format(self.focus_patternFile_number),list.step_number)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_測定時間".format(self.focus_patternFile_number),list.test_time)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_測定sampletime".format(self.focus_patternFile_number),list.test_sampletime)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_BG0測定時間".format(self.focus_patternFile_number),list.BG0_test_time)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_BG測定時間".format(self.focus_patternFile_number),list.BG_test_time)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_BG測定sampletime".format(self.focus_patternFile_number),list.BG_sampletime)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_speed".format(self.focus_patternFile_number),list.speed)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_filter_type".format(self.focus_patternFile_number),list.filter_type)
        self.set_memorypool_register("Measurement Pattern","PTNData_{}_filter_count".format(self.focus_patternFile_number),list.filter_count)



        
        for step in range(1,9):
            self.set_memorypool_register("Measurement Pattern","PTNData_{}_STEP_{}_電圧".format(self.focus_patternFile_number,step),list.units[step].voltage)
            
        #Reload cache_list from memory
        self.patternFile_Load()

    def patternFile_New(self):
        NameString_fromDialog=""

        if self.content_Change:
            result=self.lunchOptionDialog("変更内容は未保存です。保存してから新規作成しますか？",PyDialog.warning_3_type)

            if result=="Yes":
                #User is not want Delete file
                self.patternFile_Save_work()
                NameString_fromDialog=self.lunchMessageDialog("新規パターン作成","新規ファイル名称入力 :")
                
            elif result=="No":
                #User is not want Delete file
                NameString_fromDialog=self.lunchMessageDialog("新規パターン作成","新規ファイル名称入力 :")

            elif result=="Cancel":
                #User is not want Delete file
                return

        else:
            NameString_fromDialog=self.lunchMessageDialog("新規パターン作成","新規ファイル名称入力 :")

        #if we got availible name string
        if NameString_fromDialog!="Dialog reject" and NameString_fromDialog!="":
            
            #Create new cache_steplist
            self.availlible_patternFile_count+=1
            self.focus_patternFile_number=self.availlible_patternFile_count
            self.cache_steplist=testlist(name=NameString_fromDialog)
            self.cache_steplist.set_Active(True)
            #write new availlible_patternFile_count to memory
            self.set_memorypool_register("Measurement Pattern","有効PTN総数",self.availlible_patternFile_count)

            #Save it to database
            self.patternFile_Save()

    def set_memorypool_register(self,pool_name,registor_name,value):
        if self._parent.MMG.memoryPool[pool_name][registor_name].getValue()!=value:
            
            self.PoolSemaphore.acquire(timeout=10)
            self._parent.MMG.memoryPool[pool_name][registor_name].setValue(value)
            sendItem=MemoryUnit(pool_name,registor_name)
            self.queuePool["memory_UploadToMaster_Queue"].put(sendItem)
            self.PoolSemaphore.release()

    def ultility_Update_Work(self):
        #print("self.test1 = ",self.test1)
        #self.test1+=1
        #while 1:
        #    time.sleep(0.1)

            #if time.time()-self.test >0.2 and time.time()-self.test <1000:
            #    print("Temp lag occur time = ",time.time()-self.test)

            #self.test=time.time()

        if self.IconButtonUpdate:
            self.delete_IconButton.set_active(self.delete_IconButtonActiveState)
            self.add_IconButton.set_active(self.add_IconButtonActiveState)
            self.save_IconButton.set_active(self.save_IconButtonActiveState)
            self.IconButtonUpdate=False
        
        if self.update_Request:
            self.update_Request=False
            self.update()

    def scroll_adjust_TestPattern(self):
        self._parent.ui.load_pages.scrollArea_4.horizontalScrollBar().setValue(self._parent.ui.load_pages.scrollArea_4.horizontalScrollBar().maximum())

    def menu_btn_handler(self,btn):
        if btn == "pattern_menu_cut_pushButton":
            self.cache_step=self.cache_steplist.getStep(self.focus_step_number)
            self.cache_steplist.step_number-=1
            self.cache_steplist.units.append(testUnit())
            self.cache_steplist.units.pop(self.focus_step_number)
            self.paste_ready=True
            #print("pattern_menu_cut ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_copy_pushButton":

            self.cache_step=self.cache_steplist.getStep(self.focus_step_number)
            self.paste_ready=True

            #print("pattern_menu_copy ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_paste_pushButton":
            if self.paste_ready:
                self.cache_steplist.setStep(self.focus_step_number,self.cache_step)
            #print("pattern_menu_paste ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_rightinsert_pushButton":
            if not self.cache_steplist.step_number==8:
                if self.paste_ready:
                    self.cache_steplist.units.pop(8)
                    self.cache_steplist.units.insert(self.focus_step_number+1,testUnit())
                    self.cache_steplist.setStep(self.focus_step_number+1,self.cache_step)
                    self.cache_steplist.step_number+=1
            #print("pattern_menu_rightinsert ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_leftinsert_pushButton":
            if not self.cache_steplist.step_number==8:
                if self.paste_ready:
                    self.cache_steplist.units.pop(8)
                    self.cache_steplist.units.insert(self.focus_step_number,testUnit())
                    self.cache_steplist.setStep(self.focus_step_number,self.cache_step)
                    self.cache_steplist.step_number+=1
            #print("pattern_menu_leftinsert ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_rightinsertblank_pushButton":
            if not self.cache_steplist.step_number==8:
                self.cache_steplist.units.pop(8)
                self.cache_steplist.units.insert(self.focus_step_number+1,testUnit())
                self.cache_steplist.step_number+=1
            #print("pattern_menu_rightinsertblank ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_leftinsertblank_pushButton":
            if not self.cache_steplist.step_number==8:
                self.cache_steplist.units.pop(8)
                self.cache_steplist.units.insert(self.focus_step_number,testUnit())
                self.cache_steplist.step_number+=1
            #print("pattern_menu_leftinsertblank ",self.focus_step_number)
            pass

        elif btn == "pattern_menu_delete_pushButton":
            self.cache_steplist.units.append(testUnit())
            self.cache_steplist.units.pop(self.focus_step_number)
            self.un_focus_step(self.focus_step_number)
            self.cache_steplist.step_number-=1
            #print("pattern_menu_delete ",self.focus_step_number)
            pass


        self.update_Request=True


    def focus_step(self,_step):
        
        self._parent.ui.load_pages.scrollArea_4.ensureWidgetVisible(self.step_widges_list[_step])
        self.step_widges_list[_step].setFocusStyle(True)
        self.GraphRegionList[_step].setFocusStyle(True)
        self.focus_step_number=_step

    def un_focus_step(self,_step):
        self.step_widges_list[_step].setFocusStyle(False)
        self.GraphRegionList[_step].setFocusStyle(False)
        
        if self.focus_step_number==_step:
            self.focus_step_number=1


    def content_change_check(self):

        if (self.cache_steplist!=None and
            self.patternFiles[self.focus_patternFile_number]!=None
            ):
            
            self.content_Change=False

            if(
                self.cache_steplist.name            != self.patternFiles[self.focus_patternFile_number].name or
                self.cache_steplist.comment         != self.patternFiles[self.focus_patternFile_number].comment or
                self.cache_steplist.active          != self.patternFiles[self.focus_patternFile_number].active or
                self.cache_steplist.step_number     != self.patternFiles[self.focus_patternFile_number].step_number or
                self.cache_steplist.test_time       != self.patternFiles[self.focus_patternFile_number].test_time or
                self.cache_steplist.test_sampletime != self.patternFiles[self.focus_patternFile_number].test_sampletime or
                self.cache_steplist.BG0_test_time   != self.patternFiles[self.focus_patternFile_number].BG0_test_time or
                self.cache_steplist.BG_test_time    != self.patternFiles[self.focus_patternFile_number].BG_test_time or
                self.cache_steplist.BG_sampletime   != self.patternFiles[self.focus_patternFile_number].BG_sampletime or 
                self.cache_steplist.speed   != self.patternFiles[self.focus_patternFile_number].speed or 
                self.cache_steplist.filter_type != self.patternFiles[self.focus_patternFile_number].filter_type or 
                self.cache_steplist.filter_count    != self.patternFiles[self.focus_patternFile_number].filter_count

                ):
                
                self.content_Change=True

        
            for step in range(1,9):

                cache_stepUnit=self.cache_steplist.getStep(step)
                memory_stepUnit=self.patternFiles[self.focus_patternFile_number].getStep(step)

                if(
                cache_stepUnit.voltage                !=memory_stepUnit.voltage
                ):
                    
                    self.content_Change=True



    def step_modifly_manager(self,step):
        stepUnit=self.cache_steplist.getStep(step)

        stepUnit.voltage =self.step_widges_list[step]._voltage

        self.cache_steplist.setStep(step,stepUnit)

        self.update_Request=True


    def update(self):
        self.content_change_check()
        self.updata_step_widge()
        self.update_graph()
        self.utility_update()
  