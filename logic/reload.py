from left_elements.theme_buttons import theme_buttons


def reload(parent):
    for i in reversed(range(parent.container_layout.count())):
        widget = parent.container_layout.itemAt(i).widget()
        if widget is not None:
            widget.deleteLater()
            parent.container_layout.removeItem(parent.container_layout.itemAt(i))

    theme_buttons(parent)
