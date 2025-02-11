"""
Модуль работы с БД и шифрованием
"""
import sqlite3

from database.decrypt import decrypt
from database.encrypt import encrypt
from database.key_generator import generate_random_alphanumeric, generate_key
from database.obfuscate import obfuscate, deobfuscate


class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('nestor.db')
        self.cursor = self.conn.cursor()

        # Инициализация БД
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                theme TEXT,
                text TEXT,
                label TEXT,
                tags TEXT,
                ch_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                deleted BOOLEAN,
                uid1 TEXT,
                uid2 TEXT
            )
        ''')

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS setting (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              sorting INT,
              height INT,
              width INT,
              uname TEXT,
              pwwd TEXT,
              ch_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    
              sha TEXT
            )
        '''
        )

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS labels (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              color1 TEXT,
              color2 TEXT,
              uid1 TEXT,
              uid2 TEXT              
            )
        '''
        )
        self.conn.commit()

    def get_settings(self):
        self.cursor.execute('SELECT sorting, height, width, uname, pwwd, sha FROM setting WHERE id = ?', (1,))
        result = self.cursor.fetchone()
        if result is None:
            secret_key = generate_key()
            self.cursor.execute('''
                        INSERT INTO setting (id, sorting, height, width, sha) VALUES (?, ?, ?, ?, ?)
                    ''', (1, 0, 620, 1010, secret_key))
            self.cursor.connection.commit()

            self.cursor.execute('SELECT sorting, height, width, uname, pwwd, sha FROM setting WHERE id = ?', (1,))
            result = self.cursor.fetchone()
        return result

    def get_themes_indexes(self, sorting):  # получение списка ИД

        if sorting == 0:
            order_by = 'ch_data ASC'  # Сортировка по ch_data по возрастанию
        elif sorting == 1:
            order_by = 'ch_data DESC'  # Сортировка по ch_data по убыванию
        elif sorting == 2:
            order_by = 'theme ASC'  # Сортировка по theme по возрастанию
        elif sorting == 3:
            order_by = 'theme DESC'  # Сортировка по theme по убыванию
        elif sorting == 4:
            order_by = 'id ASC'  # Сортировка по id по убыванию
        elif sorting == 5:
            order_by = 'id DESC'  # Сортировка по id по убыванию
        else:
            order_by = 'id ASC'  # По умолчанию сортировка по id

        sql_query = f'SELECT id FROM notes WHERE deleted = 0 OR deleted IS NULL ORDER BY {order_by}'
        self.cursor.execute(sql_query)
        request = self.cursor.fetchall()
        if not request:
            uid1 = generate_random_alphanumeric()
            uid2 = generate_random_alphanumeric()
            self.cursor.execute('''
                    INSERT INTO notes (theme, text, label, uid1, uid2) VALUES (?, ?, ?, ?, ?)
                ''', (obfuscate('Новая заметка...'), encrypt('Введите текст...'), '1', uid1, uid2))
            self.cursor.connection.commit()

            self.cursor.execute(sql_query)
            request = self.cursor.fetchall()
        return request

    def get_note_by_id(self, index):
        self.cursor.execute('SELECT theme, text, label, tags FROM notes WHERE id = ?', (
            index,))
        request = self.cursor.fetchone()
        request = list(request)
        request[0] = deobfuscate(request[0])
        request[1] = decrypt(request[1])
        return request

    def get_label_by_id(self, ident):
        self.cursor.execute('SELECT name, color1, color2 FROM labels WHERE id = ?', (
            ident,))
        result = self.cursor.fetchone()
        if result is None:
            text = obfuscate("Без метки...")
            color1 = obfuscate("#ffffff")
            color2 = obfuscate("#ced9f2")
            uid1 = generate_random_alphanumeric()
            uid2 = generate_random_alphanumeric()
            self.cursor.execute('''
                    INSERT OR REPLACE INTO labels (id, name, color1, color2, uid1, uid2) VALUES (?, ?, ?, ?, ?, ?)
                    ''', (1, text, color1, color2, uid1, uid2))
            self.cursor.connection.commit()
            self.cursor.execute('SELECT name, color1, color2, uid1, uid2 FROM labels WHERE id = ?', (
                1,))
            result = self.cursor.fetchone()
        result = list(result)
        result[0] = deobfuscate(result[0])
        result[1] = deobfuscate(result[1])
        result[2] = deobfuscate(result[2])
        return result

    def add_new_note(self):
        uid1 = generate_random_alphanumeric()
        uid2 = generate_random_alphanumeric()
        self.cursor.execute('''
                INSERT INTO notes (theme, text, label, uid1, uid2) VALUES (?, ?, ?, ?, ?)
                ''', (obfuscate('Новая заметка...'), encrypt('Введите текст...'), '1', uid1, uid2))
        new_id = self.cursor.lastrowid
        self.cursor.connection.commit()
        return new_id

    def update_window_size(self, height, width):
        sql_update_query = '''UPDATE setting SET height = ?, width = ? WHERE id = ?'''
        params = (height, width, 1)
        self.cursor.execute(sql_update_query, params)
        self.conn.commit()

    def update_sorting(self, sorting):
        sql_update_query = '''UPDATE setting SET sorting = ?, ch_data = CURRENT_TIMESTAMP WHERE id = ?'''
        params = (sorting, 1)
        self.cursor.execute(sql_update_query, params)
        self.conn.commit()

    def hot_theme_save(self, index, theme):
        sql_update_query = '''UPDATE notes SET theme = ?, ch_data = CURRENT_TIMESTAMP WHERE id = ?'''
        params = (obfuscate(theme), index)
        self.cursor.execute(sql_update_query, params)
        self.conn.commit()

    def hot_text_save(self, index, text):
        sql_update_query = '''UPDATE notes SET text = ?, ch_data = CURRENT_TIMESTAMP WHERE id = ?'''
        params = (encrypt(text), index)
        self.cursor.execute(sql_update_query, params)
        self.conn.commit()

    def mark_delete_note(self, index):
        sql_update_query = '''UPDATE notes SET deleted = ?, ch_data = CURRENT_TIMESTAMP WHERE id = ?'''
        params = (1, index)
        self.cursor.execute(sql_update_query, params)
        self.conn.commit()

    def get_all_labels(self):
        sql_query = f'SELECT id FROM labels ORDER BY id'
        self.cursor.execute(sql_query)
        request = self.cursor.fetchall()
        return request

    def save_current_label(self, index, note):
        sql_update_query = '''UPDATE notes SET label = ?, ch_data = CURRENT_TIMESTAMP WHERE id = ?'''
        params = (index, note)
        self.cursor.execute(sql_update_query, params)
        self.conn.commit()

    def save_label(self, index, text, color1, color2, note):
        text = obfuscate(text)
        color1 = obfuscate(color1)
        color2 = obfuscate(color2)
        if index == 0:
            uid1 = generate_random_alphanumeric()
            uid2 = generate_random_alphanumeric()
            self.cursor.execute('''
                                INSERT OR REPLACE INTO labels (name, color1, color2, uid1, uid2) VALUES (?, ?, ?, ?, ?)
                                ''', (text, color1, color2, uid1, uid2))
            index = self.cursor.lastrowid
            self.cursor.connection.commit()
        else:
            sql_update_query = '''UPDATE labels SET name = ?, color1 = ?, color2 = ? WHERE id = ?'''
            params = (text, color1, color2, index)
            self.cursor.execute(sql_update_query, params)
            self.conn.commit()
        self.save_current_label(index, note)

    def close(self):
        self.conn.close()
