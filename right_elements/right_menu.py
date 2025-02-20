from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QHBoxLayout

from logic.click_logic import on_user_button_clicked


def right_menu(parent):
    parent.right_menu_layout = QHBoxLayout(parent)  # Задаем родительский виджет для Layout

    parent.user_button = QPushButton()
    parent.user_button.setFixedSize(50, 30)
    parent.user_button.setIcon(QIcon("img/auth.png"))  # Укажите путь к вашей картинке
    parent.user_button.setIconSize(QSize(30, 30))  # Укажите размер значка по своему усмотрению
    parent.user_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: none;
                border-radius: 15px;
                margin: 0 10 0 10;
            }

            QPushButton:hover {
                background-color: #f0f0f0;
            }

            QPushButton:pressed {
                background-color: #e0e0e0;
            }
        """)
    parent.right_menu_layout.addStretch()
    parent.right_menu_layout.addWidget(parent.user_button)

    parent.right_layout.addLayout(parent.right_menu_layout)
    parent.user_button.clicked.connect(lambda: on_user_button_clicked(parent))
