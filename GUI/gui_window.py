from GUI.gui_tab_viewer import *
import GUI.gui_comm_define as comm_define


class GuiWindow(QWidget):
    __widget_num = comm_define.widget_num

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.screen_layout = QVBoxLayout(self)
        self.btn_widget = QWidget(self)
        self.btn_layout = QHBoxLayout(self.btn_widget)
        self.tab_widget = GUITabView(self)

        self.btn_menu = []
        for cnt in range(self.__widget_num):
            self.btn_menu.append(QPushButton(self))

        menu_list = ["General Statistics", "Search Match Info", "None", "None"]
        self.set_menu_button(menu_list)
        self.tab_widget.select_menu_button(0)

        self.btn_layout.addStretch(2)
        for cnt in range(self.__widget_num):
            self.btn_layout.addWidget(self.btn_menu[cnt])
        self.btn_layout.addStretch(2)

        self.screen_layout.addWidget(self.btn_widget, 1)
        self.screen_layout.addWidget(self.tab_widget, 9)

        self.setLayout(self.screen_layout)

        self.set_btn_click_event()

    def set_btn_click_event(self):
        self.btn_menu[0].clicked.connect(self.btn_menu0_clicked)
        self.btn_menu[1].clicked.connect(self.btn_menu1_clicked)
        self.btn_menu[2].clicked.connect(self.btn_menu2_clicked)
        self.btn_menu[3].clicked.connect(self.btn_menu3_clicked)

    def btn_menu0_clicked(self):
        self.tab_widget.select_menu_button(0)

    def btn_menu1_clicked(self):
        self.tab_widget.select_menu_button(1)

    def btn_menu2_clicked(self):
        self.tab_widget.select_menu_button(2)

    def btn_menu3_clicked(self):
        self.tab_widget.select_menu_button(3)

    def set_menu_button(self, text_list: list):
        btn_width = 120
        btn_height = 40
        self.btn_layout.setSpacing(50)
        for cnt in range(self.__widget_num):
            if isinstance(text_list[cnt], str):
                self.btn_menu[cnt].setText(text_list[cnt])
            self.btn_menu[cnt].setFixedSize(btn_width, btn_height)
