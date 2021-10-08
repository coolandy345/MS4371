import pyqtgraph as pg
from gui_main.qt_core import *

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

        self.enterEventWorker = workThread()
        self.enterEventWorker.trigger.connect(self.enterEventWork)
        self.leaveEventWorker = workThread(self)
        self.leaveEventWorker.trigger.connect(self.leaveEventWork)

        
    def hoverEnterEvent(self, ev):
        if self.enterEventWorker.isRunning():
            print("work over flow - enterEvent - graph")
        self.enterEventWorker.start()

    def enterEventWork(self):
        self._parent.tempPattern.focus_step(self.step)


    def hoverLeaveEvent(self, ev):
        if self.leaveEventWorker.isRunning():
            print("work over flow - leaveEvent - graph")
        self.leaveEventWorker.start()

    def leaveEventWork(self):
        self._parent.tempPattern.un_focus_step(self.step)


    def hoverEvent(self, ev):
        pass

    def setFocusStyle(self,enable):
        if enable:
            self.currentBrush = self.hoverBrush
        else:
            self.currentBrush = self.brush
        self.update()