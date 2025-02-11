from PyQt5.QtWidgets import QFrame


def v_separator(parent):
    parent.separator = QFrame(parent)
    parent.separator.setFrameShape(QFrame.VLine)  # разделитель
    parent.separator.setFrameShadow(QFrame.Sunken)
    parent.separator.setContentsMargins(0, 0, 0, 0)
    parent.main_layout.addWidget(parent.separator)
