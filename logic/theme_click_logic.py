def theme_button_clicked(event, index, parent):
    parent.event = event
    last_button = parent.themes_buttons[parent.current_theme]

    last_button.setStyleSheet(
        "background-color: " + parent.last_fon_color + "; border: none; color: #40474f;")
    current_button(index, parent)


def current_button(index, parent):
    parent.auto_input = True
    note = parent.db_manager.get_note_by_id(index)
    theme_name = note[0]
    theme_text = note[1]
    theme_label = note[2]

    note_label = parent.db_manager.get_label_by_id(theme_label)
    label_name = note_label[0]
    label_fon_color = note_label[1]
    label_front_color = note_label[2]

    curr_button = parent.themes_buttons[index]

    curr_button.setStyleSheet(
        "background-color: " + label_front_color + "; border: none; color: #40474f;")
    # Меняем метку
    parent.label.setText(label_name)
    parent.label.setStyleSheet(
        "background-color: " + label_fon_color + "; border: none; color: #40474f; border-radius: 10px; padding: 10px;")

    parent.theme_line.setText(theme_name)
    parent.text_fld.setText(theme_text)

    parent.last_selected_label = curr_button
    parent.last_fon_color = label_fon_color
    parent.current_theme = index
    parent.auto_input = False
