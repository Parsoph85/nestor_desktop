
def save_label_edit(main, parent, high):
    text = parent.label_text.text()

    color_fon = parent.colors_fon[parent.colors_index]
    color_front = parent.colors_front[parent.colors_index]
    high.db_manager.save_label(parent.current_label_index, text, color_fon, color_front, high.current_theme)
    main.close()
    parent.close()


def close_window(parent):
    parent.close()
