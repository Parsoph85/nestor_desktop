import requests

from database.syncronization import synchronization_from_server_to_db
from datetime import datetime


def get_sync_to_db(parent):
    result = ''
    error = None
    url = "http://127.0.0.1:5000//api/v1/get_all"  # Замените на ваш URL
    login, password = parent.db_manager.creds()
    data = {"login": login, "password": password}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.HTTPError as err:
        error = err
    except Exception as err:
        error = err
    if result:
        synchronization_from_server_to_db(result, parent)
    if error:
        error_log(error)
    get_sync_to_serv(parent)


def get_sync_to_serv(parent):
    result = ''
    error = None
    data = parent.db_manager.sync()
    url = "http://127.0.0.1:5000//api/v1/sync_all"
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.HTTPError as err:
        error = err
    except Exception as err:
        error = err

    if result is None:
        error = "Не удалось получить ответ от сервера."
    if error:
        error_log(error)


def error_log(error):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{current_time} - {error}\n"
    with open("error_log.txt", "a") as file:
        file.write(log_message)
