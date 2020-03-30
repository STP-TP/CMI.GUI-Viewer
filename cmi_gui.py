import sys
import copy
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class CmiGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_window()

        # tab widget 설정
        self.table_widget = GuiTabWindow(self)
        self.setCentralWidget(self.table_widget)

        self.show()

    def set_window(self):
        self.setWindowTitle("CyphersMatchInformation")
        self.setGeometry(300, 50, 1200, 800)


class GuiTabWindow(QWidget):
    __widget_num = 4

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.screen_layout = QVBoxLayout(self)
        self.btn_widget = QWidget(self)
        self.btn_layout = QHBoxLayout(self.btn_widget)
        self.tab_widget = QWidget(self)
        self.tab_layout = QVBoxLayout(self.tab_widget)

        self.btn_menu_tab = []
        self.main_tab = []
        for cnt in range(self.__widget_num):
            self.btn_menu_tab.append(QPushButton(self))
            self.main_tab.append(QGroupBox(self))
            # Test
            self.main_tab[cnt].setTitle("test" + str(cnt))

        menu_list = ["General Statistics", "Search Match Info", "None", "None"]
        self.set_menu_button(menu_list)
        self.select_menu_button(0)

        for cnt in range(self.__widget_num):
            self.btn_layout.addWidget(self.btn_menu_tab[cnt])
            self.tab_layout.addWidget(self.main_tab[cnt])

        self.screen_layout.addWidget(self.btn_widget, 1)
        self.screen_layout.addWidget(self.tab_widget, 9)

        self.setLayout(self.screen_layout)

        self.set_btn_click_event()

    def set_btn_click_event(self):
        self.btn_menu_tab[0].clicked.connect(self.btn_menu_tab0_clicked)
        self.btn_menu_tab[1].clicked.connect(self.btn_menu_tab1_clicked)
        self.btn_menu_tab[2].clicked.connect(self.btn_menu_tab2_clicked)
        self.btn_menu_tab[3].clicked.connect(self.btn_menu_tab3_clicked)

    def btn_menu_tab0_clicked(self):
        self.select_menu_button(0)

    def btn_menu_tab1_clicked(self):
        self.select_menu_button(1)

    def btn_menu_tab2_clicked(self):
        self.select_menu_button(2)

    def btn_menu_tab3_clicked(self):
        self.select_menu_button(3)

    def select_menu_button(self, btn_index):
        if btn_index > self.__widget_num:
            btn_index = 0
        tab_visible = [False]*4
        tab_visible[btn_index] = True
        for cnt in range(self.__widget_num):
            self.main_tab[cnt].setVisible(tab_visible[cnt])

    def set_menu_button(self, text_list: list):
        btn_width = 120
        btn_height = 40
        self.btn_layout.setSpacing(50)
        for cnt in range(self.__widget_num):
            if isinstance(text_list[cnt], str):
                self.btn_menu_tab[cnt].setText(text_list[cnt])
            self.btn_menu_tab[cnt].setFixedSize(btn_width, btn_height)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win_gui = CmiGui()
    app.exec()
