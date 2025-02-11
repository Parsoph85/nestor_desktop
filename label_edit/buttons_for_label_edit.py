from functools import partial

from PyQt5.QtWidgets import QPushButton

from label_edit.label_logic import edit_label


def buttons_for_label_edit(parent, main):
    add_button = QPushButton("Добавить", parent)
    add_button.setFixedSize(135, 40)  # Установка ширины и высоты кнопки
    add_button.setStyleSheet(f"""
        background-color: #cccccc; color: #40474f; border: none; border-radius: 10px;
         font: 14px '{main.font_family_regular}';""")

    edit_button = QPushButton("Редактировать", parent)
    edit_button.setFixedSize(135, 40)  # Установка ширины и высоты кнопки
    edit_button.setStyleSheet(f"""
            background-color: #cccccc; color: #40474f; border: none; border-radius: 10px;
             font: 14px '{main.font_family_regular}';""")

    delete_button = QPushButton("Удалить", parent)
    delete_button.setFixedSize(135, 40)  # Установка ширины и высоты кнопки
    delete_button.setStyleSheet(f"""
                background-color: #cccccc; color: #40474f; border: none; border-radius: 10px;
                 font: 14px '{main.font_family_regular}';""")

    parent.button_layout_edit.addWidget(add_button)
    parent.button_layout_edit.addWidget(edit_button)
    parent.button_layout_edit.addStretch()
    parent.button_layout_edit.addWidget(delete_button)

    add_button.clicked.connect(partial(edit_label, main, parent, 0))
    edit_button.clicked.connect(partial(edit_label, main, parent, parent.current_label))
