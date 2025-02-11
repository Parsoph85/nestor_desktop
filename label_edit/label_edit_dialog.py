from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLineEdit

from label_edit.label_active import buttons_for_edit_label_active
from label_edit.label_edit_logic import colors_buttons


class LabelEditDialog(QDialog):

    def __init__(self, main, parent=None, index=None):
        super(LabelEditDialog, self).__init__(parent)
        self.setFixedSize(500, 250)

        self.colors_fon = ("", "#FFFFFF", "#E6E6A1", "#A1C6E7", "#F2B2B2", "#D1E7D1", "#F9E6A1", "#D1C6E7", "#E6B3E0",
                           "#99CCCC")
        self.colors_front = ("", "#ced9f2", "#B3B300", "#007BFF", "#FF4C4C", "#28A745", "#FF8C00", "#6F42C1", "#A500B5",
                             "#339999")

        if index == 0:
            current_label_name = "Без названия"
            self.colors_index = 1
            self.current_label_index = 0
        else:
            current_label = main.db_manager.get_label_by_id(index)
            self.current_label_index = index
            current_label_name = current_label[0]
            current_label_color_front = current_label[2]
            self.colors_index = self.colors_front.index(current_label_color_front)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.setStyleSheet("""
            QDialog {
                border: 1px solid black;
                border-radius: 10px;
                background-color: white;
            }
        """)

        self.main_label_layout = QVBoxLayout(self)

        self.colors_layout = QHBoxLayout()
        self.colors_layout.setContentsMargins(5, 5, 5, 5)
        self.colors_layout.addStretch()
        colors_buttons(self)
        self.colors_layout.addStretch()
        self.main_label_layout.addLayout(self.colors_layout)

        self.label_text_layout = QHBoxLayout()
        self.label_text_layout.addStretch()
        self.label_text = QLineEdit()
        self.label_text.setText(current_label_name)
        main.font_manager_regular.set_font(self.label_text, main.font_family_regular, 13)
        self.label_text.setFixedHeight(45)
        self.label_text.setFixedWidth(300)

        self.label_text.setStyleSheet("""
                                        QLineEdit {
                                            color: #40474f;
                                            border-radius: 10px;
                                            border: 1px solid #aaa;
                                            padding: 5px;
                                            margin-bottom: 10px;
                                        }""")
        self.label_text_layout.addWidget(self.label_text)
        self.label_text_layout.addStretch()
        self.main_label_layout.addLayout(self.label_text_layout)

        self.edit_layout_active = QHBoxLayout()
        self.edit_layout_active.setContentsMargins(5, 5, 5, 5)

        buttons_for_edit_label_active(self, parent, main)

        self.main_label_layout.addLayout(self.edit_layout_active)
