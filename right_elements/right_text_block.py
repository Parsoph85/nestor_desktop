from PyQt5.QtWidgets import QTextEdit, QFrame

from logic.edit_logic import text_change


def right_text_block(parent):
    parent.text_fld = QTextEdit()
    parent.text_fld.setFrameShape(QFrame.NoFrame)  # Убираем рамку
    parent.text_fld.setPlaceholderText("")
    parent.font_manager_regular.set_font(parent.text_fld, parent.font_family_regular, 12)

    parent.text_fld.setStyleSheet("""
                        QTextEdit{
                        color: #40474f;
                        }                         
                        QScrollBar:vertical {
                            border: 1px solid #888;
                            background: #f0f0f0;
                            width: 7px;
                            margin: 0px 0 0px 0;
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
                        }""")

    parent.right_layout.addWidget(parent.text_fld)
    parent.text_fld.textChanged.connect(lambda: text_change(parent))
