from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

from logic.click_logic import on_delete_button_clicked


def del_button(parent):
    parent.delete_button = QPushButton()
    parent.delete_button.setIcon(QIcon("img/delete.png"))  # Укажите путь к вашей картинке
    parent.delete_button.setIconSize(QtCore.QSize(30, 30))  # Укажите размер значка по своему усмотрению

    # Установка стиля для кнопки (круглая форма)
    parent.delete_button.setStyleSheet("""
                QPushButton {
                    background-color: white; 
                    border: none;          
                    border-radius: 15px;
                }

                QPushButton:hover {
                    background-color: white;
                }

                QPushButton:pressed {
                    background-color: #e0e0e0;
                }
            """)

    parent.left_menu.addWidget(parent.delete_button)

    parent.delete_button.clicked.connect(lambda: on_delete_button_clicked(parent))
