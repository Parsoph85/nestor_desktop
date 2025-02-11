from PyQt5.QtWidgets import QRadioButton


def colors_buttons(parent):
    parent.radio_buttons = []
    for i in range(9):
        if i != 0:
            color_fon = parent.colors_fon[i]
            color_front = parent.colors_front[i]
            if i == 1:
                color_fon = "#ECECEC"
            radio_button = QRadioButton(parent)
            radio_button.setStyleSheet(f"QRadioButton::indicator {{"
                                       f"width: 30px;"
                                       f"height: 30px;"
                                       f"border: 5px solid {color_fon};"
                                       f"border-radius: 15px;"
                                       f"background-color: {color_fon};"
                                       f"}}"
                                       f"QRadioButton::indicator:checked {{"
                                       f"border: 5px solid {color_front};"
                                       f"background-color: {color_front};"
                                       f"}}")
            radio_button.toggled.connect(lambda checked, index=i: update_color_index(parent, index, checked))
            parent.radio_buttons.append(radio_button)
            if i == parent.colors_index:
                radio_button.setChecked(True)
            parent.colors_layout.addWidget(radio_button)


def update_color_index(parent, index, checked):
    if checked:
        parent.colors_index = index
