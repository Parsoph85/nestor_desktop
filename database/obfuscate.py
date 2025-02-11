def obfuscate(text):
    obf_text = [f"{char}~" for char in text]
    obf_text = ''.join(obf_text)
    return obf_text


def deobfuscate(obf_text):
    return ''.join(char for index, char in enumerate(obf_text) if index % 2 == 0)
