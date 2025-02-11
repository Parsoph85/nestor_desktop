from PyQt5.QtWidgets import QHBoxLayout, QFrame

from left_elements.add_button import add_button
from left_elements.del_button import del_button
from left_elements.sort_list import sort_list


def left_menu(parent):
    parent.left_menu = QHBoxLayout(parent)
    parent.left_menu.setContentsMargins(5, 5, 5, 5)
    parent.left_menu.addStretch()

    # import_button = frame_import_button(parent)
    # parent.left_menu.addWidget(import_button)

    parent.left_menu.addStretch()

    sort_list(parent)
    add_button(parent)
    del_button(parent)

    parent.left_layout.addLayout(parent.left_menu)

    # разделитель
    sep_left = QFrame()
    sep_left.setFrameShape(QFrame.HLine)
    sep_left.setFrameShadow(QFrame.Sunken)
    sep_left.setFixedWidth(385)
    parent.left_layout.addWidget(sep_left)
