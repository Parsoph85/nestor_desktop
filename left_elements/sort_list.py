from PyQt5.QtWidgets import QComboBox

from logic.reload import reload
from logic.theme_click_logic import current_button


def sort_list(parent):
    parent.sort_list = QComboBox()
    sort_options = {
        "Изменен ▼": 0,
        "Изменен ▲": 1,
        "Алфавит ▼": 2,
        "Алфавит ▲": 3,
        "Создан ▼": 4,
        "Создан ▲": 5
    }
    parent.sort_list.addItems(sort_options.keys())
    parent.font_manager_regular.set_font(parent.sort_list, parent.font_family_regular, 12)

    parent.sort_list.setStyleSheet("""
        QComboBox {
            color: #40474f;
            border: 1px;
            border-radius: 10px;
            padding: 0px;
        }
        QComboBox::drop-down {
            color: #40474f;
            border: none;
            width: 20px;
        }

    """)
    parent.auto_input = True
    parent.sort_list.setCurrentIndex(parent.sorting)
    parent.auto_input = False

    parent.left_menu.addWidget(parent.sort_list)

    parent.sort_list.currentIndexChanged.connect(
        lambda index: (setattr(parent, 'sorting', index), parent.db_manager.update_sorting(index), reload(parent),
                       current_button(parent.current_theme, parent))
    )
