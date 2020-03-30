from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from GUI.Contents.tab0_General_Statistics import *
from GUI.Contents.tab1_Search_Match_Information import *
import GUI.gui_comm_define as comm_define


class GUITabView(QWidget):
    __widget_num = comm_define.widget_num

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.tab_layout = QVBoxLayout(self)

        self.btn_menu_tab = []
        self.main_tab = []

        self.main_tab.append(Tab0(self))
        self.main_tab.append(Tab1(self))
        self.main_tab.append(QGroupBox(self))
        self.main_tab.append(QGroupBox(self))

        for cnt in range(self.__widget_num):
            self.tab_layout.addWidget(self.main_tab[cnt])

    def select_menu_button(self, btn_index):
        if btn_index > self.__widget_num:
            btn_index = 0
        tab_visible = [False]*self.__widget_num
        tab_visible[btn_index] = True
        for cnt in range(self.__widget_num):
            self.main_tab[cnt].setVisible(tab_visible[cnt])
