import pyqtgraph as pg

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

    def hoverEvent(self, ev):
        if not ev.isExit():
            self.setMouseHover(True)
        else:
            self.setMouseHover(False)

    def setMouseHover(self, hover):
        ## Inform the item that the mouse is(not) hovering over it
        if self.mouseHovering == hover:
            return
        self.mouseHovering = hover
        if hover:
            self._parent.tempPattern.focus_step(self.step)
            self.currentBrush = self.hoverBrush
        else:
            self._parent.tempPattern.un_focus_step(self.step)
            self.currentBrush = self.brush
        self.update()

    def setFocusStyle(self,enable):
        if enable:
            self.currentBrush = self.hoverBrush
        else:
            self.currentBrush = self.brush
        self.update()