from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout

from auth.auth_logic import on_login


class MainAuthDialog(QDialog):
    def __init__(self, parent=None):
        super(MainAuthDialog, self).__init__(parent)
        self.setFixedSize(300, 400)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setStyleSheet("""
            QDialog {
                border: 1px solid black;
                border-radius: 10px;
                background-color: white;
            }
        """)

        layout = QVBoxLayout()

        layout.addStretch()

        # Поле для ввода логина
        self.login_label = QLabel("Логин:")
        self.login_input = QLineEdit()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        self.login_input.setStyleSheet("""
                                        QLineEdit {
                                            color: #40474f;
                                            border-radius: 10px;
                                            border: 1px solid #aaa;
                                            padding: 5px;
                                            margin-bottom: 10px;
                                        }""")

        # Поле для ввода пароля
        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        self.password_input.setStyleSheet("""
                                                QLineEdit {
                                                    color: #40474f;
                                                    border-radius: 10px;
                                                    border: 1px solid #aaa;
                                                    padding: 5px;
                                                    margin-bottom: 10px;
                                                }""")

        self.button_layout_active = QHBoxLayout()
        self.button_layout_active.setContentsMargins(5, 5, 5, 5)
        layout.addLayout(self.button_layout_active)

        # Кнопка "Войти"
        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(lambda: on_login(self, parent))
        self.button_layout_active.addWidget(self.login_button)
        self.login_button.setFixedSize(120, 40)
        self.login_button.setStyleSheet(f"""
                        background-color: #cccccc; color: #40474f; border: none; border-radius: 10px;
                         font: 14px '{parent.font_family_regular}';""")

        # Кнопка "Закрыть"
        self.close_button = QPushButton("Закрыть", parent)
        self.close_button.setFixedSize(120, 40)
        self.close_button.setStyleSheet(f"""
                            background-color: #cccccc; color: #40474f; border: none; border-radius: 10px;
                             font: 14px '{parent.font_family_regular}';""")

        self.button_layout_active.addWidget(self.close_button)

        layout.addStretch()

        self.setLayout(layout)

        self.close_button.clicked.connect(self.close)
