from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout

from label_edit.label_logic import label_button_clicked


def labels_field(parent, main, index):
    labels = main.db_manager.get_all_labels()
    parent.current_label = int(main.db_manager.get_note_by_id(index)[2])
    total_length = 0
    labels_h_layout = QHBoxLayout()
    labels_h_layout.setAlignment(Qt.AlignTop)
    max_length = 40

    for label in labels:
        current_label_index = label[0]
        current_label = main.db_manager.get_label_by_id(current_label_index)
        current_label_name = current_label[0]
        current_label_color_fon = current_label[1]
        current_label_color_front = current_label[2]

        length = len(current_label_name) + total_length

        if length > max_length:
            parent.scroll_content_layout.addLayout(labels_h_layout)
            labels_h_layout = QHBoxLayout()
            labels_h_layout.setAlignment(Qt.AlignTop)
            total_length = 0

        label_widget = QLabel(current_label_name, parent.scroll_content)
        label_widget.setAlignment(Qt.AlignCenter)

        if current_label_index == parent.current_label:
            label_widget.setStyleSheet(f"""
                background-color: {current_label_color_front}; border: none; color: #40474f; 
                padding: 10px; border-radius: 10px; font: 14px '{main.font_family_bold}';""")
            parent.label_last_fon = current_label_color_fon
        else:
            label_widget.setStyleSheet(f"""
                background-color: {current_label_color_fon}; border: none; color: #40474f; 
                padding: 10px; border-radius: 10px; font: 14px '{main.font_family_regular}';""")

        labels_h_layout.addWidget(label_widget)

        total_length += len(current_label_name)
        parent.labels[current_label_index] = label_widget

        label_widget.mousePressEvent = lambda event, id_label=current_label_index: label_button_clicked(id_label,
                                                                                                        parent, main)

    if not labels_h_layout.isEmpty():
        parent.scroll_content_layout.addLayout(labels_h_layout)
