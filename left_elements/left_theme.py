from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea, QFrame, QHBoxLayout, QWidget, QVBoxLayout

from left_elements.theme_buttons import theme_buttons


def left_theme(parent):
    # Создание горизонтального макета для родительского элемента
    parent.scroll_area_layout = QHBoxLayout(parent)

    # Создание области прокрутки
    parent.scroll_area = QScrollArea()
    parent.scroll_area.setWidgetResizable(True)
    parent.scroll_area.setFixedWidth(370)
    parent.scroll_area.setFrameStyle(QFrame.NoFrame | QFrame.Plain)
    parent.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    parent.scroll_area.setContentsMargins(0, 0, 0, 0)

    # Создание контейнера для виджетов
    parent.container_widget = QWidget()
    parent.container_widget.setFixedWidth(370)
    parent.container_widget.setContentsMargins(0, 0, 0, 0)

    # Создание вертикального макета для содержимого контейнера
    parent.container_layout = QVBoxLayout(parent.container_widget)
    parent.container_layout.setContentsMargins(0, 0, 0, 0)
    parent.container_layout.setSpacing(0)
    parent.container_layout.setAlignment(Qt.AlignTop)

    # Вызов функции для добавления кнопок тем
    theme_buttons(parent)

    # Установка контейнера как виджета для области прокрутки
    parent.scroll_area.setWidget(parent.container_widget)
    parent.scroll_area.setContentsMargins(0, 0, 0, 0)

    parent.scroll_area.setStyleSheet("""
                           QScrollBar:vertical {
                               border: 1px solid #888;
                               background: #f0f0f0;
                               width: 7px;
                               margin: 0;
                               border-radius: 2px;
                           }

                           QScrollBar::handle:vertical {
                               background: #888;
                               min-height: 20px;
                               border-radius: 2px;
                           }

                           QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                               background: none;
                               height: 0px;
                           }

                           QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                               background: none;
                           }

                           QScrollBar::handle:vertical:hover {
                               background: #555;
                           }""")

    parent.scroll_area_layout.addWidget(parent.scroll_area)
    parent.left_layout.addLayout(parent.scroll_area_layout)
