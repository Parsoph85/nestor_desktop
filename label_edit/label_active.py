from functools import partial

from PyQt5.QtWidgets import QPushButton

from label_edit.label_edit_buttons_logic import save_label_edit, close_window


def buttons_for_edit_label_active(parent, main, high):
    save_button = QPushButton("Сохранить", parent)
    save_button.setFixedSize(135, 40)
    save_button.setStyleSheet(f"""
                background-color: #cccccc; color: #40474f; border: none; border-radius: 10px;
                 font: 14px '{high.font_family_regular}';""")

    close_button = QPushButton("Закрыть", parent)
    close_button.setFixedSize(135, 40)
    close_button.setStyleSheet(f"""
                    background-color: #cccccc; color: #40474f; border: none; border-radius: 10px;
                     font: 14px '{high.font_family_regular}';""")

    parent.edit_layout_active.addWidget(save_button)
    parent.edit_layout_active.addStretch()
    parent.edit_layout_active.addWidget(close_button)

    save_button.clicked.connect(partial(save_label_edit, main, parent, high))
    close_button.clicked.connect(partial(close_window, parent))
