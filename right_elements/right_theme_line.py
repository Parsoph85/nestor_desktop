from PyQt5.QtWidgets import QLineEdit

from logic.edit_logic import theme_change


def right_theme_line(parent):
    parent.theme_line = QLineEdit()
    parent.theme_line.setPlaceholderText("")
    parent.font_manager_regular.set_font(parent.theme_line, parent.font_family_regular, 12)

    # Установка высоты и ширины
    parent.theme_line.setFixedHeight(45)
    parent.theme_line.setMinimumWidth(300)
    parent.theme_line.setMaxLength(25)

    # Применение стилей для скругления углов
    parent.theme_line.setStyleSheet("""
                                QLineEdit {
                                    color: #40474f;
                                    border-radius: 10px;
                                    border: 1px solid #aaa;
                                    padding: 5px;
                                    margin-bottom: 10px;
                                }""")

    parent.right_layout.addWidget(parent.theme_line)
    parent.theme_line.textChanged.connect(lambda: theme_change(parent))
