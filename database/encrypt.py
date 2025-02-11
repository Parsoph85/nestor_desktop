import base64
import os
import sqlite3

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt(plain_text: str, db_path='nestor.db') -> str:
    # Функция для генерации SHA-256 хэша из строки
    def get_sha_value(secret: str) -> bytes:
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(secret.encode('utf-8'))
        return digest.finalize()

    # Функция для получения секретного ключа из базы данных
    def get_secret_key_from_db(db: str) -> bytes:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute("SELECT sha FROM setting LIMIT 1")
        row = cursor.fetchone()
        conn.close()

        if row is not None:
            return get_sha_value(row[0])  # Получаем хэш от значения sha
        else:
            raise ValueError("Ключ не найден в базе данных.")

    # Получаем секретный ключ из базы данных
    secret_key = get_secret_key_from_db(db_path)

    # Генерируем случайный вектор инициализации (IV)
    iv = os.urandom(16)  # IV размером 16 байт для AES

    # Создаем экземпляр шифра AES
    cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Добавляем паддинг к тексту
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_text = padder.update(plain_text.encode('utf-8')) + padder.finalize()

    # Шифруем текст
    encrypted_bytes = encryptor.update(padded_text) + encryptor.finalize()

    # Кодируем IV и зашифрованные данные в Base64
    encrypted_data = base64.b64encode(iv + encrypted_bytes).decode('utf-8')

    return encrypted_data
