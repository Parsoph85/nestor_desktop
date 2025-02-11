from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QSizePolicy

from logic.click_logic import on_label_clicked
from logic.theme_click_logic import current_button


def right_label_block(parent):
    parent.label_layout = QHBoxLayout()
    parent.label_layout.setContentsMargins(5, 5, 5, 5)
    parent.label_layout.setAlignment(Qt.AlignLeft)
    parent.right_layout.addLayout(parent.label_layout)

    parent.label = QLabel("")
    parent.label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    parent.font_manager_regular.set_font(parent.label, parent.font_family_regular, 11)
    parent.label.setFixedHeight(40)

    parent.label_layout.addWidget(parent.label)
    current_button(parent.current_theme, parent)
    parent.label.mousePressEvent = lambda event: on_label_clicked(event, parent.current_theme, parent)
