from PyQt5.QtGui import QFontDatabase, QFont


class FontManager:
    def __init__(self):
        self.fonts = {}

    def add_font(self, font_path):
        font_path = "fonts/" + font_path
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.fonts[font_family] = font_family
        return font_family

    def set_font(self, widget, font_family, size):
        font = QFont(font_family, size)
        widget.setFont(font)
