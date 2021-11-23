# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PyQt5
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

class PyIconButton_simple(QPushButton):
        def __init__(
        self,
        icon = None,
        icon_hover = None,
        icon_active = None,
        icon_deactive = None,

        tooltip_text = "",
        btn_id = None,

        width = 30,
        height = 30,
        border_radius=5,

        bg_color = "#343b48",
        bg_color_hover = "#3c4454",
        bg_color_pressed = "#2c313c",

        is_active = True
    ):
            super().__init__()

             # SET DEFAULT PARAMETERS
            self.setFixedSize(width, height)
            #self.setCursor(Qt.PointingHandCursor)
            self.setObjectName(btn_id)
            self.setMinimumSize(QSize(width, height))
            self.setMaximumSize(QSize(width, height))

            

            self.btn_id=btn_id

            font = QFont()
            font.setItalic(False)
            self.setFont(font)
            

            self.setStyleSheet("QPushButton {{ border-radius: {}px;background-color: {} }} QPushButton:hover {{ background-color: {} }} QPushButton:pressed {{ background-color: {} }}".format(border_radius,bg_color,bg_color_hover,bg_color_pressed))

            
            self.icon_deactive = QIcon()
            self.icon_deactive.addFile( Functions.set_svg_icon(icon_deactive), QSize(), QIcon.Normal, QIcon.Off)
            self.icon = QIcon()
            self.icon.addFile( Functions.set_svg_icon(icon), QSize(), QIcon.Normal, QIcon.Off)
            self.icon_active = QIcon()
            self.icon_active.addFile( Functions.set_svg_icon(icon_active), QSize(), QIcon.Normal, QIcon.Off)
            self.icon_hover = QIcon()
            self.icon_hover.addFile( Functions.set_svg_icon(icon_hover), QSize(), QIcon.Normal, QIcon.Off)

            
            self._is_inside=False

            self._is_active = -1
            self.style=-1
            
            self.setIconSize(QSize(width-9, height-9))

            self.set_active(is_active)
            self.change_style(self._is_active)

            

        def change_style(self,style):
            if self.style!=style:
                self.style=style
                if self.style==0:
                    self.setIcon(self.icon_deactive)
                elif self.style==1:
                    self.setIcon(self.icon)
                elif self.style==2:
                    self.setIcon(self.icon_hover)
                elif self.style==3:
                    self.setIcon(self.icon_active)


        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                # EMIT SIGNAL
                if self._is_active and self._is_inside:
                    self.change_style(3)
                    return self.clicked.emit()

        # MOUSE RELEASED
        # Event triggered after the mouse button is released
        # ///////////////////////////////////////////////////////////////
        def mouseReleaseEvent(self, event):
            if event.button() == Qt.LeftButton:
                # EMIT SIGNAL
                if self._is_active:
                    if self._is_inside:
                        self.change_style(2)
                    else:
                        self.change_style(1)
                    return self.released.emit()

        # MOUSE OVER
        # Event triggered when the mouse is over the BTN
        # ///////////////////////////////////////////////////////////////
        def enterEvent(self, event):
            if self._is_active:
                self._is_inside=True
                self.change_style(2)

        # MOUSE LEAVE
        # Event fired when the mouse leaves the BTN
        # ///////////////////////////////////////////////////////////////
        def leaveEvent(self, event):
            if self._is_active:
                self._is_inside=False
                self.change_style(1)

        def set_active(self, enable):
            enable=bool(enable)
            if self._is_active != enable:
                self._is_active=enable
                self.change_style(self._is_active)
                self.setEnabled(enable)



