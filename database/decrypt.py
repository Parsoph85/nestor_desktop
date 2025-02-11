import base64
import sqlite3

from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def decrypt(encrypted_text: str, db_path='nestor.db') -> str:
    # Функция для генерации SHA-256 хэша из строки
    def get_sha_value(secret: str) -> bytes:
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(secret.encode('utf-8'))
        return digest.finalize()

    # Функция для получения секретного ключа из базы данных
    def get_secret_key_from_db(db_pathy: str) -> bytes:
        conn = sqlite3.connect(db_pathy)
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

    # Декодируем данные из Base64
    encrypted_data = base64.b64decode(encrypted_text)

    # Извлекаем IV и зашифрованные данные
    iv = encrypted_data[:16]  # IV размером 16 байт для AES
    encrypted_bytes = encrypted_data[16:]

    # Создаем экземпляр шифра AES
    cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Дешифруем текст
    decrypted_padded_text = decryptor.update(encrypted_bytes) + decryptor.finalize()

    # Убираем паддинг
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_text = unpadder.update(decrypted_padded_text) + unpadder.finalize()

    return decrypted_text.decode('utf-8')
