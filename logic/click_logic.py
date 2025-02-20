from PyQt5.QtCore import Qt

from auth.main_auth import MainAuthDialog
from label_edit.main_label import MainLabelDialog
from logic.reload import reload
from logic.theme_click_logic import current_button


def on_add_button_clicked(parent):
    result = parent.db_manager.add_new_note()
    parent.current_theme = result
    reload(parent)
    current_button(result, parent)


def on_delete_button_clicked(parent):
    parent.db_manager.mark_delete_note(parent.current_theme)
    parent.themes_indexes = parent.db_manager.get_themes_indexes(parent.sorting)
    parent.current_theme = parent.themes_indexes[0][0]
    reload(parent)
    current_button(parent.current_theme, parent)


def on_user_button_clicked(parent):
    auth_dialog = MainAuthDialog(parent)
    auth_dialog.exec_()


def on_label_clicked(event, index, parent):
    if event.button() == Qt.LeftButton:
        settings_dialog = MainLabelDialog(parent, index)
        settings_dialog.exec_()
        reload(parent)
        current_button(parent.current_theme, parent)
