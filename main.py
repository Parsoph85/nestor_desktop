import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

from database.db_manager import DBManager
from font_manager import FontManager
from left_panel import left_panel
from right_panel import right_panel
from v_separator import v_separator


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('img/icon.png'))

        self.db_manager = DBManager()
        self.settings = self.db_manager.get_settings()
        self.sorting = self.settings[0]
        self.height = self.settings[1]
        self.width = self.settings[2]
        self.uname = self.settings[3]
        self.pwwd = self.settings[4]
        self.setWindowTitle("Нестор")
        self.setGeometry(100, 100, self.width, self.height)
        self.setMinimumSize(710, 460)
        self.setStyleSheet("background-color: white;")
        self.current_theme = 0
        self.auto_input = False
        self.font_manager_regular = FontManager()
        self.font_family_regular = self.font_manager_regular.add_font("OpenSans_Regular.ttf")
        self.font_manager_bold = FontManager()
        self.font_family_bold = self.font_manager_bold.add_font("OpenSans-Bold.ttf")
        self.resizeEvent = self.on_resize

        # Создаем главный горизонтальный layout
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Левый фрейм
        left_panel(self)

        # Добавляем разделитель между фреймами
        v_separator(self)

        # Создаем правый фрейм
        right_panel(self)

    def on_resize(self, event):
        new_size = self.size()
        self.db_manager.update_window_size(new_size.height(), new_size.width())
        super().resizeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
