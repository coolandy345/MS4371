from gui_main.gui.uis.windows.main_window import *
from gui_main.gui.widgets import *
from gui_main.gui.core.functions import *
from gui_main.gui.core.json_settings import Settings
from gui_main.gui.core.json_themes import Themes
from gui_main.qt_core import *



class TempPatternWidget():
    
    def __init__(
            self, 
            parent,
            app_parent
        ):
        self.Step_number=0
        self.Step_List=[]
        self._parent=parent
        self._app_parent=app_parent
        self.setup_utility()
        self.setup_TempPattern()
        self.Step_number=0

    def setup_utility(self):
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        self.settings = Settings().items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        self.themes = Themes().items

        self.icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-trash.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                tooltip_text = "削除",
                width = 30,
                height = 30,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = "#ff5869",
                icon_color_hover = "#ff5869",
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = self.themes["app_color"]["dark_one"],
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["green"],
            )
        self._parent.ui.load_pages.gridLayout_34.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)

        self.icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-file-add.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                tooltip_text = "追加",
                width = 30,
                height = 30,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = self.themes["app_color"]["dark_one"],
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["green"],
            )
        self._parent.ui.load_pages.gridLayout_35.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)

        self.icon = PyIconButton(
                icon_path = Functions.set_svg_icon("fi-rr-edit.svg"),
                parent = self._parent,
                app_parent = self._app_parent,
                tooltip_text = "保存",
                width = 30,
                height = 30,
                radius = 10,
                dark_one = self.themes["app_color"]["dark_one"],
                icon_color = self.themes["app_color"]["icon_color"],
                icon_color_hover = self.themes["app_color"]["icon_hover"],
                icon_color_pressed = self.themes["app_color"]["white"],
                icon_color_active = self.themes["app_color"]["icon_active"],
                bg_color = self.themes["app_color"]["dark_one"],
                bg_color_hover = self.themes["app_color"]["dark_three"],
                bg_color_pressed = self.themes["app_color"]["green"],
            )
        self._parent.ui.load_pages.gridLayout_36.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)

    def setup_TempPattern(self):
        
        self.first_pattern = PyTempStep(
            active=False,
            step=1,
            type=PyTempStep.Temp_Type,
            parent = self._parent,
            app_parent=self._app_parent,
            )
        self.Step_List.append(self.first_pattern)
        self._parent.ui.load_pages.horizontalLayout_3.addWidget(self.Step_List[0])
        

    def new_TempPattern(self):
        self.Step_number+=1
        self.Step_List[self.Step_number-1].pattern.page.setCurrentIndex(True)
        if self.Step_number<20:
            self.new_pattern = PyTempStep(
                active=False,
                step=self.Step_number+1,
                type=PyTempStep.Temp_Type,
                parent = self._parent,
                app_parent=self._app_parent
                )
            self.Step_List.append(self.new_pattern)
            self._parent.ui.load_pages.horizontalLayout_3.addWidget(self.Step_List[self.Step_number])

    def scroll_adjust_TempPattern(self):
        self._parent.ui.load_pages.scrollArea_3.horizontalScrollBar().setValue(self._parent.ui.load_pages.scrollArea_3.horizontalScrollBar().maximum())

    def close_menu(self):
        print("close menu")

    




    