import requests

from database.syncronization import synchronization_from_server_to_db
from datetime import datetime


def get_sync_to_db(parent):
    login, password = parent.db_manager.creds()
    check = check_creds(parent, login, password)
    if check:
        data = {"login": login, "password": password}
        result = ''
        error = None
        url = parent.address + "api/v1/get_all"
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
    url = parent.address + "api/v1/sync_all"
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


def check_creds(parent, login, password):
    result = ''
    error = None
    url = parent.address + "api/v1/login"
    data = {"login": login, "password": password}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        data = response.json()
        result = data['request']

    except requests.exceptions.HTTPError as err:
        error = err
    except Exception as err:
        error = err
    if result == "True":
        return True
    if error:
        error_log(error)
        return False
