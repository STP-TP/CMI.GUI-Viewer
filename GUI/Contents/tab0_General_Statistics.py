from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class Tab0(QGroupBox):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setTitle("test0")
        self.btn_test = QPushButton(self)

        self.layout.addWidget(self.btn_test)