class PyIconButton(QPushButton):
    def __init__(
        self,
        icon_path = None,
        parent = None,
        app_parent = None,
        tooltip_text = "",
        btn_id = None,
        width = 30,
        height = 30,
        radius = 8,
        bg_color = "#343b48",
        bg_color_hover = "#3c4454",
        bg_color_pressed = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_deactive = "#f5f6f9",
        dark_one = "#1b1e23",
        text_foreground = "#8a95aa",
        top_margin = 40,
        is_active = True

    ):
        super().__init__()
        
        # SET DEFAULT PARAMETERS
        self.setFixedSize(width, height)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName(btn_id)
        
        # PROPERTIES

        self._bg_color = bg_color
        self._bg_color_hover = bg_color_hover
        self._bg_color_pressed = bg_color_pressed
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_deactive = icon_color_deactive
        self._top_margin = top_margin
        self._is_active = is_active
        # Set Parameters
        self._set_bg_color = bg_color
        self._set_icon_path = icon_path
        self._set_icon_color = icon_color
        self._set_border_radius = radius
        # Parent
        self._parent = parent
        self._app_parent = app_parent

        # TOOLTIP
        self._tooltip_text = tooltip_text
        self._tooltip = _ToolTip(
            app_parent,
            tooltip_text,
            dark_one,
            text_foreground
        )
        self._tooltip.hide()
        self.set_active(self._is_active)
        

    # SET ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        self._is_active = is_active
        self.change_style(QEvent.Leave)
        self.setEnabled(is_active)
        self.repaint()

    # RETURN IF IS ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def is_active(self):
        return self._is_active

    # PAINT EVENT
    # painting the button and the icon
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        
        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        brush = QBrush(QColor(self._set_bg_color))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width(), self.height())
        
       
        paint.setPen(Qt.NoPen)
        paint.setBrush(brush)
        paint.drawRoundedRect(
            rect, 
            self._set_border_radius, 
            self._set_border_radius
        )

        # DRAW ICONS
        self.icon_paint(paint, self._set_icon_path, rect)
        # END PAINTER
        paint.end()




    # CHANGE STYLES
    # Functions with custom styles
    # ///////////////////////////////////////////////////////////////
    def change_style(self, event):
        if event == QEvent.Enter:
            
            if self._is_active:
                self._set_bg_color = self._bg_color_hover
                self._set_icon_color = self._icon_color_hover
            else:
                self._set_bg_color = self._bg_color
                self._set_icon_color = self._icon_color_deactive

            
            self.repaint()         
        elif event == QEvent.Leave:
            
            self._set_bg_color = self._bg_color

            if self._is_active:
                self._set_icon_color = self._icon_color
            else:
                self._set_icon_color = self._icon_color_deactive
            
            
            self.repaint()
        elif event == QEvent.MouseButtonPress:           
            
            if self._is_active:
                self._set_bg_color = self._bg_color_pressed
                self._set_icon_color = self._icon_color_pressed
            else:
                self._set_bg_color = self._bg_color
                self._set_icon_color = self._icon_color_deactive


            
            self.repaint()
        elif event == QEvent.MouseButtonRelease:

            if self._is_active:
                self._set_bg_color = self._bg_color_hover
                self._set_icon_color = self._icon_color_hover
            else:
                self._set_bg_color = self._bg_color
                self._set_icon_color = self._icon_color_deactive
            
            self.repaint()

    # MOUSE OVER
    # Event triggered when the mouse is over the BTN
    # ///////////////////////////////////////////////////////////////
    def enterEvent(self, event):
        self.change_style(QEvent.Enter)
        self.move_tooltip()
        self._tooltip.show()

    # MOUSE LEAVE
    # Event fired when the mouse leaves the BTN
    # ///////////////////////////////////////////////////////////////
    def leaveEvent(self, event):
        self.change_style(QEvent.Leave)
        self.move_tooltip()
        self._tooltip.hide()

    # MOUSE PRESS
    # Event triggered when the left button is pressed
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            # SET FOCUS
            self.setFocus()
            # EMIT SIGNAL
            return self.clicked.emit()

    # MOUSE RELEASED
    # Event triggered after the mouse button is released
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            # EMIT SIGNAL
            return self.released.emit()

    # DRAW ICON WITH COLORS
    # ///////////////////////////////////////////////////////////////
    def icon_paint(self, qp, image, rect):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self._set_icon_color)

        qp.drawPixmap(
            (rect.width() - icon.width()) / 2, 
            (rect.height() - icon.height()) / 2,
            icon
        )        
        painter.end()

    # SET ICON
    # ///////////////////////////////////////////////////////////////
    def set_icon(self, icon_path):
        self._set_icon_path = icon_path
        self.repaint()

    # MOVE TOOLTIP
    # ///////////////////////////////////////////////////////////////
    def move_tooltip(self):
        # GET MAIN WINDOW PARENT
        gp = self.mapToGlobal(QPoint(0, 0))

        # SET WIDGET TO GET POSTION
        # Return absolute position of widget inside app
        pos = self._parent.mapFromGlobal(gp)

        # FORMAT POSITION
        # Adjust tooltip position with offset
        pos_x = (pos.x() - (self._tooltip.width() // 2)) + (self.width() // 2)
        pos_y = pos.y() - self._top_margin

        # SET POSITION TO WIDGET
        # Move tooltip position
        self._tooltip.move(pos_x, pos_y)

# TOOLTIP
# ///////////////////////////////////////////////////////////////
class _ToolTip(QLabel):
    # TOOLTIP / LABEL StyleSheet
    style_tooltip = """ 
    QLabel {{		
        background-color: {_dark_one};	
        color: {_text_foreground};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
        font: 800 9pt "游ゴシック";
    }}
    """
    def __init__(
        self,
        parent,
        tooltip,
        dark_one,
        text_foreground
    ):
        QLabel.__init__(self)

        # LABEL SETUP
        style = self.style_tooltip.format(
            _dark_one = dark_one,
            _text_foreground = text_foreground
        )
        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style)
        self.setMinimumHeight(34)
        self.setParent(parent)
        self.setText(tooltip)
        self.adjustSize()

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)
