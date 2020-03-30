import sys
from GUI.gui_window import *


class CmiGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_window()

        # tab widget 설정
        self.table_widget = GuiWindow(self)
        self.setCentralWidget(self.table_widget)

        self.show()

    def set_window(self):
        self.setWindowTitle("CyphersMatchInformation")
        self.setGeometry(300, 50, 1200, 800)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win_gui = CmiGui()
    app.exec()
