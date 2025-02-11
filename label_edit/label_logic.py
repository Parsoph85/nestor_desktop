from label_edit.label_edit_dialog import LabelEditDialog


def label_button_clicked(index, parent, main):
    last_label_button = parent.labels[parent.current_label]
    last_label_button.setStyleSheet(f"""
                    background-color: {parent.label_last_fon}; border: none; color: #40474f;
                    padding: 10px; border-radius: 10px; font: 14px '{main.font_family_regular}';""")
    parent.current_label = index
    last_label_button = parent.labels[parent.current_label]
    current_label = main.db_manager.get_label_by_id(parent.current_label)
    parent.label_last_fon = current_label[1]
    current_label_color_front = current_label[2]
    last_label_button.setStyleSheet(f"""
                        background-color: {current_label_color_front}; border: none; color: #40474f;
                        padding: 10px; border-radius: 10px; font: 14px '{main.font_family_bold}';""")


def edit_label(main, parent, index):
    if index != 0:
        index = parent.current_label
    settings_dialog = LabelEditDialog(main, parent, index)
    settings_dialog.exec_()


def save_label(main, parent):
    main.db_manager.save_current_label(parent.current_label, main.current_theme)
    parent.close()
