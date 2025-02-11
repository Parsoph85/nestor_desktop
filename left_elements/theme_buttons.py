from PyQt5.QtWidgets import QLabel, QFrame

from logic.theme_click_logic import theme_button_clicked


def theme_buttons(parent):
    parent.themes_indexes = parent.db_manager.get_themes_indexes(parent.sorting)
    parent.themes_buttons = {0: 0}

    for index_db in parent.themes_indexes:
        index = index_db[0]
        if parent.current_theme is None or parent.current_theme == 0:
            parent.current_theme = index
        note = parent.db_manager.get_note_by_id(index)
        theme_name = note[0]
        theme_text = note[1]
        theme_label = note[2]

        note_label = parent.db_manager.get_label_by_id(theme_label)
        label_fon_color = note_label[1]

        text_len = len(theme_text)
        if text_len > 40:
            parent.short_text = theme_text[:40] + " ..."
        else:
            parent.short_text = theme_text
        theme_button_label = QLabel()
        html_text = f"""
        <span style='font-family:"{parent.font_family_bold}"; font-size:11pt;'>{theme_name}</span><br />
        <span style='font-family:"{parent.font_family_regular}"; font-size:10pt;'>{parent.short_text}</span>
        """
        theme_button_label.setText(html_text)
        theme_button_label.setFixedHeight(62)
        theme_button_label.setFixedWidth(370)
        parent.themes_buttons[index] = theme_button_label
        if index != parent.current_theme:
            theme_button_label.setStyleSheet(
                "background-color: " + label_fon_color + "; border: none; color: #40474f;")
        theme_button_label.setContentsMargins(30, 0, 0, 0)  # Внешние отступы (снизу, справа, сверху, слева)
        parent.container_layout.addWidget(theme_button_label)

        # Добавляем разделитель между радиокнопками
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setFixedWidth(370)
        separator.setFixedHeight(2)
        separator.setContentsMargins(0, 0, 0, 0)
        parent.container_layout.addWidget(separator)

        theme_button_label.mousePressEvent = lambda event, id_theme=index: theme_button_clicked(event, id_theme, parent)
