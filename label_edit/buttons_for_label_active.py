from PyQt5.QtWidgets import QPushButton

from label_edit.label_edit_buttons_logic import close_window
from label_edit.label_logic import save_label
from functools import partial


def buttons_for_label_active(parent, main):
    save_button = QPushButton("Сохранить", parent)
    save_button.setFixedSize(135, 40)
    save_button.setStyleSheet(f"""
            background-color: #cccccc; color: #40474f; border: none; border-radius: 10px;
             font: 14px '{main.font_family_regular}';""")

    close_button = QPushButton("Закрыть", parent)
    close_button.setFixedSize(135, 40)
    close_button.setStyleSheet(f"""
                background-color: #cccccc; color: #40474f; border: none; border-radius: 10px;
                 font: 14px '{main.font_family_regular}';""")

    parent.button_layout_active.addWidget(save_button)
    parent.button_layout_active.addStretch()
    parent.button_layout_active.addWidget(close_button)

    save_button.clicked.connect(partial(save_label, main, parent))
    close_button.clicked.connect(partial(close_window, parent))
