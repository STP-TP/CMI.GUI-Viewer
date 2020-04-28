from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class Tab1(QGroupBox):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.top_search_view = QWidget(self)
        self.search_view_layout = QHBoxLayout(self.top_search_view)
        self.edit_nickname = QLineEdit()
        self.btn_search = QPushButton()
        self.group_game_type = QGroupBox()
        self.group_layout = QHBoxLayout(self.group_game_type)
        self.radio_normal = QRadioButton()
        self.radio_rating = QRadioButton()

        self.radio_rating.setText("공식")
        self.radio_normal.setText("일반")
        self.btn_search.setText("전적 검색")
        self.edit_nickname.setPlaceholderText("닉네임 입력")

        self.edit_nickname.setMinimumHeight(30)
        self.btn_search.setMaximumHeight(30)

        self.search_view_layout.addWidget(self.edit_nickname, 3)
        self.search_view_layout.addWidget(self.btn_search, 1)
        self.search_view_layout.addWidget(self.group_game_type, 2)
        self.search_view_layout.addStretch(6)
        self.group_layout.addWidget(self.radio_normal)
        self.group_layout.addWidget(self.radio_rating)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.radio_normal.clicked.connect(self.radio_clicked)
        self.radio_rating.clicked.connect(self.radio_clicked)

        # Contents
        self.main_view = QWidget(self)
        self.main_layout = QGridLayout(self.main_view)
        self.game_list = QGroupBox()
        self.total_match_info = QGroupBox()
        self.match_info = QGroupBox()

        # Contents layout
        self.main_layout.addWidget(self.game_list, 0, 0, 2, 1)
        self.main_layout.addWidget(self.total_match_info, 0, 1)
        self.main_layout.addWidget(self.match_info, 1, 1)
        self.layout.addWidget(self.top_search_view, 1)
        self.layout.addWidget(self.main_view, 14)

    def btn_search_clicked(self):
        pass

    def radio_clicked(self):
        if self.radio_normal.isChecked():
            pass
        elif self.radio_rating.isChecked():
            pass
