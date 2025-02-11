import re


def theme_change(parent):
    if not parent.auto_input:
        html_text = ""
        index_id = parent.current_theme
        theme = parent.theme_line.text()
        old_text = parent.themes_buttons[index_id].text()
        match = re.search(r"<span style='font-family:\"Open Sans\"; font-size:10pt;'>(.*?)</span>", old_text)
        if match:
            text = match.group(1)
            html_text = f"""
                        <span style='font-family:"{parent.font_family_bold}"; font-size:11pt;'>{theme}</span><br/>
                        <span style='font-family:"{parent.font_family_regular}"; font-size:10pt;'>{text}</span>"""

        parent.themes_buttons[index_id].setText(html_text)
        parent.db_manager.hot_theme_save(parent.current_theme, theme)


def text_change(parent):
    if not parent.auto_input:
        html_text = ""
        index_id = parent.current_theme
        text = parent.text_fld.toPlainText()
        old_text = parent.themes_buttons[index_id].text()
        match = re.search(r"<span style='font-family:\"OpenSans-Bold\"; font-size:11pt;'>(.*?)</span>", old_text)
        text_len = len(text)
        if text_len >= 40:
            text_cut = text[:40] + "..."
        else:
            text_cut = text
        if match:
            theme = match.group(1)
            html_text = f"""<span style='font-family:"{parent.font_family_bold}"; font-size:11pt;'>{theme}</span><br
            /><span style='font-family:"{parent.font_family_regular}"; font-size:10pt;'>{text_cut}</span>"""

        parent.themes_buttons[index_id].setText(html_text)
        parent.db_manager.hot_text_save(parent.current_theme, text)
