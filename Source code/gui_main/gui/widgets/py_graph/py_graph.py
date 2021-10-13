import pyqtgraph as pg
from gui_main.qt_core import *
import time

class workThread(QThread):

    trigger = Signal()

    def __int__(self):
        # 初始化函式
        print("Initial")
        super(workThread, self).__init__()

    def run(self):
        self.trigger.emit()

class PyGraphRegionItem(pg.LinearRegionItem):

    def __init__(self, parent = None,step=0,values=(0, 1), orientation='vertical', brush=None, pen=None,
                 hoverBrush=None, hoverPen=None, movable=True, bounds=None, 
                 span=(0, 1), swapMode='sort'):

        super().__init__(values=values, orientation=orientation, brush=brush, pen=pen,
                 hoverBrush=hoverBrush, hoverPen=hoverPen, movable=movable, bounds=bounds, 
                 span=span, swapMode=swapMode)
        
        self._parent=parent
        self.step=step
        self.setAcceptHoverEvents(True)

        self.FocusStyleChange=False
        self.currentBrushFocusStyle=self.brush
        self.timer=QTimer()
        self.timer.timeout.connect(self.timerCallback)
        self.timer.start(100)


    def timerCallback(self):
        if self.FocusStyleChange:
            self.currentBrush = self.currentBrushFocusStyle
            self.update()
            self.FocusStyleChange=False

        
    def hoverEnterEvent(self, ev):
        self._parent.tempPattern.focus_step(self.step)


    def hoverLeaveEvent(self, ev):
        self._parent.tempPattern.un_focus_step(self.step)


    def setFocusStyle(self,enable):
        if enable:
            self.currentBrushFocusStyle = self.hoverBrush
            self.FocusStyleChange=True
        else:
            self.currentBrushFocusStyle = self.brush
            self.FocusStyleChange=True