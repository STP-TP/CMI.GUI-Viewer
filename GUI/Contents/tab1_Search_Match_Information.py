from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class Tab1(QGroupBox):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setTitle("test1")
        self.btn_test = QPushButton(self)
        self.btn_test1 = QPushButton(self)

        self.layout.addWidget(self.btn_test)
        self.layout.addWidget(self.btn_test1)
