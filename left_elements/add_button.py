from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from logic.click_logic import on_add_button_clicked


def add_button(parent):
    parent.add_button = QPushButton()
    parent.add_button.setIcon(QIcon("img/add.png"))  # Укажите путь к вашей картинке
    parent.add_button.setIconSize(QtCore.QSize(30, 30))  # Укажите размер значка по своему усмотрению

    # Установка стиля для кнопки (круглая форма)
    parent.add_button.setStyleSheet("""
                    QPushButton {
                        background-color: white;
                        border: none;             
                        border-radius: 15px; 
                        margin: 0 10 0 10;
                    }

                    QPushButton:hover {
                        background-color: white;
                    }

                    QPushButton:pressed {
                        background-color: #e0e0e0;
                    }
                """)
    parent.left_menu.addWidget(parent.add_button)

    parent.add_button.clicked.connect(lambda: on_add_button_clicked(parent))
