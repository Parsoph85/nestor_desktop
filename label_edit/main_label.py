from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QScrollArea, QWidget, QHBoxLayout

from label_edit.buttons_for_label_active import buttons_for_label_active
from label_edit.buttons_for_label_edit import buttons_for_label_edit
from label_edit.labels_field import labels_field


class MainLabelDialog(QDialog):

    def __init__(self, parent=None, index=None):
        super(MainLabelDialog, self).__init__(parent)
        self.setFixedSize(500, 350)
        self.current_label = None
        self.labels = {}

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.setStyleSheet("""
            QDialog {
                border: 1px solid black;
                border-radius: 10px;
                background-color: white;
            }
        """)

        self.main_label_layout = QVBoxLayout(self)

        self.label_scroll_area = QScrollArea(self)
        self.label_scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_content_layout = QVBoxLayout(self.scroll_content)
        self.scroll_content.setStyleSheet("QWidget { border: none; }")

        self.scroll_content_layout.addStretch()
        labels_field(self, parent, index)
        self.scroll_content_layout.addStretch()

        self.label_scroll_area.setWidget(self.scroll_content)

        self.main_label_layout.addWidget(self.label_scroll_area)

        self.button_layout_edit = QHBoxLayout()
        self.button_layout_edit.setContentsMargins(5, 5, 5, 5)

        buttons_for_label_edit(self, parent)

        self.main_label_layout.addLayout(self.button_layout_edit)

        self.button_layout_active = QHBoxLayout()
        self.button_layout_active.setContentsMargins(5, 5, 5, 5)

        buttons_for_label_active(self, parent)

        self.main_label_layout.addLayout(self.button_layout_active)

        self.label_scroll_area.setStyleSheet("""
            QScrollArea { border: none; }
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
            }
        """)
