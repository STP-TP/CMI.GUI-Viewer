import sys
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
        self.setGeometry(300, 50, 1000, 800)


class GuiTabWindow(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        self.tabs.addTab(self.tab1, "기본")
        self.tabs.addTab(self.tab2, "전적검색")

        self.tab1_layout()
        self.tab2_layout()

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def tab1_layout(self):
        self.tab1.layout = QVBoxLayout(self)

    def tab2_layout(self):
        self.tab2.layout = QVBoxLayout(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win_gui = CmiGui()
    app.exec()
