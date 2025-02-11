from PyQt5.QtWidgets import QWidget, QVBoxLayout

from left_elements.left_menu import left_menu
from left_elements.left_theme import left_theme


def left_panel(parent):
    parent.left_frame = QWidget(parent)
    parent.left_frame.setFixedWidth(379)
    parent.left_frame.setContentsMargins(0, 0, 0, 0)
    parent.left_layout = QVBoxLayout(parent)

    # add layout menu
    left_menu(parent)

    # add layout themes
    left_theme(parent)

    parent.left_frame.setLayout(parent.left_layout)
    parent.main_layout.addWidget(parent.left_frame)
