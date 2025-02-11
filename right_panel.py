from PyQt5.QtWidgets import QWidget, QVBoxLayout

from right_elements.right_label_block import right_label_block
from right_elements.right_menu import right_menu
from right_elements.right_text_block import right_text_block
from right_elements.right_theme_line import right_theme_line


def right_panel(parent):
    parent.right_frame = QWidget(parent)
    parent.right_layout = QVBoxLayout(parent)

    # add right menu
    right_menu(parent)

    # add theme line
    right_theme_line(parent)

    # add text block
    right_text_block(parent)

    # add label
    right_label_block(parent)

    parent.right_frame.setLayout(parent.right_layout)
    parent.main_layout.addWidget(parent.right_frame)
