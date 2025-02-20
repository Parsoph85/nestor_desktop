from PyQt5.QtWidgets import QMessageBox

from sync.get_sync import check_creds


def on_login(self, parent):
    login = self.login_input.text()
    password = self.password_input.text()
    if login == "":
        login = " "
    if password == "":
        password = " "
    check = check_creds(parent, login, password)
    if check:
        parent.db_manager.save_creds(login, password)
        QMessageBox.information(self, "Успех", "Вы успешно вошли в систему.")
        self.accept()
    else:
        QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль. Попробуйте еще раз.")
